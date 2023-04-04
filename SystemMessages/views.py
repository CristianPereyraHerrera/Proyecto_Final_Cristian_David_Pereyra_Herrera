from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User


# Create your views here.
@login_required
def send_message(request, user_username=None):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            username = request.POST.get('user_username')
            content = form.cleaned_data['content']
            user_receiver = User.objects.filter(username=username).first()
            message = Message(user_sender=request.user, content=content)
            if user_receiver:
                message.user_receiver = user_receiver
                message.save()
                messages.success(request, 'Message sent successfully.')
                return redirect('SendMessage')
    else:
        form = MessageForm()

    context = {
        'form': form,
        'user_username': user_username
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


@login_required
def delete_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id, user_sender=request.user)
    except Message.DoesNotExist:
        messages.error(request, 'The message you are trying to delete does not exist or you do not have permission to delete it.')
        return redirect('SendMessage')

    message.delete()
    messages.success(request, 'The message was successfully deleted.')
    return redirect('SeeMessage')
