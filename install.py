def install():
    import os
    from time import sleep
    while True:
        try:
            from colorama import *
            init()
        except:
            os.system('pip install colorama')
            from colorama import *
            init()
        else:
            break
    while True:
        try:
            from bs4 import BeautifulSoup
            import zipfile
            import tarfile
            import urllib
            import base64
            import urllib3
            from urllib import *
            import websocket
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.action_chains import ActionChains
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.remote.command import Command
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.remote.webdriver import WebDriver
            import json
            import speech_recognition as sr
            import shutil
            from pydub import AudioSegment
            import getpass
            import cv2
            import requests
            from urllib import request as urlrequest
            import threading
            from threading import Thread
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.action_chains import ActionChains
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.remote.command import Command
            from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.remote.webdriver import WebDriver
            import json
            import os
            import math
            from queue import Queue
            import urllib
            import time
            from urllib.request import Request, urlopen
            import zipfile
            from random import *
            import os.path
            import signal
            import random
            from clarifai.rest import ClarifaiApp
            from PIL import Image
            from io import BytesIO
            from urllib.request import Request, urlopen
            from colorama import *
            print("---Requirements Success---")
        except:
            print(Fore.RED + "Requirements Failed")
            try:
                print(Fore.YELLOW + "---Installing Requirements---")
                sleep(1)
                os.system('python -m pip install --upgrade pip')
                os.system('pip install bcolors')
                os.system('pip install bs4')
                
                os.system('pip install websocket-client')
                os.system('pip install speechrecognition')
                os.system('pip install selenium')
                os.system('pip install pydub')
                os.system('pip install requests[socks]')
                os.system('pip install requests')
                os.system('pip install clarifai')
                os.system('pip install pillow')
                os.system('pip install colorama')
                os.system('pip install opencv-python')
                os.system('pip install opencv-contrib-python')
            except:
                pass
            else:
                os.system('cls')
        else:
            break