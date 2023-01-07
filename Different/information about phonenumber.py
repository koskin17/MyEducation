# Модуль phonenumbers позволяет получить информацию о номере телефона.
# В данном случае методом geocoder выводится информация о регионе
import phonenumbers
from phonenumbers import geocoder, carrier

PhoneNumber = phonenumbers.parse("+380675811930")
Region = geocoder.description_for_number(PhoneNumber, "en")

print(Region)
