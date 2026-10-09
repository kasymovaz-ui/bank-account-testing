import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Zhaina", "123456789")
        self.second_account = BankAccount("Ali", "987654321")

    def test_account_creation(self):
        self.assertEqual(self.account.owner, "Zhaina")
        self.assertEqual(self.account.account_number, "123456789")
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-500)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.deposit("1000")

    def test_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(400)
        self.assertEqual(self.account.get_balance(), 600)

    def test_withdraw_more_than_balance(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_negative_amount(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_withdraw_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.withdraw("500")

    def test_transfer(self):
        self.account.deposit(1000)
        self.account.transfer(self.second_account, 300)

        self.assertEqual(self.account.get_balance(), 700)
        self.assertEqual(self.second_account.get_balance(), 300)

    def test_transfer_more_than_balance(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 1000)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_transfer_negative_amount(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, -100)

        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_transfer_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.transfer(self.second_account, "100")

    def test_transfer_to_same_account(self):
        self.account.deposit(500)

        with self.assertRaises(ValueError):
            self.account.transfer(self.account, 100)

        self.assertEqual(self.account.get_balance(), 500)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_empty_account(self):
        self.assertTrue(self.account.is_empty())

    def test_not_empty_account(self):
        self.account.deposit(100)
        self.assertFalse(self.account.is_empty())


if __name__ == "__main__":
    unittest.main()
