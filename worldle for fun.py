#list for random word
from random import choice
word = ["hello","tiger","phone","table","apple","zebra","learn","books"]
main_word = choice(word)
print(main_word)
keep_loop = 0
while keep_loop < 6:
    input_word = input("Enter 5 charater words: ")
    while len(input_word) > 5 or len(input_word) < 5:
        print("you word is not 5 charaters")
        input_word = input("Enter 5 charater words: ")
    i = 0
    for char in input_word:
            if char == main_word[i]:
                print("yes",char)
            else :
                print("no",char)
            i += 1
    keep_loop += 1
    if input_word == main_word:
        break
    # end=input("want again?(y/n):")
    # keep_loop = end== "y"