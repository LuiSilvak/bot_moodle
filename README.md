# Bot Automatizado para Moodle

## Descrição
Um bot automatizado em Python que realiza o login em uma plataforma Moodle, acessa um curso específico e lista as seções disponíveis no curso. Este projeto utiliza a biblioteca Selenium para interagir com a interface web da plataforma.


## 🚀 Funcionalidades
- Login automático na plataforma Moodle.
- Navegação pela lista de cursos.
- Acesso a um curso específico.
- Listagem de seções dentro do curso.


## 📋 Requisitos
Antes de executar o projeto, certifique-se de que possui:
1. Python 3.x instalado no sistema.
2. Biblioteca **Selenium** instalada:
   
```bash
   pip install selenium
```

3. ChromeDriver compatível com sua versão do Google Chrome:
- Baixar ChromeDriver


## 🛠️ Configuração

1. Clone este repositório:

```bash
    git clone https://github.com/LuiSilvak/bot_moodle.git
    cd bot_moodle
```

2. Configure o caminho do ChromeDriver no arquivo bot_moodle.py:

```bash
    caminho_driver = "caminho/para/seu/chromedriver"
```

3. Utilize o Moodle demo para testes ou configure com suas credenciais:

```bash
    URL do Moodle Demo: https://sandbox.moodledemo.net/login/index.php
    Usuário: student
    Senha: sandbox24
```


## 🖥️ Como Usar
1. Execute o script:

```bash
    python bot_moodle.py
```

2. O bot realizará as seguintes ações:

- Login na plataforma Moodle.
- Busca pelo curso configurado no script.
- Exibição das seções disponíveis no console.


## 🔧 Estrutura do Código

Configura o driver do Selenium para utilizar o ChromeDriver.
```bash
    configurar_driver(caminho_driver):
```

Realiza o login na plataforma Moodle.
```bash
    login_moodle(driver, url, usuario, senha):
```

Procura um curso específico na lista e acessa sua página.
```bash
    acessar_curso(driver, nome_curso):
```

Lista e exibe no console as seções disponíveis no curso.
```bash
    listar_secoes(driver):
```


## 🤖 Exemplo de Saída

Seções disponíveis no curso:
- Introdução
- Aula 1: Conceitos Básicos
- Aula 2: Exercícios Práticos


## 📚 Referências
1. Documentação Selenium
2. Moodle Sandbox


## 🛡️ Licença
Este projeto está licenciado sob a MIT License.


Sinta-se à vontade para contribuir ou adaptar este bot conforme necessário!


