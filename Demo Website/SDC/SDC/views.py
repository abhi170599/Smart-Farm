from django.views.generic import TemplateView


class HomePageView(TemplateView):

     template_name="index.html"

class RiceView(TemplateView):

    template_name="Rice.html"

class Rice_stats_view(TemplateView):

    template_name="Rice_stats.html"

class Rice_demand_view(TemplateView):

    template_name = "Rice_demand.html"

class RicePriceView(TemplateView):

    template_name = "rice_price.html"                 
