#---------------------------------------- 4
# Automated teller machine system >>>>> نظام الصراف ATM
balance = 1000
action = (input("Enter action withdraw / Deposit: ").capitalize())
if action == "Withdraw" :
    amount = int(input("Enter amount to withdraw : "))
    if amount <= balance:
        balance = balance - amount
        print(f"Done! Take your money. Your remaining balance is {balance}")
    else :
        print("Sorry not enough balance.")
elif action == "Deposit" :
     amount = int (input("Enetr amount to deposit : "))
     balance = balance + amount
     print(f"Money deposited successfully. Your new balance is {balance}")
else :
    print("Invalid option.")
#-------------------------------------------