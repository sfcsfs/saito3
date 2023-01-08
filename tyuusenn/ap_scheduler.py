from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponse
from django.shortcuts import render
import random
import sys 
from .models import Device

"""
class X1: #グローバルな変数を用意するためだけの存在
    kazu = {"x":0}

x2 = X1()


def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(rannsuu, 'interval',  seconds=5)#5秒おきに実行
  scheduler.start()

def rannsuu(): # 任意の関数名  # ここに定期実行したい処理を記述する
    #print("ただいまテスト中")
    
    x3 = random.randint(1,18) #ランダムにid生成。上のクラスのを上書きもする。
    x2.kazu = {
    'x': x3
    }
    i = x2.kazu["x"] #部屋のidをランダムで取得
    i2 = Device.objects.get(pk=i)
    print(i2) #テスト出力
    i2.touhyou = i2.touhyou + 1 #投票数１プラス
    print(i2.touhyou) #テスト出力
    i2.save() 

"""