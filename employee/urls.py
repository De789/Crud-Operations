from django.contrib import admin  
from django.urls import path  
from employee import views  
from .views import LoginView
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.add_emp),  
    path('show',views.show), 
    path('add/', views.add_emp, name='add_employee'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('count-visit/', views.count_visit, name='count-visit'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('visit/', views.count_visit, name='visit'),
    path('studentapi/',views.LCStudentList.as_view()),
    path('studentapi/<int:pk>',views.RUDStudentRetrive.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
 
    path('s/<int:id>/', views.student_info), 
    path('students/', views.student_list),

    path('login',LoginView.as_view(),name='login'),



]  