from django.http.response import JsonResponse
from django.http import Http404
from core.models import Product
from core.models import Category


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        products = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(products.to_json())
def products_of_category(requst, category_id):
    products = Product.objects.filter(category=category_id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_details(request, category_id):
    try:
        categories = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(categories.to_json())