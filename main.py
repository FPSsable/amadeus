import json
import random
import time
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info = json.load(file)

CHANNELACCESSTOKEN = info["CHANNELACCESSTOKEN"]
line_bot_api = LineBotApi(CHANNELACCESSTOKEN)

def main():
    USERID = info["USERID"]
    l = ["おきなさい","いつまで寝てるんや？","遅刻するで",]
    messages = TextSendMessage(text="おはよ")
    line_bot_api.push_message(USERID,messages=messages)
    time.sleep(600)
    messages = TextSendMessage(text=random.choice(l))
    line_bot_api.push_message(USERID,messages=messages)
    
if __name__=="__main__":
    main()

