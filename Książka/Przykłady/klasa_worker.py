class Worker:
    def __init__(self, name, pay):
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Robert Zielony', 50000)
anna = Worker('Anna Czerwona', 60000)
print(bob.lastName())