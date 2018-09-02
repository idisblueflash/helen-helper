from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Command
from .serializers import AlfredSerializer


@csrf_exempt
def alfred_list(request):

    if request.method == 'GET':
        commands = Command.objects.all()
        serializer = AlfredSerializer()
        return JsonResponse(serializer.serialize(commands), safe=False)
