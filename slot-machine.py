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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

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
def main():
    balance = deposit()
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your cant bet ${total_bet} more then your balance ${balance}")
        else:
            print(f"Your are beting ${bet} on {lines} lines total ${total_bet}")
            break



main()