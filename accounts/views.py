from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import View


from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Profile, FriendRequest
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(View):
    template_name = 'accounts/home.html'
    def get(self, request):
        return render(request, self.template_name)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
