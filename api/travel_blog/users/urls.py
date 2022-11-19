from django.urls import path
from .views import MyUserCreate, MyUserDetail, MyUserList 

app_name = 'users'

urlpatterns = [
    path('register/', MyUserCreate.as_view(), name="create_user"),
    path('', MyUserList.as_view(), name='users_list'),
    path('<int:pk>', MyUserDetail.as_view(), name='user_detail')
]