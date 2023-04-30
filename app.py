from tkinter import *

class BankAccount:
    def __init__(self, name, dob, pin):
        self.name = name
        self.dob = dob
        self.pin = pin
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
            
class BankApp:
    def __init__(self, master):
        self.master = master
        master.title("Bank App")
        
        self.label_name = Label(master, text="Name:")
        self.label_name.grid(row=0, column=0)
        
        self.entry_name = Entry(master)
        self.entry_name.grid(row=0, column=1)
        
        self.label_dob = Label(master, text="Date of Birth:")
        self.label_dob.grid(row=1, column=0)
        
        self.entry_dob = Entry(master)
        self.entry_dob.grid(row=1, column=1)
        
        self.label_pin = Label(master, text="PIN:")
        self.label_pin.grid(row=2, column=0)
        
        self.entry_pin = Entry(master, show="*")
        self.entry_pin.grid(row=2, column=1)
        
        self.button_create = Button(master, text="Create Account", command=self.create_account)
        self.button_create.grid(row=3, column=0, columnspan=2)
        
        self.label_balance = Label(master, text="Balance: $0.00")
        self.label_balance.grid(row=4, column=0, columnspan=2)
        
        self.label_deposit = Label(master, text="Deposit Amount:")
        self.label_deposit.grid(row=5, column=0)
        
        self.entry_deposit = Entry(master)
        self.entry_deposit.grid(row=5, column=1)
        
        self.button_deposit = Button(master, text="Deposit", command=self.deposit_money)
        self.button_deposit.grid(row=6, column=0, columnspan=2)
        
        self.label_withdraw = Label(master, text="Withdraw Amount:")
        self.label_withdraw.grid(row=7, column=0)
        
        self.entry_withdraw = Entry(master)
        self.entry_withdraw.grid(row=7, column=1)
        
        self.button_withdraw = Button(master, text="Withdraw", command=self.withdraw_money)
        self.button_withdraw.grid(row=8, column=0, columnspan=2)
        
    def create_account(self):
        name = self.entry_name.get()
        dob = self.entry_dob.get()
        pin = self.entry_pin.get()
        
        self.account = BankAccount(name, dob, pin)
        self.label_balance.config(text=f"Balance: ${self.account.balance:.2f}")
        
    def deposit_money(self):
        amount = float(self.entry_deposit.get())
        self.account.deposit(amount)
        self.label_balance.config(text=f"Balance: ${self.account.balance:.2f}")
        
    def withdraw_money(self):
        amount = float(self.entry_withdraw.get())
        self.account.withdraw(amount)
        self.label_balance.config(text=f"Balance: ${self.account.balance:.2f}")
        

root = Tk()
app = BankApp(root)
root.mainloop()
