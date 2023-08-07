from django.urls import path
from . import views

urlpatterns=[

    path("news/",views.index_news_view,name="news"),
    path("news/<slug:slug>/",views.detail_news_view,name="news-details"),
    path("notice/",views.index_notice_view,name="notice"),
    path("notice/<slug:slug>/",views.detail_notice_view,name="notice-details"),
    path("holiday/",views.index_holiday_view,name="holiday"),
    path("holiday/<int:id>/",views.detail_holiday_view,name="holiday-details"),
    path("career/",views.career,name="career"),
    path("about/",views.about,name="about")
]