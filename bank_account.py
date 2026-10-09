class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.balance -= amount

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Получатель должен быть банковским счётом")

        if other_account is self:
            raise ValueError("Нельзя переводить деньги на тот же счёт")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        if amount > self.balance:
            raise ValueError("Недостаточно средств для перевода")

        self.balance -= amount
        other_account.balance += amount

    def get_balance(self):
        return self.balance

    def is_empty(self):
        return self.balance == 0
