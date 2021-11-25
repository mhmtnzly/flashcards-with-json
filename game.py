import requests
import json
import os
class Game:
    def __init__(self, level,language='english'):
        self.level = level
        self.language = language
        self.known_words = 0
        self.total_words = 20
    def begin(self):
        self.download() # Game start
        with open('data/{}.json'.format(self.language), 'r') as f:
            glossary = json.load(f)
            self.glossary1 = glossary['{}'.format(self.level)]
            self.dutch = [i for i in self.glossary1.keys()]        
    def download(self):
        os.chdir('data')
        self.data_files=[name.split(".")[0]  for name in os.listdir('.') if os.path.isfile(name)]
        if self.language not in self.data_files:
            os.chdir("..")
            url = "https://drive.google.com/uc?export=download&id=17jCwEwaU4SBULqWZx580Bm_iitsh7k_f"
            r = requests.get(url)
            with open("data/{}.json".format(self.language), "wb") as f:
                f.write(r.content)
        else:
            os.chdir("..")   
    def flashcard(self):                                    #In the begin function we reach the words by making list and dictionary.In this function we are returning the flashcards by using that list and the dictionary.
        return [self.dutch[0],self.glossary1[self.dutch[0]]]#And we always returning the first indexes by using pop function in the true_button and false_button function.
    def progress(self, choice):#In this function we are using the information that is provided in true_button and false_button function.This information includes the number of the known words and the total words.We're  
        if choice:             # simply returning those values.
            self.true_button_()
        else: 
            self.false_button_()
        return [self.known_words,self.total_words]  
    def true_button_(self):
        self.known_words+=1
        self.dutch.pop(0)
    def false_button_(self):
        self.total_words+=1
        self.dutch.append(self.dutch[0])
        self.dutch.pop(0)