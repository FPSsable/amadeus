import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info = json.load(file)

CHANNELACCESSTOKEN = info["CHANNELACCESSTOKEN"]
line_bot_api = LineBotApi(CHANNELACCESSTOKEN)

def main():
    USERID = info["USERID"]
    messages = TextSendMessage(text="おはよう")
    line_bot_api.push_message(USERID,messages=messages)
    
if __name__=="__main__":
    main()

