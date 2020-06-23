# _*_coding:utf-8_*_
"""
自动验证数据ｎｅｒ

"""
from tkitMarker_bert import Marker
Ner_Marker=Marker(model_path="./model/tmarker_bert_ner/")

Ner_Marker.load_model()

import tkitFile
tfile=tkitFile.File()


tj=tkitFile.Json(file_path='data/ner/dev.json')
i=0
n=0
f=0
good=0
all=0
for item in tj.auto_load():
    print("###"*20)
    o_ners=Ner_Marker.get_mark_data(item).get("实体")
    text= ''.join(item['text'])
    # result=TNer.pre([text])
    result=Ner_Marker.pre_ner(text)
    all=all+1
    if o_ners==result:
        good=good+1
        pass
    else:
        print('all',all,'good',good)
        print("句子：",text)
        print("实体：",o_ners)
        print("预测：",result)

    # if o == result[0][1]:
    #     i=i+1
    # elif len(result[0][1])==0:
    #     n=n+1
    # else:
    #     f=f+1


    # print('预测准确',i,'没有结果',n,'失败',f,'准确率',i/all)

    # print('预测准确',i,'没有结果',n,'失败',f,'准确率(只计算有返回的)',i/(all-n),'准确率',i/all)

