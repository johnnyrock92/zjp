import json
import math

plays = json.load(open('Data/plays.json'))
invoices = json.load(open('Data/invoices.json'))

def statement(invoices, plays):
    totalAmount = 0
    volumeCredits = 0
    result = 'Rachunek dla {}\n'.format(invoices['customer'])
    
    for perf in invoices['performances']:
        play = plays[perf['playID']]
        thisAmount = 0
        
        if play['type'] == "tragedia":
            thisAmount = 40000
            if perf['audience'] > 30:
                thisAmount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "komedia":
            thisAmount = 30000
            if perf['audience'] > 20:
                thisAmount += 10000 + 500 * (perf['audience'] - 20)
            thisAmount += 300 * perf['audience']
        else:
            print('Nieznany typ przedstawienia: {}'.format(play['type']))

        #Przyznanie punktów promocyjnych
        volumeCredits += max(perf['audience'] - 30, 0)
        #Przyznanie dodatkowego punktu promocyjnego za każdych 5 widzów komedii
        if "komedia" == play['type']:
            volumeCredits += math.floor(perf['audience'] / 5)

        #Utworzenie wiersza rachunku
        result += " {}: {:.2f} zł (liczba miejsc: {})\n".format(play['name'], thisAmount/100, perf['audience'])
        totalAmount += thisAmount

    result += "Należność: {:.2f} zł\n".format(totalAmount/100)
    result += "Punkty promocyjne: {}".format(volumeCredits)
    return result

print(statement(invoices, plays))