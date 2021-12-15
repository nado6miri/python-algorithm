# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import qrcode
from PIL import Image
import cv2 as cv




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def basic_qrcode(filename, data):
    img = qrcode.make(data)
    img.save(filename)
    pass

def advanced_qrcode(ver, filename, data):
    qr = qrcode.QRCode(version=ver, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save(filename)
    pass

def decode_qrcode(finename):
    im = cv.imread(finename)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print("retval = ", retval)
    print("points = ", points)
    print("straight_qrcode = ", straight_qrcode)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
#    basic_qrcode("naver1.png", "https://www.naver.com")
#    advanced_qrcode(1, "naver2.png", "https://www.naver.com")
    decode_qrcode("naver1.png")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
