from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status,viewsets
from rest_framework.authentication import TokenAuthentication
from . import permissions
from profiles_api import models
from .serializers import HelloSerializer,UserProfileSerializer

class HelloAPI(APIView):
    """Test API view"""

    serializer_class = HelloSerializer

    def get(self,request,format= None):
        """Return  a list of APIView features"""
        api_views = [
            'Uses HTTP as function(get,post,delete,path)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'msg':'Hey Django API','apiViews':api_views})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hi {name}'

            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        return Response({'method':'put'})
    def patch(self,request,pk=None):
        return Response({'method':'patch'})
    def delete(self,request,pk=None):
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """

    serializer_class = HelloSerializer
    def list(self,req):
        """retur hello message"""

        list_viewsets = [
            'Uses actions (list,create,delete,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'msg':'Hello ViewSet','viewSets':list_viewsets})
    
    def create(self,req):
        """create a new name"""
        serializer = self.serializer_class(data=req.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hi {name}'
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,req,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,req,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,req,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PUTCH'})

    def destroy(self,req,pk=None):
        """Handle removing object"""
        return Response({"http_method":'DELETE'})
        
class UserProfileviewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
        

