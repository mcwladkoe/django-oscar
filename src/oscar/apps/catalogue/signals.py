import django.dispatch

product_viewed = django.dispatch.Signal(
    providing_args=["product", "user", "request", "response"])

category_viewed = django.dispatch.Signal(
    providing_args=["category", "context", "user", "request", "response"])
