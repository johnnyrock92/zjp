# Zaawansowane Języki Programowania
## Uniwersytet Gdański - Informatyka NS II st. semestr 1. - 2019/2020
## Autor: Schonrock Janusz 246654
## Link: https://github.com/johnnyrock92/zjp
### Kod do refaktoryzacji został napisany w języku Python na podstawie kodu z książki [Refaktoryzacja. Ulepszanie struktury istniejącego kodu](https://martinfowler.com/books/refactoring.html).

Repozytorium zawiera projekt zaliczeniowy laboratorium. Celem projektu jest refaktoryzacja kodu, czyli poprawienie jego struktury oraz zastosowanie konwencji przedstawionych w książce [Refaktoryzacja. Ulepszanie struktury istniejącego kodu](https://martinfowler.com/books/refactoring.html).

---
## Opis
Stworzony program jest używany przez firmę zatrudniającą aktorów teatralnych do grania w różnych przedstawieniach. Klienci zamawiają przedstawienia, a firma wystawia rachunki uzależnione od przedstawienia i liczebności publiki. Do wyboru są dwa rodzaje przedstawień: tragedie i komedie. Firma również przyznaje punkty promocyjne, które można wymieniać na rabaty za przyszłe przedstawienia.

Aktorzy zapisują dane przedstawień w pliku ```plays.json```, dane do rachunku są zapisane w pliku ```invoices.json```.

---

## Narzędzia
+ Wily
+ Radon
---
## Proces refaktoryzacji
>### ```statement_v0.py```
>#### Metryki:
>+ Maintainability Index (MI): 65.9664
>+ Lines of Code (LOC): 42
>+ Cyclomatic Complexity (CC): 7
>
>#### Code smells
>+ Powielony kod (Duplicated Code)
>+ Długa metoda (Long method)


>### ```statement_v1.py```
>#### Metryki:
>+ Maintainability Index (MI): 72.16
>+ Lines of Code (LOC): 76
>+ Cyclomatic Complexity (CC): 15
>
>#### Dokonane refaktoryzacje:
>+ Ekstrakcja metody (Extract Method)
>    - utworzenie funkcji openJsonFile()
>    - utworzenie funkcji amountFor()
>    - utworzenie funkcji playFor()
>    - utworzenie funkcji volumeCreditsFor()
>    - utworzenie funkcji totalVolumeCredits()
>    - utworzenie funkcji totalAmount()
>
>+ Zmiana nazw zmiennych 
>    - perf -> aPerformance
>    - użycie nazwy result w nowych funkcjach
>
>+ Zmniejszenie liczby parametrów
>    - usunięcie parametru play z funkcji amountFor()
>
>+ Zastąpienie zmiennej tymczasowej zapytaniem
>    - wchłonięcie zmiennej play i użycie w jej miejsce funkcji playFor()
>    - wchłonięcie zmiennej thisAmount i użycie w jej miejsce funkcji amountFor()

