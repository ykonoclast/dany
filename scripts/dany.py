#!/usr/bin/python3

import AnaLex
import argparse
import json


#gestion des arguments, on peut passer un fichier texte à l'application qui analysera son contenu
parser = argparse.ArgumentParser()
parser.add_argument("filename",type=str, nargs='?')
args = parser.parse_args()
	
#lecture de la configuration
with open('../ressources/provinces.json') as data_file:#TODO gérer la position de ce fichier en fonction du lieu d'exécution
	conffile = json.load(data_file)
	
if args.filename is not None:#un fichier a été passé en ligne de commande, on le traite		
	filename=args.filename.strip()
	with open(filename, "r") as text:
		for line in text:	
			try:
				tokens=AnaLex.tokenize(line.strip(),conffile)
				answer = "validé"#l'ordre est passé au tokenizer sans émission d'exception
			except ValueError as error:
				answer=str(error)#on enregistre le message d'erreur à destination de l'utilisateur
			print("{}: {}".format(line.strip(),answer))
else:#TODO : mode serveur
	print("PLACEHOLDER : mode serveur")
	
