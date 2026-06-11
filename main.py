from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "ia_academy_secret_token"

# ROTA 1: Página Inicial (Login)
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email_digitado = request.form.get("email")
        senha_digitada = request.form.get("senha")
        perfil_escolhido = request.form.get("perfil")
        
        login_sucesso = False
        
        # Valida se as credenciais coincidem com o arquivo usuarios.txt
        try:
            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    if f"Email: {email_digitado} |" in linha and f"Senha: {senha_digitada}" in linha:
                        login_sucesso = True
                        break
        except FileNotFoundError:
            pass

        if login_sucesso:
            flash(f"Bem-vindo de volta! Login realizado como {perfil_escolhido}.", "success")
            return redirect(url_for('home'))
        else:
            flash("Erro: Usuário ou senha incorretos.", "danger")
            return redirect(url_for('home'))

    return render_template("index.html")

# ROTA 2: Página de Cadastro (Criar Conta)
@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome_digitado = request.form.get("nome")
        email_digitado = request.form.get("email")
        senha_digitada = request.form.get("senha")
        
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

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"Perfil: aluno | Email: {email_digitado} | Senha: {senha_digitada}\n")

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('home'))

    return render_template("cadastro.html")

# ROTA ADICIONADA: Direciona para a página de cursos em anexo
@app.route('/cursos')
def cursos():
    return render_template("cursos.html")

if __name__ == "__main__":
    app.run(debug=True)