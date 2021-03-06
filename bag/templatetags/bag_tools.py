from django import template


register = template.Library()


# Taken from CI Ecommerce project
@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name="calc_priceperunit")
def calc_priceperunit(total, quantity):
    return total/quantity


@register.filter(name="calc_delivery_extra")
def calc_delivery_extra(total, delivery_threshold):
    return delivery_threshold - total
