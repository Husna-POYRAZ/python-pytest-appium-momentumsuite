import pytest
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.ios import XCUITestOptions
import time

with open("test_settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

    localHost = jsonObject['LOCAL']['host']
    localIosApp = jsonObject['LOCAL']['ios']['app']
    localIosDeviceName = jsonObject['LOCAL']['ios']['deviceName']
    localIosRemoteDebugProxy = jsonObject['LOCAL']['ios']['remoteDebugProxy']
    print(localHost)

    options = XCUITestOptions().load_capabilities({
    'platformName': 'iOS',
    'appium:automationName': 'XCUITest',
    'appium:app': localIosApp,
    'appium:autoAcceptAlerts': True,
    'appium:language': 'en',
    'appium:locale': 'en',
    'appium:fullReset': True,
    'appium:noReset': False,
    'appium:deviceName': localIosDeviceName,
    'appium.remoteDebugProxy': localIosRemoteDebugProxy,
    })

driver = webdriver.Remote(localHost, options=options)

def test_local_ios():
  elOne = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//*[contains(@label , '2')])[1]")))
  elOne.click()

  elTwo = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='+']")
  elTwo.click()

  elThree = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='5']")
  elThree.click()

  elFour = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name='=']")
  elFour.click()

  time.sleep(3)

  driver.quit()