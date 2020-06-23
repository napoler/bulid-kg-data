# _*_coding:utf-8_*_
"""
读取ｂｍｅｓ格式数据
保存为ｊｓｏｎ

"""
import tkitFile
tfile=tkitFile.File()

f2 = open("./data/onlyner_bio/dev.txt","r")
lines = f2.readlines()
one_sent={
    "text":[],
    "label":[]
}
data=[]
for line3 in lines:
    # print (line3.replace("\n",'').split("\t"))
    one =line3.replace("\n",'').split(" ")
    print(one)
    # exit()
    if len(one)==2:
        one_sent['text'].append(one[0])
        one_sent['label'].append(one[1])
    elif len(one)==1:
        # print(one_sent)
        print(len(data))
        data.append(one_sent)
        one_sent={
            "text":[],
            "label":[]
        }
    else:
        pass
tj=tkitFile.Json(file_path='data/nerdev.json')
tj.save(data)
print(len(data))
    

    


