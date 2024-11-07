# Step 1: Create an empty list
my_list = []

# Step 2: Append elements 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Step 3: Insert 15 at the second position
my_list.insert(1, 15)

# Step 4: Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)
