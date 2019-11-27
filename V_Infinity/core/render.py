"""Moduł renderujący tekst"""
from .calculate import Calculate

class Render():
    """Klasa renderująca:
    zwraca informacje do wyświetlenia"""

    def render_plain_text(self, invoices, plays):
        """Return: rachunek w formie stringa:
        nazwa firmy, przedstawienia, należność, punkty promocyjne"""
        return 'Rachunek dla {}\n'.format(invoices['customer']) + self.perf_info(invoices, plays)+\
        "Należność: {:.2f} zł\n".format(Calculate().total_amount(invoices, plays)/100)+\
        "Punkty promocyjne: {}".format(Calculate().total_volume_credits(invoices, plays))

    def perf_info(self, invoices, plays):
        """Return: informacje o poszczególnych przedstawienich:
        nazwa, cena, liczba miejsc"""
        result = ""
        for perf in invoices['performances']:
            result += " {}: {:.2f} zł (liczba miejsc: {})\n".format(
                Calculate().play_for(perf, plays)['name'],
                Calculate().amount_for(perf, invoices, plays)/100, perf['audience'])
        return result
