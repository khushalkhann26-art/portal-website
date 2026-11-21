from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[:10]
    unread_count = notifications.filter(is_read=False).count()
    
    return JsonResponse({
        'notifications': [
            {
                'title': n.title,
                'message': n.message,
                'created_at': n.created_at.isoformat(),
                'is_read': n.is_read
            } for n in notifications
        ],
        'unread_count': unread_count
    })

@login_required
def mark_as_read(request):
    if request.method == 'POST':
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400) 