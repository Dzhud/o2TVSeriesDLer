# o2TVSeriesDLer
Script that automates show downloads from selected links on o2tvseries.com. Users are expected to fill a field from a Captcha picture. That is a drawback to automation but this script takes care of that with Pytesseract.- an OCR tool.
- The script screenshots the Captcha's element on the web page with the help of Chromedriver, saves the picture locally, reads the image, and submits the recognized characters. 
- If all goes well, a webpage streams the video of choice in your Chrome browser while the video file is being downloaded. It is powered by Selenium. You could use any browser's drive though. 
- This small project allows for smooth UX when you want to download your favorite shows on the website. The website is known to be ridden with annoying Ads much to the frustration of users. 
# Prerequisites 
Pytesseract, Selenium, and Pillow (external libraries)
Install [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract). You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable `pytesseract.pytesseract.tesseract_cmd`.
Do not forget to install it:
`pip install pytesseract`

- You can download Selenium Driver for your machine [here](https://chromedriver.chromium.org/downloads).
- Do not also forget to install and import the necessary the necesary pacakages:
`pip install selenium`
- You'll need the Python Imaging Library (PIL) (or the Pillow [fork](https://pypi.org/project/Pillow/))
# Other Information
- Observe this download link:
`https://o2tvseries.com/Awkwafina-Is-Nora-from-Queens/Season-02/Episode-06`
It's how the site can be scraped to download the video.
- The OCR that is powered by Pytesseract has a success rate of about 65% in reading the 5 CAPTCHA characters on the picture.
# Example
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
# Licence
This project is licensed under the MIT license - see the [LICENCE.txt](https://github.com/Dzhud/o2TVSeriesDLer/blob/main/LICENSE.txt) for details.
