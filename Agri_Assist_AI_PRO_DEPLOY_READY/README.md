# 🌱 Agri Assist AI — Complete Starter

This repository contains a working full-stack starter for the project in your document:
Responsive web frontend + FastAPI backend + JWT login + SQLite/PostgreSQL-ready database +
Gemini AI + local RAG-style knowledge retrieval + OpenWeather + disease-model training +
fertilizer guidance + farmer profile.

## 1. Backend

Windows PowerShell:
```powershell
cd Agri_Assist_AI_PRO_DEPLOY_READY
cd backend
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Put your keys in `backend/.env`:
```env
GEMINI_API_KEY=YOUR_GEMINI_KEY
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_KEY
SECRET_KEY=YOUR_LONG_RANDOM_SECRET
```

The local `backend/.env` file is the key configuration space. Keep Gemini and OpenWeather keys there only; never put provider keys in React or `frontend/.env`.

Run:
```powershell
uvicorn app.main:app --reload --port 8000
```

Open:
`http://127.0.0.1:8000/docs`

Set `ADMIN_EMAIL` in `backend/.env` to the registered email that should access the admin dashboard. Admin routes are protected at the API layer.

## 2. React Website

```powershell
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal, usually `http://127.0.0.1:5173`.
The app uses `VITE_API_BASE_URL`, defaulting to `http://127.0.0.1:8000/api`.

For production:
```powershell
npm run build
npm run preview
```

Set `VITE_API_BASE_URL=https://YOUR-SERVICE.onrender.com/api` in `frontend/.env.production` before building.

## 3. Disease model

The app does not fake a disease prediction. Obtain a PlantVillage-style dataset and arrange:
```text
dataset/
  Class_A/
  Class_B/
  ...
```

Install TensorFlow:
```powershell
pip install -r backend/requirements-ml.txt
```

Download and export the PlantVillage dataset into class folders:
```powershell
python backend/ml/download_plantvillage.py --output_dir dataset
```

Train:
```powershell
python backend/ml/train.py --data_dir dataset
```

The trained files are:
```text
backend/ml_model/crop_disease.keras
backend/ml_model/classes.txt
```

The classifier uses transfer learning with TensorFlow/Keras MobileNetV2. Validation metrics are printed after training. If no local model is present, the API can use Gemini Vision when `GEMINI_API_KEY` is configured.

RAG uses chunked agriculture documents, vector embeddings, similarity search, and Gemini prompt context with source filenames. Set `VECTOR_STORE=local` for the built-in TF-IDF index or `VECTOR_STORE=chroma` after installing `backend/requirements-vector.txt`; use PostgreSQL plus pgvector for production scale.

## 4. Core API endpoints

POST /api/auth/register
POST /api/auth/login
GET  /api/profile
PUT  /api/profile
POST /api/chat
GET  /api/chat/history
GET  /api/weather?lat=...&lon=...
POST /api/disease/analyze
POST /api/fertilizer/recommend
GET  /api/crops
POST /api/crops/advice
GET  /api/admin/stats
GET  /api/admin/users
GET  /api/admin/chats
GET  /api/admin/disease-records
GET  /api/admin/knowledge
PUT  /api/admin/knowledge/{filename}

## 5. Final FYP upgrades

Add a proper vector DB (FAISS/pgvector + sentence-transformers), admin dashboard,
source citations in answers, refresh tokens, email verification/password reset,
cloud image storage, HTTPS, rate limiting, automated tests, model evaluation,
and agriculture-expert validation before presenting recommendations as authoritative.

Never put API keys in the website. Keep them in the backend `.env`.

The admin dashboard is available at `/admin` for the configured `ADMIN_EMAIL` account. Swagger UI is available at `/docs`, and the OpenAPI schema is available at `/openapi.json`.


## Complete deployment
Read `DEPLOYMENT_GUIDE.md` for the full zero-to-deployment procedure and `API_TESTING.md` for endpoint testing.
