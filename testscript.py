#!/usr/bin/python
# -*- coding: latin-1 -*-
import nltk
from nltk import *
from os import chdir, getcwd
from nltk import load_parser

# Positionnement dans le bon r�pertoire de travail
from os import chdir, getcwd
chdir('/users/2asri10/Projet TAP')
print(getcwd())

# ANALYSEUR bas� sur une grammaire FCFG = Feature context Free Grammar (extension .fcfg)
# une structure de traits repr�sentant l'interpr�tation de la commande trait�e
# sera alors construite lors de l'analyse

#nom_fichier = 'IHR1_COMMANDE_EXEC10.fcfg'
#nom_fichier = 'file:IHR1_COMMANDE_EXEC10_aip.fcfg'
nom_fichier = 'myGrammar.fcfg'

# Cr�ation de diff�rentes versions d'analyseur associ� � la grammaire FCFG
# version avec trace
analyseur_trace = load_parser(nom_fichier, 2)
# version sans trace
analyseur_notrace = load_parser(nom_fichier)

# analyse de commande saisie au clavier ... ne pas oublier les ''
# exemple : 'prends le verre bleu'
# 'stop' pour arr�ter

traiter_commande = True

while(traiter_commande):
      # saisie d'une phrase � analyser
      print('saisir la commande � analyser entre \"\" et\"stop\" pour arr�ter')
      commande = input()
      if commande == 'stop':
          traiter_commande = False
      else:
          # Choix du type d'analyse
          print("choix du type d\'analyse :")
          print("1 avec trace")
          print("2 sans trace (mode par d�faut)")
          type_analyse = input()
          
          # analyse de la phrase avec l'analyseur � disposition
          print(commande)
          # la phrase est �clat�e en suite de mots = ruban d'entr�e
          tokens = commande.split()
          print(tokens)       # Affichage du ruban d'entr�e
          print(len(tokens))  # Affichage du nombre de mots
          
          # g�n�ration de toutes les possibilit�s = trees = arbre de d�rivation r�sultat de l'analyse
          if type_analyse ==1:
              resultat_analyse = analyseur_trace.parse(tokens)
          else:
              resultat_analyse = analyseur_notrace.parse(tokens)
          # si pas de solution alors echec
          # sinon, il y a au moins un arbre de d�rivation
          # pour chaque arbre 
          if resultat_analyse:   # l'analyseur a obtenu au moins un r�sultat
	    for arbre in resultat_analyse :
		print(arbre)      # affichage de l'arbre
		print('-------------------------')
		#print(arbre[0])   # arbre[0] est le 1er fils de l'arbre 
		#print('-------------------------')
		#print(arbre[1])   # arbre[1] est le 2�me fils de l'arbre
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
		print('COMMANDE A EXECUTER : ')
		print(arbre)
	  else:
	    print(commande +" : Phrase rejet�e")
              
print("Goodbye")

# PHRASES A TESTER
# 'prends le verre'
# 'prends le petit verre'
# 'prends le verre bleu'
# 'prends le petit verre bleu'
# 'prends le petit verre bleue'
# 'prends la verre'
# 'stop'






