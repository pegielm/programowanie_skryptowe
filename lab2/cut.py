import re
import sys
def cut(args):
    result = []
    if(args[0]=="-d"):
        separator = args[1]
        if(args[2]=="-f"):
            try:
                column = int(args[3])
            except ValueError:
                print("Nie podano kolumny")
                return
            for line in sys.stdin:
                line = line.split(separator)
                try:
                    result.append(line[column-1])
                except IndexError:
                    print("Nie ma takiej kolumny")
                    return
            print("\n".join(result))
        else:
            print("Nie podano kolumny")
            return
    else:
        print("Nie podano separatora")
        return