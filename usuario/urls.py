from django.urls import path

from . import views

urlpatterns = [
    path('teste', views.usuario_list, name='usuario_list'),

    path('teste/<int:usuario_id>', views.buscar_usuario, name='buscar_usuario'),

    path('teste/editar/<int:usuario_id>', views.editar_usuario, name='editar_usuario'),

    path('teste/adicionar', views.adicionar_usuario, name='adicionar_usuario'),

    path('teste/render', views.usuario_render, name='usuario_render'),
    path('teste/adicionar/render', views.adicionar_render, name='adicionar_render'),

    path('teste/deletar/<int:usuario_id>', views.deletar_usuario, name='deletar_usuario'),

    path('teste/email', views.buscar_usuario_por_email, name='buscar_usuario_por_email'),
]