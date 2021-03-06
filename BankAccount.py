class account:
    def __init__(self, name, balance, password = ''):
        self.__name = name
        self.__balance = balance
        self.__history = []
        self.__history_id = 0
        self.loan = 0
        self.__passhash = hash(password)

    @property 
    def name(self):
        print(self.__name)
    
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
    
    def return_loan_payment(self, amount):
        if(self.__balance<ammount):
            raise Exception("return ammount greater than balance")
        if(self.loan<ammount):
            ammount=self.loan
        self.__balance -= ammount
        self.loan -= ammount
        self.__history_id += 1
        self.__history.append("transaction N"+str(self.__history_id)+", type � loan payment, amount - "+str(ammount)+", new balance - "+str(self.__balance),", new loan - "+str(self.__loan))

    def checkPassword(self, password = ''):
        return self.__passhash == hash(password)

    def changePassword(self, password = '', newPassword = ''):
        if(self.checkPassword(password)):
            self.__passhash = hash(newPassword)