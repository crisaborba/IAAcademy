IA Academy - Sistema de Autenticação
O IA Academy é uma aplicação web moderna e responsiva desenvolvida com Python e Flask para o back-end, utilizando um design futurista com estilo Glassmorphism no front-end via Bootstrap 5.

O sistema simula um portal educacional onde os usuários podem selecionar seu tipo de acesso (Aluno, Professor ou Visitante) e realizar o cadastro ou validação de login. Os dados dos usuários são persistidos de forma simples em um arquivo de texto local.

Tecnologias Utilizadas
Python 3 - Linguagem base do back-end.

Flask - Micro-framework web para roteamento e lógica de servidor.

Jinja2 - Motor de templates do Flask para renderização dinâmica do HTML e gerenciamento de mensagens flash.

Bootstrap 5 - Framework CSS para estilização moderna, responsiva e layout em grade.

Google Fonts (Urbanist) - Tipografia personalizada para o projeto.

Estrutura de Pastas do Projeto
Para que o Flask consiga localizar os arquivos corretamente e evitar erros de TemplateNotFound, certifique-se de que a estrutura do seu diretório está exatamente assim:

IA-Academy/
│
├── app.py              (Arquivo principal contendo o código Python/Flask)
├── usuarios.txt         (Arquivo gerado automaticamente para salvar os dados)
│
└── templates/          (Pasta obrigatória para os arquivos de visualização)
└── index.html      (Código da interface visual HTML/CSS)

Funcionalidades Implementadas
Interface Futurista (Dark Mode): Layout imersivo baseado em tons escuros com degradês em ciano e roxo, além de cartões translúcidos (glassmorphism).

Validação de Cadastro Existente: O sistema lê o arquivo usuarios.txt para checar se o e-mail digitado já foi registrado antes de salvar uma nova conta.

Persistência em Arquivo: Cadastro de novos perfis salvando os dados no formato: Perfil: X | Email: Y | Senha: Z.

Mensagens Flash Dinâmicas: Alertas nativos do Bootstrap informando se o cadastro foi realizado com sucesso (alerta verde) ou se o e-mail já existe (alerta vermelho).

Redirecionamento Seguro: Uso de redirect(url_for(...)) para evitar o reenvio duplicado de formulários ao atualizar a página (F5).

Como Executar o Projeto
1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Você também precisará instalar o Flask. Caso não tenha instalado, execute o comando abaixo no seu terminal/prompt de comando:

pip install Flask

2. Rodando a Aplicação
Navegue até a pasta raiz do projeto onde está o arquivo app.py e execute o comando:

python app.py

O servidor local será iniciado em modo de depuração (Debug Mode). Abra o seu navegador e acesse o endereço: http://127.0.0.1:5000

Licença
Este projeto foi desenvolvido para fins educacionais e de aprendizado prático em desenvolvimento web com Python e Flask.
