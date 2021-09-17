# o2TVSeriesDLer
Script that downloads shows from selected links on o2tvseries.com. Users are expected to fill a field from a Captcha picture. That is a drawback to automation but this script takes care of that with Pytesseract.- an OCR tool. The script screenshots the Captcha's element on the web page with the help of Chromedriver, saves the picture locally, reads the image, and submits the recognized characters. If all goes well, a webpage streams the video of choice in your Chrome browser while the video file is being downloaded. It is powered by Selenium.  
This small project allows for smooth UX when you want to download your favorite shows on the website. The website is known to be ridden with annoying Ads much to the frustration of users. 
Requirements: Pytesseract, Selenium, and Pillow (external libraries)

Example:
```
executable_path = r"C:\\Program Files\\ChromeDriver for Selenium\\chromedriver_for_93.0.4577.exe"
driver = webdriver.Chrome(options=Options(), executable_path=executable_path)
download_dir = r"C:\Users\Priceless\Documents\Programming Projects\showDLer\o2tvDLer"
pytesseract_dir = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
link = "https://o2tvseries.com/Awkwafina-Is-Nora-from-Queens/Season-02/Episode-06"

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
```
