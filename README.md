
# Visualisation de la corrélation entre le nombre d'accidents de la route et de la consommation d'alcool

## Table des matières

 - [Introduction](#Introduction)
 - [User's Guide](#users-Guide)
 - [Developer's Guide](#developers-Guide)
 - [Rapport d'analyse](#rapport-danalyse)
 - [Lien vers les datasets](#lien-vers-les-datasets)
 - [Instructions d'execution](#instructions-dexecution)

## Introduction

Tous les ans, de jeunes conducteurs sont victimes d'accidents de la route, ce dashboard cherchera à savoir  si la consommation d'alcool des jeunes influe sur ce nombre d'accidents.

## User's Guide

Afin d'exécuter sans erreur ce code, il faudra installer tous les packages suivant dans votre invite de commande en tapant ceci : pip install le_nom_du_package.

Liste des librairies/packages utilisés :
- dash
- dash_bootstrap_components
- pandas
- dash_html_components
- dash_core_components
- dash.dependencies
- plotly.express
- base64
- datetime
- io
- dash_table

Il vous ait aussi possible d'installer tous ces packages directement via le requirements.txt en tapant la commande : **$ pip install -r requirements.txt**

Une fois les packages installés vous devez lancer l'application avec la commande : **py main.py**



## Developer's Guide

Ce guide mentionnera l'architecture ainsi que les fonctions utiles du projet ainsi que des pistes de développement.

#### L'architecture du projet

Le projet se décompose en 4 sous-dossiers qui sont Rapport, apps, data, pycache.<br>
A la racine du projet, il y a 5 fichiers :
- app.py (initialise l'application et crée le serveur Dash)
- data.py (Ce fichier met en forme et traite la data afin de la rendre exploitable)
- main.py (Ce fichier génère le layout en fonction de l'url, il initialise aussi l'application sur l'adresse  localhost:5000/)
- requirements.txt (Liste de toutes les librairies nécessaire au lancements de l'application)
- README.md

Le dossier **apps** se compose d'un dossier pycache et de 6 fichiers :
- **__init__.py** (permet de définir le dossier comme packages)
- app1.py (contient la page 1 du dashboard)
- app2.py (contient la page 2 du dashboard)
- app3.py (contient la page 3 du dashboard)
- erreur.py (contient la page à afficher en cas de mauvais URL)
- nav.py (contient la barre de navigation présente sur toutes les pages)
Le dossier **data** est le dossier où se trouve les csv nécessaire à l'application.<br>
Le dossier **Rapport** comprend les captures d'écrans des différents graphes affichés.<br>

#### Les différentes fonctions présentent dans le projet

Dans le fichier main.py<br>
> La fonction display_page(pathname) prend en parametre une string et renvoie la bonne affichage en fonction de l'url

Dans le fichier app1.py<br>
> La fonction recuperationDataAlcool(type) prend en parametre une string et renvoie les informations voulues.<br>
Pour la string : <br>
> - "data" la fonction ouvre le csv et le retourne<br>
> - "total" la fonction renvoie le nom de la colonne du csv qui selectionne le pourcentage totale (hommes+femmes) du nombre de consommateur d'alcool ainsi que le nom à afficher<br>
> - "man" la fonction renvoie le nom de la colonne du csv qui selectionne le pourcentage d'hommes consommant de l'alcool ainsi que le nom à afficher<br>
> - "female" la fonction renvoie le nom de la colonne du csv qui selectionne le pourcentage de femmes consommant de l'alcool ainsi que le nom à afficher<br>
> - "moyenne" renvoie la moyenne par continent de consommateur d'alcool<br>
> - "continent" renvoie la liste des continents<br>

> La fonction recuperationDataAccident(type) prend en parametre une string et renvoie les informations voulues.<br>
> Pour la string : <br>
> - "data" la fonction ouvre le csv et le retourne<br>
> - "dataClear" la fonction nettoye les données en supprimant toutes les lignes inutiles et renvoie les données nécessaire<br>
> - "MapAccident" la fonction nettoye les données et renvoie les données nécessaire ainsi que le nom de la colonne à sélectionner<br>
> - "PaysSelect" la fonction retourne la liste des pays possibles<br>

> La fonction recuperationDataTolerance(type) prend en parametre une string et renvoie les informations voulues.<br>
> Pour la string : <br>
> - "data" la fonction ouvre le csv et le retourne<br>
> - "MapTolerance" la fonction retourne le nom de la colonne à selectionner pour la création d'une carte ainsi que le nom à afficher en français<br>

## Rapport d'analyse

Les résultats obtenus montrent une nette diminution du nombre d'accidents de la route chez les jeunes.
C'est en Europe et en Amérique du Sud que les jeunes consomment le plus d'alcool (53% des jeunes en consomment en Europe, et 36% en Amérique du Sud).

&nbsp;
![Histogramme](Rapport/HistogrammeMoyenneAlcool.JPG)
&nbsp;



En Europe, la limite légale de concentration d'alcool dans le sang pour les jeunes conducteurs est d'environ 0.03g (en moyenne).
Or, on voit qu'au fil du temps, le nombre d'accidents de la route baisse beaucoup dans tous les pays.
Le nombre maximal d'accidents par pays passe de plus de 8000 à moins de 3500.

Cette tendance peut se constater en Europe, mais aussi dans la quasi totalité des pays du monde que nous avons pu étudier.

Aux Etats-Unis cependant, nous observons que le nombre d'accidents reste stable chez les jeunes. En effet, les jeunes américains peuvent conduire en moyenne dès l'âge de 16 ans.
Ne pouvant consommer légalement de l'alcool avant l'age de 21 ans, ce n'est pas un facteur qui impacte significativement le nombre d'accidents de la route.


## Lien vers les datasets

Base de données "youth" : https://apps.who.int/gho/data/node.main.A1206?lang=en

Le préprocessing des bases de données est dans le dossier nettoyage_bdd.



## Instructions d'execution

- Télécharger le dossier "ProjetV1-master"
- Le dézipper
- Ouvrir l'invite de commande
- Se déplacer dans les répertoires afin que le répertoire courant soit ProjetV1-master
- Rentrer cette ligne de commande dans l'invité : python main.py
