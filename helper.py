


# a list comprehension thingy, makes every element to lower in the splitted Userinput list
def format_rawData(userInput):
    return [c.lower() for c in userInput.split()]
