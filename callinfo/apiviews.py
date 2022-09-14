from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import GlobalUsersSerializer
from .models import GlobalUsers


class GlobalUsersApi(viewsets.ViewSet):
    def list(self, request):
        if 'phoneno' in request.data:
            phoneno = request.data.get('phoneno', '')
            if phoneno is not '':
                exist = GlobalUsers.objects.filter(phoneno=phoneno)
                if exist:
                    serializer = GlobalUsersSerializer(exist, many=True)
                    return Response(serializer.data)
                return Response({'msg': "Sorry We Didn't Have An Update For This Number"})
            return Response({'msg': 'Invalid Phone No pls enter correct number'})
        return Response({'msg': 'phoneno is not provided in request body'})

    def create(self, request):
        if 'phoneno' in request.data:
            phoneno = request.data.get('phoneno', '')
            if phoneno is not '':
                serializer = GlobalUsersSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'msg': 'Invalid Phone No pls enter correct number'})
        return Response({'msg': 'phoneno is not provided in request body'})

    def retrieve(self, request, pk=None):
        if 'phoneno' in request.data:
            phoneno = request.data.get('phoneno', '')
            if phoneno is not '':
               try:
                   guser = GlobalUsers.objects.get(phoneno=phoneno)
                   serializer = GlobalUsersSerializer(guser)
                   return Response(serializer.data)
               except:
                   return Response({'msg': "Sorry We didn't have the no you are searching for or too many nos are there! Pls try without giving pk or id"})
            return Response({'msg': 'Invalid Phone No pls enter correct number'})
        return Response({'msg': 'phoneno is not provided in request body'})
