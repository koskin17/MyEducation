Как отправить электронное письмо с помощью smtplib.
Если посмотреть на API модуля smtplib, то сразу становится понятно, как его использовать. Напишем быстрый пример, который показывает, как отправить электронное письмо.

import smtplib

# данные почтового сервиса
user = "your-address@yandex.ru"
passwd = "**********"
server = "smtp.yandex.ru"
port = 587

# тема письма
subject = "Тестовое письмо от Python."
# кому
to = "person@mail.ru"
# кодировка письма
charset = 'Content-Type: text/plain; charset=utf-8'
mime = 'MIME-Version: 1.0'
# текст письма
text = "Отправкой почты управляет Python!"

# формируем тело письма
body = "\r\n".join((f"From: {user}", f"To: {to}", 
       f"Subject: {subject}", mime, charset, "", text))

try:
    # подключаемся к почтовому сервису
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.ehlo()
    # логинимся на почтовом сервере
    smtp.login(user, passwd)
    # пробуем послать письмо
    smtp.sendmail(user, to, body.encode('utf-8'))
except smtplib.SMTPException as err:
    print('Что - то пошло не так...')
    raise err
finally:
    smtp.quit()
Здесь импортируется только модуль smtplib. Две трети этого кода используются для настройки электронной почты. Большинство переменных не требуют пояснений, поэтому рассмотрим только одну переменную body.

Для создания этой переменной используется метод str.join(), который объединяет все предыдущие переменные в одну строку, где каждая строка заканчивается символом возврата каретки ('/r') плюс новая строка ('/n'). В итоге, переменная body, будет выглядеть как-то так:

'From: your-address@yandex.ru\r\nTo: person@mail.ru\r\n
Subject: Тестовое письмо от Python.\r\nMIME-Version: 1.0\r\n
Content-Type: text/plain; charset=utf-8\r\n\r\n
Отправкой почты управляет Python!'
После этого, устанавливается соединение с сервером электронной почты, а затем вызываете метод smtp.sendmail модуля smtplib для отправки электронной почты. Если сервер электронной почты требует аутентификации, то перед отправкой письма необходимо авторизироваться на этом сервере:

smtp.login(user, passwd)
Обычно, представленный код выше оборачивают в функцию и вызывают ее с некоторыми из этих параметров.

import smtplib

def send_email(from_addr, to_addr, subject, text, encode='utf-8'):
    """
    Отправка электронного письма (email)
    """

    # оставшиеся настройки
    passwd = "**********"
    server = "smtp.yandex.ru"
    port = 587
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {to_addr}", 
           f"Subject: {subject}", mime, charset, "", text))

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)
        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

if __name__ == "__main__":
    from_addr = "your-address@yandex.ru"
    to_addr = "person@mail.ru"
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    send_email(from_addr, to_addr, subject, text)
Иногда, часть оставшихся настроек задается файлом конфигурации в создаваемом приложения. Добавим файл конфигурации для хранения информации о сервере и адресе отправителя. Сохраним файл конфигурации как email.ini. Это удобно, если почтовый сервер обновляется и имя меняется, то не надо лезть в код, нужно только изменить файл конфигурации.

[smtp]
server = smtp.yandex.ru
port = 587
email = your-address@yandex.ru
passwd = **********
Получился очень простой файл конфигурации, в котором есть только один раздел с пометкой [smtp]. Чтобы прочитать файл конфигурации и превратить его в словарь Python, будем использовать модуль ConfigParser. Вот обновленная версия кода.

import os
import smtplib
from configparser import ConfigParser

def send_email(to_addr, subject, text, encode='utf-8'):
    """
    Отправка электронного письма (email)
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    # проверка наличия файла `email.ini`
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Конфигурация не найдена!")

    # извлечение переменных из конфигурации
    server = cfg.get("smtp", "server")
    port = cfg.get("smtp", "port")
    from_addr = cfg.get("smtp", "email")
    passwd = cfg.get("smtp", "passwd")
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {to_addr}", 
           f"Subject: {subject}", mime, charset, "", text))

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)
        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

if __name__ == "__main__":
    to_addr = "person@mail.ru"
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    send_email(to_addr, subject, text)
Добавили небольшую проверку в код. Сначала получаем путь, по которому находится сам скрипт отправки электронной почты base_path. Затем объединяем этот путь с именем email.ini, чтобы получить полный путь к файлу конфигурации. Потом проверяем наличие этого файла и в случае успешной проверки создаем объект ConfigParser, если нет, то выводим сообщение и выходим из сценария.

В дальнейшем, следует еще добавить обработчик исключений вокруг вызова ConfigParser.read(), так как файл может существовать, но быть поврежденным, или может не быть разрешения на его открытие, что вызовет исключение.


Отправка письма нескольким адресатам одновременно.
Для отправки письма нескольким адресатам одновременно необходимо вместо одного email-адреса, записанного в качестве строки, предоставить список адресов электронной почты. Чтобы это работало, нужно создать строку, разделенную запятыми, в части f"To: {', '.join(to_addr)}", при создании переменной body, а также передать список адресов электронной почты методу smtp.sendmail().

import os
import smtplib
from configparser import ConfigParser

def send_email(to_addr, subject, text, encode='utf-8'):
    """
    Отправка электронного письма (email)
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    # проверка наличия файла `email.ini`
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Конфигурация не найдена!")

    # извлечение переменных из конфигурации
    server = cfg.get("smtp", "server")
    port = cfg.get("smtp", "port")
    from_addr = cfg.get("smtp", "email")
    passwd = cfg.get("smtp", "passwd")
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {', '.join(to_addr)}", 
           f"Subject: {subject}", mime, charset, "", text))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_addr, passwd)
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

if __name__ == "__main__":
    to_addr = ["person-one@mail.ru", "person-two@mail.ru"]
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    send_email(to_addr, subject, text)

Использование строк TO, CC и BCC при отправке email.
В этом коде передадим три списка, в каждом из которых по одному адресу электронной почты. Создадим поля CC и BCC точно так же, как и раньше, а также необходимо объединить три списка адресов в один, чтобы передать его методу smtp.sendmail().

import os
import smtplib
from configparser import ConfigParser

def send_email(to_eml, subject, text, cc_eml, bcc_eml, encode='utf-8'):
    """
    Отправка электронного письма (email)
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    # проверка наличия файла `email.ini`
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Конфигурация не найдена!")

    # извлечение переменных из конфигурации
    server = cfg.get("smtp", "server")
    port = cfg.get("smtp", "port")
    from_addr = cfg.get("smtp", "email")
    passwd = cfg.get("smtp", "passwd")
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {', '.join(to_eml)}", 
           f"CC: {', '.join(cc_eml)}", f"BCC: {', '.join(bcc_eml)}"
           f"Subject: {subject}", mime, charset, "", text))
    all_emails = to_eml + cc_eml + bcc_eml

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_addr, passwd)
        smtp.sendmail(from_addr, all_emails, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

if __name__ == "__main__":
    to_addr = ["person@mail.ru"]
    cc_addr = ["person-one@mail.ru"] 
    bcc_addr = ["person-two@mail.ru"]
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    send_email(to_addr, subject, text, cc_addr, bcc_addr)

Добавление вложения/файла с помощью модуля email.
Модуль email делает добавление вложений чрезвычайно простым.

В этом примере, в функцию отправки электронной почты добавим новый аргумент file_to_attach, а также создадим и добавим заголовок Content-Disposition и объект MIMEMultipart. Заголовок можно создать и добавить в любое время, но, до добавления вложения.

Письмо формируется в объекте MIMEMultipart() путем добавления необходимых полей, как ключей словаря. Если необходимо указать дату формирования письма, нужно использовать функцию formatdate модуля email, чтобы вставить правильно отформатированную дату.

Чтобы добавить тело сообщения, как вложение, нужно создать экземпляр MIMEText(text). Далее добавляется вложение, как результат чтения файла вложения в режиме 'rb' (байтовый объект) MIMEBase(data). Обратите внимание, что для отправки сообщения, необходимо преобразовать словарный объект msg в строку методом msg.as_string().

import os
import smtplib
from configparser import ConfigParser

from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

def send_email(to_addr, subject, text, file_to_attach,  
                cc_addr, bcc_addr):
    """
    Отправка электронного письма с вложением
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    # проверка наличия файла `email.ini`
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Конфигурация не найдена!")

    # извлечение переменных из конфигурации
    server = cfg.get("smtp", "server")
    port = cfg.get("smtp", "port")
    from_addr = cfg.get("smtp", "email")
    passwd = cfg.get("smtp", "passwd")
    # формируем тело письма
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if text:
        # текст письма отправляем как вложение
        msg.attach(MIMEText(text))
    msg["To"] = ', '.join(to_emails)
    msg["cc"] = ', '.join(cc_emails)
    emails = to_emails + cc_emails

    attachment = MIMEBase('application', "octet-stream")
    header = 'Content-Disposition', f'attachment; filename="{file_to_attach}"'
    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        print(f"Ошибка при открытии файла вложения {file_to_attach}")

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(from_addr, passwd)
        smtp.sendmail(from_addr, emails, msg.as_string())
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

if __name__ == "__main__":
    to_addr = ["person@mail.ru"]
    cc_addr = ["person-one@mail.ru"] 
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    file_attach = '/path/to/file_attach'
    send_email(to_addr, subject, text, file_attach, cc_addr)

Заключение.
Теперь вы знаете, как отправлять электронные письма с помощью Python. Для тех, кто любит мини-проекты,
нужно вернуться и добавить более подробную обработку ошибок в часть кода smtp.sendmail() на случай,
если во время процесса произойдет что-то странное. Одним из примеров может быть добавление исключений SMTPAuthenticationError или SMTPConnectError и т. д.

Можно усилить обработку ошибок во время прикрепления файла, чтобы отловить другие ошибки.
Наконец, можно взять различные списки адресов электронной почты и создать один нормализованный список,
в котором будут удалены дубликаты. Это особенно важно, если читать список адресов из файла.
