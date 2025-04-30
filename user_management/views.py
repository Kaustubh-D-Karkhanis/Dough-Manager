from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'user_management/signup.html', {'form':form})


class CustomLoginView(LoginView):
    template_name = 'user_management/login.html'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('dashboard')

