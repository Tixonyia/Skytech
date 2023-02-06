from django.views.generic import ListView
from .models import Person
import re


def select_deportments_tree(list_persons):
    staff = {'departments': {}}
    for person in list_persons:
        if "директор" in person.position.lower():
            staff['director'] = person.name

        elif re.search(r'"(\w* ?\w*)*"', person.position):
            dep = re.search(r'"(\w* ?\w*)*"', person.position).group(0)

            if dep not in staff['departments']:
                staff['departments'][dep] = {f'{person.position} id={person.id}': person.name}
            else:
                staff['departments'][dep][f'{person.position} id={person.id}'] = person.name
        else:
            if '"Техперсонал"' not in staff['departments']:
                staff['departments']['"Техперсонал"'] = {f'{person.position} id={person.id}': person.name}
            else:
                staff['departments']['"Техперсонал"'][f'{person.position} id={person.id}'] = person.name
    return staff


class TreePageView(ListView):
    model = Person
    context_object_name = 'tree_persons'
    template_name = 'people/tree.html'
    list_persons = model.objects.all()

    def get_context_data(self, *, object_list=None, list_persons=list_persons, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = select_deportments_tree(list_persons)
        return context


def select_deportments_list(list_persons):
    staff = {}
    for person in list_persons:
        man = {'id': person.id, 'name': person.name, 'position': person.position,
               'date_employment': person.date_employment, 'salary': person.salary, 'photo': person.image}
        staff[man['id']] = man
    return staff


class ListPageView(ListView):
    model = Person
    template_name = 'people/list.html'
    context_object_name = 'list_persons'
    ordering = 'salary'

    def get_ordering(self):
        if 'name' in self.request.GET:
            self.ordering = self.request.GET['name']
        return self.ordering

    def get_context_data(self, *, object_list=None, ordering=ordering, model=model, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordering'] = self.get_ordering()
        list_persons = model.objects.order_by(self.ordering)
        data = select_deportments_list(list_persons)
        context['persons'] = data
        return context

