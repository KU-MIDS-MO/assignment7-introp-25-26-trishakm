def make_account(initial_balance):
    if initial_balance < 0:
        raise ValueError("Please input a positive value")

    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Amount must be positive")
        balance = balance + amount  
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance = balance - amount
        return balance

    return deposit, withdraw
    pass





#Write a function:

#make_account(initial_balance)

#that creates and returns two functions representing operations on a bank account:

#- a function for depositing money,

#- a function for withdrawing money.

#The account balance must be initialized using initial_balance and must persist betwen function calls.

#The following rules apply;

#- Deposits and withdrawals must use positive numeric values.

#- The account balance must never become negative.

#- Invalid operations must raise appropriate Python exceptions.

#- The account balance must not be directly accessible from outside the returned functions.