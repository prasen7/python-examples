# 3 Dimensional Array--
# A huge hotel consisting of three buildings, 15 floors each, with 20 rooms on each floor.
# we need to create a 3 dimensional array to collect and process data on free/occupied rooms.
# 1st step- boolean value for representing the state of room(free or occupied)
# 2nd step- 3D array for 3 buildings, 15 floors, and 20 rooms each floor. 
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# 1st index(t in range(3)) selects one of the buildings, the 2nd index(f in range(15)) selects the floor. 
# 3rd index(r in range(20)) selects the room no.
# initially each room's state is empty so we choose false as default value.
rooms[1][9][13] = True # book a room in the second building, on the tenth floor, room 14.
rooms[0][4][1] = False # release the second room on the fifth floor in 1st building.

# Check if there are any vacancies on the 15th floor of the 3rd building.
vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]: # if room[2][14][roomNumber]==False
        vacancy += 1
print("the no. of available rooms on 15th floor of 3rd building:", vacancy)