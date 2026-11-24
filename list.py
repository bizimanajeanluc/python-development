# Create a list of build pipeline stages in execution order
stages = ["checkout", "test"]

# append(): Add "build" to the end of the pipeline
stages.append("build")

# extend(): Add multiple trailing stages at once from another iterable
stages.extend(["package", "deploy"])

# insert(): Place "lint" right at index 1 before "test" runs
stages.insert(1, "lint")

# remove(): Drop "package" by value because we deploy directly from build artifacts
stages.remove("package")

# pop(): Remove and return the last stage ("deploy") to inspect or archive it
last_stage = stages.pop()
print("Popped last stage:", last_stage)

# pop(index): Remove and return the item at a specific index (index 1, now "lint")
removed_at_index = stages.pop(1)
print("Popped at index 1:", removed_at_index)

# index(): Find where "test" sits in the current sequence
test_index = stages.index("test")
print("Index of 'test':", test_index)

# count(): Check how many times "build" appears in the sequence
build_count = stages.count("build")
print("Count of 'build':", build_count)

# sort(): Arrange stage names alphabetically in place
stages.sort()
print("Sorted stages:", stages)

# reverse(): Flip the current order of items in place
stages.reverse()
print("Reversed stages:", stages)

# copy(): Make an independent shallow copy before clearing the working list
stages_backup = stages.copy()
print("Backup stages:", stages_backup)

# clear(): Remove all stages to reset the pipeline list
stages.clear()
print("Cleared stages:", stages)