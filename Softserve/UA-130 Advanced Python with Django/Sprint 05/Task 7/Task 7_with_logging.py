import os
import logging

# Получаем путь к директории текущего файла (а не текущей рабочей директории!)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к лог-файлу
log_file_path = os.path.join(base_dir, "sum_slice_array.log")

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=log_file_path,
    filemode="w"
)

class MyExceptions(Exception):
    pass

def sum_slice_array(arr, first, second):
    logging.info(f"Function called with arr={arr}, first={first}, second={second}")
    
    if not (isinstance(first, int) and isinstance(second, int) and first >= 1 and second >= 1):
        logging.error("Indexes must be integers ≥ 1")
        raise MyExceptions("Indexes must be integers ≥ 1")
    
    if first > len(arr) or second > len(arr):
        logging.error("Indexes out of range")
        raise MyExceptions("Indexes out of range")

    elem1 = arr[first - 1]
    elem2 = arr[second - 1]
    if not (isinstance(elem1, (int, float)) and isinstance(elem2, (int, float))):
        logging.error(f"Elements at positions {first} or {second} are not numbers")
        raise MyExceptions("Elements must be numbers")

    result = float(elem1 + elem2)
    logging.info(f"Sum calculated successfully: {result}")
    return result

# Пример использования:
try:
    print(sum_slice_array([1, 2, 3], 1, 2))
except MyExceptions:
    print("MyExceptions")
