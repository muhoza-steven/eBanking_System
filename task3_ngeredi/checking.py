#Importing the class BankAccount  from Account module
from Account import BankAccount
#Creating the class CheckingAccount and inherits it from BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_owner, balance, account_number,overdraftLimit):
        super().__init__(account_owner, balance, account_number)
        self.overdraftLimit=overdraftLimit
        #Creating the method that calculate the overdraft by passing in the amount parameter
    def overdraft(self,amount):
        newbalance=self.getBalance()+self.overdraftLimit
        #Using the if condition just to check the if the amout customer want to use is less or greater than the balance he has  plus the the overdraft allowed
        if amount>newbalance:
            print('please select minimum Overdraft limit')
        else:
            # super().withdraw(amount)
           return f" Dear client you have now a debt of : {self.getBalance()-amount}"
        #creating the method __str__ to represent the class information where I used super class in this case to access the method __str__ from the parent class
    def __str__(self):
        return f'{super().__str__()}, and your overdraft limit =  {self.overdraftLimit}, therefore you new balance is {self.getBalance()}, then you are now allowed to purchase until to  {self.getBalance()+self.overdraftLimit}'
    


if __name__=="__main__":
        #Crearing the instance of CheckingAccount child class
        objchecking=CheckingAccount("Odile",4500,218005257,500)
        #Printing the instance of the class 
        print(objchecking)
        print(objchecking.overdraft(5000))
        
    