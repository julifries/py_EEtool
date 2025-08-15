from typing import Union, List


class resistorColor4BAND:
    def __init__(self, colorName, firstDigit, secondDigit, multiplier, tolerance):
        self.colorName = colorName
        self.firstDigit = firstDigit
        self.secondDigit = secondDigit
        self.multiplier = multiplier
        self.tolerance = tolerance


#color objects
blackColor = resistorColor4BAND("black", 0, 0, 1, None)
brownColor = resistorColor4BAND("brown", 1, 1, 10, "+-1%")
redColor = resistorColor4BAND("red", 2, 2, 10**2, "+-2%")
orangeColor = resistorColor4BAND("orange", 3, 3, 10**3, None)
yellowColor = resistorColor4BAND("yellow", 4, 4, 10**4, None)
greenColor = resistorColor4BAND("green", 5, 5, 10**5, "+-0.5%")
blueColor = resistorColor4BAND("blue", 6, 6, 10**6, "+-0.25%")
violetColor = resistorColor4BAND("violet", 7, 7, 10**7, "+-0.1%")
greyColor = resistorColor4BAND("grey", 8, 8, 10**8, "+-0.05")
whiteColor = resistorColor4BAND("white", 9, 9, 10**9, None)
goldColor = resistorColor4BAND("gold", None, None, 10 ** (-1), "+-5%")
silverColor = resistorColor4BAND("silver", None, None, 10 ** (-2), "+-10%")

#dictionary for the accurate colors
COLORS_4BAND = {
    blackColor.colorName: blackColor,
    brownColor.colorName: brownColor,
    redColor.colorName: redColor,
    orangeColor.colorName: orangeColor,
    yellowColor.colorName: yellowColor,
    greenColor.colorName: greenColor,
    blueColor.colorName: blueColor,
    violetColor.colorName: violetColor,
    greyColor.colorName: greyColor,
    whiteColor.colorName: whiteColor,
    goldColor.colorName: goldColor,
    silverColor.colorName: silverColor,
}

#a list comprehension thingy, makes every element to lower in the splitted Userinput list
def format_rawData(userInput):
     return [c.lower() for c in userInput.split()]

#checks if an invalid color is encountered
def check_colorValues(processedData):
    #all will only return true if all colors exist in COLORS_4BAND
    #basically, if every color in processedData is a valid dictionary key, will return True
    return all(color in COLORS_4BAND for color in processedData)
  
def check_colorFormat(processedData):
    not_allowed_1and2band=[goldColor.colorName,silverColor.colorName]
    not_allowed_4band=[blackColor.colorName,orangeColor.colorName,yellowColor.colorName,whiteColor.colorName]
    
    if processedData[0] in not_allowed_1and2band:
        return False
    if processedData[1] in not_allowed_1and2band:
        return False
    if processedData[3] in not_allowed_4band:
        return False
    return True

#checks all demands for valid input
def check_inputValid(processedData):
    return (len(processedData)==4 and check_colorValues(processedData) and check_colorFormat(processedData))

#creates actual color objects from the keys
def create_colorObjects(processedData):
    colorsList = [COLORS_4BAND[color] for color in processedData]
    return colorsList

#calculates the integer value and adds the tolerance
def calculateValue(colorsList: List[resistorColor4BAND])->str:
    actualValue=((colorsList[0].firstDigit*10+colorsList[1].secondDigit)*colorsList[2].multiplier)
    return str(actualValue)+"Ω, tolerance "+str(colorsList[3].tolerance)


