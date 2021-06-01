class People :
    def __init__(self, name, age, eating=False, speaking=False, ) :
        self.name=name
        self.age=age
        self.eating=eating
        self.speaking=speaking

    def speak(self,subject):
        if self.eating:
            print( f'{self.name} is already eating and cant speak' )
            return
        if self.speaking:
            print(f'{self.name} is already speaking')
            return
        print(f'{self.name} is speaking about {subject}')
        self.speaking = True

    def stop_speaking(self):
        if not self.speaking:
            print( f'{self.name} is not speaking')
            return
        print(f'{self.name} stopped speaking')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print( f'{self.name} is already eating' )
            return
        print(f'{self.name} is eating {food}')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating')
            return
        print(f'{self.name} stops eating')
        self.eating = False

