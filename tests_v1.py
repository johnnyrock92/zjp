import unittest
from statement_v1 import *

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

class AmountForTest(unittest.TestCase):
    def test_performance_price_1(self):
        perf = {"playID": "hamlet", "audience": 55}
        self.assertEqual(amountFor(perf), 65000)

    def test_performance_price_2(self):
        perf = {"playID": "as-like", "audience": 35}
        self.assertEqual(amountFor(perf), 58000)

    def test_performance_price_3(self):
        perf = {"playID": "othello", "audience": 40}
        self.assertEqual(amountFor(perf), 50000)

class PlayForTest(unittest.TestCase):
    def test_name_type_1(self):
        aPerformance = {"playID": "hamlet"}
        self.assertEqual(playFor(aPerformance), {"name": "Hamlet", "type": "tragedia"})

    def test_name_type_2(self):
        aPerformance = {"playID": "as-like"}
        self.assertEqual(playFor(aPerformance), {"name": "Jak wam sie podoba", "type": "komedia"})

    def test_name_type_3(self):
        aPerformance = {"playID": "othello"}
        self.assertEqual(playFor(aPerformance), {"name": "Otello", "type": "tragedia"})

class VolumeCreditsForTest(unittest.TestCase):
    def test_promo_points_1(self):
        perf = {"playID": "hamlet", "audience": 55}
        self.assertEqual(volumeCreditsFor(perf), 25)

    def test_promo_points_2(self):
        perf = {"playID": "as-like", "audience": 35}
        self.assertEqual(volumeCreditsFor(perf), 12)

    def test_promo_points_3(self):
        perf = {"playID": "othello", "audience": 40}
        self.assertEqual(volumeCreditsFor(perf), 10)

class TotalVolumeCreditsTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(totalVolumeCredits(), 47)

class TotalAmountTest(unittest.TestCase):
    def test_total_amount(self):
        self.assertEqual(totalAmount(), 173000)

if __name__ == "__main__":
    unittest.main()
