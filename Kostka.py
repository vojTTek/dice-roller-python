from random import randrange
print('Losowanie liczby we wskazanym zakresie - wynik losowy')
print('Ile ścian ma mieć kostka?')
s=int(input())
print('Ile rzutów?')
t=int(input())
print('Powyżej jakiej wartości sukces?')
w=int(input())
wynik=[]
for i in range(t):
     wynik.append(randrange(1, s))
     print('wyniki kolejnych rzutów', wynik)
     zaliczone =[n for n in wynik if n>=w] #tutaj można wprowadzić modyfikator
     print('Rzuty powyżej sukcesu:', zaliczone)
