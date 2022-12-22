# импортировать библиотеку
from pytube import YouTube

# попросить пользователя ввести ссылку 
link = input("Enter the link of youtube video:  ")

# создать объект
yt = YouTube(link)
# для наивысшего разрешения
ys = yt.streams.get_highest_resolution()

# показывать сообщение во время загрузки
print("Downloading...")

# указать путь, куда сохранять видео
ys.download("Downloads\python")

# показать сообщение, когда загрузка будет завершена
print("Download completed!!")
