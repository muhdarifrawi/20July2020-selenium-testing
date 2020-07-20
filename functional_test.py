from selenium import webdriver


browser = webdriver.Chrome(executable_path=r"C:\\Users\\Muhd Arif Bin Rawi\\chromedriver_win32\\chromedriver.exe")


# browser.get("https://localhost:8000")
browser.get("http://127.0.0.1:5000/")