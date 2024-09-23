arr = []
data = {}
states = int(input("Enter the number of states: "))
inpu = input("Enter the state values : \n").split(",")
for i in inpu:
    i = i.split(":")
    data[i[0]] = i[1]

print(data)
print("Enter the transitions:")
for i in range(states):
    inp = input().split(":")
    arr.append(inp)

print(arr)
loc = input("Enter the start state : ")
start = loc
while True:
    print()
    string = input("Enter the test string: ")
    for i in string:
        try:
            print(data[loc], end="")
            loc = arr[int(loc)][int(i)]
        except KeyError:
            break
    if int(loc) >= 0:
        print(data[loc])
    loc = start
