# Diolab07 - Projetos diversos

Este repositório reúne múltiplos projetos desenvolvidos no contexto do Diolab07. Cada subprojeto possui uma proposta distinta, abrangendo desde uma API Node.js para consulta de endereços até diferentes implementações de jogos de roleta interativas em HTML, CSS e JavaScript. A seguir, uma visão geral e instruções detalhadas para cada um.

---

## Estrutura do Repositório

diolab07/
├── API/
│   └── my-node-api/
│       ├── package.json
│       ├── README.md         -> API/my-node-api/README.md
│       └── src/
│           ├── app.js
│           ├── controllers/
│           │   └── addressController.js
│           ├── routes/
│           │   └── address.js
│           └── services/
│               └── viaCepService.js
├── cloud/
│   └── roulette-project/
│       ├── index.html
│       ├── README.md         -> cloud/roulette-project/README.md
│       ├── script.js
│       └── style.css
├── gemini/
│   └── roulette-project/
│       ├── index.html
│       ├── README.md         -> gemini/roulette-project/README.md
│       ├── script.js
│       └── style.css
├── gpt/
│   └── roulette-project/
│       ├── README.md         -> gpt/roulette-project/README.md
│       └── src/
│           ├── index.html
│           ├── main.js
│           └── style.css
└── io3/
    └── roulette-project/
        ├── index.html
        ├── README.md         -> io3/roulette-project/README.md
        ├── script.js
        └── style.css

---

## Detalhamento dos Subprojetos

### 1. API - My Node API

Descrição:  
API construída com Node.js/Express que consulta o serviço VIA CEP (https://viacep.com.br) para retornar informações de endereço com base no CEP informado.

Principais Componentes:
- Servidor: Implementado em src/app.js.
- Rotas: Definidas em src/routes/address.js.
- Controller: Lógica de consulta em src/controllers/addressController.js.
- Serviço: Integração com a API do VIA CEP em src/services/viaCepService.js.

Instalação e Execução:
1. Navegue até a pasta do projeto:
   cd diolab07/API/my-node-api
2. Instale as dependências:
   npm install
3. Inicie o servidor:
   npm start
4. Realize uma requisição GET para obter o endereço pelo CEP:
   http://localhost:3000/address/{cep}

Consulte o README da API (diolab07/API/my-node-api/README.md) para mais detalhes.

---

### 2. Cloud Roulette Project

Descrição:  
Projeto de um jogo de roleta web que utiliza HTML, CSS e JavaScript. O design conta com cores vibrantes definidas em CSS, e a interação é realizada por meio de cliques que disparam a rotação do elemento.

Principais Componentes:
- HTML: index.html – Estrutura base do jogo.
- CSS: style.css – Estilização com design moderno.
- JavaScript: script.js – Lógica de desenho e animação da roleta.

Como Executar:
1. Abra o arquivo index.html em seu navegador.
2. Clique sobre a roleta para acionar a animação.

Veja mais detalhes no README do Cloud Roulette (diolab07/cloud/roulette-project/README.md).

---

### 3. Gemini Roulette Project

Descrição:  
Outra versão do jogo de roleta, com um design diferenciado e cores que alternam entre tons suaves (como rosa e branco). Este projeto foca em proporcionar uma experiência visual agradável.

Principais Componentes:
- HTML: index.html
- CSS: style.css – Define um fundo claro e estiliza a roleta.
- JavaScript: script.js – Controla a animação e a física da roleta.

Como Executar:
1. Abra o arquivo index.html no navegador.
2. Interaja com a roleta clicando para iniciar a animação.

Para mais informações, consulte o README do Gemini Roulette (diolab07/gemini/roulette-project/README.md).

---

### 4. GPT Roulette Project

Descrição:  
Projeto que utiliza recursos avançados do HTML5 e da API Canvas para implementar uma roleta com simulação de física (gravidade, atrito, etc.). Esta versão apresenta uma experiência mais realista com elementos dinâmicos.

Estrutura:
- HTML: src/index.html
- JavaScript: src/main.js – Lógica de animação e controle da roleta.
- CSS: src/style.css – Estilos para melhorar a visualização e responsividade.

Como Executar:
1. Entre na pasta do projeto:
   cd diolab07/gpt/roulette-project/src
2. Abra o arquivo index.html no navegador para ver a roleta em ação.

Consulte o README do GPT Roulette (diolab07/gpt/roulette-project/README.md) para mais informações e instruções de uso.

---

### 5. IO3 Roulette Project

Descrição:  
Projeto de um jogo de roleta simples e interativo utilizando HTML, CSS e JavaScript. Focado em demonstrar noções básicas de animação e manipulação de elementos gráficos via Canvas.

Principais Componentes:
- HTML: index.html
- CSS: style.css
- JavaScript: script.js – Contém a lógica de animação e controle de velocidades da roleta e da bola.

Como Executar:
1. Abra o index.html em um navegador.
2. Clique sobre a roleta para iniciar o giro e acompanhar a movimentação da bola.

Mais detalhes estão disponíveis no README do IO3 Roulette (diolab07/io3/roulette-project/README.md).

---

## Observações Gerais

- Interatividade: Em todos os projetos de roleta, a interação é realizada via cliques no canvas, acionando a função de rotação e animação do jogo.
- Design e Layout: Cada subprojeto possui uma identidade visual própria, variando entre paletas de cores (ex.: amarelo/púrpura, rosa/branco, e outros) conforme o objetivo de cada versão.
- Tecnologias Utilizadas:
  - Front-end: HTML5, CSS3, JavaScript (Canvas API).
  - Back-end (API): Node.js, Express, Axios.

---
