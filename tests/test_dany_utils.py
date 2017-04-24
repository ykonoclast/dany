import unittest
import sys

sys.path.insert(0, "/home/ykonoclast/sources/code/GeanyProjects/dany/scripts")
import dany_utils

class UtilsTest(unittest.TestCase):
	def test_check_format(self):
		self.assertTrue(dany_utils.check_format("a PaR s F BoU  -  GaS   "))
		self.assertTrue(dany_utils.check_format("A PAR - PIC"))
		self.assertFalse(dany_utils.check_format("A PAR -"))
		self.assertTrue(dany_utils.check_format("F PaR s a BoU"))
		self.assertTrue(dany_utils.check_format("A PAR-PIC"))
		self.assertTrue(dany_utils.check_format("APAR t"))
		self.assertTrue(dany_utils.check_format("F aTlCa BoU - CoN"))
		self.assertTrue(dany_utils.check_format("A PAR-PIC"))
		self.assertFalse(dany_utils.check_format("F Ion CASTP"))
		
if __name__ == '__main__':
    unittest.main()
	
	
	
	
	
	
	
	
	
	
	
	
	

