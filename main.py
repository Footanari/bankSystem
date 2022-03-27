from BankSystemem import system
from BankAccount import account

if __name__ == '__main__':
    system.Register_new_user(account('Aleksander Iliev', 0))
    system.Register_new_user(account('Joe Mama', 0))

    system.accounts[0].deposit(420)
    system.accounts[0].withdraw(69)

    system.Give_loan_to_user(1, 100, 10, 12)

    system.Register_new_user(account('Deez Nuts', 3))
    system.Register_new_user(account('Joe Biden', 99999999999))

    system.Delete_user(0)
    system.Delete_user(0)
