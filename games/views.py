from django.views.generic import DetailView
from .models import Game


class GameDetailView(DetailView):
    model = Game
    template_name = "games/detail.html"
    context_object_name = "game"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_version"] = self.get_object().latest
        return context
    