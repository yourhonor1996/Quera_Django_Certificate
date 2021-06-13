from .models import Musician, Album
from django.views.generic import ListView, DetailView
# the list view
class MusicianListView(ListView):
    queryset = Musician.objects.all().order_by('name')
    template_name = 'musician_list.html'
    paginate_by = 1
    
    

# the detail view
class AlbumDetailView(DetailView):
    queryset = Album.objects.filter(num_stars__gte = 3)
    template_name = 'album_detail.html'
