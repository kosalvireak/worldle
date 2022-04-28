#list for random word
from random import choice
word = ["hello","tiger","phone","table","apple","zebra","learn"]
main_word = choice(word)
print(main_word)
print(main_word[2])
input_word = input("Enter 5 charater words: ")
i = 0
for char in input_word:
    if char == main_word[i]:
        print("yes",char)
    else :
        print("no",char)
    i += 1