# -*- coding: utf-8 -*-

import sys
import os
import time


def phone_analyze(device_ids):
    if device_ids == "":
        cmd1 = "adb shell uiautomator dump -x"
        cmd2 = "adb shell cat "
    else:
        cmd1 = "adb -s " + str(device_ids) + " shell uiautomator dump -x"
        cmd2 = "adb -s " + str(device_ids) + " shell cat "

    dump_file = ""
    print(cmd1)
    resp1 = os.popen(cmd1)
    resp_lines1 = resp1.readlines()
    for resp_line in resp_lines1:
        if "to:" in resp_line:
            dump_file = str(resp_line).split("to:")[1].strip()

    if dump_file == "":
        print("Dump File Error Please Try Again!")
        return False
    time.sleep(3)
    cmd2 = cmd2 + dump_file
    print(cmd2)
    resp = os.popen(cmd2)
    resp_lines = resp.readlines()
    value_dict_list = []
    for resp_line in resp_lines:
        if "xml" in resp_line:
            nodes = str(resp_line).split("><")
            for node in nodes:
                temp_dict = {}
                contents = str(node).split('" ')
                for content in contents:
                    if "=" in content:
                        title = str(content).split("=")[0]
                        value = str(content).split("=")[1].replace('"', '')
                        temp_dict[title] = value
                try:
                    if len(temp_dict) > 0 and temp_dict["resource-id"] != "":
                        value_dict_list.append(temp_dict)
                except Exception as errs:
                    print("Exception ", errs)

    for value_dict in value_dict_list:
        print(value_dict)


try:
    device_id = str(sys.argv[1])
except Exception as err:
    print("Device ID is auto matching.. Exception: ", err)
    device_id = ""
phone_analyze(device_id)
