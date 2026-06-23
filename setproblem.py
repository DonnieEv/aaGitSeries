from statistics import mean

players = [
    ("Alice", 4200, 3),
    ("Bob", 8750, 5),
    ("Carol", 3100, 2),
    ("Diana", 8750, 4),
    ("Eve", 5600, 3),
]

maxt = max(players, key=lambda x:x[1])
print(maxt)

average = mean(value[1] for value in players)
print(average)

filtered_list = [t[0] for t in players if t[2] == 3]
print(filtered_list)

sorted_data = sorted(players, key=lambda x:x[2], reverse=True)
print(sorted_data)
