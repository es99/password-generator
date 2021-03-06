# password-generator
Programa gerador de senhas feitos em Python Flask com o objetivo de estudar alguns conceitos de git e GitHub e frontend Web.

### Etapa 1:
#### Criação do ambiente:
- Criado repositório no github
- git clone para baixar o repositório e trabalhar com ele localmente
- [Configurado ambiente virtual (virtualenv) no interpretador python Conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

#### Instalação de dependências:
* requirements.txt / requirements-dev.txt
* criado arquivo Makefile
* criação do diretório do aplicativo com o mesmo nome da pasta raiz
* criação da aplicação através do arquivo app.py
  - Não esquecer de setar as variáveis de ambiente FLASK_ENV e FLASK_APP
  - Criação da primeira rota blueprint: ext -> site -> __init__.py -> main.py (@bp.route)
  
### Etapa 2:
#### Tornando a aplicação instalável
* Especificação do pacote dentro do arquivo setup.py
  - pip install -e (para instalar em modo editável, ou seja, a cada alteração será feito uma nova
  instalação/empacotamento)
  - O pip install empacota a aplicação e a insere em site-packages possibilitando que a mesma seja
  chamada através do import sem precisar que o arquivo esteja no diretório corrente.

### Etapa 3: (12/08/2020)
#### Configurado as extensões Debug Toolbar e Config
* Habilitado o debug toolbar
* As configurações do app foram transferidas para um arquivo especial em ext/config

#### Elaborado templates
* Utilização de blocos (extends) para automatizar a criação de templates
* Templates base.html, index.html, senhas.html e about.html concluídos e operacionais

### Etapa 4: (13/08/2020)
#### flask_sqlalchemy, modelagem do banco, extensão cli do Flask
* Criada extensão generatorpass/ext/gerador que através da função generate que recebe os dados
enviados pelo formulário de cadastro e salva no banco. 
* comando "create-db" criado através da extensão cli
* banco modelado
* A query para inserir dados no banco ocorre com sucesso

### Etapa 5: (14/08/2020)
* Criação de tables no template senhas.html
    * tabela criada
* Realizar select no banco para mostrar os dados já inseridos 
    * Na rota site.senhas realizada consulta de todos os dados da tabela do banco (User.query.all())
    os dados são passados como callback para o render_templete através da variável items
    * Utilizado o Jinja para fazer um laço for iterando sobre os items da tabela e exibindo cada campo.
    
### Etapa 6:
* Adicionar feature para copiar a senha ou excluir a entrada de dados diretamente do template da tabela.