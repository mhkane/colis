import paypalrestsdk
from account.actions import request as trequests
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from airspress.settings import PAYPAL_MODE, PAYPAL_ID, PAYPAL_SECRET
from django.shortcuts import render

def paypal_create(request, rqkey):
    """
    Payment > Paypal > Create a Payment
    """
    paypalrestsdk.configure({
        "mode": PAYPAL_MODE,
        "client_id": PAYPAL_ID,
        "client_secret": PAYPAL_SECRET })

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal" },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('payment:paypal_execute', args=(rqkey,))),
            "cancel_url": request.build_absolute_uri(reverse('account:deals',args=(rqkey,))) },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "deal",
                    "price": "25",
                    "currency": "USD",
                    "quantity": 1 }]},
            "amount":  {
                "total": "25",
                "currency": "USD" },
            "description": "Transaction traveler-requester" }]})

    redirect_url = ""

    if payment.create():
        # Store payment id in user session
        request.session['payment_id'] = payment.id

        # Redirect the user to given approval url
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = link.href
        return HttpResponseRedirect(redirect_url)

    else:
        messages.error(request, 'We are sorry but something went wrong. We could not redirect you to Paypal.')
        return HttpResponseRedirect(reverse('account:deals',args=(rqkey,)))
def paypal_execute(request, rqkey):
    """
    MyApp > Paypal > Execute a Payment
    """
    payment_id = request.session['payment_id']
    payer_id = request.GET['PayerID']

    paypalrestsdk.configure({
        "mode": PAYPAL_MODE,
        "client_id": PAYPAL_ID,
        "client_secret": PAYPAL_SECRET })

    payment = paypalrestsdk.Payment.find(payment_id)
    payment_name = payment.transactions[0].item_list.items[0].name

    if payment.execute({"payer_id": payer_id}):
        return HttpResponseRedirect(reverse('payment:paysuccess', args=(rqkey,)))
    else:
        # the payment is not valid
        return HttpResponseRedirect(reverse('payment:payinvalid', args=(rqkey,)))

    return HttpResponseRedirect(reverse('trips:index'))

def payment_success(request, rqkey):
    alert={'text':'The payment was successfully done. Funds will be held until you confirm delivery of your articles',
            'type':'success'}
    anyRequest = trequests.Query.get(objectId=rqkey)
    anyRequest.paymentStatus = True
    anyRequest.deliveryStatus = False
    anyRequest.save()
    return render(request, 'trips/modals.html', {'alert':alert})

def payment_invalid(request, rqkey):
    alert={'text':'The payment is invalid. Your account has not been debited. Check your funds and try again later',
            'type':'error'}
    anyRequest = trequests.Query.get(objectId=rqkey)
    anyRequest.paymentStatus = False
    anyRequest.deliveryStatus = False
    anyRequest.save()
    return render(request, 'trips/modals.html', {'alert':alert})