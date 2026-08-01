class Bankacount:
    def __init__(self,balance):
        self.__balance = balance

    def showbalance(self):
        print(f"Balance: {self.__balance}")

account = Bankacount(5000)

account.showbalance()