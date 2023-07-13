from .cart import Cart


def cart(request):
    """ Контекст процессор корзины. """
    return {'cart': Cart(request)}
