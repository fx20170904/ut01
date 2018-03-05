from random import randint

x = randint(1, 6)

class Die():

    def __init__(self, sides=6):
       self.sides = sides

    def roll_die(self):
        side_num = randint(1, self.sides)
        return side_num


for num in range(0, 20):
    side = Die()
    print("第 " + str(num) + '局点数：' + str(side.roll_die()))
