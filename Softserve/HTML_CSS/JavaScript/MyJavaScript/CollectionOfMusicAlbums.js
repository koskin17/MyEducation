/*
Колекція музичних альбомів
Ви створюєте функцію, яка допомагає підтримувати колекцію музичних альбомів. Колекція організована як об’єкт, який містить кілька альбомів, які також є об’єктами. Кожен альбом представлено в колекції унікальним id як назвою властивості. У кожному об’єкті альбому є різні властивості, що описують інформацію про альбом. Не всі альбоми мають повну інформацію.

Функція updateRecords приймає 4 аргументи, представлені такими параметрами функції:

records — об’єкт, що містить декілька окремих альбомів
id — число, що позначає певний альбом в об’єкті records
prop — рядок, що позначає назву властивості альбому, яку потрібно оновити
value — рядок, що містить інформацію, яка використовується для оновлення властивості альбому
Завершіть функцію, використовуючи правила нижче, щоб змінити об’єкт, переданий до функції.

Ваша функція завжди повинна повертати весь об’єкт records.
Якщо value є пустим рядком, видаліть дану властивість prop з альбому.
Якщо prop не є tracks та value не є пустим рядком, призначте value до prop альбому.
Якщо prop є tracks та value не є пустим рядком, але альбом не має властивості tracks, створіть порожній масив та додайте value до нього.
Якщо prop є tracks та value не є пустим рядком, додайте value в кінець наявного масиву tracks.
Примітка: копія об’єкту recordCollection використовується для тестів. Ви не повинні напряму змінювати об’єкт recordCollection.
*/

// Налаштування
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

// Змініть код лише під цим рядком
function updateRecords(records, id, prop, value) {
  if (value === "") {
    delete records[id][prop]; // Видалення властивості, якщо значення порожнє
  } else if (prop === "tracks") {
    // Якщо проп - "tracks" і немає такої властивості, створюємо масив
    if (!records[id].hasOwnProperty("tracks")) {
      records[id]["tracks"] = [];
    }
    records[id]["tracks"].push(value); // Додаємо значення в масив tracks
  } else {
    records[id][prop] = value; // Оновлення або створення властивості
  }
  
  return records; // Повертаємо оновлений об'єкт
}

// Приклади викликів
updateRecords(recordCollection, 5439, 'artist', 'ABBA');  // Додає 'artist': 'ABBA' для альбому 5439
updateRecords(recordCollection, 5439, 'tracks', 'Dancing Queen');  // Додає трек до альбому 5439
updateRecords(recordCollection, 2548, 'artist', '');  // Видаляє 'artist' з альбому 2548

/*
Пояснення:
Видалення властивості: якщо передане значення value — це порожній рядок, властивість видаляється за допомогою delete.
Додавання або оновлення властивості: якщо властивість не є "tracks", і значення не порожнє, вона оновлюється або створюється.
Оновлення треків: якщо властивість — це "tracks", перевіряється, чи існує ця властивість. Якщо її немає, створюється порожній масив, а потім додається новий трек у масив.
Ця функція дотримується правил і правильно оновлює об'єкт колекції.
*/