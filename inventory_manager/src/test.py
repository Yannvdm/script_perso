import unittest
from unittest.mock import patch, mock_open
from utils import is_equal_to, load_csv, write_csv, merge_csv, sort_data

class TestUtils(unittest.TestCase):

    # Test de is_equal_to
    def test_is_equal_to(self):
        self.assertTrue(is_equal_to(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertFalse(is_equal_to(['a', 'b'], ['a', 'b', 'c']))
        self.assertFalse(is_equal_to(['x', 'y', 'z'], ['a', 'b', 'c']))
        self.assertTrue(is_equal_to([], []))

    # Test de load_csv
    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open,
           read_data="product_id,product_name,quantity,price\n1,Apple,150,0.5\n")
    def test_load_csv_valid_file(self, mock_file, mock_isfile):
        header, data = load_csv("test.csv")
        self.assertEqual(header, ["product_id", "product_name", "quantity", "price", "département"])
        self.assertEqual(data, [[1, "Apple", 150, 0.5, "test"]])

    @patch("os.path.isfile", return_value=False)
    def test_load_csv_file_not_found(self, mock_isfile):
        with self.assertRaises(FileNotFoundError):
            load_csv("missing.csv")

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_csv_empty_file(self, mock_file, mock_isfile):
        with self.assertRaises(ValueError):
            load_csv("test.csv")

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="header1,header2,header3\nvalue1,1.0,2.0\n")
    def test_load_csv_incorrect_columns(self, mock_file, mock_isfile):
        with self.assertRaises(ValueError):
            load_csv("test.csv")

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="header1,header2,header3,header4\nvalue1,not_a_float,2.0,value2\n")
    def test_load_csv_invalid_data(self, mock_file, mock_isfile):
        with self.assertRaises(ValueError):
            load_csv("test.csv")

    # Test de write_csv
    @patch("os.listdir", return_value=["existing.csv"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=['no'])
    def test_write_csv_no_overwrite(self, mock_input, mock_file, mock_listdir):
        write_csv("existing.csv", [["data1", 1.0, 2.0]], ["col1", "col2", "col3"])
        mock_file.assert_not_called()

    @patch("os.listdir", return_value=["existing.csv"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=['yes'])
    def test_write_csv_with_overwrite(self, mock_input, mock_file, mock_listdir):
        write_csv("existing.csv", [["data1", 1.0, 2.0]], ["col1", "col2", "col3"])
        mock_file.assert_called_once_with("existing.csv", "w", newline="", encoding="utf-8")

    # Test de merge_csv
    @patch("utils.load_csv", side_effect=[
        (["col1", "col2"], [["data1", 1.0]]),
        (["col1", "col2"], [["data2", 2.0]])
    ])
    def test_merge_csv_valid(self, mock_load_csv):
        header, data = merge_csv(["file1.csv", "file2.csv"], [], [])
        self.assertEqual(header, ["col1", "col2"])
        self.assertEqual(data, [["data1", 1.0], ["data2", 2.0]])

    @patch("utils.load_csv", side_effect=[
        (["col1", "col2"], [["data1", 1.0]]),
        (["col1", "col3"], [["data2", 2.0]])
    ])
    def test_merge_csv_inconsistent_headers(self, mock_load_csv):
        with self.assertRaises(AttributeError):
            merge_csv(["file1.csv", "file2.csv"], [], [])

    # Test de sort_data
    def test_sort_data_valid(self):
        header = ["col1", "col2"]
        data = [["data1", 2.0], ["data2", 1.0], ["data3", 3.0]]
        sorted_data = sort_data(data, header, "col2")
        self.assertEqual(sorted_data, [["data2", 1.0], ["data1", 2.0], ["data3", 3.0]])

    def test_sort_data_invalid_column(self):
        header = ["col1", "col2"]
        data = [["data1", 2.0], ["data2", 1.0]]
        with self.assertRaises(ValueError):
            sort_data(data, header, "col3")

if __name__ == "__main__":
    unittest.main()
