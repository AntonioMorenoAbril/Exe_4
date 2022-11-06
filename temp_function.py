# Transform Fahr to Celsius
def fahrToCelsius(fahrTemp):
    celsiusTemp = (fahrTemp - 32)/1.8
    return celsiusTemp

#fahrTemp = 32
#print(f"{fahrTemp} fahr is equivalent to {fahrToCelsius(32)} celsius")


# Classifier of celsius degrees temperatures
#celsiusTemp = int(input("Tell me your chooseen temperature"))
def tempClassifier(celsiusTemp):
    if celsiusTemp < -2:
        tempClass = 0
    elif celsiusTemp >= -2 and celsiusTemp < 2:
        tempClass = 1
    elif celsiusTemp >= 2 and celsiusTemp < 15:
        tempClass = 2
    elif celsiusTemp >= 15:
        tempClass = 3
    return tempClass
    
#print(tempClassifier(0))
#tempClassifier(celsiusTemp)



