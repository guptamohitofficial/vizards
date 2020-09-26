"""bizards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import bizards.views as bv
import users.views as uv
import cards.views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bv.homepage, name="homepage"),
    path('login', uv.login, name="login"),
    path('signup', uv.signup, name="signup"),
    path('logout', uv.logout, name="logout"),
]
