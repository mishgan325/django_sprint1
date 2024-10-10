from django.shortcuts import render


def about(request):
    template = 'html/about.html'
    return render(request, template)


def rules(request):
    template = 'html/rules.html'
    return render(request, template)