from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria do Produto', blank='False', null='False', max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'

    def _str_(self):
        return self.nome        