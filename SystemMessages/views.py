from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User

# Create your views here.
@login_required
def inbox(request):
    return render(request, 'SystemMessages/messages.html')


@login_required
def send_message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_username']
            content = form.cleaned_data['content']
            user_receiver = User.objects.filter(username=username).first()
            message = Message(user_sender=request.user, user_receiver=user_receiver, content=content)
            message.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('SendMessage')

    context = {
        'form': form
    }
    return render(request, 'SystemMessages/send_message.html', context=context)


@login_required
def see_message(request):
    sent_messages = Message.objects.filter(user_sender=request.user).order_by('-date_posted')
    received_messages = Message.objects.filter(user_receiver=request.user).order_by('-date_posted')

    context = {
        'sent_messages': sent_messages,
        'received_messages': received_messages
    }
    return render(request, 'SystemMessages/see_message.html', context=context)

