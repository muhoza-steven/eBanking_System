#importing all required classes for testing
from Account import BankAccount
from Savings import SavingsAccount
from checking import CheckingAccount
from credit import CreditCardAccount
# #use the main function to initialize all instances of the classes
def main():
    objAccount=BankAccount("Geredi NIYIBIGIRA",2000, 218007257)
    objsaving=SavingsAccount("Geredi NIYIBIGIRA", 7200,1234567, 5)
    objchecking=CheckingAccount("Odile",4500,218005257,500)
    objCreditAccount=CreditCardAccount("Dianne",5000, 144444, 700)

#     print(objsaving, f'and your intrest rate is : {objsaving.calculateInterest()} Thus your new balance is {objsaving.calculateInterest()+objsaving.getBalance()}\n')
#     # print(objsaving.calculateInterest())
#     # objchecking=CheckingAccount("Odile",4500,218005257,500)
#         #Printing the instance of the class 
#     print(objchecking)
#     print(objchecking.overdraft(5000))
#     objCreditAccount.makePurchase(600)
#     print(objCreditAccount)

#     # # print(objAccount)
#     # objAccount.deposit(3000)
#     # # print(objAccount)
#     # objAccount.withdraw(1500)
#     # # print(objAccount)
#     # print(objsaving, f'ad your intrest rate is : {objsaving.calculateInterest()} Thus your new balance is {objsaving.calculateInterest()+objsaving.getBalance()}\n')
#     # # # print(objsaving.calculateInterest())
#     # # print(objchecking)
#     # print(objchecking.overdraft(5000))
#     # # # print(objCreditAccount)
#     # objCreditAccount.makePurchase(800)
#     # # print(objCreditAccount)
#Initializing the list to store all instances
    AccountInformation_List = [objAccount, objsaving, objchecking, objCreditAccount]
    #Use for loop to iriterate the conditionn and print out the results as well as 
    for account in AccountInformation_List:
        print(f"\nAccount Type: {type(account).__name__}")
        print(account)

    

if __name__=="__main__":
    main()

    

