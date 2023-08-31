from django import forms


class CouponForm(forms.Form):
    """ Форма активации купона. """
    code = forms.CharField
