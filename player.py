from game import *

game = Game()
words = game.new_game()
print(words)
print(game.get_password())

choice = random.sample(words,3)
remaining = list(set(words) - set(choice))
guesses = {}
won = False

for word in choice:
    round = game.play(word)
    guesses[word] = round[0]
    if round[2]:
        won = True

print(guesses)

if won:
    print("Congratulations! You won!")

for key, value in guesses.items():
    if value > 0:
        guesses[key] = 1
    else:
        guesses[key] = -1

print(guesses)

candidates = {}

for guess in guesses.keys():
    for word in remaining:
        matching = 0
        for i in range(0,len(guess)):
            if word[i] == guess[i]:
                matching += 1
        candidates[word] = candidates.get(word,0) + guesses[guess]*matching

print(candidates)
new_candidates={}
for candidate, value in candidates.items():
    new_candidates[value]=candidate
winner=new_candidates[max(new_candidates.keys())]

print(winner)

final_round = game.play(winner)
print(final_round)