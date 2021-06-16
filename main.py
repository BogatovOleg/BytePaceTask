from urllib.request import urlopen
from bs4 import BeautifulSoup
import cv2
import urllib
import os
import time


# Примечание к программе: работает долго из-за того, что каждый раз скачивается и удаляется картинка, скачивать нужно для определения ее разрешения

# функция для получения изображения
def get_image(url):
    img = urllib.request.urlopen(url).read()
    out = open("img.jpg", "wb")
    out.write(img)
    out.close


# функция для получения разрешения картинки
def get_height_and_width():
    image = cv2.imread('img.jpg', 0)
    height, width = image.shape[:2]
    return height, width


# функция для получения размера картинки в кб
def get_size(url):
    site = urlopen(url)
    meta = site.info()['Content-Length']
    return int(meta) / 1000


dict = []
print("The program may take some time to process after entering the link.\nWrite a link: ")
url = input()
f = urllib.request.urlopen(url).read()
soup = BeautifulSoup(f)
for link in soup.findAll('img'):
    if 'http' in str(link.get('src')):
        dict.append(str(link.get('src')))

output = open('output.txt', 'w', encoding='utf-8')
for i in dict:
    get_image(i)
    output.write(i + ', ' + str(get_height_and_width()) + ", " + str(get_size(i)) + '\n')
    os.remove('img.jpg')

output.close()
print("Check file output.txt with results")
