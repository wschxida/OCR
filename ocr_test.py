import json
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14705875'
API_KEY = 'cMmbG105NN0jMnYKafsw9hst'
SECRET_KEY = 'ET9hCv0FNO44YguH6MscekYkYkaVkAMm'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# image = get_file_content('example.jpg')
#
# """ 调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)

url = "https://wx2.sinaimg.cn/mw690/006NGRWIly1fwz7o2gugij30u00ez419.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
ocr_result = client.basicGeneralUrl(url, options)

words_result = ocr_result['words_result']
result = ''

for words in words_result:
    result = result + '\n'  + words['words']

print(result)