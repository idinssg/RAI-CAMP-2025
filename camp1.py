# txt = "rai"
# print(txt)

# fruits = ["apple", "banana"]
# fruits.append("orange")
# fruits.remove("apple")
# fruits.insert(0, "melon")
# for fruit in fruits:
#     print(f"This is a {fruit}.")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Done")

###### Dictionary in Mobile Robot
#     A
#    / \
#   B   C
#  / \   \
# D   E   F

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],
}

start = 'A'
goal = 'E'
frontier = [start]
explored = set() # Use set for unique (ignore duplicate append)

print(frontier, explored)
print(f"Start at {start} , Goal is {goal}")
while len(frontier) > 0:
    current = frontier.pop() # Remove and put into variable
    print (f"Check {current} :")

    if current ==  goal:
        print("Goal Reach!!!")
        break
    
    print(f"Neighbor of {current} is {graph[current]}")
    print("------------------------------")

    for neighbor in  graph[current]:
        frontier.append(neighbor)
