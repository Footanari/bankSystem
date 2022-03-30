from BankSystemem import system
from BankAccount import account

if __name__ == '__main__':
    system.Register_new_user(account('Aleksander Iliev', 0))
    system.Register_new_user(account('Joe Mama', 0))

    system.depositTo(0, 420)
    system.withdrawFrom(0, 69)

    system.Give_loan_to_user(1, 100, 10, 12)

    system.Register_new_user(account('Deez Nuts', 3))
    system.Register_new_user(account('Joe Biden', 99999999999))

    system.Delete_user(0)
    system.Delete_user(0)

    system.Register_new_user(account('Sugondese Nuts', 1, 'password1234'))

    print(system.accounts[2].checkPassword('1234'))
    print(system.accounts[2].checkPassword('password1234'))
    system.accounts[2].changePassword('password1234', 'VerySecurePassword123456')
    print(system.accounts[2].checkPassword('password1234'))
    print(system.accounts[2].checkPassword('VerySecurePassword123456'))