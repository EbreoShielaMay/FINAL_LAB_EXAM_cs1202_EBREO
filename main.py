from dice_game import DiceGame, game_main

def main(): #main is run first
    game = DiceGame() #create an instance for the DiceGame class
    while True:
        print("======= DICE ROLL GAME ========")
        print("\n Main Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")
        #prompt the user to input username and password
        if choice == "1": #conditions for log in
            username = input("Enter your username (at least 4 characters) or leave blank to cancel: ").strip()
            if username == '':
                print("Login cancelled...") # if blank log in is canceled
                continue
            password = input("Enter your password (at least 8 characters) or leave blank to cancel: ")
            if password == '':
                print("Cancelled...")
                continue
            if game.users.login(username, password):
                game.current_player = username
                print("Login successful!")
                game_main(game)
            else:
                print("Invalid username or password.")
        elif choice == "2":#conditions for register
            username = input("Enter your username (at least 4 characters) or leave blank to cancel:: ")
            if username == '': #blank for cancelltion again
                print("Login cancelled...")
                continue
            if len(username) < 4:
                print("Username must at least have 4 characters.")
                continue
            password = input("Enter your password (at least 8 characters) or leave blank to cancel: ")
            if password == '':
                print("Cancelled...")
                continue
            if len(password) < 8:
                print("Password must be at least 8 letters.")
                continue
            if game.users.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists. Please choose another one.")
        elif choice == "3":#for exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
