from game import *

def play():
    game = Game()
    words = game.new_game()

    choice = random.sample(words,3)
    remaining = list(set(words) - set(choice))
    guesses = {}
    won = 0

    for word in choice:
        round = game.play(word)
        guesses[word] = round[0]
        if round[2]:
            won = 1

    for key, value in guesses.items():
        if value > 0:
            guesses[key] = 1
        else:
            guesses[key] = -1

    candidates = {}
    for guess in guesses.keys():
        for word in remaining:
            matching = 0
            for i in range(0, len(guess)):
                if word[i] == guess[i]:
                    matching += 1
            candidates[word] = candidates.get(word, 0) + guesses[guess] * matching

    new_candidates={}
    for candidate, value in candidates.items():
        new_candidates[value]=candidate
    winner=new_candidates[max(new_candidates.keys())]

    final_round = game.play(winner)
    if final_round[2]:
        won = 1

    return won

num = 1000
success = 0
for i in range(0,num):
    success += play()

print(success/num*100)
