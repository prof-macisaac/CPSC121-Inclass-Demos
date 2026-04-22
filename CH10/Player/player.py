import random

class Player:
    def __init__(self, name, score = 0, lives = 3):
        self.__name = name
        self.__score = score
        self.__lives = lives

    def add_points(self, points):
        if points > 0:
            self.__score += points
    
    def lose_life(self):
        if self.__lives > 0:
            self.__lives -= 1
    
    def get_lives(self):
        return self.__lives
    
    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.__name} has {self.__lives} left | Current score: {self.__score}"
    

def winner(player1, player2):
    if player1.get_score() > player2.get_score():
        return player1
    if player1.get_score() < player2.get_score():
        return player2

    r = random.randint(1,2)
    if r == 1:
        return player1
    return player2


def simulate_match(player, score_prob=0.5, lose_prob = 0.5):
    while player.get_lives() > 0:
        score = random.random()
        if score <= score_prob:
            player.add_points(1)
        lose = random.random()
        if lose <= lose_prob:
            player.lose_life()

player1 = Player("A")
player2 = Player("B")

simulate_match(player1)
simulate_match(player2)

win_player = winner(player1, player2)
print(f"Winner is {win_player.get_name()}")

print(player1)
print(player2)
