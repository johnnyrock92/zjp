import unittest
from .statement import Statement, json
from .render import Render
from .calculate import Calculate

plays = json.load(open('../../Data/plays.json'))
invoices = json.load(open('../../Data/invoices.json'))
ST = Statement('../../Data/invoices.json', '../../Data/plays.json')
R = Render()
C = Calculate()

class StatementTest(unittest.TestCase):
    def test_result(self):
        result = 'Rachunek dla SuperFirma\n'
        result += " Hamlet: 650.00 zł (liczba miejsc: 55)\n"
        result += " Jak wam sie podoba: 580.00 zł (liczba miejsc: 35)\n"
        result += " Otello: 500.00 zł (liczba miejsc: 40)\n"
        result += "Należność: 1730.00 zł\n"
        result += "Punkty promocyjne: 47"
        self.assertEqual(ST.statement(invoices, plays), result)

class RenderPlainTextTest(unittest.TestCase):
    def test_result(self):
        result = 'Rachunek dla SuperFirma\n'
        result += " Hamlet: 650.00 zł (liczba miejsc: 55)\n"
        result += " Jak wam sie podoba: 580.00 zł (liczba miejsc: 35)\n"
        result += " Otello: 500.00 zł (liczba miejsc: 40)\n"
        result += "Należność: 1730.00 zł\n"
        result += "Punkty promocyjne: 47"
        self.assertEqual(R.render_plain_text(invoices, plays), result)

class AmountForTest(unittest.TestCase):
    def test_performance_price_1(self):
        perf = {"playID": "hamlet", "audience": 55}
        self.assertEqual(C.amount_for(perf, invoices, plays), 65000)

    def test_performance_price_2(self):
        perf = {"playID": "as-like", "audience": 35}
        self.assertEqual(C.amount_for(perf, invoices, plays), 58000)

    def test_performance_price_3(self):
        perf = {"playID": "othello", "audience": 40}
        self.assertEqual(C.amount_for(perf, invoices, plays), 50000)

class PlayForTest(unittest.TestCase):
    def test_name_type_1(self):
        performance = {"playID": "hamlet"}
        self.assertEqual(C.play_for(performance, plays), {"name": "Hamlet", "type": "tragedia"})

    def test_name_type_2(self):
        performance = {"playID": "as-like"}
        self.assertEqual(C.play_for(performance, plays), {"name": "Jak wam sie podoba", "type": "komedia"})

    def test_name_type_3(self):
        performance = {"playID": "othello"}
        self.assertEqual(C.play_for(performance, plays), {"name": "Otello", "type": "tragedia"})

class VolumeCreditsForTest(unittest.TestCase):
    def test_promo_points_1(self):
        perf = {"playID": "hamlet", "audience": 55}
        self.assertEqual(C.volume_credits_for(perf, invoices, plays), 25)

    def test_promo_points_2(self):
        perf = {"playID": "as-like", "audience": 35}
        self.assertEqual(C.volume_credits_for(perf, invoices, plays), 12)

    def test_promo_points_3(self):
        perf = {"playID": "othello", "audience": 40}
        self.assertEqual(C.volume_credits_for(perf, invoices, plays), 10)

class TotalVolumeCreditsTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(C.total_volume_credits(invoices, plays), 47)

class TotalAmountTest(unittest.TestCase):
    def test_total_amount(self):
        self.assertEqual(C.total_amount(invoices, plays), 173000)

if __name__ == "__main__":
    unittest.main()
