# Task 2 : Guess the Secret Number Game using While True
secret_number = 7
while True :
    guess = int(input("Enter Guess the number : "))
    if guess > secret_number :
        print("Too Hige try again")
    elif guess < secret_number :
        print("Too Low try again")
    else :
        print("Congratulations! You guessed it")
        break
#------------------------