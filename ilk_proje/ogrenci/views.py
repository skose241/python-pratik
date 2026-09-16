from django.http import HttpResponse
from .models import Ogrenci

def merhaba(request):
    return HttpResponse("Merhaba Django")


from django.shortcuts import render
def liste(request):
    ogrenciler=Ogrenci.objects.all()
    sonuc=""

    return render(request,"liste.html",{"ogrenciler":ogrenciler})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OgrenciSerializer

@api_view(["GET","POST"])
def api_liste(request):
    if request.method=="GET":
        ogrenciler=Ogrenci.objects.all()
        serializer=OgrenciSerializer(ogrenciler,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=OgrenciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET","PUT","DELETE"])
def api_detay(request,id):
    try:
        ogrenci=Ogrenci.objects.get(id=id)
    except Ogrenci.DoesNotExists:
        return Response({"hata":"Öğrenci bulunamadı"},status=404)

    if request.method=="GET":
        serializer=OgrenciSerializer(ogrenci)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=OgrenciSerializer(ogrenci,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=="DELETE":
        ogrenci.delete()
        return Response({"mesaj":"Öğrenci silindi"})