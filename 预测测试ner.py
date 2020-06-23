# _*_coding:utf-8_*_
"""
自动验证数据ｎｅｒ

"""

from tkitMarker_bert import Marker
Ner_Marker=Marker(model_path="./model/tmarker_bert_ner/")

Ner_Marker.load_model()
import os

from pyltp import Parser
from pyltp import SementicRoleLabeller
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
LTP_DATA_DIR = '/mnt/data/dev/model/ltp/ltp_data_v3.4.0' 

ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl.model')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`



def ner(text):
    """
    获取ｎｅｒ数据
    """
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    words = segmentor.segment(text)  # 分词
    # print ('\t'.join(words))
    segmentor.release()  # 释放模型

    postagger = Postagger() # 初始化实例
    postagger.load(pos_model_path)  # 加载模型

    # words = ['元芳', '你', '怎么', '看']  # 分词结果
    postags = postagger.postag(words)  # 词性标注
    # print("##"*30)
    # print ('\t'.join(postags))
    postagger.release()  # 释放模型

    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型
    # words = ['元芳', '你', '怎么', '看']
    # postags = ['nh', 'r', 'r', 'v']
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    recognizer.release()  # 释放模型
    words_list=[]
    for word, flag in zip(words, netags):
        # print(word,flag)
        if flag.startswith("B-"):
            one=[]
            one.append(word)
        elif flag.startswith("I-"):
            one.append(word)
        elif flag.startswith("E-"):
            one.append(word)
            words_list.append("".join(one))
        elif flag.startswith("S-"):
            words_list.append(word)
    # print(words_list)
    # return words_list,words, postags,netags
    return words_list














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
        print("ltp:",ner(text))

    # if o == result[0][1]:
    #     i=i+1
    # elif len(result[0][1])==0:
    #     n=n+1
    # else:
    #     f=f+1


    # print('预测准确',i,'没有结果',n,'失败',f,'准确率',i/all)

    # print('预测准确',i,'没有结果',n,'失败',f,'准确率(只计算有返回的)',i/(all-n),'准确率',i/all)

