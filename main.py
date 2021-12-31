import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Main Var

# Items
lowestValue = 200
itemDict = {'RTX 3O6O': 900, 'RTX 2070': 900, 'RTX 2060 super': 850, 'GTX 1080ti': 850, 'GTX 1080': 700,
            'GTX 1070': 550}

# Information Var
phoneNumber = "6478852142"
password = "Gk20040429!"

# Time Var
delayShort = 2
delayMedium = 5
delayLong = 10

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

# Marketplace Searchbar
searchbar = driver.find_element(By.XPATH, "//input[@placeholder='Search Marketplace']")
searchbar.send_keys("750w Power Supply")
time.sleep(delayLong)
searchbar.send_keys(Keys.ENTER)

time.sleep(delayMedium)

listingDict = {}

location = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div[2]")

adInfo = location.find_elements(By.XPATH,
                              "//div[@class='rq0escxv j83agx80 cbu4d94t i1fnvgqd muag1w35 pybr56ya f10w8fjw k4urcfbm c7r68pdi suyy3zvx']")

for ad in adInfo:
    price = ad.find_element(By.XPATH,
                            ".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 fe6kdd0r mau55g9w c8b282yb d3f4x2em mdeji52x a5q79mjw g1cxx5fr lrazzd5p oo9gr5id']").text
    title = ad.find_element(By.XPATH, ".//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']").text

    listingDict[title] = price

listingDict = {k.lower(): v for k, v in listingDict.items()}

for i in list(listingDict):
    if "power" not in i:
        del listingDict[i]

listingDict = ({k: v for k, v in listingDict.items() if "·" not in v})


for k, v in listingDict.items():
    v = v[2:]
    if "," in v:
        v = v.replace(",", "")
    v = int(v)
    listingDict[k] = v

listingDict = {k: int(v) for k, v in listingDict.items()}

listingDict = ({k: v for k, v in listingDict.items() if v <= 110})

print(listingDict)
