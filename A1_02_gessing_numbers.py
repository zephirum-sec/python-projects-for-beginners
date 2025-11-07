import random

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

print(CYAN + BOLD + """
                      _              
                     (_)             
   __ _  ___  ___ ___ _ _ __   __ _  
  / _` |/ _ \/ __/ __| | '_ \ / _` | 
 | (_| |  __/\__ \__ \ | | | | (_| | 
  \__, |\___||___/___/_|_| |_|\__, | 
   __/ |                       __/ | 
  |___/                       |___/  
""" + RESET)
def play_game():
    player_name = input('Welcome, Enter your name: ')
    print(f'''🚀 Let's go, {player_name}!
Choose your challenge:
 --------------------------------------------------
| [1] Easy   → Guess the number (1–50)             |
| [2] Medium → Try your luck (1–100)               | 
| [3] Hard   → Like finding a needle in a haystack!|
 --------------------------------------------------
''')

    choose = input("Write your choice here. Let's go! (1, 2, 3): ")

    # ---------------- EASY LEVEL ----------------
    def easy_level():
        attempts = 0
        max_attempts = 7
        secret_number = random.randint(1, 50)
        print(GREEN + 'Easy: "Nice choice! Warm up time 🔥"' + RESET)
        print("I'm thinking of a number between 1 and 50...")

        while True:
            try:
                user_input = int(input("Take your shot 🎯 What's your number?: "))
                attempts += 1

                if user_input > secret_number:
                    print("Too high! Try a smaller number ⬇️")
                elif user_input < secret_number:
                    print("Too low! Go higher 🔥")
                else:
                    print(f"🔥 Correct {player_name}! You guessed it like a pro in {attempts} attempts!")
                    break

                print(f"---------------------------- {attempts}/{max_attempts}\n")

                if attempts == max_attempts:
                    print("❌ Out of attempts! Game Over!")
                    print(f"The correct number was: {secret_number}")
                    break

            except ValueError:
                print(f"Hey {player_name}, I said a NUMBER not magic words 😅")

        play_again()

    # ---------------- MEDIUM LEVEL ----------------
    def medium_level():
        attempts = 0
        max_attempts = 10
        secret_number = random.randint(1, 100)
        print(YELLOW + 'Medium: "Cool! Let’s see how good you are 😎"' + RESET)
        print("I'm thinking of a number between 1 and 100...")

        while True:
            try:
                user_input = int(input("Take your shot 🎯 What's your number?: "))
                attempts += 1

                if user_input > secret_number:
                    print("Too high! Try a smaller number ⬇️")
                elif user_input < secret_number:
                    print("Too low! Go higher 🔥")
                else:
                    print(f"🔥 Correct {player_name}! You nailed it in {attempts} attempts!")
                    break

                print(f"---------------------------- {attempts}/{max_attempts}\n")

                if attempts == max_attempts:
                    print("❌ Out of attempts! Game Over!")
                    print(f"The correct number was: {secret_number}")
                    break

            except ValueError:
                print(f"Hey {player_name}, I said a NUMBER not magic words 😅")

        play_again()

    # ---------------- HARD LEVEL ----------------
    def hard_level():
        attempts = 0
        max_attempts = 15
        secret_number = random.randint(1, 200)
        print(RED + 'Hard: "Brave choice! Let’s see if you can survive 💀"' + RESET)
        print("I'm thinking of a number between 1 and 200...")

        while True:
            try:
                user_input = int(input("Take your shot 🎯 What's your number?: "))
                attempts += 1

                if user_input > secret_number:
                    print("Too high! Try a smaller number ⬇️")
                elif user_input < secret_number:
                    print("Too low! Go higher 🔥")
                else:
                    print(f"🔥 Correct {player_name}! You crushed it in {attempts} attempts!")
                    break

                print(f"---------------------------- {attempts}/{max_attempts}\n")

                if attempts == max_attempts:
                    print("❌ Out of attempts! Game Over!")
                    print(f"The correct number was: {secret_number}")
                    break

            except ValueError:
                print(f"Hey {player_name}, I said a NUMBER not magic words ")

        play_again()

    # ---------------- PLAY AGAIN FUNCTION ----------------
    def play_again():
        again = input("\n🎮 Wanna play again? (y/n): ").lower()
        if again == 'y':
            play_game()
        else:
            print(f"\nThanks for playing, {player_name}! 👋 See you next time!")
            exit()

    # ---------------- LEVEL SELECTION ----------------
    if choose == '1':
        easy_level()
    elif choose == '2':
        medium_level()
    elif choose == '3':
        hard_level()
    else:
        print("⚠️ Invalid choice! Please restart and select 1, 2, or 3.")
        play_again()


# ---------------- START THE GAME ----------------
play_game()
