lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self):
        self.name = 'Rolf'
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

# This object gets two proprieties (name, numbers) defined in self
player = LotteryPlayer()
print(player.name)
print(player.numbers)
print(player.total())

## Adding other instance
class LotteryPlayer_v2:
    def __init__(self, name):
        # self.name = 'Rolf'
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

# These are two different instancies of self
#player_one = LotteryPlayer_v2()
#player_two = LotteryPlayer_v2()

# Prove the player_one is different than player_two
# Two differebt objects
#print(player_one == player_two) # False
#print(player_one.name == player_two.name) # True

# But now wean especify an argumet in th init method (name)
# This allow us to define to different player name
player_one = LotteryPlayer_v2('Rolf')
player_one.numbers = (1, 2, 3, 6, 7, 8) # change the oigianl tuple
player_two = LotteryPlayer_v2('John')
print(player_one.name == player_two.name) # False
print(player_one.numbers == player_two.numbers) # False

## Student Class
class Student(object):
    """docstring for Student."""

    def __init__(self, name, school):
        super(Student, self).__init__()
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())
