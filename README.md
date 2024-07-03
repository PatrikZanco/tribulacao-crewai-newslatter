# Objetivo
Automação diária de emails de newslatter sobre crypto

## sobre o projeto
Criar uma aplicação de agentes com IA para fazer pesquisas na web e trazer os principais tópicos sobre as movimentações no mercado cripto e gerar um markdown com a resposta.

## Configuração

```
python3 -m venv .venv
souce .venv/bin/activate
criar o arquivo ".env" e adicionar as chaves de api
pip install -r requirements.txt

```

```
poetry config virtualenvs.in-project true
poetry run newslatter_crypto


```
