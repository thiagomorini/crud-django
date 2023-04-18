# CRUD with Django

Este projeto é um CRUD simples construído com Django para demonstrar o uso básico do framework. O projeto possui um aplicativo chamado "app_edu", que permite a listagem, cadastro, alteração e exclusão de módulos, e os testes do model e das views.

## Tecnologias utilizadas

- Python 3.11
- Django 4.2

## Instalação e execução

Para executar o projeto localmente, siga os seguintes passos:

1. Clone o repositório para o seu computador:

```
git clone https://github.com/thiagomorini/crud-django.git
```

2. Instale as dependências do projeto.

3. Execute as migrações do banco de dados:

```
python manage.py migrate
```

4. Execute o servidor:

```
python manage.py runserver
```

5. Acesse o projeto em seu navegador através do endereço http://127.0.0.1:8000/modules/

6. Se precisar executar os testes do modelo e das views, basta rodar o comando:

```
python manage.py test app_edu
```

## Contribuição

Você pode contribuir com o projeto de várias formas:

1. Reportando bugs e problemas no Github.
2. Fazendo pull requests com correções e novas funcionalidades.
3. Compartilhando o projeto e incentivando outros desenvolvedores a usá-lo.

## Licença
Este projeto é distribuído sob a licença MIT.

## Contato
Você pode entrar em contato comigo sempre que tiver alguma dúvida ou sugestão de melhorias.
