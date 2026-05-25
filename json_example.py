import json

json_data = '{"name": "Иванн", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))

data = {
    "name": "Иванн",
    "age": 30,
    "is_student": False
}

json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", encoding="utf-8") as file:
    data = json.load(file)
    print(data)


with open ('data.json', mode = "w", encoding="utf-8") as file:
    data = json.dump(data, file, indent=4, ensure_ascii=False)
    print(data)