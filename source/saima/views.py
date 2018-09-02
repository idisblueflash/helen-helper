from django.http import HttpResponse


def index(request):
    return HttpResponse("Hallo, world! You're in Saima Index page.")
