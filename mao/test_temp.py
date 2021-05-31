import argparse
import storetbutter
import buy
import os
import quitbuy
import time
# import output
import butter
import kaishi
import gameover
from u3driver import AltrunUnityDriver,By

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help="ip")   # 命令行参数 -i ip地址
    parser.add_argument('-s', help="device serial")   # 命令行参数 -s 设备号

    args = parser.parse_args()
    ip = args.i or None
    device_s = args.s or ""

    udriver = AltrunUnityDriver(device_s,"",ip,TCP_PORT=13000,timeout=60)
    num = 0
    kaishi.AutoRun(udriver)
    while True:
        while True:
            if udriver.object_exist(By.PATH,"//UICamera//Game//DeathPopup//GameOver"):
                gameover.AutoRun(udriver)
                break
        storetbutter.AutoRun(udriver)
        text = udriver.find_object(By.PATH, "//Canvas//Background//Coin//CoinsCounter",).get_text()
        text = int(text)
        text1 = udriver.find_object(By.PATH, "//Canvas//Background//Premium//PremiumCounter",).get_text()
        text1 = int(text1)
        if text >= 1500 and text1 >=5 :
            buy.AutoRun(udriver)
            print("当前鱼骨头有{}个".format(text))
            break
        else:
            quitbuy.AutoRun(udriver)
            num1 = udriver.find_object(By.PATH, "//UICamera//GameOver//Highscore//PlayerEntry//score",).get_text()
            num += int(num1)
            print("当前鱼骨头{}个，你已跑{}米".format(text, num))
            butter.AutoRun(udriver)

        # 开始脚本的回放:

    udriver.stop()