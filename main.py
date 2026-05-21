from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
# Chave de segurança necessária para o funcionamento do recurso 'flash'
app.secret_key = "ia_academy_secret_token"

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email_digitado = request.form.get("email")
        senha_digitada = request.form.get("senha")
        perfil_escolhido = request.form.get("perfil")

        email_existe = False

        # Verifica se o e-mail já existe no arquivo de texto
        try:
            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    if f"Email: {email_digitado} |" in linha:
                        email_existe = True
                        break
        except FileNotFoundError:
            pass

        # Se existir, envia um alerta de erro e recarrega a página
        if email_existe:
            flash("Erro: Este e-mail já está cadastrado no sistema!", "danger")
            return redirect(url_for('home'))

        # Se não existir, salva o novo usuário no arquivo
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(
                f"Perfil: {perfil_escolhido} | Email: {email_digitado} | Senha: {senha_digitada}\n"
            )

        # Envia um alerta de sucesso e recarrega a página
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('home'))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)