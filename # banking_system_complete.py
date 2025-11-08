# banking_system_complete.py
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, holder, balance=0.0):
        self._acc_no = acc_no
        self._holder = holder
        self._balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def show_details(self):
        pass
    
    def get_balance(self):
        return self._balance
    
    def _set_balance(self, amount):
        self._balance = amount


class SavingsAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount:,.2f} deposited to Savings A/c")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance!")
        elif amount > 50000:
            print("Daily limit exceeded!")
        else:
            self._balance -= amount
            print(f"₹{amount:,.2f} withdrawn")
    
    def add_interest(self, rate=0.04):
        interest = self._balance * rate
        self._balance += interest
        print(f"Interest ₹{interest:,.2f} credited")
    
    def show_details(self):
        print(f"SAVINGS ACCOUNT")
        print(f"Holder: {self._holder}")
        print(f"A/c No: {self._acc_no}")
        print(f"Balance: ₹{self._balance:,.2f}")
        print("-" * 40)


class CurrentAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount:,.2f} deposited to Current A/c")
    
    def withdraw(self, amount):
        if self._balance - amount >= -100000:
            self._balance -= amount
            print(f"₹{amount:,.2f} withdrawn")
            if self._balance < 0:
                print(f"Overdraft used: ₹{-self._balance:,.2f}")
        else:
            print("Overdraft limit exceeded!")
    
    def show_details(self):
        print(f"CURRENT ACCOUNT")
        print(f"Holder: {self._holder}")
        print(f"A/c No: {sel# banking_system_complete.py
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, holder, balance=0.0):
        self._acc_no = acc_no
        self._holder = holder
        self._balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def show_details(self):
        pass
    
    def get_balance(self):
        return self._balance
    
    def _set_balance(self, amount):
        self._balance = amount


class SavingsAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount:,.2f} deposited to Savings A/c")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance!")
        elif amount > 50000:
            print("Daily limit exceeded!")
        else:
            self._balance -= amount
            print(f"₹{amount:,.2f} withdrawn")
    
    def add_interest(self, rate=0.04):
        interest = self._balance * rate
        self._balance += interest
        print(f"Interest ₹{interest:,.2f} credited")
    
    def show_details(self):
        print(f"SAVINGS ACCOUNT")
        print(f"Holder: {self._holder}")
        print(f"A/c No: {self._acc_no}")
        print(f"Balance: ₹{self._balance:,.2f}")
        print("-" * 40)


class CurrentAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount:,.2f} deposited to Current A/c")
    
    def withdraw(self, amount):
        if self._balance - amount >= -100000:
            self._balance -= amount
            print(f"₹{amount:,.2f} withdrawn")
            if self._balance < 0:
                print(f"Overdraft used: ₹{-self._balance:,.2f}")
        else:
            print("Overdraft limit exceeded!")
    
    def show_details(self):
        print(f"CURRENT ACCOUNT")
        print(f"Holder: {self._holder}")
        print(f"A/c No: {self._acc_no}")
        print(f"Balance: ₹{self._balance:,.2f}")
        if self._balance < 0:
            print(f"Overdraft: ₹{-self._balance:,.2f}")
        print("-" * 40)


# Demo with polymorphism
if __name__ == "__main__":
    accounts = [
        SavingsAccount("SAV001", "Rahul Kumar", 30000),
        CurrentAccount("CUR001", "ABC Traders", 50000)
    ]
    
    print("BANKING SYSTEM WITH POLYMORPHISM\n")
    
    for acc in accounts:
        acc.deposit(10000)
        acc.withdraw(15000)
        acc.show_details()f._acc_no}")
        print(f"Balance: ₹{self._balance:,.2f}")
        if self._balance < 0:
            print(f"Overdraft: ₹{-self._balance:,.2f}")
        print("-" * 40)


# Demo with polymorphism
if __name__ == "__main__":
    accounts = [
        SavingsAccount("SAV001", "Rahul Kumar", 30000),
        CurrentAccount("CUR001", "ABC Traders", 50000)
    ]
    
    print("BANKING SYSTEM WITH POLYMORPHISM\n")
    
    for acc in accounts:
        acc.deposit(10000)
        acc.withdraw(15000)
        acc.show_details()


        #### Output Example ####
        # BANKING SYSTEM WITH POLYMORPHISM      

₹10,000.00 deposited to Savings A/c
₹15,000.00 withdrawn
SAVINGS ACCOUNT
Holder: Rahul Kumar
A/c No: SAV001
Balance: ₹25,000.00
----------------------------------------
₹10,000.00 deposited to Current A/c
₹15,000.00 withdrawn
CURRENT ACCOUNT
Holder: ABC Traders
A/c No: CUR001
Balance: ₹45,000.00