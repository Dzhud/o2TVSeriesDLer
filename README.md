# o2TVSeriesDLer
Script that downloads shows from selected links on o2tvseries.com. Users are expected to fill a field from a Captcha picture. That is a drawback to automation but this script takes care of that with Pytesseract.- an OCR tool. The script screenshots the Captcha's element on the web page with the help of Chromedriver, saves the picture locally, reads the image, and submits the recognized characters. If all goes well, a webpage streams the video of choice in your Chrome browser while the video file is being downloaded. It is powered by Selenium.  