from django.http import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import DeviceLoginRequest


class InitiateDeviceLoginView(APIView):
    """
    Step 1: Launcher asks for a code
    """
    def post(self, request: HttpRequest) -> Response:
        login_request = DeviceLoginRequest.objects.create()
        return Response({
            "device_code": str(login_request.device_code),
            "verification_url": f"http://localhost:8000/auth/device/{login_request.device_code}/"
        })
    

class PollDeviceLoginView(APIView):
    """
    Step 3: Launcher polls this endpoint to check if user approved
    """
    def post(self, request: HttpRequest) -> Response:
        device_code: str = request.data.get("device_code")

        try:
            req = DeviceLoginRequest.objects.get(device_code=device_code)

            if req.is_expired():
                return Response({"status": "expired"}, status=status.HTTP_400_BAD_REQUEST)
            
            if req.is_approved and req.user:
                # Generate or get the Auth Token for the user
                token, _ = Token.objects.get_or_create(user=req.user)

                # Prepare the absolute URL for the avatar
                avatar_full_url = None
                if hasattr(req.user, 'avatar') and req.user.avatar:
                    # request.build_absolute_uri prepends the domain (e.g., http://localhost:8000)
                    avatar_full_url = request.build_absolute_uri(req.user.avatar.url)

                # Delete the request for security (one-time use)
                req.delete()

                return Response({
                    "status": "approved",
                    "token": token.key,
                    "username": req.user.username,
                    "avatar_url": avatar_full_url
                })
            
            return Response({"status": "pending"})
        except DeviceLoginRequest.DoesNotExist:
            return Response({"status": "invalid"}, status=status.HTTP_404_NOT_FOUND)
