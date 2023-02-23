# タイトル：水道料金当番抽選サイト


![image](https://user-images.githubusercontent.com/105050060/220829743-cab397af-74fa-42f7-a7d5-ba3f84b55c8b.png)

## URL:  https://2-nennsaito.pythonanywhere.com/tyuusenn/

## 使用技術
・Python 3.8.10
・Django 4.1.3
・Ajax
・SQLite
・Ubuntu
・PythonAnywhere

## 構造
tyuusenn/test.py = HTTP のレスポンスステータスコードが想定通りになっているか確認するためのプログラム。  
tyuusenn/views.py = メインプログラム。各種ページへの遷移機能、ログイン・ログアウト、グラフ出力、Ajaxとの連携、またローカル環境では一定間隔ごとに数字の抽選を行う。  
tyuusenn/g.py = tyuusenn/views.pyと共にグラフの出力を担う。  
tyuusenn/apps.py = ローカル環境ではtyuusenn/views.pyと共に一定間隔ごとに数字の抽選を行う。  
tyuusenn/models.py  = 投票（抽選結果）を格納するためのモデルクラス。  

templates/home.html = Ajaxが実装され一定間隔で投票結果が出力されるメインページ。表を更新するため３０秒で自動リロードされる設定。  
templates/home2.html = グラフの出力ができるページ。  
templates/home3.html = 抽選の公平性を担保するため一部のプログラムを紹介しているページ。  
