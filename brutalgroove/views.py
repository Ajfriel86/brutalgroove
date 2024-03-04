from django.shortcuts import render


def handler404(request, error_message=None):
    """
    View to handle custom error
    """
    context = {
        'error_message': error_message or "An unexpected error occurred."
    }

    return render(request, '404.html', context)
