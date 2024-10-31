"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.conf import admin
from django.contrib import admin
from django.urls import path
from sistema.views import FuncionarioUpdateView
from sistema.views import FuncionarioCreateView
from sistema.views import FuncionarioDeleteView

urlpatterns = [

    path('', include('website.urls', namespace='website')),
    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('funcionario/<id>', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario')
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),

]

urlpatterns = [
    path('admin/', admin.site.urls),
]
