# notifications/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DetailRequest
from django.contrib.auth.models import User

@login_required
def send_request(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    if request.method == 'POST':
        DetailRequest.objects.create(sender=request.user, recipient=recipient)
        messages.success(request, 'Request sent successfully!')
        return redirect('profile')
    return render(request, 'notifications/send_request.html', {'recipient': recipient})

@login_required
def respond_request(request, request_id, response):
    detail_request = get_object_or_404(DetailRequest, id=request_id)
    if detail_request.recipient != request.user:
        messages.error(request, 'You are not authorized to respond to this request.')
        return redirect('profile')

    if response == 'accept':
        detail_request.accepted = True
        detail_request.rejected = False
        messages.success(request, 'Request accepted!')
    elif response == 'reject':
        detail_request.accepted = False
        detail_request.rejected = True
        messages.success(request, 'Request rejected!')

    detail_request.save()
    return redirect('profile')
