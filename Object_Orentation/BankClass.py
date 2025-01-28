class Bank:
    bank_name = 'SBI' #class based variable
    def __init__(self,name,age,balance):
        #instance variable
        self.name = name 
        self.age = age
        self.balance = balance
    
    def get_info(self):
        print(f'''User Name: {self.name} and
User Balance: {self.balance}
for Bank {Bank.bank_name} ''') # In place of {Bank.bank_name} we can also write {self.bank_name}


b1 = Bank("tesuj",25,55000)

print(Bank.bank_name) #SBI
print(b1.bank_name)

b1.get_info()