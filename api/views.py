from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status 
from datetime import datetime, timezone

class UserView(APIView):
    def get(self, request):
       
        current_datetime = datetime.now(timezone.utc).isoformat()
        return Response({
            "email": "anuoluwapoali25@gmail.com",
            "current_datetime": current_datetime, 
            "github_url": "https://github.com/Anuoluwapo25/HNG-Stage0"  
        }, status=status.HTTP_200_OK)
        