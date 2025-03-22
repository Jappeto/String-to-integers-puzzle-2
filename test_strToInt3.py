#test_strToInt3.py
#Jacob Reppeto

import unittest
import strToInt3

class Test_StrToInt(unittest.TestCase):
    def test_strToInt3(self):
        self.assertEqual(strToInt3.strToInt3("phonetw3oneighty"), 182318)
        self.assertEqual(strToInt3.strToInt3("onxonbexighnte"), 19198)
        self.assertEqual(strToInt3.strToInt3("tw3xo4n5sio8nxe"), 231495618)
        self.assertEqual(strToInt3.strToInt3("onxonbeightwo"), 1182)
        self.assertEqual(strToInt3.strToInt3(""), None)
        self.assertEqual(strToInt3.strToInt3("twoneighthree"), 23183)
        self.assertEqual(strToInt3.strToInt3("nineighthreighte"), 9838)