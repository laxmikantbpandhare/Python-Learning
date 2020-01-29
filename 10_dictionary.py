example = {"user_id":2,"message":"ABCD","location":(44.45,-100.100)}
print(example)

print(example["location"])

if "location" in example:
  print(example["location"])
else:
 print("location not in example")

if "location1" in example:
  print(example["location1"])
else:
 print("location1 not in example")

for key in example.keys():
  value = example[key]
  print("key = ", value)

for key, value in example.items():
  print(key, "=", value)
