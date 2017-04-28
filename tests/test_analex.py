import unittest

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'scripts'))
import analex

class AnalexTest(unittest.TestCase):
    
    listProv = None
    
    @classmethod
    def setUpClass(cls):
        AnalexTest.listProv = [{"nom":"BRE", "type":"cotiere","adj":["ATL","MAN","PAR","PIC","GAS"],"centre":"France"},
					{"nom":"PAR", "type":"terrestre","adj":["PIC","BOU","MAR","GAS","BRE"],"centre":"France"},
                    {"nom":"STPCS", "type":"cote","adj":["BOT","LIV","FIN"]},
                    {"nom":"BULCE", "type":"cote","adj":["ROU","NOI","CON"]},
                    {"nom":"BOU", "type":"terrestre","adj":["PIC","PAR","GAS","MAR","RUH","MUN","BEL"]},
                    {"nom":"PIC", "type":"cotiere","adj":["BEL","BRE","PAR","BOU","MAN"]},
                    {"nom":"STPCN", "type":"cote","adj":["BAR","FIN"]}]
    
    def test_tokenize_nominal(self):
        token_groups = [[analex.Token(categorie='UNITE', valeur='A'), analex.Token(categorie='PROVINCE', valeur='PAR'), analex.Token(categorie='ORDRE', valeur='S'), analex.Token(categorie='UNITE', valeur='F'), analex.Token(categorie='PROVINCE', valeur='BOU')],
                        [analex.Token(categorie='UNITE', valeur='F'), analex.Token(categorie='PROVINCE', valeur='PAR'), analex.Token(categorie='ORDRE', valeur='S'), analex.Token(categorie='UNITE', valeur='A'), analex.Token(categorie='PROVINCE', valeur='BOU')],
                        [analex.Token(categorie='UNITE', valeur='A'), analex.Token(categorie='PROVINCE', valeur='PAR'), analex.Token(categorie='ORDRE', valeur='-'), analex.Token(categorie='PROVINCE', valeur='PIC')],
                        [analex.Token(categorie='UNITE', valeur='A'), analex.Token(categorie='PROVINCE', valeur='STPCS'), analex.Token(categorie='ORDRE', valeur='C'), analex.Token(categorie='UNITE', valeur='F'), analex.Token(categorie='PROVINCE', valeur='STPCN'), analex.Token(categorie='ORDRE', valeur='-'), analex.Token(categorie='PROVINCE', valeur='BOU')],#convoi, côtes, casse et espaces en avant, syntaxe invalide, lexique OK
                        [analex.Token(categorie='UNITE', valeur='A'), analex.Token(categorie='PROVINCE', valeur='BULCE'), analex.Token(categorie='ORDRE', valeur='XXX')],
                        [analex.Token(categorie='UNITE', valeur='A'), analex.Token(categorie='PROVINCE', valeur='PAR'), analex.Token(categorie='ORDRE', valeur='XXX')],
                        [analex.Token(categorie='UNITE', valeur='F'), analex.Token(categorie='PROVINCE', valeur='BRE'), analex.Token(categorie='ORDRE', valeur='XXX')]]
        
        orders = ["a PaR s F BoU  -  PiC   ",#soutien offensif, casse
                  "F PaR s a BoU","A PAR - PIC",#soutien défensif, casse, OK lexique et syntaxe mais sémantique fausse
                  "       A STPcs C f stpCN - BOU",#attaque nominale
                  "A BULCE xxx",#tenue casse,côtes, syntaxe fausse lexique ok
                  "A PAR xxx",#tenue casse
                  "F BRE XXX"]#tenue classique

        for tokens, order in zip(token_groups, orders):
            self.assertEqual(tokens, analex.tokenize(order,AnalexTest.listProv))


    def test_tokenize_erreur(self):
        with self.assertRaises(ValueError) as context:
            analex.tokenize("A PAR -",AnalexTest.listProv)#attaque sans cible
        self.assertEqual("refusé, format d'ordre incorrect",str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            analex.tokenize("F BRE C A PIC",AnalexTest.listProv)#convoi sans destination
        self.assertEqual("refusé, format d'ordre incorrect",str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            analex.tokenize("A BOU S",AnalexTest.listProv)#soutien sans objet
        self.assertEqual("refusé, format d'ordre incorrect",str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            analex.tokenize("A BOU S A",AnalexTest.listProv)#soutien sans province cible
        self.assertEqual("refusé, format d'ordre incorrect",str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            analex.tokenize("A CON XXX",AnalexTest.listProv)#province inconnue
        self.assertEqual("refusé, CON: province inconnue",str(context.exception))
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    

