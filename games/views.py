from django.views.generic import DetailView, ListView
from .models import Game


class GameListView(ListView):
    model = Game
    template_name = "games/list.html"
    context_object_name = "games"
    paginate_by = 12

    def get_queryset(self):
        return Game.objects.select_related('latest', 'creator').all().order_by('name')


class GameDetailView(DetailView):
    model = Game
    template_name = "games/detail.html"
    context_object_name = "game"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_version"] = self.get_object().latest
        return context
    