import requests
from io import BytesIO
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Film show downloader for o2TVSeries

__author__ = 'Dzhud' #Dzhud on Github

class SeriesDLerfor02TVSeries:
    
    def inputURL(self, url):
        global self_url
        self_url = url

    def enable_download_headless(self, browser, download_dir):
        
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)

    def for_chromedriver(self, download_dir, executable_path):
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
        chrome_options.add_argument(f'user-agent={userAgent}')
        chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False})
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        global driver
        driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)

    def get_title(self):
        global video_text1, video_text2, video_text3
        driver.get(self_url)
        video_text1 = driver.find_element_by_xpath("/html/body/div/div[6]/a[3]").text
        video_text2 = driver.find_element_by_xpath("/html/body/div/div[6]/a[4]").text
        video_text2 = video_text2[0] + video_text2[-1]
        video_text3 = driver.find_element_by_xpath("/html/body/div/div[6]/a[5]").text 
        video_text3 = video_text3[0] + video_text3[-1]

    def get_video(self):
        
        videoDL = driver.find_element_by_xpath("/html/body/div/div[12]/div[2]/a")
        get_href = videoDL.get_attribute('href')
        element = driver.get(get_href)

    def screenshot_webpage(self):
        global png, var_location, var_size
        target_Captcha_to_screenshot = driver.find_element_by_xpath("//img[@alt='CAPTCHA Code']")
        var_location = target_Captcha_to_screenshot.location
        var_size = target_Captcha_to_screenshot.size
        png = driver.get_screenshot_as_png()
        
    def filter_webpage_image(self):
        global im
        im = Image.open(BytesIO(png))
        left = var_location['x']
        top = var_location['y']
        right = var_location['x'] + var_size['width']
        bottom = var_location['y'] + var_size['height']
        im = im.crop((left, top, right, bottom))
        im = ImageEnhance.Sharpness(im)
        im = im.enhance(0.0)
        im = im.filter(ImageFilter.MinFilter(3))
        im.save('study_img.png')

    def get_image_texts(self, pytesseract_dir):
        global image_to_string
        pytesseract.pytesseract.tesseract_cmd = pytesseract_dir
        image_to_string = pytesseract.image_to_string(im)
        image_to_string = image_to_string[0:5]
        print(image_to_string)

    def submit_read_texts(self):
        global current_page
        element = driver.find_element_by_xpath("/html/body/center/form/input[1]")
        element.send_keys(image_to_string)
        captcha_submit = driver.find_element_by_xpath("/html/body/center/form/input[2]")
        driver.execute_script("arguments[0].click();", captcha_submit)
        current_page = driver.current_url
        current_page_content = driver.find_element_by_xpath("/html/body").text
        if "Error: You did not enter text !!" or "Error: Captcha Does Not Match" in current_page_content:
            return "Oops!!! Seem Captcha Field is null or Captcha doesn't match.\nLoad script again" 

    def download_stream_video(self):
         
        req = requests.get(current_page, headers={'User-Agent': 'Mozilla/5.0'}, stream = True)
        with open(f'{video_text1 }{video_text2 } {video_text3}.mp4', 'wb') as video_file:
            for i in req.iter_content():
                if i:
                    video_file.write(i)
                    

executable_path = ""
driver = webdriver.Chrome(options=Options(), executable_path=executable_path)
download_dir = ""
pytesseract_dir = ""
link = ""

initializer = SeriesDLerfor02TVSeries()
initializer.inputURL(link)
initializer.enable_download_headless(driver, download_dir)
initializer.for_chromedriver(download_dir, executable_path)
initializer.get_title()
initializer.get_video()
initializer.screenshot_webpage()
initializer.filter_webpage_image()
initializer.get_image_texts(pytesseract_dir)
initializer.submit_read_texts()
initializer.download_stream_video()
