"""
作者:  马茼茼   

时间:  2018/12/4  12:27  

文件:  Controller.py

"""

from flask import Flask,request
from flask_cors import *
from textrank4zh import TextRank4Keyword,TextRank4Sentence
import json

server=Flask(__name__)
CORS(server, supports_credentials=True)
@server.route("/lda/word",methods=["GET"])
def ldaWord():

    doc_word=request.args.get("content")

    # 返回词
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=doc_word, lower=True, window=2)
    item_word=str(tr4w.get_keywords(num=20))
    return item_word

@server.route("/lda/sentence",methods=["GET"])
def ldaSentence():

    doc_sen = request.args.get("content")
    #返回句子
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=doc_sen, lower=True, source='all_filters')
    item_sentence=str(tr4s.get_key_sentences(num=3))

    return item_sentence


if __name__ == '__main__':
    server.run(debug=True,port=1234)