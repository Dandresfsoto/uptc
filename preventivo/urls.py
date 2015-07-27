from django.conf.urls import url
from .views import InventarioView,NuevaActividadForm,CalendarioView,EventListFull,PlanView, PlanUpdateView
from .views import EventList,EventDetail,EventListMachine,ActividadList,ActividadDeleteView,ActividadView,ActividadUpdateView,ActividadEditarView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<idmantenimiento>\w+)/$',login_required(InventarioView.as_view()),name="preventivo"),
    url(r'^api/event/(?P<mantenimiento>[0-9]+)/(?P<maquina>[0-9]+)/$', login_required(EventList.as_view())),

    url(r'^api/event/maquina/(?P<maquina>[0-9]+)/$', login_required(EventListMachine.as_view())),
    url(r'^api/event/all/$', login_required(EventListFull.as_view())),
    url(r'^api/event/actividad/(?P<nombre>.*)/$', login_required(ActividadList.as_view())),

    url(r'^api/event/(?P<pk>[0-9]+)/(?P<mantenimiento>[0-9]+)/(?P<maquina>[0-9]+)/$', login_required(EventDetail.as_view())),


    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/plan/$',login_required(PlanView.as_view())),
    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/plan/actualizar/$',login_required(PlanUpdateView.as_view())),


    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/actividades/$',login_required(ActividadView.as_view())),
    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/actividad/$',login_required(ActividadEditarView.as_view())),

    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/agregar/$',login_required(NuevaActividadForm.as_view())),
    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/eliminar/(?P<pk>\w+)/$',login_required(ActividadDeleteView.as_view())),
    url(r'^(?P<tipo>\w+)/(?P<idmachine>\w+)/editar/(?P<pk>\w+)/$',login_required(ActividadUpdateView.as_view())),


    url(r'^(?P<idmantenimiento>\w+)/calendario/(?P<idmachine>\w+)/$',login_required(CalendarioView.as_view()),name="calendario"),
]

urlpatterns = format_suffix_patterns(urlpatterns)