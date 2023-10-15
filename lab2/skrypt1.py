import sys
import operations
def execute_operations(arg):
    print(operations.first_character(arg))
    print(operations.first_two_characters(arg))
    print(operations.all_characters_except_first_two(arg))
    print(operations.penultimate_character(arg))
    print(operations.last_three_characters(arg))
    print(operations.all_characters_in_even_positions(arg))
    print(operations.merge_characters_and_duplicate(arg))        
if __name__ == "__main__":
    execute_operations(sys.argv[1])  