import itertools

def get_pins(observed):
    # 1. Define the adjacent digits for each key on the keypad
    adjacents = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0']
    }
    
    # 2. Get the list of possible digits for each position in the observed PIN
    possible_digits = [adjacents[digit] for digit in observed]
    
    # 3. Use product to find all combinations and join them into strings
    # product(['1','2'], ['3','4']) -> ('1','3'), ('1','4'), etc.
    combinations = list(itertools.product(*possible_digits))
    pins = [''.join(combo) for combo in combinations]
    
    # 4. Return the list sorted in ascending order
    return sorted(pins)

# Example Usage:
print(get_pins("1111"))