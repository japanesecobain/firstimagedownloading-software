'''Welcome to the Aoi Araki Web Image Downloader'''

from selenium import webdriver
from selenium.webdriver.common.by import By

def searches_online():
    driver = webdriver.Chrome()

    whatever_you_search = input("What do you want an image of? ")
    driver.get(f"https://www.google.com/search?tbm=isch&q={whatever_you_search}")

    all_img = driver.find_element(By.CLASS_NAME, 'MjjYud')
    img = all_img.find_element(By.TAG_NAME, "img")

    image_url = img.get_attribute('src')
    print(f'Image URL: {image_url}')

    with open("file.png", "wb") as f:
        f.write(img.screenshot_as_png)

    driver.quit()

searches_online()