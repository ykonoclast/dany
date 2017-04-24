u"""fonctions utilitaires appelées par les autres modules"""
import re

def check_format(p_order):
	u"""fonction vérifiant qu'un ordre respecte le format général de Diplomacy, la syntaxe précise et le lexique des provinces n'est pas étudié"""
	result = False
	formatStr = re.compile(r"^[AaFf] *[\w]{3} *(t|- *[\w]{3}|[SsCc] *[AaFf] *[\w]{3} *- *[\w]{3}|[Ss] *[AaFf] *[\w]{3}) *$")
	if formatStr.match(p_order):
		result = True
	return(result)
