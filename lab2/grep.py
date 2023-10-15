import re
import sys

def grep(args):
    matching_lines = []
    if((args[0]=="-i" and args[1]=="-w") or (args[0]=="-w" and args[1]=="-i")): # ignoruje wielkosc liter i wyszukuje tylko cale slowa
        try:
            pattern = re.compile(r'\b'+args[2]+r'\b', re.IGNORECASE)
        except IndexError:
            print("Nie podano wzorca")
            return
        for line in sys.stdin:
            if pattern.search(line):
                matching_lines.append(line)
        print("".join(matching_lines))
    elif(args[0]=="-i"): # ignoruje wielkosc liter
        try:
            pattern = re.compile(args[1], re.IGNORECASE)
        except IndexError:
            print("Nie podano wzorca")
            return
        for line in sys.stdin:
            if pattern.search(line):
                matching_lines.append(line)
        print("".join(matching_lines))
    elif(args[0]=="-w"):
        try:
            pattern = re.compile(r'\b'+args[1]+r'\b') #b - tylko cale slowa
        except IndexError:
            print("Nie podano wzorca")
            return
        for line in sys.stdin:
            if pattern.search(line):
                matching_lines.append(line)
        print("".join(matching_lines))
    else: # bez flagi
        try:
            pattern = re.compile(args[0])
        except IndexError:
            print("Nie podano wzorca")
            return
        for line in sys.stdin:
            if pattern.search(line):
                matching_lines.append(line)
        print("".join(matching_lines))
    