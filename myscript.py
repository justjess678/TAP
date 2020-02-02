#!/usr/bin/python
# -*- coding: latin-1 -*-
import nltk
from nltk import *
from os import chdir, getcwd
from nltk import load_parser

# Positionnement dans le bon répertoire de travail
from os import chdir, getcwd
chdir('/users/2asri10/Projet TAP')
print(getcwd())

# ANALYSEUR basé sur une grammaire FCFG = Feature context Free Grammar (extension .fcfg)
# une structure de traits représentant l'interprétation de la commande traitée
# sera alors construite lors de l'analyse

#nom_fichier = 'IHR1_COMMANDE_EXEC10.fcfg'
#nom_fichier = 'file:IHR1_COMMANDE_EXEC10_aip.fcfg'
nom_fichier = 'myGrammar.fcfg'

# Création de différentes versions d'analyseur associé à la grammaire FCFG
# version sans trace
analyseur_notrace = load_parser(nom_fichier)

# saisie d'une phrase à analyser
file = open('calc.txt','r')

commande = file.read()
# analyse de la phrase avec l'analyseur à disposition
print(commande)
# la phrase est éclatée en suite de mots = ruban d'entrée
tokens = commande.split()
# print(tokens)       # Affichage du ruban d'entrée
# print(len(tokens))  # Affichage du nombre de mots

# génération de toutes les possibilités = trees = arbre de dérivation résultat de l'analyse
# we don't show the tree
resultat_analyse = analyseur_notrace.parse(tokens)
# si pas de solution alors echec
# sinon, il y a au moins un arbre de dérivation
# pour chaque arbre 
if resultat_analyse:   # l'analyseur a obtenu au moins un résultat
	for arbre in resultat_analyse :
		#print(arbre)      # affichage de l'arbre
		#print('-------------------------')
		#print(arbre[0])   # arbre[0] est le 1er fils de l'arbre 
		#print('-------------------------')
		#print(arbre[1])   # arbre[1] est le 2ème fils de l'arbre
		#print('-------------------------')
		#print(arbre.flatten())     # arbre applatit
		#print(arbre.flatten()[1])  # arbre racine et terminaux
		#print('-------------------------')
		#interpretation = arbre.label()
		#print('-------------------------')
		##print(len(interpretation))
		#print('-------------------------')
		#for element in interpretation:
				          #print(element)
				          #print(interpretation[element])
		#print('-------------------------')
		#print(interpretation['INTERP'])
		#resultat = ' '.join(interpretation['INTERP'])
		#print('-------------------------')
		#print('COMMANDE A EXECUTER : ')
		print(arbre)
else:
	print(commande +" : Phrase rejetée")
print("Comprehension finished")
file.close()
