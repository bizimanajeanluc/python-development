# Create two sets representing attendees who registered for two workshops
python_attendees = {"u1", "u2", "u3"}
sql_attendees = {"u3", "u4", "u5"}

# add(): Add a new attendee to the Python workshop without creating duplicates
python_attendees.add("u6")

# remove(): Remove "u2" because they canceled, raising KeyError if "u2" was missing
python_attendees.remove("u2")

# discard(): Safely try to remove "u99" without crashing if they were never registered
python_attendees.discard("u99")

# pop(): Remove and return one arbitrary attendee to assign an immediate spot check
checked_user = python_attendees.pop()
print("Popped user:", checked_user)

# union(): Get everyone in either workshop without modifying either original set
all_attendees = python_attendees.union(sql_attendees)
print("Union:", all_attendees)

# intersection(): Find attendees registered for both workshops
both_workshops = python_attendees.intersection(sql_attendees)
print("Intersection:", both_workshops)

# difference(): Find attendees in Python who are not in SQL
only_python = python_attendees.difference(sql_attendees)
print("Difference (python - sql):", only_python)

# symmetric_difference(): Find attendees in one workshop or the other, but not both
exclusive_attendees = python_attendees.symmetric_difference(sql_attendees)
print("Symmetric difference:", exclusive_attendees)

# issubset(): Check if {"u3"} is completely contained inside sql_attendees
print("Is {'u3'} a subset of sql_attendees?:", {"u3"}.issubset(sql_attendees))

# issuperset(): Check if all_attendees contains every person in python_attendees
print("Is all_attendees a superset of python_attendees?:", all_attendees.issuperset(python_attendees))

# isdisjoint(): Check if {"u8", "u9"} shares zero members with sql_attendees
print("Are {'u8', 'u9'} and sql_attendees disjoint?:", {"u8", "u9"}.isdisjoint(sql_attendees))

# update(): Merge new IDs directly into python_attendees in place
python_attendees.update({"u7", "u8"})

# intersection_update(): Keep only IDs in python_attendees that also appear in all_attendees
python_attendees.intersection_update(all_attendees)

# difference_update(): Remove any IDs from python_attendees that also appear in sql_attendees
python_attendees.difference_update(sql_attendees)

# symmetric_difference_update(): Keep IDs unique to either python_attendees or {"u10"} in place
python_attendees.symmetric_difference_update({"u10"})

# copy(): Create a separate shallow copy so future edits do not affect the snapshot
snapshot = python_attendees.copy()
print("Snapshot:", snapshot)

# clear(): Empty all items from python_attendees when resetting the list
python_attendees.clear()
print("After clear:", python_attendees)