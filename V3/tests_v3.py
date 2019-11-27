import unittest
from statement_v3 import Statement, json

plays = json.load(open('../Data/plays.json'))
invoices = json.load(open('../Data/invoices.json'))
ST = Statement('../Data/invoices.json', '../Data/plays.json')

class StatementTest(unittest.TestCase):
    def test_result(self):
        result = 'Rachunek dla SuperFirma\n'
        result += " Hamlet: 650.00 zł (liczba miejsc: 55)\n"
        result += " Jak wam sie podoba: 580.00 zł (liczba miejsc: 35)\n"
        result += " Otello: 500.00 zł (liczba miejsc: 40)\n"
        result += "Należność: 1730.00 zł\n"
        result += "Punkty promocyjne: 47"
        self.assertEqual(ST.statement(invoices), result)

class RenderPlainTextTest(unittest.TestCase):
    def test_result(self):
        result = 'Rachunek dla SuperFirma\n'
        result += " Hamlet: 650.00 zł (liczba miejsc: 55)\n"
        result += " Jak wam sie podoba: 580.00 zł (liczba miejsc: 35)\n"
        result += " Otello: 500.00 zł (liczba miejsc: 40)\n"
        result += "Należność: 1730.00 zł\n"
        result += "Punkty promocyjne: 47"
        self.assertEqual(ST.render_plain_text(invoices), result)

class AmountForTest(unittest.TestCase):
    def test_performance_price_1(self):
        perf = {"playID": "hamlet", "audience": 55}
        self.assertEqual(ST.amount_for(perf), 65000)

    def test_performance_price_2(self):
        perf = {"playID": "as-like", "audience": 35}
        self.assertEqual(ST.amount_for(perf), 58000)

    def test_performance_price_3(self):
        perf = {"playID": "othello", "audience": 40}
        self.assertEqual(ST.amount_for(perf), 50000)

class PlayForTest(unittest.TestCase):
    def test_name_type_1(self):
        performance = {"playID": "hamlet"}
        self.assertEqual(ST.play_for(performance), {"name": "Hamlet", "type": "tragedia"})

    def test_name_type_2(self):
        performance = {"playID": "as-like"}
        self.assertEqual(ST.play_for(performance), {"name": "Jak wam sie podoba", "type": "komedia"})

    def test_name_type_3(self):
        performance = {"playID": "othello"}
        self.assertEqual(ST.play_for(performance), {"name": "Otello", "type": "tragedia"})

class VolumeCreditsForTest(unittest.TestCase):
    def test_promo_points_1(self):
        perf = {"playID": "hamlet", "audience": 55}
        self.assertEqual(ST.volume_credits_for(perf), 25)

    def test_promo_points_2(self):
        perf = {"playID": "as-like", "audience": 35}
        self.assertEqual(ST.volume_credits_for(perf), 12)

    def test_promo_points_3(self):
        perf = {"playID": "othello", "audience": 40}
        self.assertEqual(ST.volume_credits_for(perf), 10)

class TotalVolumeCreditsTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(ST.total_volume_credits(), 47)

class TotalAmountTest(unittest.TestCase):
    def test_total_amount(self):
        self.assertEqual(ST.total_amount(), 173000)

if __name__ == "__main__":
    unittest.main()
