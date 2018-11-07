import json

aa = {'log_id': 6949279247979303911, 'direction': 0, 'words_result_num': 8, 'words_result': [{'probability': {'variance': 0.001704, 'average': 0.985727, 'min': 0.838386}, 'words': '他9-13赞过的微博(34)'}, {'probability': {'variance': 0.0, 'average': 0.999635, 'min': 0.999406}, 'words': '王中磊'}, {'probability': {'variance': 0.037171, 'average': 0.857503, 'min': 0.584912}, 'words': '十关注'}, {'probability': {'variance': 0.003846, 'average': 0.963925, 'min': 0.810645}, 'words': '9-12来自 iphone X'}, {'probability': {'variance': 2.2e-05, 'average': 0.997937, 'min': 0.981243}, 'words': '她会在天堂里!弟弟,节哀顺变!'}, {'probability': {'variance': 0.006675, 'average': 0.960202, 'min': 0.761532}, 'words': '唐家三少:我好想她。带我走吧'}, {'probability': {'variance': 0.0, 'average': 0.999754, 'min': 0.999723}, 'words': '评论'}, {'probability': {'variance': 0.0, 'average': 0.999735, 'min': 0.999363}, 'words': '132'}], 'language': -1}


# bb = json.dumps(aa)
cc = aa['words_result']
result = ''
for i in cc:
    result = result + '\n'  + i['words']

print(result)

