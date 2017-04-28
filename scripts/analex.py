from collections import namedtuple
import re

Token = namedtuple('Token', ['categorie', 'valeur'])
formatStr = re.compile(r"^[AaFf] +(\w{3}([Cc][SsEeNn])?) +((xxx|XXX)|- +(\w{3}([Cc][SsEeNn])?)|[SsCc] +[AaFf] +(\w{3}([Cc][SsEeNn])?) +- +(\w{3}([Cc][SsEeNn])?)|[Ss] +[AaFf] +(\w{3}([Cc][SsEeNn])?))$")
listprov=[]
				
def scan_unit(p_scanner,p_lexeme):
	return Token(categorie='UNITE', valeur=p_lexeme.upper())

def scan_prov(p_scanner,p_lexeme):
	if p_lexeme.upper() in listprov:#si la province fait bien partie du vocabulaire
		return Token(categorie='PROVINCE', valeur=p_lexeme.upper())
	else:
		raise ValueError("refusé, {}: province inconnue".format(p_lexeme))
	
def scan_order(p_scanner,p_lexeme):
	return Token(categorie='ORDRE', valeur=p_lexeme.strip().upper())

def tokenize(p_text,p_conffile):
	global listprov#on met à jour la liste globale de provinces utilisée par le module
	listprov = [d['nom'] for d in p_conffile]#crée une liste à partir d'une compréhension de liste obtenue par le parcours du contenu du JSON en ne gardant que les champs "nom"
	order = p_text.strip()
	if formatStr.match(order):#le format de l'ordre est correct, on peut en extraire les lexèmes pour vérifier leur appartenance au vocabulaire et les tokenizer pour envoi vers l'analyseur syntaxique
		scanner=re.Scanner([(r"\b[AaFf]\b", scan_unit),(r"\b([Cc]|[Ss]| - |(xxx|XXX))\b", scan_order),(r"\b(\w{3}([Cc][SsEeNn])?)\b", scan_prov),(r" +", None)])#tokenization effective via expressions régulières
		results, remainder=scanner.scan(order)
		return(results)#on jette ce qui n'a pas été matché, à ce stade il ne peut rien s'y trouver d'intéressant car toutes les REGEXP ont matché
	else:
		raise ValueError("refusé, format d'ordre incorrect")
