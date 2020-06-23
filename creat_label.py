# -*- coding: utf-8 -*-
import sys
"""
生成标记对应的ｌａｂｅｌｓ列表

"""
def data2label(t_file,label_file):
    f2 = open(t_file,"r")
    lines = f2.readlines()
    one_sent={
        "text":[],
        "label":[]
    }
    data=[]
    for line3 in lines:
        # print (line3.replace("\n",'').split("\t"))
        one =line3.replace("\n",'').split(" ")
        # print(one)
        # exit()

        if len(one)==2:
            # one_sent['text'].append(one[0])
            # one_sent['label'].append(one[1])
            data.append(one)

    save_labels(data,label_file)

def save_labels(data,file="labels.txt"):
    """
    构建数据保存
    """
    labels={}
    with open(file,'w',encoding = 'utf-8') as f1:
        for it in data:
            # for m in it[1]:
            labels[it[1]]=1
            # print(it)
        keys=[]
        for key in labels.keys():
            keys.append(key)
        f1.write("\n".join(keys))

if __name__ == '__main__':
    # if sys.argv[1].upper() == "IOB2BIO":
    "python creat_label.py data/Bmes/train.txt data/Bmes/labels.txt"
    data2label(sys.argv[1],sys.argv[2])