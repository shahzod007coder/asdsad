from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# from django.utils.translation import gettext_lazy as _


class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        request.title = ("Ro'yxatdan utish")

    def get(self, request):
        return render(request, "layouts/form.html", {
            "form": RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            messages.success(request, ("Ro'xatdan utdingiz"))
            return redirect("client:login")

        return render(request, "layouts/form.html", {
            "form": form
        })


class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Tizimga kirish")

    def get(self, request):
        return render(request, "layouts/form.html", {
            "form": LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if not user is None:
                login(request, user)
                messages.success(request, ("Xush kelibsiz, {}!".format(user.username)))

                return redirect("index")
            form.add_error("password", ("Login yoki parol noto'g'ri"))

            return render(request, "layouts/form.html", {
                "form": form
            })


@login_required
def client_logout(request):
    messages.success(request, "Bupti sog'bul!", format(request.user.username))
    logout(request)

    return redirect("index")
