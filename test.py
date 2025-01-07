import random
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    print(all_symbols)
    
    columns = []
    for col in range(cols):
        column = []
        for row in range(rows):
            current_symbol = all_symbols[:]
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    print(columns)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if(i != len(columns)-1):
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
print_slot_machine(slots)