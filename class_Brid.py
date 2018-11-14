class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaaah...')
            self.hungry = False
        else:
            print('No,thanks!')

#b = Bird()
#b.eat()

#b.eat()

class SongBrid(Bird):
    def __init__(self):
            Bird.__init__(self)
            self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)


sb = SongBrid()
sb.sing()
sb.eat()
sb.eat()



