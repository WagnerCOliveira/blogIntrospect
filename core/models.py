from django.db import models


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Blog(Base):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    apresentacao = models.CharField('Apresentação', max_length=300)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.titulo

