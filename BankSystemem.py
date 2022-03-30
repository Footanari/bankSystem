from BankAccount import account

class system:
    accounts = []
    moneyInBank = 0
    def Register_new_user(new_Bank_Account:account): #( new_Bank_Account : BankAcconut )
        system.accounts.append(new_Bank_Account)
        return len(system.accounts) - 1
    def Delete_user(user_id):
        system.accounts.remove(system.accounts[user_id])
    def Give_loan_to_user(user_id, amount, interest, return_period_in_months):
        system.accounts[user_id].loan += amount + interest
        system.accounts[user_id].deposit(amount)
    def Show_all_transactions(user_id = ""):
        if user_id == "":
            for user in system.accounts:
                user.print_all_transactions()
            return
        system.accounts[user_id].print_all_transactions()
    def withdrawFrom(user_id, amount):
        if system.moneyInBank < amount:
            raise Exception('Not enough money to withdraw from bank')
        system.accounts[user_id].withdraw(amount)
        system.moneyInBank -= amount
    def depositTo(user_id, amount):
        system.accounts[user_id].deposit(amount)
        system.moneyInBank += amount