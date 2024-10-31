from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
from sistema.models import Funcionario
from .forms import FormularioDeCriacao

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()

    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template para listar os funcionários
    return render(request, "templates/funcionarios.html", contexto)

def cria_funcionario(request, pk):
    # Verificamos se o método é POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionarios'))
    else:
        form = FormularioDeCriacao()  # Para o caso de GET, por exemplo

    # Retorna o formulário para outros métodos
    return render(request, "templates/form.html", {'form': form})


class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

def get_object(self, queryset=None):
    funcionario = None
    # Os campos {pk} e {slug} estão presentes em self.kwargs
    id = self.kwargs.get(self.pk_url_kwarg)
    # slug = self.kwargs.get(self.slug_url_kwarg)

    if id is not None:
        # Busca o funcionario apartir do id
        funcionario = Funcionario.objects.filter(id=id).first()
   
    return funcionário


class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")



