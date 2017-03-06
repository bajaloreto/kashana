from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin
from organizations.models import Organization

from logframe.mixins import AptivateDataBaseMixin
from logframe.models import LogFrame
from .mixins import OverviewMixin, update_last_viewed_item


class Home(LoginRequiredMixin, OverviewMixin, RedirectView):
    permanent = False
    pattern_name = 'dashboard'


class DashboardView(LoginRequiredMixin,
                    OverviewMixin, AptivateDataBaseMixin, TemplateView):
    template_name = 'dashboard/dashboard_base.html'


class SwitchLogframes(LoginRequiredMixin, RedirectView):
    permanent = False
    pattern_name = 'logframe-dashboard'

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(LogFrame, pk=self.request.POST['logframe'])
        update_last_viewed_item(self.request.user, self.object)
        return self.get(request, org_slug=self.object.organization.slug, slug=self.object.slug)


class DashboardOrganizationSelection(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'organization_list'
    template_name = 'dashboard/dashboard_organization_list.html'


class DashboardLogframeSelection(LoginRequiredMixin, ListView):
    model = LogFrame
    context_object_name = 'logframe_list'
    template_name = 'dashboard/dashboard_logframe_list.html'

    def get_queryset(self):
        return self.model.objects.filter(organization__slug=self.kwargs.get('org_slug'))
