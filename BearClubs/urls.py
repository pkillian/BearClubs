from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BearClubs.bc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',              'BearClubs.bc.views.index.index',   name='index'),
    url(r'^index$',         'BearClubs.bc.views.index.index',   name='index'),
    url(r'^index\.html$',   'BearClubs.bc.views.index.index',   name='index'),

    url(r'^register$',      'BearClubs.bc.views.user.userSignUp', name='register'),
    url(r'^login$',         'BearClubs.bc.views.user.userSignIn', name='login'),
    url(r'^logout$',        'BearClubs.bc.views.user.userLogOut', name='logout'),

    url(r'^clubs$',         'BearClubs.bc.views.organization.directory', name='directory'),
    url(r'^clubs/new$',     'BearClubs.bc.views.organization.addClub',   name='addClub'),
)