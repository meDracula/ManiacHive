import random
queen_x, queen_y = [int(s) for s in input().split()] ###DO NOT CHANGE###

#Game loop
while True:
    possible_move = [r for r in input().split()] ###DO NOT CHANGE###
    direction = "West" if "West" in possible_move else random.choice(possible_move)
    print(f"stdout: {direction}")

