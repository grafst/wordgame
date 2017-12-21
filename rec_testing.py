from game import *

def match(a,b):
    matching = 0
    for i in range(0, len(a)):
        if a[i] == b[i]:
            matching += 1
    return matching


def recplay(game, remaining, guessed):
    print("attempts left: "+str(game.get_attempts()))

    if game.get_password() in guessed:
        return 1
    if game.get_attempts() <= 0:
        return 0

    if not guessed:
        sample = random.sample(remaining,2)
#        choice = random.choice(remaining)
#        print("random choice: " + choice)
        for guess in sample:
            guessed[guess] = game.play(guess)
#        guessed[choice] = game.play(choice)

    remaining = list(set(remaining) - set(guessed.keys()))

    #magic code
    candidates = {}
    for guess in guessed.keys():
        for word in remaining:
            matching=match(word,guess)
            if not (guessed[guess] == -1 and matching > 0) or not (guessed[guess] == 1 and matching == 0):
                candidates[word] = candidates.get(word, 0) + guessed[guess] * (matching)
            else:
                remaining.remove(word)
                print("remove '"+word+"' from remaining")


    new_candidates={}
    for candidate, value in candidates.items():
        new_candidates[value]=candidate
    winner=new_candidates[max(new_candidates.keys())]
    print("'winner' is: '"+winner+"'")

    guessed[winner] = game.play(winner)

    return recplay(game,remaining, guessed)



num = 200
success = 0
for i in range(0,num):
    print("\n\ngame"+str(i))
    game = Game()
    words=game.new_game()
    print(words)
    print("solution: ",game.get_password())
    result=recplay(game,words, guessed={})
    if result:
        success+=1
        print("!!!!!!!!!! S U C E S S !!!!!!!!!!!!!!")
        print("in round ", 4-game.get_attempts())
print(success/num*100)

