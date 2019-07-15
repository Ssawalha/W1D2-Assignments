"""The Tower of Hanoi
===================

[The Tower of Hanoi](http://en.wikipedia.org/wiki/Tower_of_Hanoi) is a mathematical game or puzzle. 
It consists of three rods, and a number of disks of different sizes which can slide onto any rod. 
The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

* Only one disk can be moved at a time.

* Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack 
i.e. a disk can only be moved if it is the uppermost disk on a stack.
* No disk may be placed on top of a smaller disk.

* With three disks, the puzzle can be solved in seven moves. 
The minimum number of moves required to solve a Tower of Hanoi puzzle is 2<sup>n</sup> - 1, where n is the number of disks.

###Challenge

Write a function that takes the number of disks and then displays the steps needed to move that many disks from the first peg to the second peg.

For instance

```
hanoi(2)

# prints:

Move a disk from peg 1 to peg 3
Move a disk from peg 1 to peg 2
Move a disk from peg 3 to peg 2

### Suggestions

Your function will be `hanoi(n, start='peg 1', destination='peg 2', spare='peg 3')`

You will call hanoi(n) with the default arguments, 
but hanoi will call itself (maybe more than once) and maybe rearrange which peg is the start, stop, and spare.

When n=1, the case is simple. print out "Move a disk from {} to {}.".format(start, destination)

If n is more than one, can you express the solution of n in terms of n-1? 
That is, `hanoi(n)` should call `hanoi(n-1)` (with non-defaults for the other arguments) one or more times.

If you can create a solution for hanoi(n) that calls hanoi(n-1) as part of its solution, you will be done,
 since eventually it will be calling hanoi(1) which has a simple defined solution.

*You do not need to model the towers with a data structure. Recursive function calls and a print statement will do all of your work for you.

It's possible for this function to be clearly expressed in fewer than 10 lines."""

# def hanoi(numdisks,start = 'pos1', mid = 'pos2', end = 'pos3'):
#     startend = "Move a disk from {} to {}".format(start,end)
#     startmid = "Move a disk from {} to {}".format(start,mid)
#     midend = "Move a disk from {} to {}".format(mid,end)
#     midstart = "Move a disk from {} to {}".format(mid,start)
#     endstart = "Move a disk from {} to {}".format(end,start)
#     endmid = "Move a disk from {} to {}".format(end,mid)
#     start = []
#     mid = []
#     end = []
#     positions = [start,mid,end]
#     if numdisks > 1:

#         # mid.append(start[0])
#         # end.append(start[0])
#         # print(positions)
#         for disk in range(numdisks+1):
#             start.append(disk)
#         print(positions)

#         if mid == [] or start[0] > mid[0]:
#             mid.append(start)
#         # while positions[0] != [] and positions[1] != []
#         #     print (positions)
#     else:
#         print(startend)

#hanoi(2)
# hanoi(2)

def hanoi(num):
    peg1 = [num for num in range(num)]
    peg2 = []
    peg3 = []
            #if len(peg1) > 1:
                #for num in range(num):
    while peg1 != [] and peg2 != [] and peg3 != []:
        if peg1[0] > peg2[0] and peg1[0] > peg3[0]:
            if peg2[0] > peg3[0]:
                peg1.insert(0,peg3[0])
                peg3 = peg3[1:]
                print("peg3 to peg1")
            else:
                peg1.insert(0,peg2[0])
                peg2 = peg2[1:]
                print("peg2 to peg1")
        elif peg2[0] > peg1[0] and peg2[0] > peg3[0]:
            if peg1[0] > peg3[0]:
                peg2.insert(0,peg3[0])
                peg3 = peg3[1:0]
                print("peg3 to peg2")
            else:
                peg2.insert(0,peg1[0])
                peg1 = peg1[1:]
                print("peg1 to peg2")

    while peg1 == [] and peg2 != [] and peg3 != []:
        if peg2[0] > peg3[0] and len(peg3)>1:
            peg1.insert(0,peg3[0])
            peg3 = peg3[1:]
            print("peg3 to peg1")
        elif peg2[0] > peg3[0] and len(peg3) == 1:
            peg2.insert(0,peg3[0])
            peg3 = peg3[1:]
            print("peg3 to peg2")
        elif peg3[0] > peg2[0] and len(peg3) > len(peg2):
            peg1.insert(0,peg3[0])
            peg3 = peg3[1:]
            print("peg3 to peg1")
            
    while peg1 != []:
        if peg2 == [] and peg3 == []:
            peg3.insert(0,peg1[0])
            peg1 = peg1[1:]
            print("peg1 to peg3")
        elif peg2!=[] and peg3 == []:
            if peg1[0] > peg2[0]:
                peg3.insert(0,peg1[0])
                peg1 = peg1[1:]
                print("peg1 to peg3")
            else:
                peg3.insert(0,peg2[0])
                peg2 = peg2[1:]
                print("peg2 to peg3")
        elif peg2 == [] and peg3 != []:
            if peg1[0] > peg3[0]:
                peg2.insert(0,peg1[0])
                peg1 = peg1[1:]
                print("peg1 to peg2")
            else:
                peg3.insert(0,peg2[0])
                peg2 = peg2[1:]
                print("peg2 to peg3")
    
    while peg1 == []:
        if peg2!=[] and peg3 == []:
            print('you win!')
            break
        elif peg2 != [] and peg3 != []:
            if len(peg3)>1 and peg2[0] > peg3[0]:
                peg2.insert(0,peg3[0])
                peg3 = peg3[1:]
                print("peg3 to peg2")
            elif len(peg3)>1 and peg3[0] > peg2[0]:
                peg1.insert(0,peg2[0])
                peg2 = peg2[1:]
                print("peg2 to peg1")
            elif len(peg3) == 1:
                peg2.insert(0,peg3[0])
                peg3 = peg3[1:]
                print("peg3 to peg2")
         
hanoi(3)
        # elif peg2 == [] and peg3 != []
        #     else:
        #         peg3.insert(0,peg2[0])
        #         peg2 = peg2[1:]
        #         print("peg2 to peg3")
        # elif peg2 == [] and peg3 != []:
        #     if peg1[0] > peg2[0]:
        #         peg3.insert(0,peg1[0])
        #         peg1 = peg1[1:]
        #         print("peg1 to peg3")
        #     else:
        #         peg3.insert(0,peg2[0])
        #         peg2 = peg2[1:]
        #         print("peg2 to peg3")



        # elif peg2 == [] and peg3 != []:
        #     if peg1[0] > peg3[0]:
        #         peg2.insert(0,peg1[0])
        #         peg1 = peg1[1:]
        #         print("peg1 to peg2")
        #     elif peg3[0] > peg1[0]:
        #         peg2.insert(0,peg3[0])
        #         peg3 = peg3[1:]
        #         print("peg3 to peg2")
        # elif peg2 != [] and peg3 != []:
        #     if peg1[0] > peg2[0] and peg1[0] > peg3[0]:
        #         if peg2[0] > peg3[0]:
        #             peg2.insert(0,peg3[0])
        #             peg3 = peg3[1:]
        #             print("peg3 to peg2")
        #         elif peg3[0] > peg2[0]:
        #             peg3.insert(0,peg2[0])
        #             peg2 = peg2[1:]
        #             print("peg2 to peg3")
        #     elif peg3[0] > peg2[0] and peg3[0] > peg1[0]:
        #         peg1


# def hanoi(num):
#     peg1 = [num for num in range(num)]
#     peg2 = []
#     peg3 = []
#             #if len(peg1) > 1:
#                 #for num in range(num):
#     while peg1 != []:
#         if peg2 == [] and peg3 == []:
#             peg3.append(peg1[0])
#             peg1 = peg1[1:]
#             print("peg1 to peg3")
#         elif peg2 == [] and peg3 != []:
#             if peg1[0] > peg3[0]:
#                 peg2.append(peg1[0])
#                 peg1 = peg1[1:]
#                 print("peg1 to peg2")
#             elif peg3[0] > peg1[0]:
#                 peg2.append(peg3[0])
#                 peg3 = peg3[1:]
#                 print("peg3 to peg2")
#         elif peg2 != [] and peg3 != []:
#             if peg1[0] > peg2[0] and peg1[0] > peg3[0]:
#                 if 


        # elif peg2 != [] and peg3 != []:
        #     if peg1[0] > peg2[0] and peg1[0] > peg3[0]:
        #         if peg2[0] > peg3 [0]:
        #             peg2.append(peg3[0])
        #             peg3 = peg3[1:]
        #             print("peg3 to peg2")
        #         else:
        #             peg3.append(peg2[0])
        #             peg2 = peg2[1:]
        #             print("peg2 to peg3")
        
        # else:
        #     peg1 = num[0]
        #     peg2 = num[1]
        #     peg3 = num[2]
        #     if peg2 == [] or peg1[0] < peg2[-1]:
        #         peg2.append(peg1[0])#
        #         peg1 = peg1[1:]#

        #     if peg3 == [] or peg1[0] < peg3[-1]:
        #         peg3.append(peg1[0])
        #         peg1 = peg1[1:]

        #     if peg1 == [] or peg2[0] < peg3[-1]:
        #         peg3.append(peg2[0])
        #         peg2 = peg2[1:]

        #     return [peg1,peg2,peg3]
    #print("peg1:{} | peg2:{} | peg3:{}".format(peg1,peg2,peg3))