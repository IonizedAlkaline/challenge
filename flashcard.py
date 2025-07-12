class Flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    
    def __str__(self):
        return self.word + "(" + self.meaning + ")"
flash = []

while True:
    word = input('enter the word: ')
    meaning = input('enter the meaning: ')
    flash.append(Flashcard(word,meaning))

    option = int(input("do you want to continue 0 if no 1 if yes: "))
    if option == 1:
        break
for i in flash:
    print(i)