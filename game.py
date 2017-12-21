import random
import math

class Game(object):
    def __init__(self, filename="words.txt",word_len=5, attempts=4,sample=8):
        #self.__gameover = False
        #self.__won = False
        self.__filename = filename
        self.__word_len = word_len
        self.__attempts = attempts
        self.__sample = sample
        self.__words = []
        self.__password = ""

    def get_attempts(self):
        return self.__attempts

    def get_password(self):
        return self.__password

    def new_game(self):
        lst = []
        file = open(self.__filename, "r")
        for line in file.readlines():
            line = line.rstrip()
            if len(line) == self.__word_len:
                if line.isalpha():
                    lst.append(line.lower())
        file.close()

        self.__words = random.sample(lst, self.__sample)
        self.__password = random.choice(self.__words)

        return self.__words

    def play(self,guess):
        #if self.__gameover:
        #    raise PermissionError("The game is over!")

        matching = 0
        for i in range(0,self.__word_len):
            if self.__password[i] == guess[i]:
                matching += 1

        if guess == self.__password:
            self.__won = True

        self.__attempts -= 1
        if self.__attempts == 0:
            self.__gameover = True

        if matching > 0:
            return 1
        else:
            return -1
        #return matching -0.5 #self.__attempts, self.__won
