import json
import time
from adafruit_httpserver import Server, Request, Response
from src.connect_wifi import connect_wifi
from src.led_handling import blink_led

# Wifiに接続する
wifi, pool = connect_wifi()

# サーバー起動時にPicoWのルートディレクトリからデータを提供できるようにする
server = Server(pool, "/static", debug=True)

# 現在の日付を返す関数
def get_current_date():
    now = time.localtime()  # 現在のローカル時刻を取得
    return {"date": f"{now.tm_year}{now.tm_mon:02d}{now.tm_mday:02d}{now.tm_hour:02d}{now.tm_min:02d}{now.tm_sec:02d}"}

# ルートにアクセスした際に実行される関数
@server.route("/")
def base(request: Request):
    # 現在の日付データを取得
    date_data = get_current_date()
    # 辞書をJSON文字列に変換
    json_data = json.dumps(date_data)
    # JSON文字列をResponseに渡す
    return Response(request, json_data, content_type="application/json")

# Start the HTTP server
print("Starting web server")
blink_led()
server.serve_forever(str(wifi.radio.ipv4_address))
