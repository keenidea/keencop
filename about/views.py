from django.shortcuts import render


def history(request):
    context = {
        'heading': 'HISTORY',
        'active': 'active',
    }
    return render(request, 'about/about.html', context)


def activities(request):
    context = {
        'heading': 'ACTIVITIES',
    }
    return render(request, 'about/activities.html', context)


def board(request):
    context = {
        'heading': 'THE BOARD',
    }
    return render(request, 'about/board.html', context)


def theme(request):
    context = {
        'heading': 'THEME FOR THE YEAR 2017',
    }
    return render(request, 'about/theme.html', context)


def beliefs(request):
    context = {
        'heading': 'BELIEFS AND CORE VALUES',
    }
    return render(request, 'about/beliefs.html', context)
