import json
import math

def statement(invoices, plays):
    '''
    Return: rachunek w formie stringa
    '''
    result = 'Rachunek dla {}\n'.format(invoices['customer'])
    for perf in invoices['performances']:
        result += " {}: {:.2f} zł (liczba miejsc: {})\n".format(playFor(perf)['name'], amountFor(perf)/100, perf['audience'])
    result += "Należność: {:.2f} zł\n".format(totalAmount()/100)
    result += "Punkty promocyjne: {}".format(totalVolumeCredits())
    return result

def totalAmount():
    '''
    Return: kwota do zapłaty
    '''
    result = 0
    for perf in invoices['performances']:
        result += amountFor(perf)
    return result 

def totalVolumeCredits():
    '''
    Return: suma punktów promocyjnych
    '''
    result = 0
    for perf in invoices['performances']:
        result += volumeCreditsFor(perf)
    return result

def volumeCreditsFor(aPerformance):
    '''
    Return: ilość punktów promocyjnych
    '''
    result = max(aPerformance['audience'] - 30, 0)
    # Przyznanie dodatkowego punktu promocyjnego za każdych 5 widzów komedii
    if "komedia" == playFor(aPerformance)['type']:
        result += math.floor(aPerformance['audience'] / 5)
    return result

def playFor(aPerformance):
    '''
    Return: Opis przedstawienia
    '''
    return plays[aPerformance['playID']]

def amountFor(aPerformance):
    '''
    Return: cena jednego przedstawienia
    '''
    result = 0
    if playFor(aPerformance)['type'] == "tragedia":
        result = 40000
        if aPerformance['audience'] > 30:
            result += 1000 * (aPerformance['audience'] - 30)
    elif playFor(aPerformance)['type'] == "komedia":
        result = 30000
        if aPerformance['audience'] > 20:
            result += 10000 + 500 * (aPerformance['audience'] - 20)
        result += 300 * aPerformance['audience']
    else:
        print('Nieznany typ przedstawienia: {}'.format(playFor(aPerformance)['type']))
    
    return result

def openJsonFile(filepath):
    '''
    Return: dane z pliku
    '''
    return json.load(open(filepath))

invoices = openJsonFile('Data/invoices.json')
plays = openJsonFile('Data/plays.json')
print(statement(invoices, plays))
