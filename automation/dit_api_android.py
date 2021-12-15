# -*- coding: utf-8 -*-
import time
import os


class DIT_API_Android:

    def __init__(self):
        self.setup()

    def setup(self):
        self.phone_info = self.get_phone_info()
        if str(self.phone_info["manufacturer"]).upper() == "LGE":
            if self.phone_info["model"] == "LM_V510N":
                self.phone = LG_V50S(self.phone_info["device_id"])
            else:
                self.phone = LGPhone(self.phone_info["device_id"])
        elif str(self.phone_info["manufacturer"]).lower() == "samsung":
            if self.phone_info["model"] == "SM_N950N":
                self.phone = SM_N950N(self.phone_info["device_id"])
            else:
                self.phone = SamsungPhone(self.phone_info["device_id"])
        else:
            self.phone = AndroidPhone(self.phone_info["device_id"])

    def run(self):

        return True

    def get_phone_info(self):
        ids = ""
        product = ""
        model = ""
        cmd = "adb devices -l"
        resp = os.popen(cmd)
        resp_lines = resp.readlines()
        for resp_line in resp_lines:
            if "List of" not in resp_line and "device" in resp_line:
                device_info = str(resp_line).split("device")
                ids = str(device_info[0]).strip()
                product = str(device_info[1]).split("product:")[1].split(" ")[0].strip()
                model = str(device_info[1]).split("model:")[1].split(" ")[0].strip()
                manufacturer = self.get_phone_info_manufacturer(ids)
        return {"device_id": ids, "product": product, "model": model, "manufacturer": manufacturer}

    def get_phone_info_manufacturer(self, device_id):
        adb_shell_cmd = "adb -s {} shell ".format(device_id)
        cmd = adb_shell_cmd + 'getprop ro.product.manufacturer'
        resp = os.popen(cmd)
        resp_lines = resp.readlines()
        for resp_line in resp_lines:
            if resp_line != '':
                return resp_line.rstrip()
        return ''

    def touch_slide(self, x1, y1, x2, y2):
        self.phone.touch_slide(x1, y1, x2, y2)

    def touch_screen(self, x, y):
        self.phone.touch_screen(x, y)

    def touch_screen_long(self, x, y):
        self.phone.touch_screen_long(x, y)

    def key_press_by_alias(self, desc):
        self.phone.key_press_by_alias(desc)

    def run_application(self, desc1, desc2=''):
        '''
        How to get application list and use packages in desc1
        > adb shell pm list packages
        '''
        self.phone.run_application(desc1, desc2)

    def ui_click_by_text(self, desc):
        return self.phone.ui_click_by_text(desc)

    def ui_position_list_by_text(self, desc):
        return self.phone.ui_position_list_by_text(desc)

    def ui_position_list_by_resources_id(self, desc):
        return self.phone.ui_position_list_by_resources_id(desc)

    def ui_click_by_resources_id(self, desc):
        return self.phone.ui_click_by_resources_id(desc)

    def ui_find_string_by_text(self, desc):
        return self.phone.ui_find_string_by_text(desc)

    def ui_find_string_list_by_resources_id(self, desc):
        return self.phone.ui_find_string_list_by_resources_id(desc)

    def do_action_connect(self, tv_name):
        print("Connect Miracast Scenario at TVName : {} ".format(tv_name))
        return self.phone.do_action_connect(tv_name)

    def do_action_disconnect(self):
        print("Disconnect Miracast Scenario ")
        return self.phone.do_action_disconnect()

    def do_action_play(self):
        print("Play Video at Phone")
        return self.phone.do_action_play()

    def do_action_back_to_idle(self):
        print("Back To Idle at Phone")
        return self.phone.do_action_back_to_idle()

    def input_text(self, desc):
        self.phone.input_text(desc)

    def screen_shot(self, filename='temp.png'):
        self.phone.screen_shot(filename)

    def reboot(self):
        self.phone.reboot()

    def wakeup_and_screen_on(self):
        self.phone.wakeup_and_screen_on()


class AndroidPhone:
    keymap = {
        "0": "0",
        "SOFT_LEFT": "1",
        "SOFT_RIGHT": "2",
        "HOME": "3",
        "BACK": "4",
        "CALL": "5",
        "ENDCALL": "6",
        "0": "7",
        "1": "8",
        "2": "9",
        "3": "10",
        "4": "11",
        "5": "12",
        "6": "13",
        "7": "14",
        "8": "15",
        "9": "16",
        "STAR": "17",
        "POUND": "18",
        "DPAD_UP": "19",
        "DPAD_DOWN": "20",
        "DPAD_LEFT": "21",
        "DPAD_RIGHT": "22",
        "DPAD_CENTER": "23",
        "VOLUME_UP": "24",
        "VOLUME_DOWN": "25",
        "POWER": "26",
        "CAMERA": "27",
        "CLEAR": "28",
        "A": "29",
        "B": "30",
        "C": "31",
        "D": "32",
        "E": "33",
        "F": "34",
        "G": "35",
        "H": "36",
        "I": "37",
        "J": "38",
        "K": "39",
        "L": "40",
        "M": "41",
        "N": "42",
        "O": "43",
        "P": "44",
        "Q": "45",
        "R": "46",
        "S": "47",
        "T": "48",
        "U": "49",
        "V": "50",
        "W": "51",
        "X": "52",
        "Y": "53",
        "Z": "54",
        "COMMA": "55",
        "PERIOD": "56",
        "ALT_LEFT": "57",
        "ALT_RIGHT": "58",
        "SHIFT_LEFT": "59",
        "SHIFT_RIGHT": "60",
        "TAB": "61",
        "SPACE": "62",
        "SYM": "63",
        "EXPLORER": "64",
        "ENVELOPE": "65",
        "ENTER": "66",
        "DEL": "67",
        "GRAVE": "68",
        "MINUS": "69",
        "EQUALS": "70",
        "LEFT_BRACKET": "71",
        "RIGHT_BRACKET": "72",
        "BACKSLASH": "73",
        "SEMICOLON": "74",
        "APOSTROPHE": "75",
        "SLASH": "76",
        "AT": "77",
        "NUM": "78",
        "HEADSETHOOK": "79",
        "FOCUS": "80",
        "PLUS": "81",
        "MENU": "82",
        "NOTIFICATION": "83",
        "SEARCH": "84",
        "MEDIA_PLAY_PAUSE": "85",
        "MEDIA_STOP": "86",
        "MEDIA_NEXT": "87",
        "MEDIA_PREVIOUS": "88",
        "MEDIA_REWIND": "89",
        "MEDIA_FAST_FORWARD": "90",
        "MUTE": "91",
        "PAGE_UP": "92",
        "PAGE_DOWN": "93",
        "PICTSYMBOLS": "94",
        "WAKEUP": "224"
    }

    def __init__(self, device_id):
        self.device_id = device_id
        self.setup()

    def setup(self):
        self.adb_shell_cmd = "adb -s {} shell ".format(self.device_id)

    def reboot(self):
        cmd = "adb -s {} reboot ".format(self.device_id)
        resp = os.popen(cmd)

    def wakeup_and_screen_on(self):
        cmd = self.adb_shell_cmd + "input keyevent 26"  # Screen Off or Screen On
        resp = os.popen(cmd)
        time.sleep(3)
        cmd = self.adb_shell_cmd + "input keyevent 224"  # Screen On
        resp = os.popen(cmd)
        time.sleep(3)
        self.touch_slide(100, 200, 300, 400)
        time.sleep(3)

    def screen_shot(self, filename):
        cmd = self.adb_shell_cmd + "screencap /sdcard/{}".format(filename)
        resp = os.popen(cmd)
        cmd = self.adb_shell_cmd + " /sdcard/{}".format(filename)
        cmd = str(cmd).replace("shell", "pull")
        resp = os.popen(cmd)

    def input_text(self, desc):
        cmd = self.adb_shell_cmd + "input text {}".format(desc)
        resp = os.popen(cmd)

    def touch_screen(self, x, y):
        cmd = self.adb_shell_cmd + "input tap {} {}".format(x, y)
        resp = os.popen(cmd)

    def touch_slide(self, x1, y1, x2, y2):
        cmd = self.adb_shell_cmd + "input swipe {} {} {} {} 300".format(x1, y1, x2, y2)
        resp = os.popen(cmd)

    def touch_screen_long(self, x, y):
        cmd = self.adb_shell_cmd + "input swipe {} {} {} {} 2000".format(x, y, x, y)
        resp = os.popen(cmd)

    def run_application(self, desc1, desc2=''):
        if desc2 == '':
            run_cmd = "am start {}".format(desc1)
        else:
            run_cmd = "am start -a {} -n {}".format(desc1, desc1 + "/" + desc2)
        cmd = self.adb_shell_cmd + run_cmd
        resp = os.popen(cmd)

    def ui_click_by_text(self, desc):
        xml_file = ""
        for i in range(5):
            cmd = self.adb_shell_cmd + 'uiautomator dump -x'
            resp = os.popen(cmd)
            resp_line = resp.readline()
            if "dumped" in resp_line:
                xml_file = str(resp_line).split(":")[1].strip()
                break

        if xml_file != "":
            cmd = self.adb_shell_cmd + 'cat {}'.format(xml_file)
            resp = os.popen(cmd)
            resp_lines = resp.readlines()
            for resp_line in resp_lines:
                if "xml" in resp_line:
                    str_lines = str(resp_line).split(">")
                    for str_line in str_lines:
                        # print("desc: {}, str_line : {}".format(desc, str_line))
                        if desc in str_line:
                            bounds = str(str_line).split('bounds="')[1].split('"')[0].strip()
                            axy = str(bounds).split('][')[0].replace('[', '').split(',')
                            bxy = str(bounds).split('][')[1].replace(']', '').split(',')
                            x = int((int(axy[0]) + int(bxy[0])) / 2)
                            y = int((int(axy[1]) + int(bxy[1])) / 2)
                            print("{}, {}, {}, {}".format(bounds, x, y, str_line))
                            self.touch_screen(x, y)
                            print("Text {} Click OK".format(desc))
                            return True
        return False

    def ui_position_list_by_text(self, desc):
        xml_file = ""
        for i in range(5):
            cmd = self.adb_shell_cmd + 'uiautomator dump -x'
            resp = os.popen(cmd)
            resp_line = resp.readline()
            if "dumped" in resp_line:
                xml_file = str(resp_line).split(":")[1].strip()
                break

        desc_list = {}
        if xml_file != "":
            cmd = self.adb_shell_cmd + 'cat {}'.format(xml_file)
            resp = os.popen(cmd)
            resp_lines = resp.readlines()
            for resp_line in resp_lines:
                if "xml" in resp_line:
                    str_lines = str(resp_line).split(">")
                    for str_line in str_lines:
                        for desc_str in desc:
                            if desc_str in str_line:
                                bounds = str(str_line).split('bounds="')[1].split('"')[0].strip()
                                axy = str(bounds).split('][')[0].replace('[', '').split(',')
                                bxy = str(bounds).split('][')[1].replace(']', '').split(',')
                                x = int((int(axy[0]) + int(bxy[0])) / 2)
                                y = int((int(axy[1]) + int(bxy[1])) / 2)

                                print("{}, {}, {}, {}".format(bounds, x, y, str_line))
                                print("Text : {}, desc_list : {}".format(desc, desc_list))

                                desc_list[desc_str] = {"x": x, "y": y}
        return desc_list

    def ui_position_list_by_resources_id(self, desc):
        xml_file = ""
        for i in range(5):
            cmd = self.adb_shell_cmd + 'uiautomator dump -x'
            resp = os.popen(cmd)
            resp_line = resp.readline()
            if "dumped" in resp_line:
                xml_file = str(resp_line).split(":")[1].strip()
                break

        desc_list = []
        if xml_file != "":
            cmd = self.adb_shell_cmd + 'cat {}'.format(xml_file)
            resp = os.popen(cmd)
            resp_lines = resp.readlines()
            for resp_line in resp_lines:
                if "xml" in resp_line:
                    str_lines = str(resp_line).split(">")
                    for str_line in str_lines:
                        if desc in str_line:
                            bounds = str(str_line).split('bounds="')[1].split('"')[0].strip()
                            axy = str(bounds).split('][')[0].replace('[', '').split(',')
                            bxy = str(bounds).split('][')[1].replace(']', '').split(',')
                            x = int((int(axy[0]) + int(bxy[0])) / 2)
                            y = int((int(axy[1]) + int(bxy[1])) / 2)
                            print(bounds, x, y, str_line)
                            desc_list.append({"x": x, "y": y})
        return desc_list

    def ui_click_by_resources_id(self, desc):
        xml_file = ""
        for i in range(5):
            cmd = self.adb_shell_cmd + 'uiautomator dump -x'
            resp = os.popen(cmd)
            resp_line = resp.readline()
            if "dumped" in resp_line:
                xml_file = str(resp_line).split(":")[1].strip()
                break

        if xml_file != "":
            cmd = self.adb_shell_cmd + 'cat {}'.format(xml_file)
            resp = os.popen(cmd)
            resp_lines = resp.readlines()
            for resp_line in resp_lines:
                if "xml" in resp_line:
                    str_lines = str(resp_line).split(">")
                    for str_line in str_lines:
                        if desc in str_line:
                            bounds = str(str_line).split('bounds="')[1].split('"')[0].strip()
                            axy = str(bounds).split('][')[0].replace('[', '').split(',')
                            bxy = str(bounds).split('][')[1].replace(']', '').split(',')
                            x = int((int(axy[0]) + int(bxy[0])) / 2)
                            y = int((int(axy[1]) + int(bxy[1])) / 2)
                            print(bounds, x, y, str_line)
                            self.touch_screen(x, y)
                            return True
        return False

    def ui_find_string_by_text(self, desc):
        xml_file = ""
        for i in range(5):
            cmd = self.adb_shell_cmd + 'uiautomator dump -x'
            resp = os.popen(cmd)
            resp_line = resp.readline()
            if "dumped" in resp_line:
                xml_file = str(resp_line).split(":")[1].strip()
                break

        if xml_file != "":
            cmd = self.adb_shell_cmd + 'cat {}'.format(xml_file)
            resp = os.popen(cmd)
            resp_lines = resp.readlines()
            for resp_line in resp_lines:
                if "xml" in resp_line:
                    str_lines = str(resp_line).split(">")
                    for str_line in str_lines:
                        if desc in str_line:
                            resp = str(str_line) + ">"
                            return resp
        return ''

    def ui_find_string_list_by_resources_id(self, desc):
        xml_file = ""
        for i in range(5):
            cmd = self.adb_shell_cmd + 'uiautomator dump -x'
            resp = os.popen(cmd)
            resp_line = resp.readline()
            if "dumped" in resp_line:
                xml_file = str(resp_line).split(":")[1].strip()
                break

        str_list = []
        if xml_file != "":
            cmd = self.adb_shell_cmd + 'cat {}'.format(xml_file)
            resp = os.popen(cmd)
            resp_lines = resp.readlines()
            for resp_line in resp_lines:
                if "xml" in resp_line:
                    str_lines = str(resp_line).split(">")
                    for str_line in str_lines:
                        if desc in str_line:
                            str_list.append(str(str_line) + ">")
        return str_list

    def key_press_by_alias(self, desc):
        cmd = self.adb_shell_cmd + "input keyevent {}".format(self.get_numbers_for_key(desc))
        resp = os.popen(cmd)

    def get_numbers_for_key(self, desc):
        # 3 – > "KEYCODE_HOME”
        # 4 – > "KEYCODE_BACK”
        # refer - https://mkblog.co.kr/2018/09/10/android-adb-input-command/
        return self.keymap[desc.upper()]

    def do_action_back_to_idle(self):
        for i in range(5):
            self.key_press_by_alias("back")


class LGPhone(AndroidPhone):

    def do_action_connect(self, tv_name):
        self.do_action_back_to_idle()
        for i in range(3):
            self.touch_slide(700, 50, 700, 2500)
            time.sleep(1)
        self.ui_click_by_text("화면 공유")  # self.touch_screen(395, 925)
        time.sleep(0.5)
        for i in range(5):
            self.touch_screen(550, 2100)
            time.sleep(0.5)
        self.ui_click_by_text("검색")  # self.touch_screen(780, 2080)
        time.sleep(0.5)
        for i in range(50):
            if self.ui_click_by_text(tv_name):
                print("TV Name Click OK")
                return True
            time.sleep(0.5)
            self.touch_slide(700, 2000, 700, 1700)
            time.sleep(1)
        return False

    def do_action_disconnect(self):
        self.do_action_back_to_idle()
        for k in range(2):
            time.sleep(1)
            for i in range(3):
                self.touch_slide(700, 50, 700, 2500)
                time.sleep(1)
            self.ui_click_by_text("화면 공유")  # self.touch_screen(395, 925)
            time.sleep(0.5)
            for i in range(5):
                self.touch_screen(550, 2100)
                time.sleep(0.5)
            self.key_press_by_alias("back")
            time.sleep(1)
        self.do_action_back_to_idle()
        return True

    def do_action_play(self):
        self.do_action_back_to_idle()
        time.sleep(0.5)
        self.run_application("com.android.gallery3d")
        time.sleep(3)
        self.ui_click_by_text("플레이")
        time.sleep(2)
        self.touch_screen(300, 500)
        time.sleep(2)
        self.touch_screen(300, 300)
        time.sleep(2)
        self.touch_screen(540, 1070)
        time.sleep(2)
        self.touch_screen(560, 1165)
        time.sleep(10)

        return True


class SamsungPhone(AndroidPhone):

    def do_action_connect(self, tv_name):
        self.do_action_back_to_idle()
        for i in range(3):
            self.touch_slide(700, 50, 700, 2500)
            time.sleep(1)
        self.ui_click_by_text('Smart View')
        time.sleep(5)
        for i in range(50):
            if self.ui_click_by_text(tv_name):
                break
            time.sleep(0.5)
            self.touch_slide(700, 1500, 700, 1100)
            time.sleep(1)
        return True

    def do_action_disconnect(self):
        self.do_action_back_to_idle()
        for k in range(2):
            time.sleep(1)
            for i in range(3):
                self.touch_slide(700, 50, 700, 2500)
                time.sleep(1)
            self.touch_screen(395, 925)
            time.sleep(0.5)
            for i in range(5):
                self.touch_screen(550, 2100)
                time.sleep(0.5)
            self.key_press_by_alias("back")
            time.sleep(1)
        for i in range(3):
            self.key_press_by_alias("back")
        return True

    def do_action_play(self):
        self.do_action_back_to_idle()
        time.sleep(1)
        self.run_application("com.sec.android.gallery3d")
        time.sleep(3)
        self.ui_click_by_text('Movie')
        time.sleep(1)
        self.ui_click_by_text('버튼')
        time.sleep(1)
        self.ui_click_by_text('동영상 재생')
        time.sleep(10)
        return True


class LG_V50S(LGPhone):

    def print_model(self):
        print("SM_N950N")

    def ui_click_by_text(self, desc):
        if desc == "":
            self.touch_screen(395, 925)
            return True
        else:
            return LGPhone.ui_click_by_text(self, desc)


class SM_N950N(SamsungPhone):

    def print_model(self):
        print("SM_N950N")



'''
from dit_api_android import DIT_API_Android



self.android = DIT_API_Android()

self.android.run_application('com.google.android.youtube')

self.android.ui_click_by_resources_id('media_route_button')

self.android.ui_click_by_text('확인')

self.android.touch_screen(500, 650)

self.android.touch_slide(700, 50, 700, 2500)

https://developer.android.com/studio/command-line/adb
'''
