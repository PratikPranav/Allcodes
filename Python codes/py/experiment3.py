arr = []
state = int(input("Enter the number of states: "))
print("Transition on ebsilon:0:1")
for i in range(state):
    a = input().split(':')
    t = []
    # print(a)
    for x in a:
        t.append(x.split(','))
    # print(t)
    arr.append(t)

acc = input("Enter the accepting state: ").split(",")
escape = True
while escape:
    string = input("Enter the test string: ")
    loc = []

    state_queue = []
    start = int(input("Enter the start state: "))
    state_queue.append(start)

    end = False
    # for i in arr:
    #     print(i)

    for a in string:
        # till there are no states to go
        loc = []
        while len(state_queue) > 0:
            # to remove repeating elements
            state_queue = list(set(state_queue))

            # get the top element
            cur = state_queue.pop(0)
            # print("cur : "+str(cur)+" a :"+str(int(a)+1))
            # print(arr[int(cur)][int(a)+1])
            for i in arr[int(cur)][int(a) + 1]:
                if int(i) < 0:
                    continue
                if i not in loc:
                    loc.append(i)
                    print("q" + str(cur) + " -> " + a + " -> q" + str(i))
            # adding lambda to the state queues
            for i in arr[int(cur)][0]:
                if int(i) >= 0:
                    print("q" + str(cur) + " -> ^ -> q" + str(i))
                    state_queue.append(int(i))
        state_queue = loc

    print("loc : ", end="")
    print(loc)
    for i in loc:
        if i in acc:
            print("accepted")
            exit()
    print("not accepted")
    print("1: test again \n 0: exit")
    if input() == '0':
        escape = False
