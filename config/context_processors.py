from .constants import PRODUCT_NAME

def constants(request):
    return {
        'PRODUCT_NAME': PRODUCT_NAME
    }
