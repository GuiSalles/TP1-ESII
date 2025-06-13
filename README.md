# 📘 Projeto: Calculadora de IMC com Histórico

## 1. 👥 Membros do Grupo

- Lívia Castro  
- Guilherme Xavier Salles
- Gabriel Rocha Martins

---

## 2. 🩺 Explicação do Sistema

Este sistema é uma **calculadora de IMC** (Índice de Massa Corporal) desenvolvida em Flask. O usuário pode inserir seus dados (nome, idade, sexo, altura e peso) e obter seu IMC e respectiva classificação de saúde com base nas recomendações da OMS.

### Funcionalidades do sistema:

- ✅ Cálculo automático do IMC e exibição da classificação.
- ✅ Armazenamento de todas as avaliações feitas por nome de usuário.
- ✅ Página de perfil com histórico completo de avaliações (data, idade, peso, altura, IMC, classificação).
- ✅ Interface web simples e responsiva com Bootstrap.

---

## 3. 🛠 Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| **Python** | Linguagem principal do backend. |
| **Flask** | Microframework web usado para criar rotas e renderizar páginas HTML. |
| **HTML5** | Utilizado para criação da interface das páginas (formulários e tabelas). |
| **Bootstrap 5** | Framework CSS para estilização responsiva e moderna da interface. |
| **SQLite** | Banco de dados leve e local, usado para armazenar o histórico das avaliações. |
| **Jinja2** | Motor de templates do Flask, responsável por exibir variáveis e lógica nos HTMLs. |

---

### 🚀 Como executar o sistema localmente

1. Instale os requisitos:
   ```bash
   pip install -r requirements.txt

2. Execute o sistema:
    python3 main.py

3. Acesse no navegador:
    http://localhost:5000