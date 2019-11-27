"""Moduł wystawiający rachunek"""
import json
from .render import Render

class Statement():
    """Klasa obliczająca rachunek"""

    def __init__(self, invoices, plays):
        self.invoices = json.load(open(invoices))
        self.plays = json.load(open(plays))

    def print_statement(self):
        """Wyświetla rachunek na ekranie"""
        print(self.statement(self.invoices, self.plays))

    def statement(self, invoices, plays):
        """Zwraca gotowy rachunek"""
        return Render().render_plain_text(invoices, plays)
