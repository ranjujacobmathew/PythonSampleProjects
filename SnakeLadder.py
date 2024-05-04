import random
# Create a board
board = []
for i in range(100):
    board.append(i)
# Create a dictionary of snakes and ladders
snakes_and_ladders = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    16: 6,
    21: 42,
    28: 84,
    36: 44,
    46: 25,
    49: 11,
    51: 67,
    62: 19,
    64: 60,
    71: 91,
    74: 53,
    78: 98,
    87: 94,
    89: 70,
    92: 68,
    95: 75,
    99: 80
}
# Create a function to roll the dice
def roll_dice():
    return random.randint(1, 6)
# Create a function to move the player
def move_player(player, roll):
    new_position = player + roll
    if new_position > 100:
        new_position = 100
    return new_position
# Create a function to check if the player has won
def check_win(player):
    if player == 100:
        return True
    else:
        return False
# Create a function to handle exceptions
def handle_exceptions(e):
    print(e)
# Create a function to play the game
def play_game():
    # Initialize the players
    players = [1, 1]
    # Initialize the current player
    current_player = 0
    # Initialize the game loop
    while True:
        try:
            # Roll the dice
            roll = roll_dice()
            # Move the player
            players[current_player] = move_player(players[current_player], roll)
            # Check if the player has won
            if check_win(players[current_player]):
