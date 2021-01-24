from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为六面"""
        self.num_sides = num_sides


    def rool(self):
        """返回一个随机数"""
        return randint(1,self.num_sides)