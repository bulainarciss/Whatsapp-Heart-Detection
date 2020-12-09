import pyautogui

im1 = pyautogui.screenshot(region=(400, 100, 900, 600))
im1.save(r"C:\Users\Narcis\PycharmProjects\HeartRecognition\savedimage.png")