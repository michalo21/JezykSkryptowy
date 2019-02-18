import sys
a = int(sys.argv[1])
b = int(sys.argv[3])
if sys.argv[2] == "+":
        wynik = a+b
if sys.argv[2] == "-":
        wynik = a-b
if sys.argv[2] == "*":
        wynik = a*b
    
print(wynik)
