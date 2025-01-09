import random
num = random.randint(1,20)
count = 1
while count <5 :
    guess = int(input('Guess the number :'))
    if guess > num:
        print("Your number is biggier")
    elif guess < num:
        print("Your number is smaller")
    else:
        break
    count = count + 1
if num == guess:
    print("Hurrre!!! YOu have guess the Number in " + str(count)+" attempt")
else:
    print("The correct number is " + str(num) + ".")