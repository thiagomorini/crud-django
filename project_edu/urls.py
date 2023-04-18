from django.urls import path
from app_edu.views import module_list, module_create, module_update, module_delete

urlpatterns = [
    path('modules/', module_list, name='module_list'),
    path('modules/create/', module_create, name='module_create'),
    path('modules/<int:pk>/', module_update, name='module_update'),
    path('modules/<int:pk>/delete/', module_delete, name='module_delete')
]
