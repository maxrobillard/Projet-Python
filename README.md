
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

## Rapport d'analyse

Les résultats obtenus montrent une nette diminution du nombre d'accidents de la route chez les jeunes.
C'est en Europe et en Amérique du Sud que les jeunes consomment le plus d'alcool (53% des jeunes en consomment en Europe, et 36% en Amérique du Sud).

&nbsp;
![HistogrammeMoyenneAlcool](./Rapport/HistogrammeMoyenneAlcool.jpeg)
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
