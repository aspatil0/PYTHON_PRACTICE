import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low!")
            elif guess > number:
                print("📈 Too high!")
            else:
                print(f"🎉 You got it in {attempts} attempts!")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

while True:
    guess_number()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
