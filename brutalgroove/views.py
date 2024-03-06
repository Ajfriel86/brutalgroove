from django.shortcuts import render
from django.http import HttpResponseServerError


# def handler404(request, exception):
#     """ Error Handler 404 - Page Not Found """
#     return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    try:
        1/0
        return render(request, "errors/500.html", status=500)
    except Exception:
        raise HttpResponseServerError("Internal Server Error")
