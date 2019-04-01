from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "geotracker/index.html"

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data["home_page"] = " active"
        return context_data
