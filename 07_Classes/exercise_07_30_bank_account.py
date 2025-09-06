class BankAccount:
    """Class BankAccount"""
    def __init__(self, owner: str, balance: int | float = 0) -> None:
        """Constructor for BankAccount"""
        if not isinstance(owner, str):
            raise TypeError(f'Expected type str, got {type(owner).__name__}')
        if not isinstance(balance, int | float):
            raise TypeError(f'Expected type int or float, got {type(balance).__name__}')
        if balance < 0:
            raise ValueError(f'Bank account balance must be greater than zero, got {balance}')
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        """Display balance"""

        print(f'Account name: {self.owner}\nBalance: {self.balance}')

    def withdraw(self, amount:int | float) -> None:
        """Withdraw amount"""
        if amount < 0:
            raise ValueError(f'Amount must be greater than zero, got {amount}')
        if amount > self.balance:
            raise ValueError(f'Amount must be less than or equal to balance, got {amount}')
        self.balance -= amount
        print('Withdraw successful - display Balance'.center(50, '='))
        self.display_balance()

    def deposit(self, amount:int | float) -> None:
        """Deposit amount"""
        if amount < 0:
            raise ValueError(f'Amount must be greater than zero, got {amount}')
        self.balance += amount
        print('Deposit successful - display Balance'.center(50, '='))
        self.display_balance()


if __name__ == '__main__':
    a = BankAccount('Alex', 100)
    a.display_balance()
    a.deposit(150)
    a.withdraw(10)

