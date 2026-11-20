items = {"name": "Galileo", "title": "computer scientist"}
people = ["ahmed", "galal", "donya"]
for key, value in items.items():
  print(f"{key} : {value}")

for index, person in enumerate(people):
  print(f"Index {index} has a value of {person}")