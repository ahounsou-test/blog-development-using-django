from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models.user_model import User
from django.shortcuts import render, redirect

from .forms.profile_update import ProfileUpdateFrom
from .forms.user_register import UserRegisterForm
from .forms.user_update import UserUpdateForm
from .models import profile


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # pdb.set_trace()
            form.save()
            profile(user=User.objects.get(username=request.POST['username']),
                    bio=f" I {request.POST['username']}").save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log in with your credential')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
