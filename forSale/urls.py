from django.urls import path, register_converter
from forSale import views

app_name = 'forSale'


urlpatterns = [
    path('', views.item_list, name='item_list'),                        # 조회
    path('view/<int:pk>/', views.item_detail, name='item_detail'),      # 조회
    path('new/', views.item_new, name='item_new'),                      # 등록
    path('remove/<int:pk>/', views.item_remove, name='item_remove'),    # 삭제
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),          # 수정
]