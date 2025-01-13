import random
words = ['english','hippopotamous','sunil','elephant','umberella']
word = random.choice(words)
print(word)
#word_char_list = list(word)
number_of_attampt = 10
blank = '_'
print_blank = blank * len(word)
blank_list = list(print_blank)

while(number_of_attampt):
    word_char_list = list(word)
    print(word_char_list)
    guess_char = input("Enter Your Guess: ")

# input value check loop
    while True:
        if(guess_char.isalpha() and len(guess_char) == 1):
            break
        else:
            guess_char = input("Wrong Input! Enter Your Guess: ")
    if blank in blank_list:
        if guess_char in word_char_list:
            for i in word_char_list:
                print(word_char_list.index(i),i) 
                if guess_char == i:
                    word_char_list = word_char_list
                    blank_list[word_char_list.index(i)] =i
    else:
        print(f"You gussed the word ({word}) in number of attampt ")
    print(blank in blank_list)
    print(blank,blank_list)
    number_of_attampt = number_of_attampt-1  #coders block 