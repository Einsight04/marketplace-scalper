import re
import time
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Main
color = 0x0084ff
priceLowest = 0

# Discord
client = commands.Bot(command_prefix='!')
channelId = 921943794910363683
step1 = 0
step2 = 0

# Dicts / Lists
item = {}
cityInclusions = []

# Error Var
error = "Error, try again."
errorEmpty = "No Results Found"


def find_between(message, first, last):
    try:
        start = message.index(first) + len(first)
        end = message.index(last, start)
        return message[start:end]
    except ValueError:
        return ""


def filter_input(test: str) -> str:
    filtered_input = re.findall("[0-9,]", test)
    val = "".join(filtered_input)
    return val


async def run_scalper(channel):
    global step2, item, priceLowest, cityInclusions, keywordKeep

    # Discord
    step2 = 1

    # Items
    listingDict = {}
    listingDictFinal = {}
    listOfValues = []

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

    for name in item:
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

        adInfo = driver.find_elements(By.XPATH,
                                      ".//div[@class='rq0escxv j83agx80 cbu4d94t i1fnvgqd muag1w35 pybr56ya f10w8fjw "
                                      "k4urcfbm c7r68pdi suyy3zvx']")

        for ad in adInfo:
            price = ad.find_element(By.XPATH, ".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em mdeji52x a5q79mjw g1cxx5fr lrazzd5p oo9gr5id']").text
            title = ad.find_element(By.XPATH, "..//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']").text
            location = ad.find_element(By.XPATH, ".//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg "
                                                 "g0qnabr5 ojkyduve']").text

            listingDict[title] = price, location

        listingDict = {k.lower(): v for k, v in listingDict.items()}

        for text in list(listingDict):
            if name == "RTX 3090":
                if "3090" not in text:
                    del listingDict[text]
            elif name == "RTX 3080ti":
                if "3080ti" in text or "3080 ti" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 3080":
                if "3080" not in text or "ti" in text:
                    del listingDict[text]
            elif name == "RTX 3070ti":
                if "3070ti" in text or "3070 ti" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 3070":
                if "3070" not in text or "ti" in text:
                    del listingDict[text]
            elif name == "RTX 3060ti":
                if "3060ti" in text or "3060 ti" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 3060":
                if "3060" not in text or "ti" in text:
                    del listingDict[text]
            elif name == "RTX 2080ti":
                if "2080ti" in text or "2080 ti" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 2080 super":
                if "2080super" in text or "2080 super" in text or "2080s" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 2080":
                if "2080" not in text or "ti" or "super" in text:
                    del listingDict[text]
            elif name == "RTX 2070 super":
                if "2070super" in text or "2070 super" in text or "2070s" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 2070":
                if "2070" not in text or "ti" or "super" in text:
                    del listingDict[text]
            elif name == "RTX 2060 super":
                if "2060super" in text or "2060 super" in text or "2060s" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "RTX 2060":
                if "2060" not in text or "ti" or "super" in text:
                    del listingDict[text]
            elif name == "GTX 1080ti":
                if "1080ti" in text or "1080 ti" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "GTX 1080":
                if "1080" not in text or "ti" in text:
                    del listingDict[text]
            elif name == "GTX 1070ti":
                if "1070ti" in text or "1070 ti" in text:
                    pass
                else:
                    del listingDict[text]
            elif name == "GTX 1070":
                if "1070" not in text or "ti" in text:
                    del listingDict[text]
            elif name == "GTX 1060 6gb":
                if "1060" in text and "6gb" in text:
                    pass
                else:
                    del listingDict[text]
            else:
                if keywordKeep not in text:
                    del listingDict[text]

        listingDict = {k: (int(part.replace(",", "") if "," in (part := filter_input(v[0])) else part), v[1]) for k, v in listingDict.items() if
                       any(i in v[1] for i in cityInclusions) and "·" not in v[0] and "Free" not in v[0]}

        for k, v in listingDict.items():
            listingDict[k] = v[0]

        listingDict = ({k: v for k, v in listingDict.items() if v >= priceLowest})

        for key, value in listingDict.items():
            listOfValues.append(value)

        listOfValues = sorted(listOfValues)[:3]

        priceHighest = listOfValues[2]

        listingDict = ({k: v for k, v in listingDict.items() if v <= priceHighest})

        listingDictFinal.update(listingDict)

        print(listingDictFinal)

    embed = discord.Embed(title="Search Results", description=f"{'no results' if not listingDictFinal else ' '}",
                          color=color)

    for card, price1 in listingDictFinal.items():
        embed.add_field(name=card, value="$" + str(price1), inline=False)

    await channel.send(embed=embed)

    driver.quit()


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_message(message):
    global step1, step2, error, errorEmpty, cityInclusions, item, priceLowest, keywordKeep
    channel = client.get_channel(channelId)
    if message.content == "!scalpy" or message.content == "!Scalpy" or message.content == "!SCALPY":
        embed = discord.Embed(title='Location Paramters:', color=color)
        embed.add_field(name="Mississauga", value="1", inline=False)
        embed.add_field(name="Brampton", value="2", inline=False)
        embed.add_field(name="Oakville", value="3", inline=False)
        embed.add_field(name="Toronto", value="4", inline=False)
        embed.add_field(name="All", value="5", inline=False)
        embed.set_footer(text='EX: search: 1, 2, 3')
        await channel.send(embed=embed)

        step1 = 1
    elif message.content.startswith("search: ") or message.content.startswith("Search: ") or message.content.startswith(
            "SEARCH: ") and step1 == 1:

        inclusionsInput = message.content[8:]

        while True:
            try:
                cityInclusions = []

                inclusions = list(map(lambda x: int(x), inclusionsInput.split(",")))

                if 1 in inclusions:
                    cityInclusions.append("Mississauga")
                if 2 in inclusions:
                    cityInclusions.append("Brampton")
                if 3 in inclusions:
                    cityInclusions.append("Oakville")
                if 4 in inclusions:
                    cityInclusions.append("Toronto")
                if 5 in inclusions:
                    cityInclusions = ["Mississauga", "Brampton", "Oakville", "Toronto"]

                joined_string = ", ".join(cityInclusions)
                embed = discord.Embed(title="Search results within " + joined_string + " will be displayed.",
                                      color=color)
                await channel.send(embed=embed)

                embed = discord.Embed(title='Item Parameters:', color=color)
                embed.add_field(name="3090", value="1", inline=True)
                embed.add_field(name="3080ti", value="2", inline=True)
                embed.add_field(name="3080", value="3", inline=True)
                embed.add_field(name="3070ti", value="4", inline=True)
                embed.add_field(name="3070", value="5", inline=True)
                embed.add_field(name="3060ti", value="6", inline=True)
                embed.add_field(name="3060", value="7", inline=True)
                embed.add_field(name="2080ti", value="8", inline=True)
                embed.add_field(name="2080s", value="9", inline=True)
                embed.add_field(name="2080", value="10", inline=True)
                embed.add_field(name="2070s", value="11", inline=True)
                embed.add_field(name="2070", value="12", inline=True)
                embed.add_field(name="2060s", value="13", inline=True)
                embed.add_field(name="2060", value="14", inline=True)
                embed.add_field(name="1080ti", value="15", inline=True)
                embed.add_field(name="1080", value="16", inline=True)
                embed.add_field(name="1070ti", value="17", inline=True)
                embed.add_field(name="1070", value="18", inline=True)
                embed.add_field(name="All", value="19", inline=False)
                embed.set_footer(text='EX: item: 1, 2, 3')
                await channel.send(embed=embed)

                step1 = 0
                step2 = 1

                break
            except Exception as e:
                embed = discord.Embed(title=error, description=e, color=color)
                await channel.send(embed=embed)

                break
    elif message.content.startswith("search.c: ") or message.content.startswith(
            "Search.c: ") or message.content.startswith("SEARCH.C: ") and step1 == 1:

        inclusionsInput = message.content[10:]
        while True:
            try:
                cityInclusions = []

                cityInclusions = list(map(lambda x: x, inclusionsInput.split(",")))

                cityInclusions = [city.title() for city in cityInclusions]

                joined_string = ", ".join(cityInclusions)
                embed = discord.Embed(title="Search results within " + joined_string + " will be displayed.",
                                      color=color)
                await channel.send(embed=embed)

                embed = discord.Embed(title='Item Parameters:', color=color)
                embed.add_field(name="3090", value="1", inline=True)
                embed.add_field(name="3080ti", value="2", inline=True)
                embed.add_field(name="3080", value="3", inline=True)
                embed.add_field(name="3070ti", value="4", inline=True)
                embed.add_field(name="3070", value="5", inline=True)
                embed.add_field(name="3060ti", value="6", inline=True)
                embed.add_field(name="3060", value="7", inline=True)
                embed.add_field(name="2080ti", value="8", inline=True)
                embed.add_field(name="2080s", value="9", inline=True)
                embed.add_field(name="2080", value="10", inline=True)
                embed.add_field(name="2070s", value="11", inline=True)
                embed.add_field(name="2070", value="12", inline=True)
                embed.add_field(name="2060s", value="13", inline=True)
                embed.add_field(name="2060", value="14", inline=True)
                embed.add_field(name="1080ti", value="15", inline=True)
                embed.add_field(name="1080", value="16", inline=True)
                embed.add_field(name="1070ti", value="17", inline=True)
                embed.add_field(name="1070", value="18", inline=True)
                embed.add_field(name="All", value="19", inline=False)
                embed.set_footer(text='EX: item: 1, 2, 3')
                await channel.send(embed=embed)

                step1 = 0
                step2 = 1

                break
            except Exception as e:
                embed = discord.Embed(title=error, description=e, color=color)
                await channel.send(embed=embed)

                break

    elif message.content.startswith("item: ") or message.content.startswith("Item: ") or message.content.startswith(
            "ITEM: ") and step2 == 1:

        itemsInput = message.content[6:]

        while True:
            try:
                item = []
                priceLowest = 300

                items = list(map(lambda x: int(x), itemsInput.split(",")))

                if 1 in items:
                    item.append("RTX 3090")
                if 2 in items:
                    item.append("RTX 3080ti")
                if 3 in items:
                    item.append("RTX 3080")
                if 4 in items:
                    item.append("RTX 3070ti")
                if 5 in items:
                    item.append("RTX 3070")
                if 6 in items:
                    item.append("RTX 3060ti")
                if 7 in items:
                    item.append("RTX 3060")
                if 8 in items:
                    item.append("RTX 2080ti")
                if 9 in items:
                    item.append("RTX 2080 super")
                if 10 in items:
                    item.append("RTX 2080")
                if 11 in items:
                    item.append("RTX 2070 super")
                if 12 in items:
                    item.append("RTX 2070")
                if 13 in items:
                    item.append("RTX 2060 super")
                if 14 in items:
                    item.append("RTX 2060")
                if 15 in items:
                    item.append("GTX 1080ti")
                if 16 in items:
                    item.append("GTX 1080")
                if 17 in items:
                    item.append("GTX 1070ti")
                if 18 in items:
                    item.append("GTX 1070")
                if 19 in items:
                    item = ['RTX 3090', 'RTX 3080ti', 'RTX 3080', 'RTX 3070ti', 'RTX 3070',
                            'RTX 3060ti', 'RTX 3060', 'RTX 2080ti', 'RTX 2080 super', 'RTX 2080',
                            'RTX 2070 super', 'RTX 2070', 'RTX 2060 super', 'RTX 2060', 'GTX 1080ti',
                            'GTX 1080', 'GTX 1070ti', 'GTX 1070']

                joined_string = ", ".join(item)
                embed = discord.Embed(title="Searching for:", description=joined_string, color=color)
                await channel.send(embed=embed)

                await run_scalper(channel)

                break
            except Exception as e:
                embed = discord.Embed(title="Search Results",
                                      description=errorEmpty,
                                      color=color)
                await channel.send(embed=embed)

                break
    elif message.content.startswith("item.c: ") or message.content.startswith("Item.c: ") or message.content.startswith(
            "ITEM.c: ") and step2 == 1:

        itemsInput = message.content[8:]

        while True:
            try:
                item = []
                priceLowest = 25

                if '"' in itemsInput:
                    keywordKeep = (find_between(itemsInput.lower(), '"', '"'))

                itemsInput = itemsInput.replace('"', '')
                item = itemsInput.split(", ")

                joined_string = ", ".join(item)
                embed = discord.Embed(title="Searching for:", description=joined_string, color=color)
                await channel.send(embed=embed)

                await run_scalper(channel)

                break
            except Exception as e:
                embed = discord.Embed(title="Search Results",
                                      description=errorEmpty,
                                      color=color)
                await channel.send(embed=embed)

                break


client.run('OTI2OTYzMjIwOTUzMDU5NDQy.YdDTxg.To2ap4KKetYdbDd5nVqraHeqk6M')
