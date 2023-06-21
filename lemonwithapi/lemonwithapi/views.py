from django.http import HttpResponse


def handler404(request, exception):
    return HttpResponse('<center><h1 style="color:blue;">Oh Boy &#128516</h1><h2 style="color:red;">404 Page Not Found!<h2></center>')
