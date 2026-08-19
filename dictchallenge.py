user = {"id":1, "name": "John", "age": 30, "city": "New York"}
new_user= {}
for key, value in user.items():
    if isinstance(value, str):
        new_user[key] = value.upper()

print(new_user)