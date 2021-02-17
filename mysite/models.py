from django.db import models

# Create your models here.
"""
1. Construa uma aplicação web para cadastrar clientes com os seguintes dados:
a. CPF
b. Nome 
c. E-mail
d. Telefone
e. Endereço
    i. Logradouro
    ii. Número
    iii. Complemento
    iv. Bairro
    v. Cidade
    vi. Estado
O cliente pode cadastrar mais de um endereço definindo o “Tipo”. Exemplos de tipo de endereço: Entrega, Cobrança, Geral... 
"""

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nome do Cliente')
    cpf = models.CharField(unique=True, max_length=11, null=False, blank=False, primary_key=True)
    email = models.EmailField()    
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº celular')
    def __str__(self):
        return f"{self.nome}, {self.cpf}"
        


class Endereco(models.Model):
    tipo_endereco = (
        ('1', 'Residencial'),
        ('2', 'Comercial'),
        ('3', 'Outros'),
    )
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=3, choices=tipo_endereco, null=False)
    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=6, null=False, blank=False)
    complemento = models.CharField(max_length=50, blank= True, null=True )
    bairro = models.CharField(max_length=100, null=True, blank=False)
    cidade = models.CharField(max_length=50, null=True, blank=False)
    cep = models.CharField(max_length=9, null=True, blank=False)
    uf = models.CharField(max_length=2, null=True, blank=False)
    
    def __str__(self):
        return f"{self.cliente}, {self.endereco}"