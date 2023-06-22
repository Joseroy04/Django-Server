from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm ,CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from allauth.account.views import SignupView
from .models import CustomUser
def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'accounts/login2.html', {'form': form})

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('signin')
    return render(request, 'accounts/signup3.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            custom_user = CustomUser.objects.get(user=user)
        except CustomUser.DoesNotExist:
            custom_user = None

        if custom_user is None or custom_user.phone_number is None or custom_user.email is None:
            if request.method == 'POST':
                form = CustomUserForm(request.POST, instance=custom_user)
                if form.is_valid():
                    custom_user = form.save(commit=False)
                    custom_user.user = request.user  # Assign the user instance to the user field
                    custom_user.save()
                    return redirect('home')  # Replace 'home' with the desired URL after form submission
            else:
                form = CustomUserForm(instance=custom_user)
            return render(request, 'accounts/fill_form.html', {'form': form})
        else:
            return render(request, 'accounts/home.html', {})  # Render the 'accounts/home.html' template without redirection
    return render(request, 'accounts/home.html', {})


def logout_view(request):
    logout(request)
    return redirect('home')


# class CustomSignupView(SignupView):
#     template_name = 'gitaftersignup.html'
#     form_class = CustomSignupForm

#     def get_success_url(self):
#         return reverse_lazy('additional_info')

#     def form_valid(self, form):
#         user = form.save(self.request)
#         user.name = form.cleaned_data['name']
#         user.phone_number = form.cleaned_data['phone_number']
#         user.save()
#         return redirect(self.get_success_url())

# def additional_info(request):
#     if request.method == 'POST':
#         # Handle the form submission and save the additional information
#         # # Assuming you have a model named 'UserProfile' to store the additional information
#         # user_profile = user.objects.create(
#         #     user=request.user,
#         #     name=request.POST.get('name'),
#         #     phone_number=request.POST.get('phone_number')
#         # )
#         # You can perform additional actions here, such as sending emails, etc.
#         messages.success(request, 'Additional information saved successfully.')
#         return redirect('home')  # Redirect to the home page after saving the additional information
#     return render(request, 'accounts/additional_info.html')
