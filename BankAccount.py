class account:
    def __init__(self, name):
        self.__name = name
        self.__balance = 0
        self.__history = []
        self.__history_id = 0
    
    def print_all_transactions(self):
        print(self.__history)

    def deposit(self, ammount):
        self.__balance += ammount
        self.__history_id += 1
        self.__history.append("transaction N"+str(self.__history_id)+", type � deposit, amount - "+str(ammount)+", new balance - "+str(self.__balance))
    
    def withdraw(self, ammount):
        if(self.__balance<ammount):
            raise Exception("withdraw ammount greater than balance")
        self.__balance -= ammount
        self.__history_id += 1
        self.__history.append("transaction N"+str(self.__history_id)+", type � withdraw, amount - "+str(ammount)+", new balance - "+str(self.__balance))

