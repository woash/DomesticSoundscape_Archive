import json

# names = ["Alice", "Bob", "Charlie"]
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "favorites":["pizza","chocolate","movies"]
# }

# print(person)

# with open("person.json", "w") as outfile:
#     json.dump(person, outfile)

with open("person.json") as infile:
    data = json.load(infile)

print(data)