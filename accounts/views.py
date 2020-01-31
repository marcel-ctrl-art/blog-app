from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import View


class SignUpView(View):
    def get(self, request):
        template_name = 'signup.html'
        form = UserCreationForm
        return render(request, template_name, {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/accounts/login/')
