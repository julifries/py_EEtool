from resistor import *



print("Welcome to py_EEtool by Julia!")
print("For resistor code calculating, input the colors with space between colors.")
rawdata=input("Input your resistor color codes:")
processedData=format_rawData(rawdata)

if(check_inputValid(processedData)):
    resistor_value=calculateValue(create_colorObjects(processedData))
    print(resistor_value)