from django.contrib.auth.forms import PasswordResetForm, UserChangeForm

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView

from myproject.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, CustomUserChangeForm
from users.models import User
import secrets

from utils import generation_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет, необходимо подтвердить свою почту для дальнейшего использования аккаунта: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy('users:login'))


class CustomPasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            form.add_error(None, 'Пользователь не найден')
            return super().form_invalid(form)
        except User.MultipleObjectsReturned:
            form.add_error(None, 'что-то пошло не так')
            return super().form_invalid(form)

        new_password = generation_password()

        user.set_password(new_password)
        user.save()

        send_mail(
            subject = 'Восстановление пароля',
            message = f'Ваш новый пароль от сайта MyStore: {new_password}',
            from_email = EMAIL_HOST_USER,
            recipient_list = [email],
            fail_silently=False,
        )
        return redirect(self.success_url)

class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user



