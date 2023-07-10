x = ["aa", "ab", "zx", "cz", "zr", "kp", "nl", "aa"]

# add an item at the end of list

# add an item at index 4

# replace an item at index 4

# replace items from index 3 to 5 with different values

# delete an item at the end

# delete an item at index 4

# delete an item where value is 'zr'

# delete a duplicate item

# count total number of items

# count frequency of given item

# sort the list in ascending and descending order


# sort the list in ascending and descending order based on 2nd element of item

# find the index of an item

# display the list from index 3 to 5

# sort and merge two lists
y = ["an", "at", "zx", "cz", "zz", "kp", "nl", "aa"]
z = x + y

# remove each and every duplicate word and preserve the order
for item in z:
    for i in range(z.count(item) - 1):
        z.remove(item)
print(z)
