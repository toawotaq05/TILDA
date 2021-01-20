### Föreläsning 2

## Abstrakta datatyper

# Abstraktion
Fördelar med abstraktion är
* Det är lättare att överblicka program om delproblem är lösta separat
* Användaren och konstruktören kommer överens om vad som ska kunnas göras och vilken data som ska utnyttjas. Det är ett slags gränssnitt.
* Användaren behöver inte bry sig hur det kommer implementeras.
* Om implementationen ändras så kommer inte användaren att behöva ändra sin kod, givet att gränssnittet är detsamma.

# Fördel med abstrakta datatyper jämfört med konkret datatyp
* Misstag att ha datum som konkret datatyp kostade hundratals miljarder i omprogrammeringskostnader vid tusenårsskiftet.
* specifikation av vilka anrop som finns kallas datatypens gränssnitt och är det enda användaren behöver känna till.

## ny klass i python
```python
class Trams:
    def __init__(self):  
        self.x=0
```




## Kö

* Queue()                 # skapa en tom kö
* enqueue(x)          # stoppa in något sist i kön
* x = dequeue()     # plocka ut det som står först i kön
* isEmpty()              # kolla om kön är tom
* n = size()                        # antalet element i kön

FIFO = first in, first served. 


## Stack

Är som en trave tallrikar - det man lägger överst på stacken är det som kommer att tas bort först.

* push(X): lägg x överst på stacken.
* x=pop(): Plocka ut och returnera det som ligger överst.
* isEmpty(): Undersök om stacken är tom.

## Abstrakt deque

Är en tvåändad kö. 
* addFront(x): lägg in x först
* addRear(x): lägg in x sist
* x = removeFront(): Plocka ut och returnera det som ligger först
* removeRear(): Plocka ut och returnera det som ligger sist
* isEmpty(): Undersök om dequen är tom