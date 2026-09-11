# Agri Assist AI — First Run

## A. Backend
1. Open PowerShell in the repository root, then enter `backend`.
2. Create venv:
   `python -m venv venv`
3. Activate:
   `venv\\Scripts\\Activate.ps1`
4. Install:
   `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`.
6. Put your Gemini key in `GEMINI_API_KEY`.
7. Put your OpenWeather key in `OPENWEATHER_API_KEY`.
8. Start:
   `uvicorn app.main:app --reload --port 8000`
9. Test `http://127.0.0.1:8000/docs`.

## B. Website
1. Open a second PowerShell window in `frontend`.
2. Install frontend packages: `npm install`.
3. Start React: `npm run dev`.
4. Open the Vite URL, normally `http://127.0.0.1:5173`.
5. Register a new account.
6. Open Ask AI and send a question.

## C. If using another device
Set `VITE_API_BASE_URL` in `frontend/.env.local` from
`http://127.0.0.1:8000/api` to `http://YOUR_SERVER_IP:8000/api`.

For production, use the HTTPS backend URL instead.

## D. Disease detection
The API is ready, but a real trained model is required.
Install the ML and TensorFlow Datasets tools:
`pip install -r backend/requirements-ml.txt`

Download and export PlantVillage into class folders:
`python backend/ml/download_plantvillage.py --output_dir dataset`

Then train:
`python backend/ml/train.py --data_dir dataset`

Install the optional local model training dependency first:
`pip install -r backend/requirements-ml.txt`

Do not claim a disease prediction in the FYP demo until the model has been trained and evaluated.

The agriculture RAG pipeline chunks the knowledge files, builds TF-IDF vector embeddings, persists a local vector index, retrieves the most relevant chunks, and passes them to Gemini with source filenames.

## E. What is already implemented
- Login/register
- JWT authentication
- Farmer profile
- AI chat
- agriculture knowledge retrieval
- weather API integration
- image upload endpoint
- disease model inference endpoint
- disease model training script
- fertilizer guidance
- crop advice
- chat history endpoint
- Web UI for the main modules

## F. What must be obtained by the team
- Gemini API key
- OpenWeather API key
- PlantVillage or another properly licensed disease dataset
- final agriculture reference documents
- optional cloud image storage
- optional PostgreSQL production database
