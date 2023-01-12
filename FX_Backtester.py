atr = float(input("Enter ATR value (as shown): "))
entry = float(input("Enter ENTRY Price: "))
exi = (float(input("Enter EXIT Price: ")))
dir = input("Enter Buy (B) or Sell (S): ")
flag = (input("Did The Trade Reach 1*ATR? (Y) or (N): " ))

### Calculations only valid for: 1*ATR TP and 1*ATR SL

if dir == "B":
    diff = exi - entry
    ratio = diff/atr
    if flag == "Y":
        profit = float((ratio) + 1)
    elif flag == "N":
        profit = float(ratio)*2
    profit = round(profit,4)
    print(profit)

elif dir == "S":
    diff = entry - exi
    ratio = diff/atr
    if flag == "Y":
        profit = float((ratio) + 1)
    elif flag == "N":
        profit = float(ratio)*2
    profit = round(profit,4)
    print(profit)
#Enter ATR value: 39.8786
#Enter ENTRY Price: 29853.6
#Enter EXIT Price: 29865.5
