import json
import os
import pyperclip

cy = open('desktop/idioms/idiom.json')
idioms = json.load(cy)
repeat = []
digitNum = int(input("index"))
digit = input("text")

for i in idioms:
    if digit == i["word"][digitNum] and len(i["word"]) == 4:
        pyperclip.copy(i["word"])
        os.system('osascript /Users/averyjiang/Desktop/idioms/wechat.scpt')