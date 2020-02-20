class Animal:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print('{}!걷는다!'.format(self.name))

    def eat(self):
        print('{}! 먹는다!'.format(self.name))

class Dog(Animal):
    def run(self):
        print('{}! 달린다!'.format(self.name))

    def walk(self):
        print('{}! 달린다!'.format(self.name))

class Bird(Animal):
    def fly(self):
        print('{}! 푸드덕!'.format(self.name))

dog=Dog('멍멍이')
dog.walk()
dog.run()

bird=Bird('구구')
bird.walk()
bird.eat()
bird.fly()