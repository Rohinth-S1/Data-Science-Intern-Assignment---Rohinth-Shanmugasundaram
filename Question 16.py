"""
Question 16:
A gaming company wants to create an App with multiple games.
The instruction of the games is given. You are asked to write the code to prepare the games,
Where inputs will be taken from users. Once the gaming algorithm is prepared then it can be associated with production interface of the App.

Game: Stone Paper Scissor Cut

Each win of a player will be counted as a one point for the player.
The game continues until any of the player scores 5.

Expected Input:       Expected Output:
Player A   Player B    		Result
Stone       Stone      		DRAW
Stone       Paper   		Player B wins
Stone       Scissor 		Player A wins
Paper       Stone   		Player A wins
Paper       Paper   		DRAW
Paper       Scissor 		Player B wins
Scissor     Scissor 		DRAW
Scissor     Stone   		Player B wins
Scissor     Paper   		Player A wins

"""
def stone_paper_scissor():
    score_a = 0
    score_b = 0


    while score_a < 5 and score_b < 5:
        player_a = input("Player A, enter your choice (Stone, Paper, Scissor): ").strip().lower()
        player_b = input("Player B, enter your choice (Stone, Paper, Scissor): ").strip().lower()
        if player_a not in ["stone", "paper", "scissor"] or player_b not in ["stone", "paper", "scissor"]:
            print("Invalid input! Please enter Stone, Paper, or Scissor.")
            continue
        if player_a == player_b:
            print("DRAW")
        elif (player_a == "stone" and player_b == "scissor") or \
                (player_a == "paper" and player_b == "stone") or \
                (player_a == "scissor" and player_b == "paper"):
            print("Player A wins")
            score_a += 1
        else:
            print("Player B wins")
            score_b += 1
        print(f"Player A: {score_a}, Player B: {score_b}\n")
    if score_a == 5:
        print("Player A wins the game!")
    else:
        print("Player B wins the game!")

stone_paper_scissor()

"""
- Here the points for each player is defined one and the rules are established
- each win is arithmatically added to the number of counts and those who gets 5 points first wins
"""