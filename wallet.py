import pytest


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


# Тести для Wallet
@pytest.fixture
def wallet():
    return Wallet(100)


def test_initial_balance(wallet):
    assert wallet.get_balance() == 100


def test_deposit(wallet):
    wallet.deposit(50)
    assert wallet.get_balance() == 150


def test_withdraw_success(wallet):
    assert wallet.withdraw(30) is True
    assert wallet.get_balance() == 70


def test_withdraw_fail(wallet):
    assert wallet.withdraw(200) is False
    assert wallet.get_balance() == 100
