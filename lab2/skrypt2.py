import sys 
import cut
import grep
"""
opcje:
grep -i -w //ignoruje wielkosc liter i wyszukuje tylko cale slowa
cut -d -f //separator i kolumna

koniec ctrl+z enter
"""
if sys.argv[1] == "cut":
    cut.cut(sys.argv[2:])
elif sys.argv[1] == "grep":
    grep.grep(sys.argv[2:])
else:
    print("Nieznana komenda")