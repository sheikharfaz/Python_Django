from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required(login_url='/login/')
def guest_list(request):
    guest = GuestReservation.objects.all()
    return render(request, 'api/guest_list.html', {'guest': guest})


@login_required(login_url='/login/')
def guest_create(request):
    current_user = request.user.username
    if request.method == 'POST':
        form = GuestForm(request.POST or None, {'customer_name': current_user.capitalize()})
    else:
        form = GuestForm({'customer_name': current_user.capitalize()})
    # print(form.errors.as_data())
    if form.is_valid():
        form.save()
        return redirect('api:guest_list')
    return render(request, 'api/guest_form.html', {'form': form})


@login_required(login_url='/login/')
def guest_edit(request, pk):
    guest = get_object_or_404(GuestReservation, pk=pk)
    form = GuestForm(request.POST or None, instance=guest)
    if form.is_valid():
        form.save()
        return redirect('api:guest_list')
    return render(request, 'api/guest_form.html', {'form': form})


@login_required(login_url='/login/')
def guest_delete(request, pk):
    guest = get_object_or_404(GuestReservation, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('api:guest_list')
    return render(request, 'api/guest_form.html', {'form': guest})


@login_required(login_url='/login/')
def hotel_header(request):
    query = request.GET['query']
    query1 = request.GET['slider']

    if len(query) > 78:
        hotels = []
    else:
        hotelsplace = HotelModel.objects.filter(hotelPlace__icontains=query)
        modelquery = HotelModel.objects.filter(hotelPlace__lte=query1)
        hotels = hotelsplace.union(modelquery)

    if hotels.count == 0:
        messages.error(request, 'No search result found. Please refine your query!')
    context = {'context': hotels, 'query': query}
    print(context)
    return render(request, 'api/hotel_list.html', context)

