class ATM:
    def insert_card(self):
        print("Card inserted")

    def enter_pin(self, pin):
        print("PIN entered")

    def withdraw_cash(self, amount):
        print(f"Withdrawing {amount}")

atm = ATM()
atm.insert_card()
atm.enter_pin(1234)
atm.withdraw_cash(200)
