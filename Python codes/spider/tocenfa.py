# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:35:01 2022

@author: Pratik
"""

import pandas as pd
ENFA = {}
NFA = {}
DFA = {}
eclosure = {}

states = int(input("No of states : "))
trans = int(input("No of transitions : "))
print("\nStates are : ", end=" ")
for i in range(states):
   print(f'{i}', end=" ")

print("\nInputs are : ", end=" ")
for i in range(2):
   print(f'{i}', end=" ")

initial = int(input("\nInitial state : "))
print("Enter final states of ENFA (space separated) : ")
enfa_final_state = [int(x) for x in input().split()]  # Enter final state/states of NFA
print(f'Initial State : {initial} , Final state : {enfa_final_state}')

print("\nEnter transitions (if epsilon transition then symbol is e)\n")
for i in range(trans):
   t1, t2, t3 = input("Q x symbol -> Q : ").split()
   t1 = int(t1)
   if t2 != 'e':
       t2 = int(t2)
   t3 = int(t3)
   if t2 == 'e':
       ENFA[(t1, t2)] = t3
   elif (t1, t2) in ENFA.keys():

       ENFA[(t1, t2)].add(t3)
   else:
       ENFA[(t1, t2)] = {t3}
   eclosure[t1] = {t1}
   eclosure[t3] = {t3}
# final state may not have any transition on 0,1 but it has to have epsilon transition on self.
nfa_final_state = []
for key, val in ENFA.items():
   q = key[0]
   t = key[1]
   Q = val
   # q x t -> Q
   if t == 'e':
       eclosure[q].add(Q)
       while True:
           if (Q, 'e') in ENFA.keys():
               eclosure[q].add(ENFA[(Q, 'e')])
               Q = ENFA[(Q, 'e')]
           else:
               break
table = {}  # table to store Enfa and e-closure
for j in range(states):
   s1 = set()
   s2 = set()
   NFA[j] = {}
   table[j] = {}
   table[j]['eclosure'] = list(eclosure[j])
   # checking if state is accepting state
   for el in list(eclosure[j]):
       if el in enfa_final_state and el not in nfa_final_state:
           nfa_final_state.append(el)

   if (j, 0) in ENFA.keys():
       table[j][0] = list(ENFA[(j, 0)])
   else:
       table[j][0] = []
   if (j, 1) in ENFA.keys():
       table[j][1] = list(ENFA[(j, 1)])
   else:
       table[j][1] = []

   for i in eclosure[j]:
       if (i, 0) in ENFA.keys():
           for k in ENFA[(i, 0)]:
               s1 = s1.union(eclosure[k])

       if (i, 1) in ENFA.keys():
           for k in ENFA[(i, 1)]:
               s2 = s2.union(eclosure[k])
   NFA[j][0] = list(s1)
   NFA[j][1] = list(s2)

print("\nENFA table :- ")
enfa_table = pd.DataFrame(table)
print(enfa_table.transpose())

print("\nNFA table :- ")
nfa_table = pd.DataFrame(NFA)
print(nfa_table.transpose())

keys_list = [str(initial)]
# keys_list contains all the states in nfa plus the states created in dfa are also appended further
path_list = [0, 1]
new_states_list = []

# Computing first row of DFA transition table
DFA[keys_list[0]] = {}
for y in range(2):
   ls = NFA[initial][path_list[y]]
   var = ""
   for i in ls:
       var += str(i)  # creating a single string from all the elements of the list which is a new state
   DFA[keys_list[0]][path_list[y]] = var  # assigning the state in DFA table
   if var not in keys_list:  # if the state is newly created
       new_states_list.append(var)  # then append it to the new_states_list
       keys_list.append(var)  # as well as to the keys_list which contains all the states

# Computing the other rows of DFA transition table
while len(new_states_list) != 0:  # condition is true only if the new_states_list is not empty
   if new_states_list[0] == '':
       new_states_list.remove('')
       continue
   else:
       # taking the first element of the new_states_list and examining it
       DFA[new_states_list[0]] = {}
       for i in range(2):
           temp = set()  # creating a temporary set
           for j in new_states_list[0]:
               for k in NFA[int(j)][path_list[i]]:
                   temp.add(k)  # taking the union of the states
           s = ""
           # print(temp)
           for el in temp:
               s += str(el)  # creating a single string(new state) from all the elements of the set

           if s not in keys_list:  # if the state is newly created
               new_states_list.append(s)  # then append it to the new_states_list
               keys_list.append(s)  # as well as to the keys_list which contains all the states
           DFA[new_states_list[0]][path_list[i]] = s  # assigning the new state in the DFA table

       new_states_list.remove(new_states_list[0])  # Removing the first element in the new_states_list

   print("\nDFA table :- ")
   dfa_table = pd.DataFrame(DFA)
   print(dfa_table.transpose())


def func(test2):
   ptr = str(initial)
   for g in test2:
       if DFA[ptr][int(g)] == '':
           print("String rejected")
           return
       ptr = DFA[ptr][int(g)]
       if ptr == '':
           print("String rejected")
           return
   for g in ptr:
       if int(g) in nfa_final_state:
           print("String accepted")
           return
   print("String rejected")
   return


while True:
   choice = input("\nEnter 1 to test string , 2 to exit : ")
   if choice == '2':
       break
   test = input("Enter test string : ")
   func(test2=test)
