from helper import *

blackColor = resistorColor("black", 0, 0, 1, None)
brownColor = resistorColor("brown", 1, 1, 10, 0.01)
redColor = resistorColor("red", 2, 2, 10**2, 0.02)
orangeColor = resistorColor("orange", 3, 3, 10**3, 0.03)
yellowColor = resistorColor("yellow", 4, 4, 10**4, 0.04)
greenColor = resistorColor("green", 5, 5, 10**5, 0.005)
blueColor = resistorColor("blue", 6, 6, 10**6, 0.0025)
violetColor = resistorColor("violet", 7, 7, 10**7, 0.0001)
greyColor = resistorColor("grey", 8, 8, 10**8, 0.000005)
whiteColor = resistorColor("white", 9, 9, 10**9, None)
goldColor = resistorColor("gold", None, None, 10 ** (-1), 0.05)
silverColor = resistorColor("silver", None, None, 10 ** (-2), 0.1)

colors = [
    blackColor,
    brownColor,
    redColor,
    orangeColor,
    yellowColor,
    greenColor,
    blueColor,
    violetColor,
    greyColor,
    whiteColor,
    goldColor,
    silverColor,
]
