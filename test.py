error = "error"

sep = "--------------------------------------------------"

item = {}

while True:
    try:
        itemsInput = input('30 SERIES:\n3090 [1], 3080ti [2], 3080 [3], 3070ti [4], 3070 [5], 3060ti [6], 3060 [7]\n20 '
                      'SERIES:\n2080ti [8], 2080s [9], 2080 [10], 2070s [11], 2070 [12], 2060s [13], 2060 [14]\n10 '
                      'SERIES:\n1080ti [15], 1080 [16], 1070ti [17], 1070 [18], 1060 [19]\n>>> ')

        items = list(map(lambda x: int(x), itemsInput.split(",")))

        print(items)

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
        if item == 20:
            item = {'RTX 3090': 3500, 'RTX 3080ti': 2500, 'RTX 3080': 2000, 'RTX 3070ti': 1500, 'RTX 3070': 1200, 'RTX 3060ti': 1000, 'RTX 3060': 900, 'RTX 2080ti': 950, 'RTX 2080 super': 950, 'RTX 2080': 900, 'RTX 2070 super': 900, 'RTX 2070': 850, 'RTX 2060 super': 850, 'RTX 2060': 700, 'GTX 1080ti': 850, 'GTX 1080': 650, 'GTX 1070ti': 600, 'GTX 1070': 550, 'GTX 1060 6gb': 400}

        break
    except:
        print(sep)
        print(error)
        print(sep)

for name, price in item.items():
    print(name)

    print(price)