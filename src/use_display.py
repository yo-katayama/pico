import displayio
import board
import busio
import adafruit_displayio_ssd1306

def set_display():
    #ディスプレイ初期化
    displayio.release_displays()

    #I2C設定
    SDA = board.GP16
    SCL = board.GP17
    i2c = busio.I2C(SCL, SDA)

    #ディスプレイ設定
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
    return display

def set_text_group():
    return displayio.Group()
