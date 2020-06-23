##　Ｎｅｒ数据标注处理助手


## 格式转化

Argument error: sys.argv[1] should belongs to \"IOB2BIO/BIO2BIOES/BIOES2BIO/IOB2BIOES\


Convert NER tag schemes among IOB/BIO/BIOES.
        For example: if you want to convert the IOB tag scheme to BIO, then you run as following:
            python tagSchemeConverter.py IOB2BIO input_iob_file output_bio_file
        Input data format is the standard CoNLL 2003 data format.


比如
https://github.com/napoler/NER_corpus_chinese/blob/v0.1/ordata/dev.txt
转化BIO为BMOES格式

```
#BIO->BMOES
python tagSchemeConverter.py BIO2BMOES  dev.txt data.dev


```

生成对应的ｌａｂｅｌ列表

```

python creat_label.py data/Bmes/train.txt data/Bmes/labels.txt

```