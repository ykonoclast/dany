#!/usr/bin/python3

import AnaLex
import argparse



#vérification initiale du format de la chaîne d'ordre
#passed=dany_utils.check_format(order)
#if passed:
#	print(order+": valid")
#else:
#	print(order+": invalid")


if __name__ == '__main__':
	#gestion des arguments, on peut passer un fichier texte à l'application qui analysera son contenu
	parser = argparse.ArgumentParser()
	parser.add_argument("filename",type=str, nargs='?')
	args = parser.parse_args()
	
	if args.filename is not None:
		#un fichier a été passé en ligne de commande
		filename=args.filename.strip()
		with open(filename, "r") as text:
			for line in text:
				print(line)#provisoire, pour debug
				AnaLex.tokenize(line.strip())
	else:
		#TODO : mode serveur
		print("PLACEHOLDER : mode serveur")
	
