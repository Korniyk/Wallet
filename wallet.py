class Wallet:
    def __init__(self, balance=0):
        """Ініціалізація гаманця з початковим балансом"""
        self.balance = balance

    def deposit(self, amount):
        """Додає кошти до гаманця"""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Знімає кошти з гаманця, якщо є достатньо коштів"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        """Повертає поточний баланс"""
        return self.balance


# Приклад використання
if __name__ == "__main__":
    my_wallet = Wallet(100)
    print("Початковий баланс:", my_wallet.get_balance())

    my_wallet.deposit(50)
    print("Після поповнення:", my_wallet.get_balance())

    my_wallet.withdraw(30)
    print("Після зняття:", my_wallet.get_balance())
