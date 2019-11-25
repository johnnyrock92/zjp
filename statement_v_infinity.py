"""Moduł obliczający rachunek"""
import json
import math


class Statement():
    """Klasa obliczająca rachunek"""

    def __init__(self, invoices, plays):
        self.invoices = invoices
        self.plays = plays

    def print_statement(self):
        """Wyświetla rachunek na ekranie"""

        print(self.statement(self.invoices))

    def statement(self, invoices):
        """Zwraca gotowy rachunek"""

        return self.render_plain_text(invoices)

    def render_plain_text(self, invoices):
        """Return: rachunek w formie stringa"""

        result = 'Rachunek dla {}\n'.format(invoices['customer'])
        for perf in invoices['performances']:
            result += " {}: {:.2f} zł (liczba miejsc: {})\n".format(
                self.play_for(perf)['name'],
                self.amount_for(perf)/100, perf['audience'])
        result += "Należność: {:.2f} zł\n".format(self.total_amount()/100)
        result += "Punkty promocyjne: {}".format(self.total_volume_credits())
        return result

    def total_amount(self):
        """Return: kwota do zapłaty"""

        result = 0
        for perf in self.invoices['performances']:
            result += self.amount_for(perf)
        return result

    def total_volume_credits(self):
        """Return: suma punktów promocyjnych"""

        result = 0
        for perf in self.invoices['performances']:
            result += self.volume_credits_for(perf)
        return result

    def volume_credits_for(self, performance):
        """Return: ilość punktów promocyjnych"""

        result = max(performance['audience'] - 30, 0)
        # Przyznanie dodatkowego punktu
        # promocyjnego za każdych 5 widzów komedii
        if self.play_for(performance)['type'] == "komedia":
            result += math.floor(performance['audience'] / 5)
        return result

    def play_for(self, performance):
        """Return: Opis przedstawienia"""

        return self.plays[performance['playID']]

    def amount_for(self, performance):
        """Return: cena jednego przedstawienia"""
        
        def tragedy(performance):
            # Switch tragedia
            result = 40000
            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
            return result

        def comedy(performance):
            # Switch komedia
            result = 30000
            if performance['audience'] > 20:
                result += 10000 + 500 * (performance['audience'] - 20)
            result += 300 * performance['audience']
            return result

        result = 0
        # switch: przechowuje klucze (typ przedstawienia)
        # z wartością w postaci funkcji
        switch = {'tragedia': tragedy(performance), 'komedia': comedy(performance)}
        # try: próbuje dopasować typ przedstawienia do klucza w zmiennej switch
        try:
            result += switch[self.play_for(performance)['type']]
        # except: gdy nie ma odpowiedniego klucza
        # w zmiennej switch wyświetla napis
        except TypeError:
            print('Nieznany typ przedstawienia: {}'.format(self.plays['type']))
        return result


class ReadData():
    """Klasa odczytująca dane"""
    def __init__(self, invoices, plays):
        self.invoices = json.load(open(invoices))
        self.plays = json.load(open(plays))


# Tworzenie obiektu
DATA = ReadData('Data/invoices.json', 'Data/plays.json')

# Wywołanie metody print_statement() z klasy Statement
Statement(DATA.invoices, DATA.plays).print_statement()
