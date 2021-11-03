import random
queen_x, queen_y = [int(s) for s in input().split()] ###DO NOT CHANGE###

#Game loop
while True:
    possible_move = [r for r in input().split()] ###DO NOT CHANGE###
    direction = random.choice(possible_move)
    print(f"stdout: {direction}")

