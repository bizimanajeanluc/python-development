# Create a tuple of room codes to represent fixed floor assignments
rooms = ("R101", "R102", "R101", "R204", "R102")

# count(): Check how many times "R101" appears so we know how many morning slots use it
morning_room_count = rooms.count("R101")
print("Occurrences of R101:", morning_room_count)  # 2

# index(): Find the first position of "R204" so we know where it first appears in the schedule
first_r204_pos = rooms.index("R204")
print("First index of R204:", first_r204_pos)  # 3

# index() with start and stop bounds: Search only after index 2 to find a later occurrence of "R102"
later_r102_pos = rooms.index("R102", 2, 5)
print("Index of R102 between 2 and 5:", later_r102_pos)  # 4