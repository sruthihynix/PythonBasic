# duck typing
# one obj act or behave like another obj
class animal():
    print("animals performance")
class human:
    def perform(self):
        print("the human performance")

class circus:
    def play(self, animal,animal):
         animal.perform()

tiger=animal()
obj=circus()
obj.play(tiger)
