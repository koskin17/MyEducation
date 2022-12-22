# импортировать библиотеку
import qrcode

# ссылка на сайт
input_data = "https://car-price-prediction-project.herokuapp.com/"

# Создание объекта
# version: определяет размер изображения (1-40), box_size = размер каждого блока в px, border = толщина рамки.
qr = qrcode.QRCode(version=1,box_size=10,border=5)

#add_date :  передать текст из input
qr.add_data(input_data)

# конвертировать в изображение
qr.make(fit=True)

# указать цвета переднего и заднего плана  
img = qr.make_image(fill='black', back_color='white')

# сохранить изображение
img.save('qrcode_img.png')
