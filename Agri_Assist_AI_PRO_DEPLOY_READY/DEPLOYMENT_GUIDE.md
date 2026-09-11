# 🌱 Agri Assist AI — From Zero to Deployment

## 1. What you are building

A web-based AI agriculture workspace with:
- Login/Register
- Farmer profile
- AI agriculture chat
- English/Urdu/Roman Urdu
- Agriculture knowledge retrieval
- Crop disease image analysis
- Fertilizer guidance
- Weather integration
- Crop management advice
- Chat history
- Backend API
- Database
 - Production deployment

## 2. Technology stack

Frontend:
- React.js + JavaScript
- HTML5 + CSS3
- Material UI
- React Router
- Axios
- React Context API
- Browser Geolocation API
- Browser Camera API and file upload
- Local storage for JWT sessions

Backend:
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- JWT
- SQLite for local development
- PostgreSQL for production

AI:
- Gemini API
- Gemini vision fallback for leaf analysis
- Optional MobileNetV2/TensorFlow disease classifier
- RAG-style local agriculture knowledge base

External APIs:
- Gemini
- OpenWeather

Deployment:
- Render Docker Web Service for the backend
- Any static web host for the frontend
- PostgreSQL provider such as Neon/Supabase/Render Postgres

Admin dashboard:
- Configure `ADMIN_EMAIL` in Render environment variables.
- Register that email through the normal website registration flow.
- Open `/admin` after login.

## 3. Local backend setup — Windows

cd backend
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env

Edit `.env`:
GEMINI_API_KEY=...
OPENWEATHER_API_KEY=...
SECRET_KEY=...
GEMINI_MODEL=...

All provider keys belong in `backend/.env`. The React frontend only receives the backend URL through `VITE_API_BASE_URL`; it never receives Gemini or OpenWeather secrets.

Run:
uvicorn app.main:app --reload --port 8000

API docs:
http://127.0.0.1:8000/docs

## 4. React website setup

Open a terminal in `frontend`:
cd frontend
npm install
npm run dev

Open the Vite URL shown in the terminal. The backend URL is configured with `VITE_API_BASE_URL`.

## 5. Deploy the website

Build the React app:
```powershell
cd frontend
$env:VITE_API_BASE_URL="https://YOUR-SERVICE.onrender.com/api"
npm run build
```

Deploy the generated `frontend/dist` folder to Vercel or another static host.

## 6. Disease detection

Two modes are included:

A) Gemini vision fallback:
- Works with the Gemini API key.
- No TensorFlow model is required.
- It returns a possible assessment and symptoms.
- It must not be presented as a confirmed medical/agricultural diagnosis.

B) Local MobileNetV2:
- Train on a properly licensed dataset.
- PlantVillage can be downloaded/exported with `python backend/ml/download_plantvillage.py --output_dir dataset` after installing `backend/requirements-ml.txt`.
- Put dataset in class folders.
- Install the optional training dependency: `pip install -r backend/requirements-ml.txt`.
- Run:
  python backend/ml/train.py --data_dir dataset
- Copy resulting `crop_disease.keras` and `classes.txt` into `backend/ml_model/`.
- The API automatically uses the local model first.

The RAG pipeline supports the built-in local TF-IDF vector index or ChromaDB persistence with `VECTOR_STORE=chroma` after installing `backend/requirements-vector.txt`. For production, configure PostgreSQL with pgvector and migrate the same chunk/source contract to that store.

## 7. Production database

Do not use SQLite as the permanent database on a cloud web service.

Create a PostgreSQL database with your provider. Copy its connection string into Render:
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST/DBNAME

The SQLAlchemy models will create tables when the backend starts.

## 8. Deploy backend to Render

1. Push this project to GitHub.
2. Create a Render account.
3. Create a PostgreSQL database or use another PostgreSQL provider.
4. Create a Web Service from the GitHub repository.
5. Select Docker.
6. Root directory: `backend`.
7. Render can also use the included `render.yaml`.
8. Add secret environment variables:
   GEMINI_API_KEY
   OPENWEATHER_API_KEY
   DATABASE_URL
   SECRET_KEY
9. Deploy.
10. Open:
    https://YOUR-SERVICE.onrender.com/health
11. Then:
    https://YOUR-SERVICE.onrender.com/docs

The same deployment exposes `/openapi.json` for Postman import. Use the Swagger UI Authorize button with a bearer token.

## 9. Connect the website to the deployed backend

Set the Vercel environment variable `VITE_API_BASE_URL` to:
`https://YOUR-SERVICE.onrender.com/api`

Use `frontend` as the Vercel project root and `npm run build` as the build command.

## 10. GitHub

Never commit:
- `.env`
- API keys
- database files
- private uploads
- model files if they are too large

The root `.gitignore` already excludes secrets and common generated files.

## 11. Recommended Git commands

git init
git add .
git commit -m "Initial Agri Assist AI project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY
git push -u origin main

## 12. FYP demo flow

1. Register farmer.
2. Login.
3. Complete farmer profile.
4. Ask AI:
   "My wheat leaves are yellow. What should I check?"
5. Show English/Urdu/Roman Urdu capability.
6. Open Disease Detection.
7. Upload/photograph leaf.
8. Show possible disease assessment.
9. Open Weather.
10. Show location-based weather.
11. Open Fertilizer Guidance.
12. Enter crop, growth stage and soil.
13. Show generated guidance.
14. Explain that exact chemical/fertilizer rates require local label/soil-test/extension validation.

## 13. FYP architecture

Farmer
  ↓
Browser Web App
  ↓ HTTPS REST API
FastAPI Backend
  ├── JWT Authentication
  ├── Farmer Profile
  ├── Chat Service
  │    ├── Knowledge Retrieval
  │    └── Gemini
  ├── Disease Service
  │    ├── MobileNetV2 (optional trained model)
  │    └── Gemini Vision fallback
  ├── Weather Service → OpenWeather
  ├── Fertilizer Service → Gemini + knowledge
  └── Crop Advice → RAG + Gemini
  ↓
PostgreSQL

## 14. Security checklist

- Use HTTPS in production.
- Keep API keys only in backend environment variables.
- Use a long random SECRET_KEY.
- Add rate limiting before public launch.
- Validate image size and file type.
- Add password reset/email verification for production.
- Add CORS restrictions instead of `*` when domain/app setup is finalized.
- Do not expose database credentials to the website.
- Do not claim AI disease output is 100% accurate.

## 15. Future professional upgrades

- FAISS or pgvector for true vector RAG
- Embeddings + chunking + source citations
- Admin dashboard
- Farmer history/analytics
- Push notifications
- Weather forecast and disease-risk alerts
- Offline cache
- Expert verification workflow
- Model confusion matrix and explainability
- Automated tests
- CI/CD
- Cloud object storage for images
- PostgreSQL migrations with Alembic
