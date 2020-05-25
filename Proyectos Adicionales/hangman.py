import random

def hangman(word):
    wrong=0
    stages=["",
            "___________       ",
            "           |      ",
            "           |      ",
            "           O      ",
            "          /|\     ",
            "          / \     "]
    win=False
    letters=list(word)
    spaces=["_"]*len(letters)
    while wrong<len(stages) and win==False:
        print("\n")
        print(spaces)
        guess=input("Try to guess a letter and complete the hangman: ")
        if guess in letters:
            cindex=letters.index(guess)
            spaces[cindex]=guess
            letters[cindex]="$"
        else:
            wrong+=1
            print("The letter you selected is not in the word. Try again")
            print("\n".join(stages[0:wrong]))
        if "_" not in spaces:
            win=True
            print("You win! The word was {}".format("".join(spaces)))
    if not win:
        print("You lose! The word was {}".format(word))

if __name__=="__main__":
    list_of_words=["hola","como","estas"]
    randomize=random.randint(0,len(list_of_words)-1)
    hangman(list_of_words[randomize])