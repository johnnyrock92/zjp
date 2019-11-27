"""Run"""
from core.statement import Statement

if __name__ == '__main__':
    Statement('../Data/invoices.json', '../Data/plays.json').print_statement()
