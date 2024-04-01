from django.urls import path

from mrsgreenapple import views

app_name = 'mrsgreenapple'

urlpatterns = [
    path('<member_>/', views.show_member, name='member_'),
    # path('omori/', views.show_omori_html, name='omori'),
    # path('wakai/', views.show_wakai_html, name='wakai'),
]