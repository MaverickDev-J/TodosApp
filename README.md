# TodosApp (FastAPI)

A simple **Todo List** app built with **FastAPI**, using **PostgreSQL (Neon)** and deployed on **Render**.

- Live API: https://maverick-deploys.onrender.com
- Docs (Swagger): https://maverick-deploys.onrender.com/docs

---

## Tech

- **FastAPI** (Python)
- **PostgreSQL** (Neon)
- **Deployed on Render**

---

## Endpoints (Quick Map)

### Default

- `GET /` — Test
- `GET /healthy` — Health check

### Auth

- `GET /auth/login-page` — Login page
- `GET /auth/register-page` — Register page
- `POST /auth/` — Create user
- `POST /auth/token` — Login (access token)

### Todos

- `GET /todos/todo-page` — Todo page
- `GET /todos/add-todo-page` — Add todo page
- `GET /todos/edit-todo-page/{todo_id}` — Edit todo page
- `GET /todos/` — Read all todos
- `GET /todos/todo/{todo_id}` — Read todo
- `POST /todos/todo` — Create todo
- `PUT /todos/todo/{todo_id}` — Update todo
- `DELETE /todos/todo/{todo_id}` — Delete todo

### Admin

- `GET /admin/todo` — Read all todos
- `DELETE /admin/todo/{todo_id}` — Delete todo

### Users

- `GET /users/` — Get user
- `PUT /users/password/` — Change password
- `PUT /users/phonenumber/{phone_number}` — Change phone number

---

## Run Locally

```bash
git clone https://github.com/MaverickDev-J/TodosApp.git
cd TodosApp
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set your database connection (Neon) as an environment variable:

```bash
export DATABASE_URL="YOUR_NEON_POSTGRES_URL"
```

Start the server (adjust module path if your entrypoint differs):

```bash
uvicorn todos.main:app --reload --host 0.0.0.0 --port 8000
```

Then open: http://127.0.0.1:8000/docs

---

## Notes

- Keep secrets (like `DATABASE_URL`) in environment variables (Render dashboard for production).
- Hosted Postgres commonly requires SSL (Neon connection strings typically include it).
