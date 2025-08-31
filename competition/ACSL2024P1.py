'''
PROBLEM: ACSL Rings is a game where the object is to score points by tossing a ball through one of the 5 rings. Points are awarded as follows:
 
Click to insert acsl
 
Through the aqua or red ring - 1 point
Through the orange or green ring - 3 points
Through the black ring - 6 points
Through the space where 2 rings overlap - the sum of the points for the 2 rings plus 1
Any toss that is identified with a “+” at the end of the substring is awarded 2 extra points for having been tossed from a long distance
We will use a single letter to represent each of the above colors: aqua (A), red (R), orange (O), green (G), and black (B). The overlapping areas will be given by 2 letters: aqua and orange (AO or OA), orange and black (OB or BO), black and green (BG or GB), and green and red (GR or RG).
 
You will be given an integer, n, indicating the number of players, followed by n separate strings representing each player’s results for all tosses that go through at least one ring. Output a string for each player’s score in descending order using the format “player#-score”, each separated by a single space. Ties are broken based on the number of tosses; the fewer the tosses the better. We guarantee that all ties will be broken.
 
EXAMPLE:
 
Click to insert sr1
 
INPUT: The input will consist of an integer representing the number of players followed by a string for each player’s results as described above.
 
OUTPUT: Output a string in the format “player#-score” for each player’s score in descending order, each separated by a single space.
'''

num_players = int(input())

points_table = {"A" : 1, "R" : 1, "O":3, "G":3, "B":6}

def getPoints(toss:str) -> int:
    pts = 0
    if "+" in toss:
        pts += 2
        toss = toss[0:len(toss)-1]

    if len(toss) > 1:
        pts += 1
    
    for i in toss:
        pts += points_table[i]

    return pts

class Player:
    id = 0
    points = 0
    num_tosses = 0

    def __init__(self, id:int, points:int, num_tosses:int):
        self.id = id
        self.points = points
        self.num_tosses = num_tosses

    def __str__(self):
        return str(self.id) + "-" + str(self.points)

players = []
for player_num in range(num_players):
    tosses = input().split()
    pts = 0
    for toss in tosses:
        pts += getPoints(toss)
    players.append(Player(player_num+1, pts, len(tosses)))

# selection sort to arrange players in descending order
players_sorted = []
while players:
    highest_seeded_player = players[0]

    for player in players:
        higher_score = player.points > highest_seeded_player.points
        equal_score = player.points == highest_seeded_player.points
        fewer_tosses = player.num_tosses < highest_seeded_player.num_tosses

        if higher_score or (equal_score and fewer_tosses):
            highest_seeded_player = player

    players.remove(highest_seeded_player)
    players_sorted.append(highest_seeded_player)

for player in players_sorted:
    print(player, end=" ")