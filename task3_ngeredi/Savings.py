from Account import BankAccount

class SavingsAccount(BankAccount):
     # Constructor to initialize attributes of the SavingsAccount class
    def __init__(self, account_owner, balance, account_number, interestRate):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(account_owner, balance, account_number)
        self.interestRate = interestRate
        # Method to calculate interest based on the balance and interest rate
    def calculateInterest(self):
        return self.getBalance()*(self.interestRate)/100
    #Method to calculate the new balance after applying interest
    def newbalance(self):
        return self.getBalance()+(self.calculateInterest())
    # Method to represent the object as a string
    def __str__(self):
        return f'{super().__str__()}, and pacentage rate is: {self.interestRate}, and your interest is {self.calculateInterest()}, thus your new balance is {self.newbalance()} '



if __name__=="__main__":
    #initializing the instance of the SavingsAccount 
    objsaving=SavingsAccount("Geredi NIYIBIGIRA", 7200,1234567, 5)
    
    print(objsaving, f'and your intrest rate is : {objsaving.calculateInterest()} Thus your new balance is {objsaving.calculateInterest()+objsaving.getBalance()}\n')
    # print(objsaving.calculateInterest())

# print(objsaving)
