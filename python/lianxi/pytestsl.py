import pytest
from selenium import webdriver
from supermar import WebKeys
from time import sleep

def test_login():
    wx = webdriver ()
    wx.open('http://192.168.1.42')
    sleep(2)
    wx.input("id","username","admin")
    sleep(2)
    wx.input("id","passwd","123456")
    sleep(2)
    wx.quit()
if __name__=="__main__":
    pytest.main("pytestsl.py")

