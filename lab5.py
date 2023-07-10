import pandas

d1 = {
    2: ["756654101167", "Administrators"],
    6: ["799824970374", "Administrators"],
    3: ["524570508187", "Administrators"],
    1: ["975300453774", "Administrators"],
    7: ["789086873538", "ReadOnlyAccess"],
    4: ["329252691451", "ReadOnlyAccess"],
    8: ["789086873538", "Administrators"],
    5: ["329252691451", "Administrators"],
    9: ["168123580268", "ReadOnlyAccess"],
    10: ["168123580268", "ajit"],
    11: ["168123580268", "vinay"],
    12: ["168123580268", "Administrators"],
    13: ["168123580268", "temp"],
    14: ["338973819204", "Administrators"],
    15: ["338973819204", "vinay"],
    16: ["901203859849", "vinay"],
    17: ["901203859849", "Administrators"],
    18: ["575936742308", "Administrators"],
}
d2 = {
    12: ["168123580268", "AWSAdministratorAccess"],
    6: ["799824970374", "AWSAdministratorAccess"],
    11: ["168123580268", "AWSAdministratorAccess"],
    1: ["975300453774", "AWSAdministratorAccess"],
    8: ["789086873538", "AWSAdministratorAccess"],
    13: ["168123580268", "AWSAdministratorAccess"],
    5: ["329252691451", "AWSAdministratorAccess"],
    14: ["338973819204", "AWSAdministratorAccess"],
    9: ["168123580268", "AWSReadOnlyAccess"],
    15: ["338973819204", "AWSAdministratorAccess"],
    10: ["168123580268", "AWSAdministratorAccess"],
    16: ["901203859849", "AWSAdministratorAccess"],
    2: ["756654101167", "AWSAdministratorAccess"],
    7: ["789086873538", "AWSReadOnlyAccess"],
    3: ["524570508187", "AWSAdministratorAccess"],
    4: ["329252691451", "AWSReadOnlyAccess"],
    17: ["901203859849", "AWSAdministratorAccess"],
    18: ["575936742308", "AWSAdministratorAccess"],
}

x = [d1, d2]

# result = {}
# for item in d1:
#     result = result | item

# print(result)


unique_keys = list(d1.keys()) + list(d2.keys())
data_frame = pandas.DataFrame()
for key in set(unique_keys):
    sum = []
    loop = 0
    for item in x:
        loop = loop + 1
        if key in item:
            if loop == 1:
                sum = sum + item[key]
            else:
                sum = sum + [item[key][1]]
    # print(f"{key}: {sum}")
    record = pandas.DataFrame.from_records([sum])
    data_frame = pandas.concat([data_frame, record])
print(data_frame)
