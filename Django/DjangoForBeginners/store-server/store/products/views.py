from django.shortcuts import render

def index(request):
    # В данном случае возвращается результат функции render - она рендерит определённую страницу
    # В фукнцию render обязательно передаётся первый параметр - request и второй параметр - template name или путь к шаблону,
    # который нужно отрендерить / отобразить
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'store',
        'header': 'Welcome to our store!',
        'username': 'John Doe',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                    'price': 6990.00,
                    'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'name': 'Синяя куртка The North Face',
                    'price': 23725.00,
                    'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': 3390.00,
                    'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            }
        ],
        'products_of_promotion': [
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': 1500.00,
                    'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            }
        ]
    }
    return render(request, 'products/test-context.html', context)