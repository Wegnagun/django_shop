from django import forms


class CouponApplyForm(forms.Form):
    """ Форма активации купона. """
    code = forms.CharField()
