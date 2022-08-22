from django.urls import path

from users.views import login_view, logout_view, register_view, Detail_user_profile, Update_user_profile, Update_user

urlpatterns =[
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    path('detail-user-profile/<int:pk>/', Detail_user_profile.as_view(), name = 'detail_user_profile'),
    path('update-user-profile/<int:pk>/', Update_user_profile.as_view(), name = 'update_user_profile'),
    path('update-user/<int:pk>/', Update_user.as_view(), name = 'update_user'),

]