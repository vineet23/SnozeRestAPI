from rest_framework.views import APIView
from rest_framework.response import Response
from Songs.models import Song
from Songs.api.serializers import Song_Serializer



class Song_API_View(APIView):

    def get(self, request):
        Songs = Song.objects.all()
        serializer = Song_Serializer(Songs, many=True)
        return Response(serializer.data)

    def post(self):
        pass