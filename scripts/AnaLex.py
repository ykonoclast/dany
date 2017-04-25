from collections import namedtuple
import re


Token = namedtuple('Token', ['categorie', 'valeur'])
formatStr = re.compile(r"^[AaFf] +[\w]{3} +(t|- +[\w]{3}|[SsCc] +[AaFf] +[\w]{3} +- +[\w]{3}|[Ss] +[AaFf] +[\w]{3})$")

def tokenize(p_text):
	if formatStr.match(p_text):
		print("match")#provisoire, pour debug
		scanner=re.Scanner([(r"\b[AaFf]\b", lambda scanner,lexeme:Token(categorie='UNITE', valeur=lexeme)),(r"\b([Cc]|[Ss]| - |[tT])\b", lambda scanner,lexeme:Token(categorie='ORDRE', valeur=lexeme.strip())),(r"\b\w{3}\b", lambda scanner,lexeme:Token(categorie='PROVINCE', valeur=lexeme)),(r" +", None)])
		
		results, remainder=scanner.scan(p_text)
		print(results)
		print(remainder)
		
	else:
		print("pas match")#provisoire, pour debug
		#TODO exception

