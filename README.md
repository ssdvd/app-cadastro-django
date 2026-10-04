# app-cadastro-django

Aplicação web de controle de produtos em estoque, feita com Django. Permite cadastrar, listar, buscar, editar e excluir itens.

Nasceu como projeto da disciplina **Software Product: Analysis, Specification, Project**, da Faculdade Impacta, e depois virou a aplicação-base dos meus projetos de infraestrutura na AWS.

## Funcionalidades

- [x] Cadastrar e listar produtos
- [x] Alterar produtos
- [x] Excluir produtos
- [x] Buscar produtos pelo nome

Cada item tem `nome`, `tipo` e `qnt` (quantidade).

## Tecnologias

| Camada | Tecnologia |
| --- | --- |
| Back-end | Python 3.10, Django 5.0 |
| Front-end | HTML5, Bootstrap, JavaScript |
| Banco de dados | MySQL (driver `mysqlclient`) |
| Deploy | Docker, Ansible |

## Rotas

| Rota | Descrição |
| --- | --- |
| `/` | Lista os itens; aceita `?search=` para buscar pelo nome |
| `/form/` | Formulário de cadastro |
| `/create/` | Grava um novo item |
| `/view/<id>/` | Detalhes de um item |
| `/edit/<id>/` | Formulário de edição |
| `/update/<id>/` | Grava a edição |
| `/delete/<id>/` | Exclui o item |
| `/admin/` | Admin do Django |

## Como rodar

Pré-requisitos: Python 3.10 ou superior e um banco MySQL. No Debian/Ubuntu, o `mysqlclient` precisa de alguns pacotes do sistema:

```bash
sudo apt-get install -y python3-venv python3-dev libmysqlclient-dev pkg-config
```

```bash
git clone https://github.com/ssdvd/app-cadastro-django.git
cd app-cadastro-django

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Aponte o bloco `DATABASES` de [`estoqueproject/settings.py`](estoqueproject/settings.py) para o seu banco e então:

```bash
python manage.py migrate
python manage.py runserver
```

Acesse <http://localhost:8000>.

### Com Docker

```bash
docker build -t app-cadastro-django .
docker run -p 8000:8000 app-cadastro-django
```

### Em uma instância EC2 com Ansible

O [`playbook.yml`](playbook.yml) instala as dependências, clona o repositório e inicia o servidor. Coloque o IP da instância em [`host.yml`](host.yml) e rode:

```bash
ansible-playbook -i host.yml -u ubuntu --private-key SUA_CHAVE.pem playbook.yml
```

## Infraestrutura

Estes repositórios provisionam a infraestrutura na AWS para esta aplicação, em três arquiteturas:

| Repositório | Arquitetura |
| --- | --- |
| [terraform-djangoapp-project](https://github.com/ssdvd/terraform-djangoapp-project) | Uma instância EC2 configurada com Ansible |
| [terraform-djangoapp-project-as-lb](https://github.com/ssdvd/terraform-djangoapp-project-as-lb) | Auto Scaling Group e Load Balancer |
| [terraform-djangoapp-project-ecs](https://github.com/ssdvd/terraform-djangoapp-project-ecs) | Containers no ECS com Fargate |

## Estrutura

```
estoqueapp/        # app: models, views, forms, templates e estáticos
estoqueproject/    # configurações e URLs do projeto
Dockerfile         # imagem da aplicação
playbook.yml       # deploy com Ansible
host.yml           # inventário do Ansible
```

O acompanhamento das tarefas ficou no [board do projeto](https://github.com/users/ssdvd/projects/1).

## Licença

[MIT](LICENSE)
