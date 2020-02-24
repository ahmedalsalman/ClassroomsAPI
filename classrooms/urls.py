
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import classes.views
import APIapp.views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', classes.views.classroom_list, name='classroom-list'),
#    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classroomslist/', APIapp.views.APIList.as_view(), name='api-classroom-list'),
    path('classroomsdetail/<int:classroom_id>/', APIapp.views.APIdetail.as_view(), name='api-classroom-detail'),

    path('classrooms/create', classes.views.classroom_create, name='classroom-create'),
    path('classrooms_create/create/', APIapp.views.CreateClass.as_view(), name="api-classroom-create"),

    path('classrooms/<int:classroom_id>/update/', classes.views.classroom_update, name='classroom-update'),
    path('classrooms_update/<int:classroom_id>/update/', APIapp.views.UpdateClass.as_view(), name="api-classroom-update"),

    path('classrooms/<int:classroom_id>/delete/', classes.views.classroom_delete, name='classroom-delete'),
    path('classrooms_delete/<int:classroom_id>/delete/', APIapp.views.DeleteClass.as_view(), name="api-classroom-delete"),
    path('api/token/', TokenObtainPairView.as_view(), name='api-login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
