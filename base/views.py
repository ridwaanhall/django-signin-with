from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from .models import ChatMessage

def get_user_profile_data(user):
    """
    Get user's full name and profile image from Google
    """
    profile_data = {
        'full_name': user.get_full_name() or user.username,
        'profile_image': None
    }
    
    try:
        # Get Google social account data
        social_account = SocialAccount.objects.filter(user=user, provider='google').first()
        if social_account and social_account.extra_data:
            # Get full name from Google
            google_name = social_account.extra_data.get('name', '')
            if google_name:
                profile_data['full_name'] = google_name
            
            # Get profile image from Google
            profile_image = social_account.extra_data.get('picture', '')
            if profile_image:
                profile_data['profile_image'] = profile_image
                
    except Exception as e:
        # Fallback to Django user data
        pass
    
    return profile_data

# Create your views here.

def home(request):
    """
    Home page view - displays the live chat page
    """
    # Get all chat messages with user profile data
    chat_messages = ChatMessage.objects.select_related('user').all()[:50]  # Latest 50 messages
    
    # Add profile data to each message
    enriched_messages = []
    for message in chat_messages:
        profile_data = get_user_profile_data(message.user)
        message.user_full_name = profile_data['full_name']
        message.user_profile_image = profile_data['profile_image']
        enriched_messages.append(message)
    
    # Get current user profile data for navbar
    current_user_profile = None
    if request.user.is_authenticated:
        current_user_profile = get_user_profile_data(request.user)
    
    context = {
        'title': 'Live Chat',
        'chat_messages': enriched_messages,
        'current_user_profile': current_user_profile,
    }
    return render(request, 'base/home.html', context)

@login_required
def send_message(request):
    """
    Handle sending chat messages (AJAX)
    """
    if request.method == 'POST':
        message_text = request.POST.get('message', '').strip()
        if message_text:
            chat_message = ChatMessage.objects.create(
                user=request.user,
                message=message_text
            )
            
            # Get user profile data
            profile_data = get_user_profile_data(request.user)
            
            return JsonResponse({
                'success': True,
                'message': {
                    'user': profile_data['full_name'],
                    'message': chat_message.message,
                    'timestamp': chat_message.timestamp.strftime('%H:%M'),
                    'profile_image': profile_data['profile_image']
                }
            })
        else:
            return JsonResponse({'success': False, 'error': 'Message cannot be empty'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
