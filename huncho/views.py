from django.shortcuts import render
from  .models import member
from django.views.generic import  ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class memberListview(ListView):
    model = member
    template_name = 'huncho/index.html'
    context_object_name = 'profiles'
    ordering = ['name']

    def get_query(self):
        query = self.request.GET.get('q')
        if query:
            return member.objects.filter(name__icontains=query)|member.objects.filter(slogan__icontains=query)
        else:
            return member.objects.all()


class memberCreateView(CreateView):
    model= member
    fields = '__all__'
class memberUpdateView(UpdateView):
    model = member
    fields = '__all__'
class memberDeleteView(DeleteView):
    model = member
    success_url = '/'