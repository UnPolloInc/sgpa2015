from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from usuarios.forms import UserForm,UserUpdateForm
from usuarios.models import Usuario
from django.utils.decorators import method_decorator
import re
from django.db.models import Q

# Create your views here.


class IndexView(ListView):
    template_name = 'usuario_list'
    model = Usuario

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class CreateUser(CreateView):
    template_name = 'usuarios/create.html'
    form_class = UserForm
    success_url = '/usuarios'

    #@user_passes_test(lambda user: user.is_superuser)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateUser, self).dispatch(*args, **kwargs)

class UserMixin(object):
    model = Usuario

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Usuario'})
        return kwargs



class DeleteUser(UserMixin, DeleteView):
    template_name = 'usuarios/delete_confirm.html'

    success_url = '/usuarios'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteUser, self).dispatch(*args, **kwargs)
"""
class UpdateUser(UpdateView):
    context_object_name = 'variable_used_in `update.html`'
    form_class = UserUpdateForm
    template_name = 'usuarios/update.html'
    success_url = '/'

    def form_valid(self, form):
        #save cleaned post data
        clean = form.cleaned_data
        context = {}
        self.object = context.save(clean)
        return super(UpdateUser, self).form_valid(form)
"""

class UpdateUser(UpdateView):
    template_name = 'usuarios/update.html'
    model = Usuario
    form_class = UserUpdateForm
    success_url = '/usuarios/'



def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('busqueda' in request.GET) and request.GET['busqueda'].strip():
        query_string = request.GET['busqueda']

        entry_query = get_query(query_string, ['username','first_name', 'last_name',])

        found_entries = Usuario.objects.filter(entry_query).order_by('first_name')
    return render_to_response('usuarios/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))