import json
import adafruit_ntp
import socketpool
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_httpserver import Server, Request, Response
from src.connect_wifi import connect_wifi
from src.led_handling import blink_led
from src.use_display import set_display, set_text_group
from src.servo_controller import set_servo_motor, reset_servo_motor

# Wifiに接続する
wifi, pool = connect_wifi()

# ntpを用いて現在時刻を取得
pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=9)

# サーバー起動時にPicoWのルートディレクトリからデータを提供できるようにする
server = Server(pool, "/static", debug=True)

# OLEDディスプレイの初期化
display = set_display()
text_group = set_text_group()

#フォント読み込み
font_data = bitmap_font.load_font('/fonts/tuffy16.bdf')

# サーボモータの初期化
current_servo_angle = 0
reset_servo_motor()
servo_motor = set_servo_motor()

# 状態を返す関数
def get_current_data():
    now = ntp.datetime
    return {"date": f"{now.tm_year}{now.tm_mon:02d}{now.tm_mday:02d}",
            "time": f"{now.tm_hour:02d}{now.tm_min:02d}{now.tm_sec:02d}",
            "angle": f"{str(current_servo_angle)}"}

# ルートにアクセスした際に実行される関数
@server.route("/")
def base(request: Request):
    data = get_current_data()

    # text_groupを新しく初期化して以前の表示内容をクリア
    text_group = set_text_group()

    # モニタ表示
    text_area = label.Label(font_data, text=data["date"], x=5, y=15)
    text_group.append(text_area)
    text_area = label.Label(font_data, text=data["time"], x=5, y=30)
    text_group.append(text_area)
    text_area = label.Label(font_data, text=data["angle"], x=5, y=45)
    text_group.append(text_area)
    display.show(text_group)

    # 辞書をJSON文字列に変換
    json_data = json.dumps(data)
    # JSON文字列をResponseに渡す
    return Response(request, json_data, content_type="application/json")

@server.route("/servo", methods=["POST"])
def set_servo_angle(request: Request):
    global current_servo_angle
    try:
        # リクエストから角度を取得
        data = json.loads(request.body)
        angle = data["angle"]
        # 角度をサーボモータに設定
        servo_motor.angle = angle
        current_servo_angle = angle
        return Response(request, json.dumps({"status": "OK", "angle": angle}), content_type="application/json")
    except Exception as e:
        return Response(request, json.dumps({"status": "error", "message": str(e)}), content_type="application/json")


# Start the HTTP server
print("Starting web server")
blink_led()
server.serve_forever(str(wifi.radio.ipv4_address))
