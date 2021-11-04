import random
queen_id, queen_x, queen_y = [int(s) for s in input().split()] ###DO NOT CHANGE###

def queen(possible_moves):
    if "North" in possible_moves:
        direction = "North"
    elif "East" in possible_moves:
        direction = "East"
    else:
        direction = random.choice(possible_moves)
    return direction

def blob(possible_moves):
    return random.choice(possible_moves)

#Game loop
while True:
    ###DO NOT CHANGE###
    id_possible_dir = input() 
    enemy_queen = input() #id x y where x and y is int, ex: 1 3 2
    
    arr = {}
    for r in id_possible_dir.split():
        if r.isdigit():
            _id = int(r)
            if _id != 1:
                blob_id = _id
            arr[_id] = []
        else:
            arr[_id].append(r)
    
    queen_direction = queen(arr[queen_id])
    
    if len(arr) > 1:
        blob_direction = blob(arr[blob_id])
        print("stdout: {} {} {} {}".format(queen_id, queen_direction, blob_id, blob_direction))
    else:
        print("stdout: {} {}".format(queen_id, queen_direction))

