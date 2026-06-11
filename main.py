from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Chave secreta necessária para gerenciar as sessões e alertas flash do Flask
app.secret_key = "chave_secreta_super_segura_da_ia_academy"

# -------------------------------------------------------------------------
# 1. ROTA DA PÁGINA INICIAL / LOGIN
# -------------------------------------------------------------------------
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email_digitado = request.form.get("email")
        senha_digitada = request.form.get("senha")
        perfil_digitado = request.form.get("perfil")

        # Varre o arquivo local em busca de credenciais válidas correspondentes
        usuario_valido = False
        try:
            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    # O arquivo armazena os dados estruturados por pipe (|)
                    if f"Perfil: {perfil_digitado}" in linha and f"Email: {email_digitado}" in linha and f"Senha: {senha_digitada}" in linha:
                        usuario_valido = True
                        break
        except FileNotFoundError:
            # Caso o arquivo ainda não exista, indica que nenhum cadastro foi feito
            pass

        if usuario_valido:
            flash(f"Bem-vindo de volta! Login realizado como {perfil_digitado}.", "success")
            return redirect(url_for('cursos'))
        else:
            flash("Erro: E-mail, senha ou tipo de acesso incorretos!", "danger")
            return redirect(url_for('home'))

    return render_template("index.html")


# -------------------------------------------------------------------------
# 2. ROTA DE CADASTRO DE USUÁRIOS
# -------------------------------------------------------------------------
@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome_digitado = request.form.get("nome")
        email_digitado = request.form.get("email")
        senha_digitada = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")

        # Validação de segurança básica para checar se as senhas coincidem
        if senha_digitada != confirmar_senha:
            flash("Erro: As senhas digitadas não são iguais!", "danger")
            return redirect(url_for('cadastro'))

        # Verificação preventiva contra e-mails duplicados
        email_existe = False
        try:
            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    if f"Email: {email_digitado} |" in linha:
                        email_existe = True
                        break
        except FileNotFoundError:
            pass

        if email_existe:
            flash("Erro: Este e-mail já está cadastrado no sistema!", "danger")
            return redirect(url_for('cadastro'))

        # Registra de forma persistente o novo usuário com perfil de aluno
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"Perfil: aluno | Email: {email_digitado} | Senha: {senha_digitada}\n")

        flash("Cadastro realizado com sucesso! Faça login para continuar.", "success")
        return redirect(url_for('home'))

    return render_template("cadastro.html")


# -------------------------------------------------------------------------
# 3. ROTA DA PÁGINA DE CURSOS
# -------------------------------------------------------------------------
@app.route('/cursos')
def cursos():
    return render_template("cursos.html")


# -------------------------------------------------------------------------
# 4. ROTA DA PÁGINA SOBRE NÓS
# -------------------------------------------------------------------------
@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


# -------------------------------------------------------------------------
# 5. ROTA DA PÁGINA DE CONTATO
# -------------------------------------------------------------------------
@app.route('/contato', methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        # Captura os dados submetidos pelo formulário de contato
        nome = request.form.get("nome")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")
        
        # Opcional: Adicionar rotinas futuras para salvar as mensagens em arquivos ou banco
        flash("Mensagem enviada com sucesso! Entraremos em contato em breve.", "success")
        return redirect(url_for('contato'))
        
    return render_template("contato.html")


# -------------------------------------------------------------------------
# 6. ROTA DA PÁGINA DADOS DO ALUNO (DASHBOARD ANALYTICS)
# -------------------------------------------------------------------------
@app.route('/aluno')
def aluno():
    return render_template("aluno.html")


# -------------------------------------------------------------------------
# INICIALIZAÇÃO DO ECOSSISTEMA FLASK
# -------------------------------------------------------------------------
if __name__ == '__main__':
    # O modo debug ativo atualiza o ambiente dinamicamente a cada modificação nos arquivos python
    app.run(debug=True)