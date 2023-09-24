print("Welcome to ABC Bank !!")
pin = 2809
chances = 3
balance = 50000
while chances != 0:
    user_pin = int(input("Please enter the four digit code: "))
    if user_pin != pin:
        chances -= 1
        print("wrong pin number")
        print(f"you have {chances}  chances left")
    else:
        user_choice = input("B : balance, D : diposit, W : withdraw")
        if user_choice == "B":
            print(f"your total balnace is Rs.{balance}") 
        if user_choice == "D":
            diposit_user = int(input("Enter the amount that you would like to diposit: "))
            total_balance = diposit_user + balance
            print(f"You have diposited Rs.{diposit_user}")
            print(f"Your total balance is Rs.{total_balance}")
            if user_choice == "W":
                withdraw_user = int(input("Enter the amount you want to withdraw"))
                total_balance = balance - withdraw_user
                print(f"You have withdrawn Rs.{withdraw_user}")
                print(f"Your total balance is Rs.{total_balance}")
    user_exit = input("would you like to exit? Yes/No")
    if user_exit == "Yes":
        print("Thank you for using ABC bank !! ")
        break
    else:
        continue


