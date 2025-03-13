from django.http import HttpResponseNotFound
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from .models import URL
from rest_framework.decorators import api_view
from django.http import JsonResponse
import uuid
from .serializers import URLSerializer
from rest_framework.response import Response


def redirect_original_url(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        url.visits += 1
        url.save()
        return redirect(url.url)
    except URL.DoesNotExist:
        return HttpResponseNotFound("URL not Found")



@api_view(['GET'])
def get_url_by_hash(request, hash):
    url = URL.objects.get(hash=hash)
    serializer = URLSerializer(url)
    return Response(serializer.data)

@api_view(['GET'])
def get_url_stats(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        serializer = URLSerializer(url)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response({'error': 'Short URL not found'}, status=404)

@api_view(['GET'])
def get_all_urls(request):
    urls = URL.objects.all()
    serializer = URLSerializer(urls, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def create_short_url(request):
    if 'url' in request.data:
        original_url = request.data['url']

        # Check if URL already exists
        existing_url = URL.objects.filter(url=original_url).first()
        if existing_url:
            return JsonResponse({'short_url:' : f'/url/{existing_url.hash}/', 'message': 'URL already exists'}, status=200)

        hash_value = uuid.uuid4().hex[:8]
        while URL.objects.filter(hash=hash_value).exists():
            hash_value = uuid.uuid4().hex[:8]

        url = URL.objects.create(hash=hash_value, url=original_url)
        return JsonResponse({'short_url:' : f'/url/{hash_value}/'}, status=201)
    
    return JsonResponse({'error': 'Invalid request data'}, status=400)



@api_view(['PUT'])
def update_visit_count(request, hash):
    url = URL.objects.get(hash=hash)
    url.visits += 1
    url.save()
    return Response({'message': 'Visit count updated'}, status=200)





def simple_ui(request):
    urls = URL.objects.all()
    return render(request, "index.html", {"urls": urls})
