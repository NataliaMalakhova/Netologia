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
}


def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name, {})
    if not recipe:
        return HttpResponse('Recipe not found', status=404)

    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
    except ValueError:
        return HttpResponse('Invalid servings parameter', status=400)

    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    response_lines = [f"{ingredient}: {amount}" for ingredient, amount in scaled_recipe.items()]
    response_text = "\n".join(response_lines)

    return HttpResponse(response_text, content_type='text/plain; charset=utf-8')
