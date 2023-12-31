from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request, product_id):
    """ Представление добавления товара в корзину. """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart.add(
            product=product,
            quantity=data['quantity'],
            override_quantity=data['override']
        )
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """ Представление удаления товара из корзины. """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """ Представление отображения корзины. """
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    coupon_apply_form = CouponApplyForm()
    context = {'cart': cart, 'coupon_apply_form': coupon_apply_form}
    return render(request, 'cart/detail.html', context)
