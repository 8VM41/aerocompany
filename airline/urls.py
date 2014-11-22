from django.conf.urls import patterns, include, url

import flight.views
import flight.forms
import order.views
import order.forms

from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^flights/', flight.views.ListFlightView.as_view(), name='flights', ),
                       url(r'^$', flight.views.index),
                       url(r'^search/$', flight.views.search),
                       url(r'^search_results/$', flight.views.search),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^fill_data/$', order.views.fill_data),
                       url(r'^place_order/$', order.views.place_order),
                       url(r'^show_order/order_id/([0-9]+)/hash/([a-z0-9]+)/$', order.views.show_order),
                       url(r'^register/$', order.views.register)
)
