import random
a = random.randrange(1,500)
file = open("word.txt")
line = file.readlines()

main_word = line[a]
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