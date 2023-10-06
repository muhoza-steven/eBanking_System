#Importing the class BankAccount  from Account module
from Account import BankAccount
#Here I just creating the CreditCardAccount as child class and inherite it from the parent class BankAccount 
class CreditCardAccount(BankAccount):
    def __init__(self, account_owner, balance, account_number,creditLimit ):
        super().__init__(account_owner, balance, account_number)
        self.creditLimit=creditLimit
        #Creating the method that investigate the any purchse made by passing in the amount parameter
    def makePurchase(self,amount):
        creditLimit=(self.getBalance()*50)/100
        #using if condition so that we make sure the amount money for purchase must not be ecceed the credit limit allowed
        if amount>self.creditLimit+self._balance:
            print("please don't buy an expensive product")
        else:
            self._balance-=amount

            # super().withdraw(amount)
       #creating the method __str__ to represent the class information where I used super class in this case to access the method __str__ from the parent class     
    def __str__(self):
        return f"{super().__str__()} Dear client your credit limit is =  {self.creditLimit}"
    # return f'{super().__str__()}, and your overdraft limit =  {self.overdraftLimit}, therefore you new balance is {self.getBalance()}, then you are now allowed to purchase until to  {self.getBalance()+self.overdraftLimit}'
    

if __name__=="__main__":
    #creating the instance of class CreditCardAccount and the passing the urgments needed(namw, balance, account number, credit limit)
    objCreditAccount=CreditCardAccount("Dianne",5000, 144444, 700)
    # print(objCreditAccount)
    # objCreditAccount.makePurchase()
    print(objCreditAccount)
