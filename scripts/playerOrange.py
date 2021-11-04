import random
queen_id, queen_x, queen_y = [int(s) for s in input().split()] ###DO NOT CHANGE Input###
#Game loop
while True:
    ###DO NOT CHANGE Input###
    id_possible_dir = input() 

    arr = {}
    for r in id_possible_dir.split():
        if r.isdigit():
            _id = int(r)
            arr[_id] = []
        else:
            arr[_id].append(r)

    direction = "West" if "West" in arr[queen_id] else random.choice(arr[queen_id])
    print(f"stdout: {queen_id} {direction}")

