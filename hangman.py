import random
words = ['english','hippopotamous','sunil','elephant','umberella']
word = random.choice(words)
print(word)
#word_char_list = list(word)
number_of_attampt = 10
print_blank = '_'
print_blank = print_blank * len(word)

while(number_of_attampt):
    print(print_blank)
    guess_char = input("Enter Your Guess: ")

    while True:
        if(guess_char.isalpha() and len(guess_char) == 1):
            break
        else:
            guess_char = input("Wrong Input! Enter Your Guess: ")
    
    if guess_char in word:
        for i in word_char_list:
            if word_char_list[i] == guess_char:
                pass

    number_of_attampt = number_of_attampt-1