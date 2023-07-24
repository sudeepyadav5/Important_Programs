"""
Question:-
There are 100 doors in a row, all doors are initially closed. A person walks through all doors multiple times
 and toggle (if open then close, if close then open) them in the following way:
In the first walk, the person toggles every door
In the second walk, the person toggles every second door, i.e., 2nd, 4th, 6th, 8th, …
In the third walk, the person toggles every third door, i.e. 3rd, 6th, 9th, …
Likewise,
In the 100th walk, the person toggles the 100th door.
Which doors are open in the end?
"""
"""
Solution: 
A door is toggled in an ith walk if i divide door number. For example, door number 45 is toggled in the 1st,
 3rd, 5th, 9th,15th, and 45th walks.
The door is switched back to an initial stage for every pair of divisors. For example, 45 is toggled 6 times 
for 3 pairs (5, 9), (15, 3), and (1, 45). 

It looks like all doors would become closed at the end. But there are door numbers that would open, 
for example, in 16, the divisors are (1,2,4,8,16) and as the pair(4,4) contributes only one divisor making the number of divisors odd, it would become open at the end. Similarly, all other perfect squares like 4, 9,…, and 100 would become open. Now, for prime numbers like 2,3,5,7… the divisors are (1, that number) and it is a pair, so they will remain closed at the end. And for all other numbers divisors are always in pairs, e.g. 15 = (1,15),(3,5), they will also remain closed.

So the answer is 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100. 

Please write comments if you find anything incorrect, or if you want to share more information about the 
topic discussed above
"""


def get_open_doors():
    doors = [False] * 101  # Initialize all doors as closed
    for i in range(1, 101):
        for j in range(i, 101, i):
            doors[j] = not doors[j]  # Toggle the door

    open_doors = [i for i in range(1, 101) if doors[i]]  # Get the indices of open doors
    return open_doors


open_doors = get_open_doors()
print("Doors that are open at the end:", open_doors)
