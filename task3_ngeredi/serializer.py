
# import json
# from Account import BankAccount
# from Savings import SavingsAccount
# from checking import CheckingAccount
# from credit import CreditCardAccount
# # Function to serialize the account object to JSON
# # print("Type of account_obj:", type(account_obj))
# def serializeToJson(account_obj):
#     # Determine the type of the account object
#     try:
#         if isinstance(account_obj, BankAccount):
#             account_type = "BankAccount"
#         elif isinstance(account_obj, SavingsAccount):
#             account_type = "SavingsAccount"
#         elif isinstance(account_obj, CheckingAccount):
#             account_type = "CheckingAccount"
#         elif isinstance(account_obj, CreditCardAccount):
#             account_type = "CreditCardAccount"
#         else:
#             raise ValueError("Unknown account type")
# # Create a dictionary to store account data
#         account_data = {
#             "type": account_type,
#             "data": {
#                 "account_owner": account_obj.getAccountOwner(),
#                 "balance": account_obj.getBalance(),
#                 "account_number": account_obj.getAccountNumber()
#             }
#         }


#         with open("account.json", "w") as file:
#             json.dump(account_data, file, indent=4)
#             print("Account serialized to account.json")

#     except Exception as e:
#         print("An error occurred during serialization:", str(e))
# # Function to deserialize account object from JSON
# def deserializeFromJson():
#     try:
#         # Read account data from the JSON file
#         with open("account.json", "r") as file:
#             account_data = json.load(file)
#             account_type = account_data["type"]
#             account_attributes = account_data["data"]
#  # Create an account object based on the account type
#             if account_type == "BankAccount":
#                 account_obj = BankAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"])
#             elif account_type == "SavingsAccount":
#                 account_obj = SavingsAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"], account_attributes["interest_rate"])
#             elif account_type == "CheckingAccount":
#                 account_obj = CheckingAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"], account_attributes["overdraft_limit"])
#             elif account_type == "CreditCardAccount":
#                 account_obj = CreditCardAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"], account_attributes["credit_limit"])
#             else:
#                 raise ValueError("Unknown account type")

#             return account_obj

#     except Exception as e:
#         print("An error occurred during deserialization:", str(e))
#         return None
#     # Entry point of the program
# if __name__ == "__main__":
#     # Serialize a BankAccount instance
#     account_obj=CreditCardAccount("Dianne",5000, 144444, 700)
#     serializeToJson(account_obj)
    
#     # deserialized_account = deserializeFromJson()
#     # if deserialized_account:
#     #     print("Deserialized Account Details:")
#     #     print(deserialized_account.__str__())
#     deserialized_account = deserializeFromJson()
#     if deserialized_account:
#         print("Deserialized Account Details:")
#         print(f"Account Type: {type(deserialized_account).__name__}")
#         print(deserialized_account)



import json
from Account import BankAccount
from Savings import SavingsAccount
from checking import CheckingAccount
from credit import CreditCardAccount

# Function to serialize the account object to JSON
def serialize_to_json(account_obj):
    try:
        print("Type of account_obj:", type(account_obj))

        # Determine the type of the account object
        if isinstance(account_obj, BankAccount):
            account_type = "BankAccount"
        elif isinstance(account_obj, SavingsAccount):
            account_type = "SavingsAccount"
        elif isinstance(account_obj, CheckingAccount):
            account_type = "CheckingAccount"
        elif isinstance(account_obj, CreditCardAccount):
            account_type = "CreditCardAccount"
        else:
            raise ValueError("Unknown account type")

        # Create a dictionary to store account data
        account_data = {
            "type": account_type,
            "data": {
                "account_owner": account_obj.getAccountOwner(),
                "balance": account_obj.getBalance(),
                "account_number": account_obj.getAccountNumber()
            }
        }

        with open("account.json", "w") as file:
            json.dump(account_data, file, indent=4)
            print("Account serialized to account.json")
            account_type = account_data["type"]

    except Exception as e:
        print("An error occurred during serialization:", str(e))

# Function to deserialize account object from JSON
def deserialize_from_json():
    try:
        # Read account data from the JSON file
        with open("account.json", "r") as file:
            account_data = json.load(file)
            account_type = account_data["type"]
            account_attributes = account_data["data"]

            # Create an account object based on the account type
            if account_type == "BankAccount":
                account_obj = BankAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"])
            elif account_type == "SavingsAccount":
                account_obj = SavingsAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"], account_attributes["interest_rate"])
            elif account_type == "CheckingAccount":
                account_obj = CheckingAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"], account_attributes["overdraft_limit"])
            elif account_type == "CreditCardAccount":
                account_obj = CreditCardAccount(account_attributes["account_owner"], account_attributes["balance"], account_attributes["account_number"], account_attributes["credit_limit"])
            else:
                raise ValueError("Unknown account type")

            return account_obj

    except Exception as e:
        print("An error occurred during deserialization:", str(e))
        return None

# Entry point of the program
if __name__ == "__main__":
    # Serialize a CreditCardAccount instance
    account_obj = CreditCardAccount("Dianne", 5000, 144444, 700)
    serialize_to_json(account_obj)

    # Deserialize the account from JSON and print its details
    deserialized_account = deserialize_from_json()
    if deserialized_account:
        print("Deserialized Account Details:")
        print(f"Account Type: {type(deserialized_account).__name__}")
        print(deserialized_account)
