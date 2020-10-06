from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Frontend
    path('', views.index, name='Homepage'),
    path('detail/<slug>', views.detail, name='detail'),

    # bottom section
    path('about', views.about, name='about'),
    path('terms', views.terms_of_use, name='terms'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy_policy, name='privacy'),
    path('cookies', views.cookies, name='cookies'),
    path('ad-choices', views.Ad_choices, name='ad-choices'),
    path('guidance', views.parental_guidance, name='parental-guidance'),
    path('more-about-parental-guidance', views.more_parental_guidance, name='more-parental-guidance'),
    path('newsletter', views.newsletter, name='newsletter'),

    # menus
    path('BBC-news', views.BBC_news, name='BBC-news'),

    path('sport', views.BBC_sports, name='BBC-sports'),
    path('reel', views.BBC_reel, name='BBC-reel'),
    path('worklife', views.BBC_worklife, name='BBC-worklife'),
    path('travel', views.BBC_travel, name='BBC-travel'),
    path('future', views.BBC_future, name='BBC-future'),
    path('culture', views.BBC_culture, name='BBC-culture'),
    path('music', views.BBC_music, name='BBC-music'),
    path('tv', views.BBC_tv, name='BBC-tv'),
    path('weather', views.BBC_weather, name='BBC-weather'),
    path('sound', views.BBC_sound, name='BBC-sound'),

    # login section
    path('accounts/sign-in', views.login, name='login'),
    path('accounts/sign-up', views.sign_up, name='sign-up'),
    path('accounts/users', views.users, name='users'),
    path('accounts/logout', views.user_log_out, name='logout'),
    path('accounts/reset_password/',
         auth_views.PasswordResetView.as_view(template_name='menu/sign-in/reset_password.html'),
         name='reset_password'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='menu/sign-in/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('accounts/password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='menu/sign-in/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='menu/sign-in/password_reset_complete.html'),
         name='password_reset_complete'),

    # generic
    path('generic', views.BlogListData.as_view(), name='generic'),
    path('generic/<int:pk>', views.BlogDetailsViews.as_view(), name='generic-details'),
    path('generic-delete/<int:pk>', views.DeleteBlog.as_view(), name='generic-delete'),
    path('generic-edit/<int:pk>', views.UpdateBlog.as_view(), name='generic-edit')

]
