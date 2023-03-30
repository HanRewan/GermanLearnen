import random
from deep_translator import GoogleTranslator


class Word:

    def __init__(self, translation, article, forms):
        self.translation = translation
        self.forms = forms
        self.article = article

    def convertToStr(self):
        string = self.translation + " - "
        string += self.article + " - " + self.forms

        return string


class DictParser:

    def __init__(self):
        self.dict = []

    def parseDoc(self, path):
        with open(path, 'r') as file:
            for line in file:
                line = line.replace('\n', '')
                line = line.split(" - ")
                translation, article, forms = line[0], line[1], line[2:len(line)]
                self.dict.append(Word(translation, article, forms))

    def writeDoc(self, path):
        open(path, 'w').close()
        with open(path, 'w') as file:
            for word in self.dict:
                file.write(word.convertToStr()+"\n")

    def shuffleDict(self):
        random.shuffle(self.dict)

    def unRawDoc(self, path):
        with open(path, 'r') as file:
            for line in file:
                line = line.replace('\n', '')
                line = line.split(" ")
                article, forms = line[0], line[1]
                translation = GoogleTranslator(source='de', target='uk').translate(forms)
                self.dict.append(Word(translation, article, forms))

        self.writeDoc(path)