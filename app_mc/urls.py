from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # Despesas
    path('despesas', views.visualizarDespesas, name="lista_despesas"),
    path('criar/despesas', views.criarDespesas, name="criar_despesas"),
    path('atualizar/despesas/<int:id>/', views.atualizarDespesas, name="atualizar_despesas"),
    path('excluir/despesas/<int:id>/', views.excluirDespesas, name="excluir_despesas"),

    # Tipo de Despesas
    path('tipoDespesas', views.visualizarDespesas, name="lista_tipoDespesas"),
    path('criar/tipoDespesas', views.criarDespesas, name="criar_tipoDespesas"),
    path('atualizar/tipoDespesas/<int:id>/', views.atualizarDespesas, name="atualizar_tipoDespesas"),
    path('excluir/tipoDespesas/<int:id>/', views.excluirDespesas, name="excluir_tipoDespesas"),

    # Faturamentos
    #path('faturamentos', views.visualizarFaturamentos, name="lista_faturamentos"),
    path('criar/faturamentos', views.criarFaturamentos, name="criar_faturamentos"),
    path('atualizar/faturamentos/<int:id>/', views.atualizarFaturamentos, name="atualizar_faturamentos"),
    path('excluir/faturamentos/<int:id>/', views.excluirFaturamentos, name="excluir_faturamentos"),

    # Fechamentos
    path('administrarFechamentos/<int:id>', views.admFechamentos, name="adm_fechamentos"),
    path('criar/fechamentos', views.criarFechamentos, name="criar_fechamentos"),
    #path('atualizar/fechamentos/<int:id>/', views.atualizarFechamentos, name="atualizar_fechamentos"),
    #path('excluir/fechamentos/<int:id>/', views.excluirFechamentos, name="excluir_fechamentos"),


]
