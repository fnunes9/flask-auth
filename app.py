from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from model import User

# cria o serviço
app = Flask(__name__)
# chave usada apenas em ambiente dev
app.config['SECRET_KEY']= '7c5660a9fe8d887fb2459293d735cc'

login_manager = LoginManager()
login_manager.init_app(app)

# emulando um banco de dados de usuarios
users = {'prof.gustavo': {'password': '123789'},
         'aluno.joao': {'password': '123456'},
         'aluno.marta': {'password': '123321'}}

'''
Esse método carrega um objeto User por meio do 'id'.
Esse método será chamado pelo Flask-Login toda vez 
que o método 'login_user' for chamado na API. Basicamente,
este método controla a sessão do usuário.
'''
@login_manager.user_loader
def load_user(user_id):
   user = User()
   user.id = user_id
   return user


# definição das rotas
@app.route('/')
def index():
   return 'Welcome to the Flask-Login example!'

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      # abre a reqisição e extrai os valores de 'username' e 'password'
      # (espera-se que esses valores existam)
      username = request.form['username']
      password = request.form['password']

      # consulta no 'BD' se o usuário é válido
      if username in users and password == users[username]['password']:
         # loga o usuário (login_user) fornecendo um id (username) para ele.
         user = User()
         user.id = username
         login_user(user)
         return redirect(url_for('dashboard'))
      else:
         return 'Invalid username or password. Please try again.'

   return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
   # rota protegida (ao usar o decorator @login_required), que
   # garante somente usuários autenticados podem acessar essa rota.
   return 'Welcome to the dashboard!'

@app.route('/logout')
@login_required
def logout():
   # usa o método do Flask-Login para limpar a sessão do usuário.
   logout_user()
   return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
