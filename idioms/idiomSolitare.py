import json
import os
import pyperclip

cy = open('./idiom.json')
idioms = json.load(cy)
iin = input("")
ipinyin = ""
repeat = []

for l in idioms:
    if iin == l["word"] or iin[-1] == l["word"][-1]:
        ipinyin = l["pinyin"].split()[-1]

for j in range(10):
    for k in idioms:
        if ipinyin == k["pinyin"].split()[0] and len(k["word"]) == 4 and k["word"] not in repeat:
            ipinyin = k["pinyin"].split()[-1]
            repeat.append(k["word"])
            pyperclip.copy(k["word"])
            os.system('osascript /Users/averyjiang/Desktop/idioms/wechat.scpt')
