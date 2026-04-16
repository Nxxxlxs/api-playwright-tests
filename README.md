# 🚀 API Test Automation

Repositório de automação de testes de API utilizando Python, pytest, Playwright e Allure Reports.

---

## 🧠 Stack do projeto

- Python 3.14
- uv (gerenciador de dependências)
- pytest (engine de testes)
- Playwright (API testing)
- Allure Reports (relatórios visuais)

---

## 📁 Estrutura do projeto

 | src/
 |	└──api/
 |		└── clients/
 |		 |	└── base_client.py |
 |		 |	└── users_client.py
 |		└── utils/
 |			└── allure_helpers.py
 | tests/
 |	└── api/
 |	 |	└──test_users.py
 |	 |
 |	 |
 |	 |── config.py
 | 	└── conftest.py
 | pyproject.toml
 | uv.lock
 | .python-version

---

## ⚙️ Pré-requisitos

- Python 3.14
- uv instalado

Instalar uv:

Linux/macOS:
curl -Ls https://astral.sh/uv/install.sh | sh

Windows (PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

---

## 📦 Instalação

git clone `<url-do-repo>`
cd api-playwright-tests

uv sync

---

## 🌐 Instalar Playwright

uv run playwright install

---

## ▶️ Executar testes

uv run pytest

Modo verboso:
uv run pytest -v

---

## 📊 Allure Reports

Gerar dados:
uv run pytest

Abrir relatório:
allure serve allure-results

---

## 🧹 Limpeza automática

Ignorados pelo git:

- .venv/
- allure-results/
- .pytest_cache/
- playwright-report/

---

## 🧪 Exemplo de teste

def test_list_users(users):
    response = users.list_users()
    assert response.ok

---

## 🧱 Arquitetura

Clients → lógica de API
Tests → validações
conftest.py → injeção de dependências
utils → helpers (Allure, logs)

---

## ⚙️ Config pytest (pyproject.toml)

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--alluredir=allure-results --clean-alluredir"
python_files = "test_*.py"

---

## 🐍 Python

.python-version define a versão do Python
requires-python = "3.14"

---

## 🚀 Comandos principais

uv add `<pacote>`
uv sync
uv run pytest
uv run playwright install

---

## 📌 Boas práticas

- não commitar .venv
- não commitar allure-results
- não commitar .pytest_cache
- usar sempre uv run
- separar clients, tests e utils


---

## 📄 Licença

Projeto interno de automação de testes
