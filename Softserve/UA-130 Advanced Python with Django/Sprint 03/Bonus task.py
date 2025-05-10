# Goal Learn to create functions with internal state (through locking) and work with a limit on the size of stored data.
# Task Implement the function limited_cache(limit), which returns the function cache(key, value=None):
# If value is given — caches key:value. If value is not given — returns the value by key or None, if there is none. If the number of stored keys exceeds limit, the oldest key is removed (according to the FIFO principle).
# Example
# cache = limited_cache(2) cache('a', 1) cache('b', 2) print(cache('a'))  # -> 1 cache('c', 3) print(cache('b'))  # -> None (removed)

# **Цель:**  
# Освоить создание функций с внутренним состоянием (через блокировку) и работу с ограничением размера хранимых данных.  

# **Задача:**  
# Реализовать функцию `limited_cache(limit)`, которая возвращает внутреннюю функцию `cache(key, value=None)`.  

# - Если передан `value`, то `cache` сохраняет в памяти `key: value`.  
# - Если `value` не передан, функция возвращает сохранённое значение по `key` или `None`, если такого ключа нет.  
# - Если число сохранённых ключей превышает `limit`, удаляется **самый старый ключ** (по принципу FIFO — первый пришёл, первый ушёл).  

# ### **Пример использования:**  

# cache = limited_cache(2)
# cache('a', 1)
# cache('b', 2)
# print(cache('a'))  # -> 1
# cache('c', 3)
# print(cache('b'))  # -> None (удалено)
# ```
# Задача предполагает повышенную сложность, значит, в ней есть нестандартное требование, например, порядок удаления данных.

# Хитрость в задаче заключается в том, что необходимо хранить ключи в порядке их добавления, чтобы корректно удалять **самый старый ключ** при превышении лимита. Для этого идеально подходит `OrderedDict` из `collections`, который сохраняет порядок элементов.

# Ниже представлено решение:

from collections import OrderedDict

def limited_cache(limit):
    cache_store = OrderedDict()

    def cache(key, value=None):
        if value is not None:
            # Если ключ уже есть, удаляем его, чтобы обновить порядок
            if key in cache_store:
                cache_store.pop(key)
            
            # Добавляем новый элемент в конец (самый новый)
            cache_store[key] = value
            
            # Если размер кэша превышает лимит, удаляем самый старый элемент (FIFO)
            if len(cache_store) > limit:
                cache_store.popitem(last=False)  # Удаляет первый (старейший) элемент
        else:
            # Возвращаем значение по ключу или None, если нет
            return cache_store.get(key, None)

    return cache
```

### 🔎 **Как работает код?**
# 1. **Создаём `OrderedDict`** (`cache_store`)  
#    - Он сохраняет **порядок добавления** ключей, что позволяет удалять самый старый элемент, если лимит превышен.

# 2. **Функция `cache(key, value=None)`:**
#    - Если передан `value` → сохраняем `key:value`, но **перед этим удаляем старый ключ**, если он уже был в `cache_store`, чтобы обновить его позицию.
#    - Если размер хранилища превышает `limit`, удаляем **самый старый** элемент (`popitem(last=False)`).
#    - Если `value` не передан → просто возвращаем значение по ключу (`get(key, None)`).

### ✅ **Пример использования**
# cache = limited_cache(2)
# cache('a', 1)
# cache('b', 2)
# print(cache('a'))  # 1
# cache('c', 3)
# print(cache('b'))  # None (удалено по FIFO)
# ```
# **Вывод:**  
# ```
# 1
# None
# ```

### 🚀 **Почему `OrderedDict` удобен?**
# - **Автоматически сохраняет порядок вставки элементов.**
# - **Мгновенно удаляет самый старый элемент (`popitem(last=False)`).**
# - **Эффективен по скорости (O(1) для вставки и удаления).**

# Эта реализация полностью соответствует задаче, включая FIFO-удаление. Если есть вопросы — спрашивай! 😉