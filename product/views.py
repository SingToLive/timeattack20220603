from django.shortcuts import render
from .models import Category

# Create your views here.
def main(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        print(all_category)
        return render(request, 'a.html', {'cat':all_category})