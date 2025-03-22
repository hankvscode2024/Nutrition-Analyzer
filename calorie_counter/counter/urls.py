from django.urls import path
from counter.views import index

urlpatterns = [
    path('', index, name='index'),
]




















# # -------------------------------------------------------
# import views
# print(dir(views))  # This will show available attributes in `views`
