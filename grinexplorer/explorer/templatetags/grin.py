from decimal import Decimal
from django import template

register = template.Library()


def format_float(f):
    s = "{:,f}".format(f)
    if "." not in s:
        return s

    return s.rstrip("0").rstrip(".")


@register.filter
def nanogrin(nanogrin):
    if nanogrin == 0:
        return grin(0)

    if nanogrin < 1000:
        return "%d nvcash" % nanogrin

    return microgrin(Decimal(nanogrin) / Decimal(1000))


@register.filter
def microgrin(microgrin):
    if microgrin == 0:
        return grin(0)

    if microgrin < 1000:
        return "%s µvcash" % format_float(microgrin)

    return milligrin(Decimal(microgrin) / Decimal(1000))


@register.filter
def milligrin(milligrin):
    if milligrin == 0:
        return grin(0)

    if milligrin < 1000:
        return "%s mvcash" % format_float(milligrin)

    return grin(Decimal(milligrin) / Decimal(1000))


@register.filter
def grin(grin):
    return "%s vcash" % format_float(grin)
