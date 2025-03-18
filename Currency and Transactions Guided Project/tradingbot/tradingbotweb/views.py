from django.shortcuts import render
from .models import CurrencyBalance, ExchangeGoal
# Create your views here.
def index(request):
    last_balance = CurrencyBalance.objects.order_by('-created_at').first()
    exchange_goal = last_balance.exchange_goal.first()
     # Debugging print statements
    print("Last Balance Object:", last_balance)
    print("Attributes:", dir(last_balance))  # Show all available attributes
    context = {
        'last_balance': last_balance,
        'exchange_goal': exchange_goal,
    }
    return render(request, 'home.html', context)