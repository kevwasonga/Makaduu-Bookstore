from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_cancel(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == Order.PENDING:
        order.status = Order.CANCELLED
        order.save()
        messages.success(request, 'Order cancelled successfully.')
    else:
        messages.error(request, 'This order cannot be cancelled.')
    return redirect('orders:order_detail', order_id=order.id)
