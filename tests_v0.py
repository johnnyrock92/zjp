import unittest
from statement_v0 import *

class StatementTest(unittest.TestCase):
    def test_result(self):
        plays = json.load(open('Data/plays.json'))
        invoices = json.load(open('Data/invoices.json'))
        result = 'Rachunek dla SuperFirma\n'
        result += " Hamlet: 650.00 zł (liczba miejsc: 55)\n"
        result += " Jak wam sie podoba: 580.00 zł (liczba miejsc: 35)\n"
        result += " Otello: 500.00 zł (liczba miejsc: 40)\n"
        result += "Należność: 1730.00 zł\n"
        result += "Punkty promocyjne: 47"
        self.assertEqual(statement(invoices, plays), result)

if __name__ == "__main__":
    unittest.main()