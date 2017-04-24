import dany_utils

order=input("Entrez un ordre: ")
passed=dany_utils.check_format(order)
if passed:
	print(order+": valid")
else:
	print(order+": invalid")
