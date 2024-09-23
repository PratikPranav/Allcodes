# arr = []
# state = int(input("Enter number of states: "))
# print("input:output:state")
# for i in range(state):
#     a = input().split(",")
#     temp = []
#     for c in a:
#         temp.append(c.split(":"))
#     arr.append(temp)
# # print(arr)
# loc = input("Enter the starting state : ")
# escape = True
# while escape:
#     start = loc
#     s = input("Enter the test string: ")
#     for i in s:
#         try:
#             for v in arr[int(loc)]:
#                 if i == v[0]:
#                     print(v[1], end="")
#                     loc = v[2]
#         except KeyError:
#             print("")
#             break
#     print()
#     loc = start
arr=[]
states=int(input("enter the number of states"))
print("input:output:state")
for i in range(states):
    a=input().split(",")
    temp=[]
    for j in a:
        temp.append(j.split(":"))
    arr.append(temp)
print(arr)

loc=input("Enter the starting state")
escape=True

while escape:
    start=loc

    s=input("emter the test string")

    for i in s:
        try:
            for v in arr[int(loc)]:

                if i==v[0]:
                    print(v[1],end="")
                    loc=v[2]
        except KeyError:
            print("")
            break
    print()
    loc=start


