import wifi
import socketpool
import ipaddress
import json
from adafruit_httpserver import Server, Request, Response
import time

def load_env(filename=".env"):
    env_vars = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    env_vars[key] = value
    except OSError:
        pass  # ファイルが存在しない場合のエラーハンドリング
    return env_vars

# .envファイルから環境変数を読み込む
env_vars = load_env()
ssid = env_vars.get("WIFI_SSID")
password = env_vars.get("WIFI_PASSWORD")

# Wifiに接続する
wifi.radio.connect(ssid, password)
pool = socketpool.SocketPool(wifi.radio)  # Wi-Fi接続上でソケットを管理するためのオブジェクトを作成
print("Your IP is: %s" % (wifi.radio.ipv4_address))

# 外部インターネットアクセスが出来ることを確認する
external_ip = ipaddress.ip_address("8.8.8.8")
print("Internet reached with %sms round trip" % wifi.radio.ping(external_ip))

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
server.serve_forever(str(wifi.radio.ipv4_address))
