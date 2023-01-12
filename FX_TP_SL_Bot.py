
while True:
    #print("-----------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------***START***------------------------------------------------------------")
    #print("-----------------------------------------------------------------------------------------------------------------")

    entry = float(input("Enter Entry Price: "))
    atr = float(input("Enter ATR value (as shown):  "))
    direction = input("Enter BUY (b) or SELL (s): ")
    pair = input("What Pair? Regular (r) || JPY/Oil (j) || Gold/US30 (x): ")

    TPsize = atr*1.0
    SLsize = atr*1.0

    if pair == "r":
        print()

        if direction == "b":
            SL = entry - SLsize
            SL = round(SL,5)
            TP = entry + TPsize
            TP = round(TP,5)
            print("\t ==> Take Profit: ",TP)
            print("\t ==> Stop Loss:   ",SL)
        elif direction == "s":
            SL = entry + SLsize
            SL = round(SL,5)
            TP = entry - TPsize
            TP = round(TP,5)
            print("\t ==> Take Profit: ",TP)
            print("\t ==> Stop Loss:   ",SL)

    elif pair == "j":
        print()

        if direction == "b":
            SL = entry - SLsize
            SL = round(SL,3)
            TP = entry + TPsize
            TP = round(TP,3)
            print("\t ==> Take Profit: ",TP)
            print("\t ==> Stop Loss:   ",SL)
        elif direction == "s":
            SL = entry + SLsize
            SL = round(SL,3)
            TP = entry - TPsize
            TP = round(TP,3)
            print("\t ==> Take Profit: ",TP)
            print("\t ==> Stop Loss:   ",SL)

    elif pair == "x":
        print()

        if direction == "b":
            SL = entry - SLsize
            SL = round(SL,2)
            TP = entry + TPsize
            TP = round(TP,2)
            print("\t ==> Take Profit: ",TP)
            print("\t ==> Stop Loss:   ",SL)
        elif direction == "s":
            SL = entry + SLsize
            SL = round(SL,2)
            TP = entry - TPsize
            TP = round(TP,2)
            print("\t ==> Take Profit: ",TP)
            print("\t ==> Stop Loss:   ",SL)
