d1 = {"x1": 10, "x2": 5, "x5": 9}
d2 = {"x2": 1, "x7": 5, "x3": 9}
d3 = {"x2": 10, "x1": 5, "x3": 2}
d4 = {"x5": 10, "x7": 5, "x9": 2}

x = [d1, d2, d3, d4]

# merge d1, d2 and d3, d4 and keep the sum of values
# print(list(d1.keys()) + list(d2.keys()))
# unique_keys = list(d1.keys()) + list(d2.keys()) + list(d3.keys()) + list(d4.keys())
# print(set(unique_keys))

# for key in set(unique_keys):
#     sum = 0
#     for item in x:
#         if key in item:
#             sum = sum + item[key]
#     print(f"{key}: {sum}")

y = [1, 2, 3, 4, 100]
for item in y:
    var = item
print(var)
