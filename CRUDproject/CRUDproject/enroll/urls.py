from django.contrib import admin
from django.urls import path,include
from enroll import views
from enroll import urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.addshow, name='addshow'),
    path('delete/<int:id>/',views.delete_d, name='delete'),
    path('<int:id>/',views.update_d, name='update')

]