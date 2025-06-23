import random
name = input('Give me your name : ')
print('Hi!',{name})
print("Let us start the game")
words = ["apple", "banana", "carrot", "dragon", "eclipse",
    "forest", "guitar", "harmony", "island", "jungle",
    "keyboard", "lemon", "mountain", "nebula", "ocean",
    "piano", "quartz", "river", "sunset", "tornado",
    "umbrella", "volcano", "whisper", "xenon", "yacht", "zephyr"]
Pick = random.choice(words)
print('Guess the charecter : ')
Guesses = ''
turns = 12

while turns >0:

    failed =0

    for char in Pick:

        if char in Guesses :
            print(char, end=" ")
        
        else:
             print('_')
             failed += 1

    if failed==0:
        print('You Win!. And the word is ', Pick)
        break
    
    print()
    guess = input('Give a Guess : ')
    Guesses+=guess

    if guess not in Pick:
        turns-=1
        print('Wrong')
        print('You have', + turns , 'left!!')


        if turns==0:
            print('You Loose and the world is : ', Pick)