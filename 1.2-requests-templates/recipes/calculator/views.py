from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def cook_help_view(request, the_dish):
    servings = int(request.GET.get('servings', 1))
    calc_ing = {}
    for dish, ing in DATA.items():
        if dish == the_dish:
            for product, amount in ing.items():
                calc_ing[product] = amount * servings
    context = {
        'recipe': calc_ing
    }
    return render(request, 'calculator/index.html', context)


def greet_view(request):
    return HttpResponse('Введите название блюда в адресную строку. Пример: /omlet/')


