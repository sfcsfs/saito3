from django.http import HttpResponse
from django.shortcuts import render
import random
from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import sys 
from django.views.generic import View,DetailView,TemplateView
from datetime import datetime, date
from .import test
from .models import Device
from django.urls import reverse_lazy
import japanize_matplotlib
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse







class X1: #グローバルな変数を用意するためだけの存在
    kazu = {"a":0}

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

#本番環境で二回行動するようなら奇数の時選ばれたのを-1マイナス処理で対応

@login_required
def index(request):
    #print(x2.kazu)
    contacts = Device.objects.all
    context = {
        'test': contacts,
    }
    
    return render(request, 'home.html',context)




#　ajax用view
class c_AjaxView(View):
    def get(self, request):
        i = x2.kazu["x"] #部屋のidをランダムで取得
        i2 = Device.objects.get(pk=i)
        context = {
        'test1': i2.name
    }
        return HttpResponse(context.values(),request)
i_ajax = c_AjaxView.as_view()


#本番環境で二回行動するようなら奇数の時選ばれたのを-1マイナス処理で対応(重要)



@login_required
def yosouhee(request): #homeから予想のボタンの押されたら遷移させる
    if request.method == 'POST':
        return render(request, 'home2.html')

@login_required
def sousuhe(request): #homeからソースコードのボタンの押されたら遷移させる
    if request.method == 'POST':
        return render(request, 'home3.html')


"""
def kaeru(request): #yosouから投票場ボタンの押されたら遷移させる
    if request.method == 'POST':
        contacts = Device.objects.all
        context = {
            'test': contacts,
        }
    
        return render(request, 'home.html',context)

"""
class Index2(TemplateView):

    #テンプレートファイル連携
    template_name = "home2.html"

    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):

        #グラフオブジェクト
        qs    = Device.objects.all()  #モデルクラス(ProductAテーブル)読込
        x     = [x.name for x in qs]           #X軸データ
        y     = [y.touhyou for y in qs]        #Y軸データ
        #color = [('b' if i == max(x) else 'r') for i in x] # 最大の奴だけ色変える

        chart = test.Plot_Graph(x,y)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
        return context

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('tyuusenn:index'))
                """
                contacts = Device.objects.all
                context = {
                'test': contacts,
                    }
                    
    
                return render(request, 'home.html',context)
                """
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')


#ログアウト
@login_required
def Logout(request):
    if request.method == 'POST':
        logout(request)
    # ログイン画面遷移
        return HttpResponseRedirect(reverse('tyuusenn:Login'))
        
        




