import random
n = input("What is your name?")
print("Good Luck!",n)
words = ['abinaya','sai','sharmi','sharmila','nancy','monics','priya','savi','Keerthana','gopics']
word = random.choice(words)
print("guess the word")
guessing = ''
turns = 10
while turns > 0:
    fail = 0
    for char in word:
        if char in guessing:
            print(char, end=" ")
        else:
            print("_")
            fail += 1
    if fail == 0:
        print("your win")
        print("the word is:",word)
        break
    guess = input("Guess the character:")
    guessing += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have",+ turns,'more guessing try again')
    if turns == 0:
              print("you lose")
    
