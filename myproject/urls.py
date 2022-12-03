from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    path(r'', views.BoardListView.as_view(), name='home'),
    path(r'signup/', accounts_views.signup, name='signup'),
    path(r'login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),

    path(r'reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='password_reset_email.html',
             subject_template_name='password_reset_subject.txt'
         ),
         name='password_reset'),
    path(r'reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path(r'reset/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path(r'reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path(r'settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path(r'settings/password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path(r'settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),
    # path(r'boards/(<pk>\d+)/', views.board_topics, name='board_topics'),
    path(r'boards/(<pk>\d+)/', views.TopicListView.as_view(), name='board_topics'),
    path(r'boards/(<pk>\d+)/new/', views.new_topic, name='new_topic'),
    # path(r'boards/(<pk>\d+)/topics/(<topic_pk>\d+)/', views.topic_posts, name='topic_posts'),
    path(r'boards/(<pk>\d+)/topics/(<topic_pk>\d+)/', views.PostListView.as_view(), name='topic_posts'),
    path(r'boards/(<pk>\d+)/topics/(<topic_pk>\d+)/reply/', views.reply_topic, name='reply_topic'),
    path(r'boards/(<pk>\d+)/topics/(<topic_pk>\d+)/posts/(<post_pk>\d+)/edit/', views.PostUpdateView.as_view(),
         name='edit_post'),
    path(r'admin/', admin.site.urls),
]
