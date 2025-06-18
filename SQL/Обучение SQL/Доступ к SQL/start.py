##import mysql.connector
from mysql.connector import connect, Error
print('Импортирований модулей успешно.')

try:
    with connect(
        host = '31.131.18.34',
        user = 'roditeli',
        password = 'q~podhMD.(f,',
    ) as connection:
        print(connection)
except Error as e:
    print(e)
