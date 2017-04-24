import re

def check_format(p_order):
	result = False
	formatStr = re.compile(r"^[AaFf] *[\w]{3} *(t|- *[\w]{3}|[SsCc] *[AaFf] *[\w]{3} *- *[\w]{3}|[Ss] *[AaFf] *[\w]{3}) *$")
	if formatStr.match(p_order):
		result = True
	return(result)
