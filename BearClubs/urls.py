from django.conf.urls import patterns, include, url

from django.contrib import admin

from BearClubs.bc import views

admin.autodiscover();

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BearClubs.bc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^search/',                             include('haystack.urls'),  name = 'search'),
    url(r'^$',                          views.index,            name='index'),
    url(r'^index/?$',                   views.index,            name='index'),
    url(r'^index\.html/?$',             views.index,            name='index'),

    url(r'^register/?$',                views.userSignUp,       name='register'),
    url(r'^login/?$',                   views.userSignIn,       name='login'),
    url(r'^logout/?$',                  views.userLogOut,       name='logout'),

    url(r'^dashboard/?$',               views.dashboard,        name='dashboard'),
    url(r'^user/?$',                    views.dashboard,        name='dashboard'),
    url(r'^user/(?P<user_id>\d+)/?$',   views.profile,          name='profile'),
    url(r'^user/promote/?$',            views.promote,          name='promote'),
    url(r'^user/demote/?$',            views.demote,          name='demote'),

    url(r'^clubs/?$',                            views.directory,           name='directory'),
    url(r'^clubs/new/?$',                        views.addClub,             name='addClub'),
    url(r'^clubs/(?P<organization_id>\d+)/?$',   views.clubProfile,         name='club'),
    url(r'^clubs/join/?$',                       views.joinClub,            name='joinclub'),

    url(r'^events/?$',                           views.eventDirectory,      name='eventDirectory'),
    url(r'^events/new/?$',                       views.addEvent,            name='addEvent'),
    
    url(r'^clubs/(?P<organization_id>\d+)/manage_members/?$',  views.manage,        name='manage'),
)
