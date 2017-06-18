from django.shortcuts import render


def evangelism(request):
    return render(request, 'ministries/evangelism.html', {})


def men(request):
    return render(request, 'ministries/men.html', {})

    
def women(request):
    return render(request, 'ministries/women.html', {})


def youth(request):
    return render(request, 'ministries/youth.html', {})


def children(request):
    return render(request, 'ministries/children.html', {})
