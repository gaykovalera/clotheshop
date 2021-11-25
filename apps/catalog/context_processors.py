
from apps.catalog.models import MainCategory


def nav_items_processors(request):
    main_categories = MainCategory.objects.all()
    return {
        'nav_items': main_categories
    }
