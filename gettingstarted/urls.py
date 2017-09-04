from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', hello.views.login, name = 'login'),
    url(r'^signup/', hello.views.signup, name = 'signup'),
    url(r'^home/', hello.views.home, name='home'),
    url(r'^dashboard/', hello.views.dashboard, name = 'dashboard'),
]
