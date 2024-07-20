from django.http import JsonResponse
from oauth2_provider.decorators import protected_resource

@protected_resource()
def api_protected(request):
    return JsonResponse({'message': 'This is a protected resource'})