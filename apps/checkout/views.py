from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.orders.models import Order, OrderItem
from apps.orders.forms import OrderCreateForm
from apps.cart.cart import Cart

@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart:detail')
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = cart.get_total_price()
            order.save()
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    book=item['book'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            # Clear the cart
            cart.clear()
            return redirect('checkout:success', order_id=order.id)
    else:
        # Pre-fill form with user data
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        form = OrderCreateForm(initial=initial_data)
    
    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'form': form
    })

@login_required
def confirm_order(request):
    return render(request, 'checkout/confirm.html')

@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'checkout/success.html', {'order': order})
