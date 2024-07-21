from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated, TokenHasReadWriteScope])
def protected_view(request):
    return JsonResponse({'message': 'Hello, Welcome to OAuth2 concept!'})
