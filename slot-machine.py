import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    # print(all_symbols)
    
    columns = []
    for col in range(cols):
        column = []
        for row in range(rows):
            current_symbol = all_symbols[:]
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    # print(columns)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if(i != len(columns)-1):
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter amount greater than 0.")
        else:
            print("Please Enter a 'Number'")

    return amount
def number_of_lines():
    while True:
        lines = input("Please Enter Number Of lines(1-"+str(MAX_LINES)+"? $ ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please Enter valid Number of LInes")
        else:
            print("Please Enter A Number")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to Bet on Each Line? ")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= 100:
                break
            else:
                print(f"Please enter bet between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please Enter a 'Number'")

    return bet
def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your cant bet ${total_bet} more then your balance ${balance}")
        else:
            break
    print(f"Your are beting ${bet} on {lines} lines total ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"current balance:${balance}")
        answer = input("Press enter to play ('q' to quit.)")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
main()