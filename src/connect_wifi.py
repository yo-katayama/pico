import wifi
import socketpool

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

def connect_wifi():
    # .envファイルから環境変数を読み込む
    env_vars = load_env(filename="./../.env")
    ssid = env_vars.get("WIFI_SSID")
    password = env_vars.get("WIFI_PASSWORD")

    # Wifiに接続する
    wifi.radio.connect(ssid, password)
    pool = socketpool.SocketPool(wifi.radio)  # Wi-Fi接続上でソケットを管理するためのオブジェクトを作成
    print("Your IP is: %s" % (wifi.radio.ipv4_address))

    return wifi, pool
