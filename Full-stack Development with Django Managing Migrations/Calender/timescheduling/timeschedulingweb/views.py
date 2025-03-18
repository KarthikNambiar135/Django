from django.shortcuts import render
from django.utils import timezone
from .models import TimeSlot
# Create your views here.
def index(request):
    upcoming_appointments = TimeSlot.objects.filter(
        start_time__gte = timezone.now()).order_by('start_time')
    
    context = {
        'upcoming_appointments': upcoming_appointments.first(),
        'description': upcoming_appointments.first().description,
        'list_upcoming': len(upcoming_appointments),
    }

    return render(request, 'home.html', context)