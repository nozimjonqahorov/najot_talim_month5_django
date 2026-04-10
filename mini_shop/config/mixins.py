from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class MyLoginRequiredMixin(LoginRequiredMixin):
    """Login bo'lmagan userni yo'naltirishdan oldin xabar ko'rsatadi."""

    def handle_no_permission(self):
        messages.error(
            self.request,
            "Ushbu sahifaga kirish uchun avval tizimga kiring yoki ro'yxatdan o'ting (Log in / Sign up).",
        )
        return super().handle_no_permission()

