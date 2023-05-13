from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from .models import Coupon
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from string import ascii_letters, digits


# Create your views here.
#def leader(request):
  # return  render(request,'reward/leader.html')

def leaderboard(request):
    users = User.objects.order_by('-points')[:10]
    data = [{'rank': i+1, 'username': user.username, 'points': user.points} for i, user in enumerate(users)]
    return JsonResponse({'data': data})

#def redeem(request):
  # return  render(request,'reward/redeemRewards.html')

def redeem(request):
 coupons = Coupon.objects.filter(expiration_date__gte=timezone.now())
 return render(request, 'redeemRewards.html', {'coupons': coupons})

def redeem_coupon(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    if request.method == 'POST':
        if request.user.points >= coupon.points_needed:
            # generate random coupon code
            code = ''.join(random.choices(ascii_letters + digits, k=10))
            # decrement user's points
            request.user.points -= coupon.points_needed
            request.user.save()
            #TODO: save the coupon code and user information to a redemption model
            messages.success(request, f'Congratulations! Your coupon code is {code}.')
            return redirect('coupon_list')
        else:
            messages.error(request, f'Sorry, you need {coupon.points_needed - request.user.points} more points to redeem this coupon.')
            return redirect('coupon_list')



