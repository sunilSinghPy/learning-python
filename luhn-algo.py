def main():
    card_number = '4532-0151-1283-0366'
    # Senetize card number
    card_translation = str.maketrans({'-':'',' ':''})
    translated_card_number = card_number.translate(card_translation)
    print( f'\n{translated_card_number}\n' )
    if varify_card_number(translated_card_number):
        print("Valid!")
    else:
        print("Invalid!")

# Varify card Number    
def varify_card_number(card_number):
    # Reversing Card Number to start from the right
    card_number_reversed = card_number[::-1]
    
    # Doubling Every second digit from the right
    sum_of_even_digits = 0
    even_card_digits = card_number_reversed[1::2]
    for digit in even_card_digits:
        digit = int(digit) * 2
        if digit >=10:
            digit = (digit//10) + (digit % 10)
        sum_of_even_digits +=digit
    # Adding every odd digit
    sum_of_odd_digit = 0
    odd_card_digit = card_number_reversed[::2]
    for digit in odd_card_digit:
        sum_of_odd_digit += int(digit)
    total = sum_of_even_digits + sum_of_odd_digit
    print(total)
    return 0 == total % 10
    


main()