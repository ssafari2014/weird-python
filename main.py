from selenium import webdriver
from googletrans import Translator
from selenium.webdriver.common.by import By


# functions translate
def translate_text_world(word):
    translator = Translator()
    translation = translator.translate(word, src='fa', dest='en')
    word = translation.text.lower()
    print(word)


user_input = input('Enter your keyword ?  ')
user_country = input('Enter your country ?  ')
translator = Translator()
translation = translator.translate(user_country, src='fa', dest='en')
words = translation.text.lower()
translation2 = translator.translate(user_input, src='fa', dest='en')
words2 = translation2.text.lower()
driver = webdriver.Firefox()
driver.get(
    f'https://divar.ir/s/{words}-province/{words2}?goods-business-type=marketplace&q={user_input}')

# exel file in data
