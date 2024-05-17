import random #to randomize the dice rolls
import os # used on save, load scores def
from user_manager import UserManager 
from score import Score

class DiceGame:
    def __init__(self):
        #assign variables 
        self.users = UserManager()
        self.current_player = None #set to none to indicate that the variable is empty
        self.scores = {}
        self.load_scores()  # Loads the scores when initializing
    
    def space(self,lines=1): 
        for i in range(lines):
            print()

    def logout(self): 
        self.current_player = None
        print("Logged out successfully.")
        self.space()

    def play_game(self):
        print("=== Welcome to the Dice Game! ===")
        user_score = 0
        cpu_score = 0
        num_turns = 3 # set the number of turns to 3 and iterate using for loop
        for _ in range(num_turns):
            input("Press Enter to roll the dice...")
            user_roll = random.randint(1, 6) #randomize numbers on the dice
            cpu_roll = random.randint(1, 6)
            print(f"{self.current_player} rolled: {user_roll}")
            print("CPU rolled:", cpu_roll)
            if user_roll > cpu_roll: #conditions on deciding who won each round
                print(f"{self.current_player} wins this round!")
                user_score += 4  
            elif cpu_roll > user_roll:
                print("CPU wins this round!")
                cpu_score += 1
            else:
                print("It's a tie!")
                user_score += 1  
        
        print("Game Over!")
        print(f"{self.current_player}'s score:", user_score)
        print("CPU's score:", cpu_score)
        self.update_scores(user_score // 4)
        self.space()  
        self.display_top_scores()
        while True: #ask the user if they want to continue playing
                choice = input("\nDo you want to continue to the next stage? 1 for Yes , 0 for No: ")
                try:
                    choice = int(choice)
                    if choice == 1:
                        return self.play_game() 
                    elif choice == 0:
                        print("Game Over!!")
                        return
                except ValueError as e:
                    print(f"Error: {e}")

    def load_scores(self):
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file: #open scores.txt file and read each line
                for line in file:
                    username, points, wins = line.strip().split(",")
                    self.scores[username] = Score(username, int(points), int(wins))

    def save_scores(self):
        with open("scores.txt", "w") as file: #open scores.txt and write in file
            for score in self.scores.values():
               file.write(f"{score.username},{score.points},{score.wins}\n")

    def update_scores(self, win):
        if self.current_player in self.scores:
            self.scores[self.current_player].points += win * 4
            self.scores[self.current_player].wins += win
        else:
            self.scores[self.current_player] = Score(self.current_player, win * 4, win)
        self.save_scores()

    def display_top_scores(self):
        if not self.scores: # check if any player has played the game ny checking if any scores are recorded
            print("No records yet.")
            return
        
        sorted_scores = sorted(self.scores.values(), key=self.sort_key, reverse=True) #to sort scores in order
        print("\n\nTop Scores:")
        for rank, score in enumerate(sorted_scores[:10], start=1):
            print(f"{rank}. {score.username}: points- {score.points}, wins- {score.wins}")
        self.space()

    def sort_key(self, score): #create a sort_key define to keep track of the points and wins
        return (score.points, score.wins)


def game_main(game):
    while True:
        print("\n======= DICE ROLL GAME ========")
        print(f"Welcome {game.current_player} :>")
        print("========================")
        print("|Game menu:            |")
        print("|1. Play game          |")
        print("|2. Show top scores    |")
        print("|3. Log out            |")
        print("========================")

        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                game.play_game()
            elif choice == 2:
                game.display_top_scores()
            elif choice == 3:
                game.logout()
                break  # Break the loop after logging out and automatically go back to main menu
            else:
                print("Pick from the choices.")
        except ValueError:
            print("Invalid Input")
