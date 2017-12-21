import random

word_len = 5
attempts = 4
sample = 8


lst = []
file = open("words.txt","r")
for line in file.readlines():
    line = line.rstrip()
    if len(line) == word_len:
        if line.isalpha():
            lst.append(line.lower())
file.close()

words = random.sample(lst,sample)
password = random.choice(words)
print(words)

while True:
    guess = input("Please give your guess:\n")
    matching = 0
    for i in range(0,word_len):
        if password[i] == guess[i]:
            matching += 1
    print("{0:d}/{1:d} correct".format(matching, word_len))
    if guess == password:
        print("Access granted")
        break
    attempts -= 1
    print("{0:d} attempts remaining".format(attempts))


