listingDict = {'brand new asus tuf gaming geforce rtx 3060 - lhr': 1000, 'sealed msi nvidia geforce rtx 3060 ventus 3x - lhr - 4 available': 1000, 'brand new evga geforce rtx 3060 xc gaming - lhr': 1000, 'evga 3060 xc lightly used !': 950, 'gigabyte geforce rtx 3060 brand new/sealed triple fan, rgb': 1000, 'msi 3060': 150, 'new sealed asus phoenix geforce rtx 3060 v2': 900}

priceLowest = 200
listOfValues = []

listingDict = ({k: v for k, v in listingDict.items() if v >= priceLowest})

for key, value in listingDict.items():
    listOfValues.append(value)

listOfValues = sorted(listOfValues)[:2]

priceHighest = listOfValues[1]

listingDict = ({k: v for k, v in listingDict.items() if v <= priceHighest})

print(listingDict)