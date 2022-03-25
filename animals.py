# -*- 
class Dog:
    numOfDogs=0
    def __init__(self ,n ,col ,eyecol,l=30,w=1,nation='jp'):
        Dog.numOfDogs +=1
        self.name=n
        self.color=col
        self.eycolor=eyecol
        self.length=l
        self.weight=w
        self.nationlty=nation
    def run (self):
        print(self.name ,'is running now')
    def set(self,command):
        if command== 'ni haw' and self.nationlty =='jp':
            print(self.name , 'is sitting now and nihi nihi')
        elif command== 'sitDown' and self.nationlty =='england' :
            print(self.name , 'is sitting now and welcome')
        elif command== 'rayah' and self.nationlty =='egy':
            print(self.name , 'is sitting now and betmarag')
        else : ('the sog didnot understand')