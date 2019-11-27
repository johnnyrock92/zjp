"""Moduł obliczający"""
import math

class Calculate():
    """Klasa obliczająca:
    cena i punkty promocyjne"""

    def total_amount(self, invoices, plays):
        """Return: kwota do zapłaty"""
        return sum(self.amount_for(perf, invoices, plays) for perf in invoices['performances'])

    def total_volume_credits(self, invoices, plays):
        """Return: suma punktów promocyjnych"""
        return sum(self.volume_credits_for(perf, invoices, plays) for perf in invoices['performances'])

    def volume_credits_for(self, performance, invoices, plays):
        """Return: ilość punktów promocyjnych"""
        result = max(performance['audience'] - 30, 0)
        if self.play_for(performance, plays)['type'] == "komedia":
            result += math.floor(performance['audience'] / 5)
        return result

    def play_for(self, performance, plays):
        """Return: opis przedstawienia"""
        return plays[performance['playID']]

    def amount_for(self, performance, invoices, plays):
        """Return: cena jednego przedstawienia"""
        def tragedy(performance):
            """Case tragedia:
            oblicza cenę dla tragedii"""
            result = 40000
            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
            return result

        def comedy(performance):
            """Case komedia:
            oblicza cenę dla komedii"""
            result = 30000
            if performance['audience'] > 20:
                result += 10000 + 500 * (performance['audience'] - 20)
            result += 300 * performance['audience']
            return result

        def switch():
            """Wybiera ze słownika odpowiedni klucz i uruchamia
            odpowiednią metodę"""
            result = 0
            # switch: przechowuje klucze (typ przedstawienia)
            # z wartością w postaci funkcji
            switch = {'tragedia': tragedy(performance), 'komedia': comedy(performance)}
            # try: próbuje dopasować typ przedstawienia do klucza w zmiennej switch
            try:
                result += switch[self.play_for(performance, plays)['type']]
            # except: gdy nie ma odpowiedniego klucza
            # w zmiennej switch wyświetla napis
            except TypeError:
                print('Nieznany typ przedstawienia: {}'.format(plays['type']))
            return result
        return switch()
