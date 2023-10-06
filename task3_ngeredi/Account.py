#Creating the basic(parent) class named Bank account
class BankAccount():
    #initializing the attributes of the calss bank account by using the constructor __init__
    def __init__(self, account_owner, balance,account_number):
        self._account_owner=account_owner
        self._balance=balance
        self._account_number=account_number
        #creating the method of deposit that will allow the user to depositing the money on his account
    def deposit(self, amount):
        self._balance+=amount
        #creating the method of deposit that will allow the user to depositing the money on his account
    def withdraw(self, amount):
        if amount>self._balance:
            print('Insuficient balance')
        else:
            self._balance-=amount
        # self._amount=amount
        #here aftre is are series of getter and setter for all class attributes
        #setter for account number
    def setAccountNumber(self):
        self._account_number=account_number
        #getter for account number
    def getAccountNumber(self):
        return self._account_number
    #setter for account owner
    def setAccountOnwner(self):
        self._account_owner=account_owner
        #getter for account owner
    def getAccountOwner(self):
        return self._account_owner
    #setter for acoount balance
    def setBalance(self):
        self._balance=balance
        #getter for account balance
    def getBalance(self):
        return self._balance
    #creating str method just for providing the account information
    def __str__(self):
        #return and display the account information
        return f'\nThe account number is {self._account_number} and acount name is {self._account_owner} and the balance is {self._balance}\n'
    
#declaring the variable __name__ for just test the codes only in this current module

# if __name__=="__main__":
#     #initializing the instance objAccount for the class BankAccount
#     objAccount=BankAccount("Geredi NIYIBIGIRA",2000, 218007257)
#     print(objAccount)
#     #for example I deposite 3000 on bank account
#     objAccount.deposit(3000)
#     print(objAccount)
#     #when I withdraw 1500 from the account 
#     objAccount.withdraw(1500)
#     print(objAccount)
#     # objAccount.withdraw(5000)
#     # print(objAccount)

    
        
        
        