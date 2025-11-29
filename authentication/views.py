import uuid
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import DeviceLoginRequest


class ApproveDeviceLoginView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login_view")
    redirect_field_name = "next"

    def get(self, request: HttpRequest, device_code: uuid.UUID) -> HttpResponse:
        req = get_object_or_404(DeviceLoginRequest, device_code=device_code)

        if req.is_expired():
            return render(request, "authentication/device_expired.html")
        
        return render(request, "authentication/device_approve.html", {
            "device_code": device_code
        })
    
    def post(self, request: HttpRequest, device_code: uuid.UUID) -> HttpResponse:
        req = get_object_or_404(DeviceLoginRequest, device_code=device_code)

        if req.is_expired():
            return render(request, "authentication/device_expired.html")
        
        # User clicked "Approve"
        req.user = request.user
        req.is_approved = True
        req.save()
        
        return render(request, "authentication/device_success.html")
    