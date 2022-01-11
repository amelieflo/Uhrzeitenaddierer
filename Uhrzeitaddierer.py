
#Bei diesem Code, musste man, dass es bei zwei ausgewählten Uhrzeiten, es noch zusätzliche Minuten addiert, die wir ausgewählt haben=summand


def uhrzeit_minuten_addieren(stunden, minuten, summand):

  
 

    if minuten+summand >= 60:

      #bei den Stunden soll plus eins gerechnet werden
      stunden=stunden+1


     # bei den Minuten soll minus 60 gerechnet werden, damit es eine neue Stunde gibt Minuten= 0
      minuten=minuten-60

    

    print(str(stunden)+":"+str(minuten+summand))


#Diese 2, werden mit dem Code oben gerechnet werden.
uhrzeit_minuten_addieren(17,32,8)

uhrzeit_minuten_addieren(17,58,20)

