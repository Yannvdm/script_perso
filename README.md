# Comment utiliser le programme ?
Vidéo Youtube :
https://youtu.be/iNS-6usUOLc

## 1. Lancement du programme
Dans votre terminal, exécutez le programme en tapant :
```
python main.py
```
Vous verrez le message d'accueil suivant :
```
Welcome to the CSV Manager! Type 'help' or '?' to list commands.
CSV>
```
Le prompt CSV> vous invite à saisir des commandes.

## 2. Commandes disponibles et démonstration
### a) Quitter le programme
Commande : `exit`

Description : **Quitte le programme.**

Exemple :
```
CSV> exit
Exiting CSV Manager. Goodbye!
```
### b) Ajouter un fichier CSV
Commande : `add <chemin_du_fichier>`

Description : **Ajoute un fichier CSV au dataset en cours, si les en-têtes correspondent.**

Exemple :
Placez un fichier nommé data1.csv dans le répertoire courant. Ensuite, tapez :


```CSV> add data1.csv```

Si le fichier est valide et les en-têtes correspondent, vous verrez :
```
Dataset successfully updated with data from 'data1.csv'.
```
Si les en-têtes ne correspondent pas, une erreur s'affichera :
```
Error: CSV headers do not match.
```
### c) Visualiser le dataset
Commande : `view`

Description : **Affiche le contenu du dataset actuel dans un tableau aligné.**

Exemple :
```
CSV> view
product_id | product_name | quantity | price
--------------------------------------------
1          | Apple        | 150      | 0.5  
2          | Banana       | 200      | 0.3  
3          | Carrot       | 100      | 0.7  
4          | Tomato       | 50       | 1.2  
5          | Potato       | 300      | 0.2   
```     
### d) Trier le dataset
Commande : `sort <nom_colonne>`

Description : **Trie les données en fonction d'une colonne spécifique. Vous pouvez également choisir un tri décroissant.**

Exemple :
```
CSV> sort quantity
Sort in descending order? (y/n): n
```
Résultat après tri :
```
product_id | product_name | quantity | price
--------------------------------------------
4          | Tomato       | 50       | 1.2  
3          | Carrot       | 100      | 0.7  
1          | Apple        | 150      | 0.5  
2          | Banana       | 200      | 0.3  
5          | Potato       | 300      | 0.2  
  
```   
### e) Exporter le dataset
Commande : `export <nom_du_fichier>`

Description : **Exporte le dataset actuel dans un nouveau fichier CSV.**

Exemple :
Pour exporter dans un fichier nommé output.csv :
```
CSV> export output.csv
Data exported to 'output.csv'.
```
Le fichier output.csv est alors créé dans le répertoire courant.

## 3. Améliorations
Si vous ne spécifiez pas de chemin dans la commande add, le programme listera les fichiers CSV disponibles dans le répertoire courant et vous invitera à en choisir un.

Exemple :
```
CSV> add
Available CSV files:
1. data1.csv
2. data2.csv
Choose a file by number: 1
```

Si vous ne précisez pas de nom de colonne dans la commande sort, le programme listera toutes les colonnes disponibles pour vous.

Exemple :
```
CSV> sort
Available columns:
1. Name
2. Age
3. Country
Choose a column by number: 2
```
