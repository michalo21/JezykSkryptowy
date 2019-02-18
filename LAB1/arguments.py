import sys
a = len(sys.argv)
licznik = 0
zdanie = ""
for x in reversed(range(1, a)):
    if(len(sys.argv[x])>=3):
        licznik += 1
        zdanie += sys.argv[x]
        zdanie  += ' '
print(licznik)
print(zdanie)
