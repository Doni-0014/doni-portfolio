from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def to_percentage(value, max_value=10):
    """Convert a value to percentage based on max_value."""
    try:
        return (float(value) / float(max_value)) * 100
    except (ValueError, TypeError, ZeroDivisionError):
        return 0
