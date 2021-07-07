"""postbar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views, login_view, home_view, hometo_view, usermanage_view, postmange_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('prac/', views.prac),

    path('home/', home_view.home),
    path('home_verify_uid/', home_view.home_verify_uid),
    path('home_verify_uid_bug/', home_view.home_verify_uid_bug),
    path('home_bug/', home_view.home_bug),

    path('home/commit/', home_view.commitpost),
    path('home/commit_bug/', home_view.commitpost_bug),
    path('home/commit_verify_uid', home_view.commitpost_verify_uid),

    path('hometo/', hometo_view.hometo),
    path('hometo_bug/',hometo_view.hometo_bug),

    path('hometo/commit_bug/', hometo_view.commitreply_bug),
    path('hometo/commit/', hometo_view.commitreply),

    path('register/', login_view.register),
    path('login/', login_view.login),
    path('login_bug/', login_view.login_bug),
    path('loginrsa/', login_view.login_rsa),
    path('login_verify_uid/', login_view.login_verify),
    path('login_verify_uid_bug/', login_view.login_verify_bug),
    path('login_first/', login_view.login_first),
    path('login_second/', login_view.login_second),
    path('login_first_bug/', login_view.login_first_bug),
    path('login_second_bug/', login_view.login_second_bug),
    path('login_verify/', login_view.login_verify),
    path('login_verify_identity/',login_view.login_verify_identity),
    path('logout/', login_view.logout),

    path('usermanage/', usermanage_view.usermanage),
    path('postmanage/', postmange_view.postmanage),
    path('replymanage/', postmange_view.replymanage),
    path('replymanage_bug/', postmange_view.replymanage_bug),
    path('replymanage/delreply/', postmange_view.delreply),
    path('replymanage/delreply_bug/', postmange_view.delreply_bug),
    path('replymanage/delreply_identity/', postmange_view.delreply_identity),
    path('replymanage/delreply_identity_bug/', postmange_view.delreply_identity_bug),

    path('upload/', usermanage_view.upload_fie),
    path('upload_bug/', usermanage_view.upload_fie_bug),

    path('display/',usermanage_view.display_file),
    path('display_bug/', usermanage_view.display_file_bug),
    path('download/', usermanage_view.download_file),
    path('download_bug/', usermanage_view.download_file_bug),

]
