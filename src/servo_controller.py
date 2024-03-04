import board
import time
import pwmio
from adafruit_motor import servo


def set_servo_motor():
    pwm_pin = pwmio.PWMOut(board.GP0, frequency=50)

    # サーボモータオブジェクトの作成
    servo_motor = servo.Servo(pwm_pin, min_pulse=500, max_pulse=2500)

    return servo_motor

def reset_servo_motor():
    pwm_pin = pwmio.PWMOut(board.GP0, frequency=50)

    # サーボモータオブジェクトの作成
    servo_motor = servo.Servo(pwm_pin, min_pulse=500, max_pulse=2500)

    # モーター位置の初期化
    servo_motor.angle = 0
    time.sleep(1)  # サーボが移動するのを待つ
    servo_motor.angle = 180
    time.sleep(1)  # サーボが移動するのを待つ
    servo_motor.angle = 0
    time.sleep(1)  # サーボが移動するのを待つ

    # GPIOピンの開放
    pwm_pin.deinit()
