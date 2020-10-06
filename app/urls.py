
from django.urls import path, include
from . import views

app_name = 'app'
urlpatterns = [
    path(

        route  = '',
        view   = views.IndexView.as_view(),
        name   = 'index'

    ),
    path(

        route  = 'registro',
        view   = views.SignUpView.as_view(),
        name   = 'user_register'

    ),
     path(

        route  = 'registro/success',
        view   = views.SuccessView.as_view(),
        name   = 'success'

    )
]
