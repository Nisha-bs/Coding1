#!/usr/bin/python3
import pyautogui,time

pyautogui.keyDown('alt')
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.keyUp('alt')
time.sleep(2)
pyautogui.screenshot('word_pdf_1.png')

