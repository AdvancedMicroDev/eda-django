"""
URL configuration for rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import (
    filter_records, 
    get_records, 
    insert_record, 
    landing_page, 
    show_result, 
    record_inserted
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='home_page'),
    path('filter-records/', filter_records, name='filter_records'),
    path('filter-records/show-result', show_result, name='show_result'),
    path('get-records/', get_records, name='get_records'),
    path('insert-record/', insert_record, name='insert_record'),
    path('insert-record/record-inserted', record_inserted, name='record_inserted'),
]
