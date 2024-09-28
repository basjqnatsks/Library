import os
import requests
import zipfile
import json
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
from selenium.webdriver.chrome.service import Service
import shutil
from time import sleep
import io,re
class chrome:
	def __new__(cls, version: int = 127, headless=None, proxies=None, script=None, location=None, Desired_Capabilities=None, pageLoadStrategy=None, roblox_schemes=None, useragent=None, userdata=None):
		cls.__init__(cls)
		cls.Vnum = version
		cls.version = cls.Versions[version]
		cls.Check_And_install_Chrome_Driver(cls)
		cls.Check_And_Install_Chromium(cls)


		cls.chrome(cls, headless, proxies, script, location, Desired_Capabilities, pageLoadStrategy, roblox_schemes, useragent, userdata)
		return cls.var
	def __init__(self, driver_version='104.0.5084.0', headless=None, proxies=None, script=None, location=None, Desired_Capabilities=None, pageLoadStrategy=None, roblox_schemes=None, useragent=None, userdata=None):
		self.JS = """

		Object.defineProperty(navigator, 'languages', {
			get: () => ['en-US', 'en'],
		});
		Object.defineProperty(navigator, 'plugins', {
			get: () => [1, 2, 3, 4, 5],
		});
		window.chrome = {
			runtime: {},
		};
		Object.defineProperty(window, "navigator", {
			Object.defineProperty(window, "navigator", {
				value: new Proxy(navigator, {
				has: (target, key) => (key === "webdriver" ? false : key in target),
				get: (target, key) =>
					key === "webdriver"
					? false
					: typeof target[key] === "function"
					? target[key].bind(target)
					: target[key],
				}),
			});
    """

		self.Versions = {
			73 : {
				'id': '73.0.3683.68',
				'dlink' : 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/619262/chrome-win.zip',
			},
			74: {
				'id': '74.0.3729.6',
				'dlink' : 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/628610/chrome-win.zip',				
			},
			76: {
				'id': '76.0.3809.126',
				'dlink' : 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/654618/chrome-win.zip',	
			}, 
			99: {
				'id': '99.0.4820.0',
				'dlink' : 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/957227/chrome-win.zip',	
				'driver': r'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win_x64%2F957227%2Fchromedriver_win32.zip?generation=1641853561281509&alt=media'
			},
			104: {
				'id': '104.0.5084.0',
				'dlink' : 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/1007330/chrome-win.zip',	
				'driver': r'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win_x64%2F1007330%2Fchromedriver_win32.zip?generation=1653481302838809&alt=media'
			},
			127: {
				'id': '127.0.6508.0',
				'dlink' : 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/1307180/chrome-win.zip',	
				'driver': r'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win_x64%2F1307180%2Fchromedriver_win32.zip?generation=1716953744242378&alt=media'
			}
			
		}




	def Check_And_install_Chrome_Driver(self):
		#Searching For Chromedriver Directory
		if os.path.isdir("C:\\Users\\Public\\chromedriver") is False:
			#Make Dir For Driver
			os.mkdir("C:\\Users\\Public\\chromedriver")

			#Searching For Chromedriver Version Directory
		if os.path.isdir("C:\\Users\\Public\\chromedriver\\" + str(self.version['id'])) is False:
			#Make Dir For Version Driver
			os.mkdir("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']))

		#Searching For Chromedriver Version EXE
		if os.path.isfile("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chromedriver.exe") is False:
			#Download Chrome Driver File
			try:
				with open("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chromedriver.zip", 'wb') as f:
					# f.write(requests.get("http://chromedriver.storage.googleapis.com/" + str(self.version['id']) +"/chromedriver_win32.zip").content)
					print(str(self.version['driver']))
					rTEMP= requests.get(str(self.version['driver']))
					f.write(rTEMP.content)
					
					

			except TypeError:#User Messed Up
				raise ValueError("Wrong version Choice For Chrome Class Driver")
			else:
				#Managing Zip
				zip_ref = zipfile.ZipFile("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chromedriver.zip", 'r')
				zip_ref.extractall("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']))
				zip_ref.close()
				os.remove("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chromedriver.zip")
				try:
					shutil.move('C:\\Users\\Public\\chromedriver\\' + str(self.version['id']) +'\\chromedriver_win32\\chromedriver.exe', 'C:\\Users\\Public\\chromedriver\\'+ str(self.version['id']))
				except:
					pass
				self.patch_exe('C:\\Users\\Public\\chromedriver\\'+ str(self.version['id'])+'\\chromedriver.exe')
	def patch_exe(path):
		with io.open(path, "r+b") as fh:
			content = fh.read()
			match_injected_codeblock = re.search(rb"\{window\.cdc.*?;\}", content)
			if match_injected_codeblock:
				target_bytes = match_injected_codeblock[0]
				new_target_bytes = (
					b'{console.log("undetected chromedriver 1337!")}'.ljust(
						len(target_bytes), b" "
					)
				)
				new_content = content.replace(target_bytes, new_target_bytes)
				if new_content == content:
					print('error')
				else:
					print(
						"found block:\n%s\nreplacing with:\n%s"
						% (target_bytes, new_target_bytes)
					)
				fh.seek(0)
				fh.write(new_content)


	def Check_And_Install_Chromium(self: None) -> None:
		if os.path.isdir("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chrome-win") is False:
			try:
				with open("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chrome.zip", 'wb') as f:
					f.write(requests.get(self.version['dlink']).content)
			except TypeError:#User Messed Up
				raise ValueError("Wrong version Choice For Chrome Class Driver")
			else:
				#Managing Zip
				zip_ref = zipfile.ZipFile("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chrome.zip", 'r')
				zip_ref.extractall("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']))
				zip_ref.close()
				os.remove("C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chrome.zip")


	#sending Javascript file through POST in add_script()
	def send(self, driver, cmd, params={}):
		resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
		url = driver.command_executor._url + resource
		body = json.dumps({'cmd': cmd, 'params': params})
		response = driver.command_executor._request('POST', url, body)
		print(response.get('value'))
		return response.get('value')
	
	def add_script(self, driver, script):
		self.send(self, driver, "Page.addScriptToEvaluateOnNewDocument", {"source": script})


	def debug(self):
		return self.var
	def chrome(self, headless : bool, proxies : str, script : str, location : str, Desired_Capabilities : bool, pageLoadStrategy : bool, roblox_schemes : bool, useragent : str, userdata : str):
		WebDriver.add_script = self.add_script
		
		chrome_options = Options()
		settings = {
			"recentDestinations": [{
					"id": "Save as PDF",
					"origin": "local",
					"account": "",
				}],
				"selectedDestinationId": "Save as PDF",
				"version": 2
			}
		prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
	   				'savefile.default_directory': 'C:\\Users\\MichaelH\\OneDrive - Basin Disposal\\Fuel\\New folder'
	   }
		chrome_options.add_experimental_option('prefs', prefs)
		chrome_options.add_argument('--kiosk-printing')
		chrome_options.add_argument('--mute-audio')
		if userdata:
			chrome_options.add_argument('--user-data-dir=' + userdata)
		if useragent:
			chrome_options.add_argument('----user-agent='+str(useragent))
		#chrome_options.add_argument('----user-agent='+ )
		if Desired_Capabilities:
			capa = DesiredCapabilities.CHROME
			if pageLoadStrategy:
				capa["pageLoadStrategy"] = "none"
		if headless:
			chrome_options.add_argument("--headless")
		if proxies != None:
			chrome_options.add_argument('--proxy-server=' + str(proxies))
		if roblox_schemes == 't':
			prefs = {"protocol_handler.excluded_schemes":{"roblox-player":False,"roblox-studio":False}}
			chrome_options.add_experimental_option("prefs",prefs)
		chrome_options.binary_location = "C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chrome-win\\chrome.exe"
		chromedrivers = "C:\\Users\\Public\\chromedriver\\" + str(self.version['id']) +"\\chromedriver.exe"
		services = Service(executable_path=chromedrivers)
		self.var = webdriver.Chrome(options=chrome_options)
		self.add_script(self, self.var, self.JS)
		return self.var
