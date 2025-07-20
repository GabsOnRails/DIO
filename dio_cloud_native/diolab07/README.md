
# Diolab07 - Projetos Diversos

Este repositório reúne múltiplos projetos desenvolvidos no contexto do **Diolab07**, cada um com uma proposta distinta. Eles variam desde uma API em Node.js para consulta de endereços até diferentes implementações de jogos de roleta interativos usando HTML, CSS e JavaScript.

---

## 📁 Estrutura do Repositório

```
diolab07/
├── API/
│   └── my-node-api/
├── cloud/
│   └── roulette-project/
├── gemini/
│   └── roulette-project/
├── gpt/
│   └── roulette-project/
└── io3/
    └── roulette-project/
```

---

## 🔍 Detalhamento dos Subprojetos

### 1. API - My Node API

**Descrição:**  
API construída com Node.js e Express para consulta de endereços via [VIA CEP](https://viacep.com.br).

**Principais Componentes:**
- `src/app.js`: Inicializa o servidor.
- `src/routes/address.js`: Define as rotas.
- `src/controllers/addressController.js`: Contém a lógica de negócio.
- `src/services/viaCepService.js`: Realiza requisições à API do VIA CEP.

**Como executar:**
```bash
cd diolab07/API/my-node-api
npm install
npm start
```

Acesse:  
`http://localhost:3000/address/{cep}`

📄 [Leia mais](API/my-node-api/README.md)

---

### 2. Cloud Roulette Project

**Descrição:**  
Jogo de roleta com HTML, CSS e JavaScript. Design moderno com cores vibrantes e animação de giro ao clique.

**Componentes:**
- `index.html`
- `style.css`: Estilização.
- `script.js`: Lógica e animação.

**Como executar:**  
Abra `index.html` no navegador.

📄 [Leia mais](cloud/roulette-project/README.md)

---

### 3. Gemini Roulette Project

**Descrição:**  
Versão da roleta com design leve, utilizando tons suaves (rosa e branco). Foco em uma experiência visual limpa.

**Componentes:**
- `index.html`
- `style.css`: Estilo claro e agradável.
- `script.js`: Controla o giro da roleta.

**Como executar:**  
Abra `index.html` no navegador.

📄 [Leia mais](gemini/roulette-project/README.md)

---

### 4. GPT Roulette Project

**Descrição:**  
Roleta avançada com animações realistas via Canvas API, simulando física como gravidade e atrito.

**Estrutura:**
- `src/index.html`
- `src/main.js`: Lógica da roleta com física.
- `src/style.css`: Estilo responsivo e adaptável.

**Como executar:**
```bash
cd diolab07/gpt/roulette-project/src
```
Abra `index.html` no navegador.

📄 [Leia mais](gpt/roulette-project/README.md)

---

### 5. IO3 Roulette Project

**Descrição:**  
Versão simplificada e didática do jogo de roleta, com foco em conceitos básicos de animação e manipulação de Canvas.

**Componentes:**
- `index.html`
- `style.css`
- `script.js`: Lógica do jogo e animação da roleta.

**Como executar:**  
Abra `index.html` no navegador.

📄 [Leia mais](io3/roulette-project/README.md)

---

## ⚙️ Tecnologias Utilizadas

- **Front-end:** HTML5, CSS3, JavaScript (Canvas API)
- **Back-end (API):** Node.js, Express, Axios

---

## 💡 Observações

- Todos os jogos de roleta são interativos e utilizam o clique para acionar a rotação.
- Cada versão possui uma identidade visual própria, com diferentes estilos e paletas de cores.


