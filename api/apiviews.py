from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def list_hotels(request):
    if request.method == "GET":
        hotels = HotelModel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
    else:  # Post
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  #Invalid data


@api_view(['GET', 'DELETE', 'PUT'])
def hotel_details(request, id):
    try:
        hotels = HotelModel.objects.get(id=id)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = HotelSerializer(hotels)
        return Response(serializer.data)
    elif request.method == 'PUT':    #Update
        serializer = HotelSerializer(hotels, data=request.data)
        if serializer.is_valid():
            serializer.save()    # Update table in DB
            return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        hotels.delete()
        return Response(status=204)

