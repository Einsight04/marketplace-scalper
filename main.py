import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Main Var
sep = "-----------------------------------------------"
error = "Error, try again."

# Items
cityInclusions = []
item = {}

# Information Var
phoneNumber = "6478852142"
password = "Gk20040429!"

# Time Var
delayShort = 2
delayMedium = 5
delayLong = 10

# Inputs
print(sep)
print('Enter comma separated integers ')
print(sep)

while True:
    try:
        inclusionsInput = input('Mississauga [1] | Brampton [2] | Oakville [3]\n>>> ')

        inclusions = list(map(lambda x: int(x), inclusionsInput.split(",")))

        if 1 in inclusions:
            cityInclusions.append("Mississauga")
        if 2 in inclusions:
            cityInclusions.append("Brampton")
        if 3 in inclusions:
            cityInclusions.append("Oakville")

        print(sep)

        joined_string = ", ".join(cityInclusions)
        print("Search results within " + joined_string + " will be displayed.")

        break
    except:
        print(sep)
        print(error)
        print(sep)

print(sep)

while True:
    try:
        itemsInput = input('30 SERIES:\n3090 [1], 3080ti [2], 3080 [3], 3070ti [4], 3070 [5], 3060ti [6], 3060 [7]\n20 '
                      'SERIES:\n2080ti [8], 2080s [9], 2080 [10], 2070s [11], 2070 [12], 2060s [13], 2060 [14]\n10 '
                      'SERIES:\n1080ti [15], 1080 [16], 1070ti [17], 1070 [18], 1060 [19]\n>>> ')

        items = list(map(lambda x: int(x), itemsInput.split(",")))

        if 1 in items:
            item["RTX 3090"] = 3500
        if 2 in items:
            item["RTX 3080ti"] = 2500
        if 3 in items:
            item["RTX 3080"] = 2000
        if 4 in items:
            item["RTX 3070ti"] = 1500
        if 5 in items:
            item["RTX 3070"] = 1200
        if 6 in items:
            item["RTX 3060ti"] = 1000
        if 7 in items:
            item["RTX 3060"] = 900
        if 8 in items:
            item["RTX 2080ti"] = 950
        if 9 in items:
            item["RTX 2080 super"] = 950
        if 10 in items:
            item["RTX 2080"] = 900
        if 11 in items:
            item["RTX 2070 super"] = 900
        if 12 in items:
            item["RTX 2070"] = 850
        if 13 in items:
            item["RTX 2060 super"] = 850
        if 14 in items:
            item["RTX 2060"] = 700
        if 15 in items:
            item["GTX 1080ti"] = 850
        if 16 in items:
            item["GTX 1080"] = 650
        if 17 in items:
            item["GTX 1070ti"] = 600
        if 18 in items:
            item["GTX 1070"] = 550
        if 19 in items:
            item["GTX 1060 6gb"] = 400
        if items == 20:
            item = {'RTX 3090': 3500, 'RTX 3080ti': 2500, 'RTX 3080': 2000, 'RTX 3070ti': 1500, 'RTX 3070': 1200,
                    'RTX 3060ti': 1000, 'RTX 3060': 900, 'RTX 2080ti': 950, 'RTX 2080 super': 950, 'RTX 2080': 900,
                    'RTX 2070 super': 900, 'RTX 2070': 850, 'RTX 2060 super': 850, 'RTX 2060': 700, 'GTX 1080ti': 850,
                    'GTX 1080': 650, 'GTX 1070ti': 600, 'GTX 1070': 550, 'GTX 1060 6gb': 400}

        print(sep)

        joined_string = ", ".join(item)
        print("Search results for " + joined_string + " will be shown.")

        break
    except:
        print(sep)
        print(error)
        print(sep)

print(sep)

# Boot Sequence
options = Options()
options.add_argument("window-size=1920,1280")
# options.add_argument("--kiosk")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/marketplace/?ref=bookmark")

time.sleep(delayShort)

# Login
phoneNumberButton = driver.find_element(By.XPATH, "//input[@name='email']")
passwordButton = driver.find_element(By.XPATH, "//input[@name='pass']")
loginButton = driver.find_element(By.XPATH, "//div[@aria-label='Accessible login button']")

# Login Process
phoneNumberButton.send_keys(phoneNumber)
passwordButton.send_keys(password)
loginButton.click()

time.sleep(delayMedium)


for name, priceLowest in item.items():
    # Marketplace Searchbar
    searchbar = driver.find_element(By.XPATH, "//input[@placeholder='Search Marketplace']")
    searchbar.send_keys(Keys.CONTROL, 'a')
    searchbar.send_keys(Keys.BACKSPACE)
    searchbar.send_keys(name)

    url1 = driver.current_url
    url2 = url1

    while url1 == url2:
        time.sleep(delayShort)
        searchbar.send_keys(Keys.ENTER)
        url2 = driver.current_url

    time.sleep(delayMedium)

    listingDict = {}

    adInfo = driver.find_elements(By.XPATH,
                                  ".//div[@class='rq0escxv j83agx80 cbu4d94t i1fnvgqd muag1w35 pybr56ya f10w8fjw k4urcfbm "
                                  "c7r68pdi suyy3zvx']")

    for ad in adInfo:
        price = ad.find_element(By.XPATH,
                                ".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm "
                                "aigsh9s9 fe6kdd0r mau55g9w c8b282yb d3f4x2em mdeji52x a5q79mjw g1cxx5fr lrazzd5p "
                                "oo9gr5id']").text
        title = ad.find_element(By.XPATH, "..//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']").text
        location = ad.find_element(By.XPATH,
                                   ".//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5 ojkyduve']").text

        listingDict[title] = price, location

    listingDict = {k.lower(): v for k, v in listingDict.items()}

    for text in list(listingDict):
        if name == "RTX 3090":
            if "3090" not in name:
                del listingDict[text]
        if name == "RTX 3080ti":
            if "3080" and "ti" not in name:
                del listingDict[text]
        if name == "RTX 3080":
            if "3080" not in name or "ti" in name:
                del listingDict[text]
        if name == "RTX 3070ti"

    listingDict = {k: (int(part.replace(",", "") if "," in (part := v[0][2:]) else part), v[1]) for k, v in
                   listingDict.items() if any(i in v[1] for i in cityInclusions) and "·" not in v[0]}

    for k, v in listingDict.items():
        listingDict[k] = v[0]

    listingDict = ({k: v for k, v in listingDict.items() if v <= priceLowest})

    print(listingDict)
