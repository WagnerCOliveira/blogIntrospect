from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Blog
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar E-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.all()
        return context


class QuemsouView(TemplateView):
    template_name = 'quemsou.html'


class ElementsView(TemplateView):
    template_name = 'elements.html'

