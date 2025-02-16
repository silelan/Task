from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import View


from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Profile, FriendRequest
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

User = get_user_model()

class HomeView(View):
    template_name = 'accounts/home.html'
    def get(self, request):
        people = Profile.objects.all()
        context = {
            'people':people
        }
        return render(request, self.template_name,context)

class ProfileView(View):
    model = Profile
    template_name = 'accounts/profile.html'
    def get(self, request, slug):
        profile = get_object_or_404(Profile, slug=slug)
        context = {
            'profile':profile
        }
        return render(request, self.template_name, context)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
