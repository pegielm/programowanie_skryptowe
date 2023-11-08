print("start")
import sys
def display(args,show_index):
    for arg in args:
        if(show_index):
            print(f"args[{args.index(arg)}]={arg}")
        else:
            print(arg)
def run(moves, move_descriptions):
    for move in moves:
        if move in move_descriptions:
            print(move_descriptions[move])

move_descriptions = {
    "f": "Zwierzak idzie do przodu",
    "b": "Zwierzak idzie do tyłu",
    "l": "Zwierzak skręca w lewo",
    "r": "Zwierzak skręca w prawo"

}
#display(sys.argv,True)
#display(sys.argv,False)
run(sys.argv[1:], move_descriptions)
print("stop")