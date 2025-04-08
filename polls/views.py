from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user_list(request):
    users = User.objects.all()
    user_list_str = ", ".join([user.username for user in users])
    return HttpResponse(f"List of users: {user_list_str}")
