from django.db import models
from django.utils.translation import gettext_lazy as _

class Base(models.Model):
    criados = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualização'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True

class Blog(Base):
    titulo = models.CharField(_('Titulo'), max_length=100)
    descricao = models.CharField(_('Descrição'), max_length=200)
    apresentacao = models.CharField(_('Apresentação'), max_length=300)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.titulo

