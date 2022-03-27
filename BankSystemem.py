from BankAccount import account as bank

class system:
    accounts = []
    moneyInBank = 0
    def Register_new_user(new_Bank_Account:bank.account): #( new_Bank_Account : BankAcconut )
        system.accounts.append()
        return len(system.accounts) - 1
    def Delete_user(user_id):
        system.accounts.remove(system.accounts[user_id])
    def Give_loan_to_user(user_id, amount, interest, return_period_in_months):
        pass
    def Show_all_transactions(user_id = ""):
        if user_id == "":
            for user in system.accounts:
                user.print_all_transactions()
            return
        system.accounts[user_id].print_all_transactions()
        