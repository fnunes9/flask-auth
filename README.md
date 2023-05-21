# Authentication with Flask-Login

Este repositório apresenta uma simples API em Flask que autenticação por meio do Flask-Login. O objetvo é um exemplo de controle de sessão de usuário.

O Flask-Login é uma extensão do Flask que oferece recursos de gerenciamento de sessão de usuário e autenticação para aplicativos Flask. Ele simplifica o processo de lidar com login de usuário, logout e gerenciamento de sessões, fornecendo um conjunto de funções, decoradores e utilitários. Leia mais em *https://flask-login.readthedocs.io/en/latest/*.

Aqui está uma explicação sobre o que é o Flask-Login e como ele funciona:

1. Gerenciamento de Sessão de Usuário: O Flask-Login lida com o gerenciamento de sessões de usuário. Ele gerencia o estado de autenticação do usuário e os cookies de sessão, permitindo que você acompanhe facilmente se um usuário está logado ou não.

2. Autenticação de Usuário: O Flask-Login fornece utilitários para lidar com a autenticação de usuário. Ele permite que você verifique as credenciais do usuário, autentique os usuários e autorize o acesso a rotas ou recursos específicos com base no estado de autenticação do usuário.

3. Função de Carregamento de Usuário: O Flask-Login requer uma função de carregamento de usuário para carregar um objeto de usuário com base no ID do usuário armazenado na sessão. Essa função é responsável por recuperar o objeto de usuário de um banco de dados ou de qualquer outra fonte de dados com base no ID do usuário fornecido.

4. Funções de Login e Logout: O Flask-Login fornece as funções *login_user()* e *logout_user()* que permitem fazer login e logout explícitos dos usuários. Essas funções lidam com tarefas como configurar a sessão do usuário, atualizar o cookie de sessão e gerenciar o estado de autenticação do usuário.

5. Decoradores: O Flask-Login fornece decoradores para proteger rotas que exigem autenticação. O decorador *@login_required* garante que apenas usuários autenticados possam acessar uma determinada rota. Se um usuário não autenticado tentar acessar uma rota protegida, o Flask-Login redirecionará automaticamente para a página de login.

6. Classe UserMixin: O Flask-Login requer uma classe de usuário que represente o objeto de usuário. Ao herdar a classe *UserMixin* fornecida pelo Flask-Login, você herda várias propriedades e métodos necessários para autenticação e autorização do usuário, como *is_authenticated*, *is_active*, *is_anonymous* e *get_id*.

O Flask-Login simplifica a implementação de autenticação de usuário e gerenciamento de sessão em aplicativos Flask. Ele fornece uma maneira conveniente de lidar com login de usuário, logout e controle de acesso, permitindo que você se concentre nas funcionalidades principais do seu aplicativo.

## Organização do projeto

* app.py: A aplicação Flask. Leia mais em *https://flask.palletsprojects.com/en/2.2.x*.
* templates: Uma view para realização de um POST via form, que representa o login do usuário.

## Laboratório

- Você não precisa clonar este repositório. Abra uma nova instância do *codespace* e use um template em branco (*Blank*).

- Instale os pacotes: flask e flask-login:
  * `pip install nome-do-pacote`

- Crie o arquivo 'app.py' e copie o conteúdo desse mesmo arquivo presente neste repositório. Faça o mesmo com o arquito 'model.py'.

- Crie o diretório 'templates' e crie o arquivo 'login.html' copiando todo o conteúdo desse mesmo arquivo neste repositório.

- Nesse momento já é possível testar a API. 
  * `python3 app.py`

- Tente acessar as rotas marcadas com o decorador *@login_required* e veja o que acontece. Em seguida, acesse o login e tente autenticar com um usuário que não existe na base de dados. Após, faça o login usando um usuário já cadastrado e acesse essas mesmas rotas.

## Proposta de exercício (opcional)

1. Incremente a API com um Banco de Dados ao invés do uso de um simples dicionário. 

2. Estenda esta aplicação com outras rotas, como por exemplo, uma rota com a funcionalidade de registrar um usuário.
  - Criar uma view para registro: Faça um novo template chamado 'register.html'. Crie a view que deve conter qualquer informação necessária de um usuário. Não se esqueça da funcionalidade de *submit*.
  - Implementação da rota de registro: Crie a rota */register*, que responde aos métodos GET e POST.
  - Requisição GET para registro: Quando um usuário acessa */register*, retorne a view *register.html*.
  - Requisição POST para registro: Quando o usuário submete uma requisição de registro via POST, recupere
  os dados da requisição. Valide os dados recebidos. Se os dados são válidos, crie um novo usuário e o
  armazene no banco. Após o registro com sucesso, redirecione o usuário para */login* ou mostre uma
  mensagem de cadastro realizado com sucesso. Você também pode, automaticamente, logar o usuário com o 
  método *login_user()*. 

3. Crie Views mais agradáveis para as rotas desta aplicação, além de outras funcionalidades. Por exemplo, apresente uma View para */dashboard* que mostre quantas vezes o usuário se autenticou na API.

- Pratique e estude bastante. :rocket: