# Laboratório 9.3 e 9.4 — Flask e Nuvem

Engenharia de Software · Aplicação Flask publicada no Azure App Service (plano Free F1) com deploy
automático pelo GitHub Actions.

**Aplicação online:** <https://lab093-gmarinho-gqdyh8dmdae9c5c5.brazilsouth-01.azurewebsites.net>

## 9.3 — Hello World na nuvem

1. Aplicação "Hello World": commit `a5b4d70`, [`app.py` nessa versão](https://github.com/gabrielmarinhorosa/Lab_09.3_EngSoft/blob/a5b4d70/app.py).
2. Repositório no GitHub: este.
3. Ambiente no Azure App Service: Web App Linux, Python 3.14, plano F1 (gratuito), região Brazil South.
4. CI/CD: o Centro de Implantação do App Service criou o workflow
   [`.github/workflows/main_lab093-gmarinho.yml`](.github/workflows/main_lab093-gmarinho.yml). A cada push na
   `main`, ele instala as dependências, empacota e publica no App Service.
5. A página raiz responde `Hello, World!`.

## 9.4 — API RESTful com deploy automático

- a) [`app.py`](app.py): CRUD de itens em `/items`. A rota `/` do 9.3 continua no ar.
- b) O commit da API (`98a102d`) disparou o workflow e entrou no ar em cerca de 90 segundos, sem passo manual.
- c) [Coleção do Postman](https://go.postman.co/collection/52575572-1fe8ad46-8571-4fc3-a25c-6605956fde97)
  (cópia em [`postman/`](postman/lab_09_4_flask_azure.postman_collection.json)), já apontando para a URL da Azure.
  Rodada duas vezes contra a aplicação online: 14 requisições, 23 asserções, nenhuma falha.

| Método | Rota | Sucesso | Erros |
|---|---|---|---|
| GET | `/items` | 200 | |
| GET | `/items/{id}` | 200 | 404 |
| POST | `/items` | 201 | 400 |
| PUT | `/items/{id}` | 200 | 404, 400 |
| DELETE | `/items/{id}` | 200 | 404 |

Os itens ficam em memória. Por isso o [`gunicorn.conf.py`](gunicorn.conf.py) usa um único worker, e a lista
volta aos dois itens iniciais quando o App Service reinicia.

## Rodar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install Flask==3.1.3
python app.py
```

Depois acesse <http://127.0.0.1:5000/items>.
