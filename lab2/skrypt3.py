import argparse
import grep
import cut
import sys
from skrypt1 import execute_operations

"""
opcje:
grep -i -w //ignoruje wielkosc liter i wyszukuje tylko cale slowa
MUSI BYC KOLEJNOSC WZORZEC -i -w


cut -d -f //separator i kolumna

koniec ctrl+z enter
"""

parser = argparse.ArgumentParser(prog='skrypt3.py', description='skrypt1 lub skrypt2')
parser.add_argument('command', type=str, help='grep lub cut')
parser.add_argument('-i', action='store_true', help='ignoruje wielkosc liter')
parser.add_argument('-w', action='store_true', help='wyszukuje tylko cale slowa')
parser.add_argument('-d', type=str, help='separator dla cut')
parser.add_argument('-f', type=int, help='kolumna dla cut')
parser.add_argument('text', type=str, help='tekst dla grep',nargs='*') ## jak zrobić żeby było opcjonalne?

args = parser.parse_args()


    

print(args)

formated_options = []

if args.command=="grep":
    #text = input("Podaj wzorzec: ")
    if args.text == None:
        print("brak wzorca")
        sys.exit(0)
    text = args.text[0]
    if args.i :
        formated_options.append("-i")
    if args.w :
        formated_options.append("-w")
    
    
    formated_options.append(text)
    #print(formated_options)
    grep.grep(formated_options)
elif args.command=="cut" :
    if args.d :
        formated_options.append("-d")
        formated_options.append(args.d)
    if args.f :
        formated_options.append("-f")
        formated_options.append(str(args.f))
    #print(formated_options)
    cut.cut(formated_options)
else:
    print("Nieznana komenda")
    #print(args.command)
    execute_operations(args.command)





