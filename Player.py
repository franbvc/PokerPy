class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f'{self.name}: {self.money} chips'