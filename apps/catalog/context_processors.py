
from apps.catalog.models import Category


def nav_items_processors(request):
    categories = Category.objects.all()
    return {
        'nav_items': categories
    }
