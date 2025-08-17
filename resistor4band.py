from typing import List


class resistorColor4BAND:
    def __init__(self, colorName, firstDigit, secondDigit, multiplier, tolerance):
        self.colorName = colorName
        self.firstDigit = firstDigit
        self.secondDigit = secondDigit
        self.multiplier = multiplier
        self.tolerance = tolerance


# color objects
blackColor4band = resistorColor4BAND("black", 0, 0, 1, None)
brownColor4band = resistorColor4BAND("brown", 1, 1, 10, "+-1%")
redColor4band = resistorColor4BAND("red", 2, 2, 10**2, "+-2%")
orangeColor4band = resistorColor4BAND("orange", 3, 3, 10**3, None)
yellowColor4band = resistorColor4BAND("yellow", 4, 4, 10**4, None)
greenColor4band = resistorColor4BAND("green", 5, 5, 10**5, "+-0.5%")
blueColor4band = resistorColor4BAND("blue", 6, 6, 10**6, "+-0.25%")
violetColor4band = resistorColor4BAND("violet", 7, 7, 10**7, "+-0.1%")
greyColor4band = resistorColor4BAND("grey", 8, 8, 10**8, "+-0.05")
whiteColor4band = resistorColor4BAND("white", 9, 9, 10**9, None)
goldColor4band = resistorColor4BAND("gold", None, None, 10 ** (-1), "+-5%")
silverColor4band = resistorColor4BAND("silver", None, None, 10 ** (-2), "+-10%")

# dictionary for the accurate colors
COLORS_4BAND = {
    blackColor4band.colorName: blackColor4band,
    brownColor4band.colorName: brownColor4band,
    redColor4band.colorName: redColor4band,
    orangeColor4band.colorName: orangeColor4band,
    yellowColor4band.colorName: yellowColor4band,
    greenColor4band.colorName: greenColor4band,
    blueColor4band.colorName: blueColor4band,
    violetColor4band.colorName: violetColor4band,
    greyColor4band.colorName: greyColor4band,
    whiteColor4band.colorName: whiteColor4band,
    goldColor4band.colorName: goldColor4band,
    silverColor4band.colorName: silverColor4band,
}


# a list comprehension thingy, makes every element to lower in the splitted Userinput list

# checks if an invalid color is encountered
def check_colorValues(processedData):
    # all will only return true if all colors exist in COLORS_4BAND
    # basically, if every color in processedData is a valid dictionary key, will return True
    return all(color in COLORS_4BAND for color in processedData)


def check_colorFormat(processedData):
    not_allowed_1and2band = [goldColor4band.colorName, silverColor4band.colorName]
    not_allowed_4band = [
        blackColor4band.colorName,
        orangeColor4band.colorName,
        yellowColor4band.colorName,
        whiteColor4band.colorName,
    ]

    if processedData[0] in not_allowed_1and2band:
        return False
    if processedData[1] in not_allowed_1and2band:
        return False
    if processedData[3] in not_allowed_4band:
        return False
    return True


# checks all demands for valid input
def check_inputValid(processedData):
    return (
        len(processedData) == 4
        and check_colorValues(processedData)
        and check_colorFormat(processedData)
    )


# creates actual color objects from the keys
def create_colorObjects(processedData):
    colorsList = [COLORS_4BAND[color] for color in processedData]
    return colorsList


# calculates the integer value and adds the tolerance
def calculateValue(colorsList: List[resistorColor4BAND]) -> str:
    actualValue = (
        colorsList[0].firstDigit * 10 + colorsList[1].secondDigit
    ) * colorsList[2].multiplier
    return str(actualValue) + "Ω, tolerance " + str(colorsList[3].tolerance)
