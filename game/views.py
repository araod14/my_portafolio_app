from django.shortcuts import render

# Create your views here.
def game_view(request):
    context = {
        'game_url': '/static/dist/index.html'
    }
    return render(request, 'game.html', context)