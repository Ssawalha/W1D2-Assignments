"""
McNugget Numbers
==================

In the 1980s, while eating McDonald's with his son, mathematician Henri Picciotto reasoned [McNugget Numbers](http://en.wikipedia.org/wiki/Coin_problem#McNugget_numbers).

At McDonalds’ Restaurants at the time, Chicken McNugget meals were available in sizes of 6 McNuggets, 9 McNuggets, or 20 McNuggets. 

A number is a McNugget number if it can be the sum of the number of McNuggets purchased in an order before eating any of them.

Some Examples:

		20 + 6 == 26
		9 + 9 + 9 + 9 + 9 == 45
		20 + 9 + 6 == 35
		...etc

###Task 1

Determine all numbers that are not McNugget numbers using 1980s order sizes - `6`, `9` and `20`.

###McNugget 2015 Redux

Determine all numbers that are not McNugget numbers using today's order sizes - `4`, `6`, `10`, `20` and `40`.
"""

#Task 1

#1980 McNugget Nums
Mcsize = [6,9,20]

def McFormula(order):
    McDict = {'large' :20, 'medium':9, 'small':6}
    McNugget = []
    McRemainder = 0
    if order/McDict['large'] >= 1:
        McRemainder = int(order%McDict['large'])
        McNugget.append(('large',int(order/McDict['large'])))
    if McRemainder/McDict['medium'] >= 1:
        McNugget.append(('medium',int(McRemainder/McDict['medium'])))
        McRemainder = int(McRemainder%McDict['medium'])
    if order/McDict['small'] >= 1:
        McNugget.append(('small',int(McRemainder/McDict['small'])))
        McRemainder = int(McRemainder%McDict['small'])
    return McRemainder
print (McFormula(14))

def isMcnum(order):
    Mclist = []
    for num in range(order):
        if McFormula(num) != 0:
            Mclist.append(num)
    return Mclist

def McDynamic(order,Mclist):
    McSize = sorted(Mclist, reverse = True)
    notMcNug = []
    McRemainder = 0
    for num in McSize:
        if order/num >= 1 and order%num == 0:
            McRemainder = 0
            return McRemainder
        if order/num > 1:
            order = order-num
            McRemainder = order % num
            notMcNug.append(McRemainder)
    return McRemainder

print(McDynamic(14,[]))


def is2015mcnum(order, Mclist):
    McSize = sorted(Mclist, reverse = True)
    notnugget = []
    for num in range(order):
        if McDynamic(num,McSize) != 0:
            notnugget.append(num)
    return notnugget

print(is2015mcnum(25,[20,4,6,40,10]))