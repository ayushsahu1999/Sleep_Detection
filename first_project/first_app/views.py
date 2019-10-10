from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app import forms
from alarm import main

# Create your views here.
def final(request):
    main()
    return render(request, 'first_app/final.html')



def form(request):
    form = forms.FormName()

    if (request.method == 'POST'):
        # form = forms.FormName(data=request.POST)

        return HttpResponseRedirect('final')

    else:
        form = forms.FormName()

    return render(request, 'first_app/form.html', {'form': form})
