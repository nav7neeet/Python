import pandas


def get_data_frame():
    table = []
    columns = ["Account ID", "Account Name", "Permission Set", "Assignment", "Type"]
    data_frame = pandas.DataFrame(table, columns=columns)
    return data_frame


"""
575936742308
unv-access-key-test-DD
['AmazonS3FullAccess']
[{'Effect': 'Allow', 'Principal': {'AWS': 'arn:aws:iam::901203859849:root'}, 'Action': ['sts:AssumeRole', 'sts:SetSourceIdentity'], 'Condition': {'StringEquals': {'sts:SourceIdentity': 'qa'}}}]
['arn:aws:iam::901203859849:root']
"""
mydataset = [
    [
        "575936742308",
        "[{'Effect': 'Allow', 'Principal': {'AWS': 'arn:aws:iam::901203859849:root'}, 'Action': ['sts:AssumeRole', 'sts:SetSourceIdentity'], 'Condition': {'StringEquals': {'sts:SourceIdentity': 'qa'}}}]",
        ["AmazonS3FullAccess"],
    ],
    [
        "ambassador",
        "[{'Effect': 'Allow', 'Principal': {'AWS': 'arn:aws:iam::901203859849:root'}, 'Action': ['sts:AssumeRole', 'sts:SetSourceIdentity'], 'Condition': {'StringEquals': {'sts:SourceIdentity': 'qa'}}}]",
        "hector",
    ],
]

data_frame = pandas.DataFrame()
for item in mydataset:
    record = pandas.DataFrame.from_records([item])
    data_frame = pandas.concat([data_frame, record])

data_frame.columns = ["car1", "car2", "car3"]
print(data_frame)
# df = data_frame.set_index("car1", inplace=True)
# print(data_frame)
