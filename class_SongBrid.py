import class_Brid
class SongBrid(Bird):
    def __init__(self):
            self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)


sb = SongBrid()
sb.sing()