# 🌾 Agri-Assist AI

### AI-Powered Smart Agriculture & Farmer Assistance Platform

**Agri-Assist AI** is a full-stack intelligent agriculture platform that combines **Artificial Intelligence, Machine Learning, Computer Vision, Retrieval-Augmented Generation (RAG), weather intelligence, and multilingual AI assistance** to provide farmers with practical, data-driven agricultural support.

The platform enables users to interact with an AI agricultural assistant, analyze crop/leaf images for disease detection, receive agriculture-focused recommendations, access weather information, and interact with the system in **English, Urdu, and Roman Urdu**.

---
<img width="1365" height="634" alt="image" src="https://github.com/user-attachments/assets/9b910e6f-6b77-4521-82dc-89ccfa431c71" />


## 🚀 Project Highlights

* 🤖 AI-powered agricultural chatbot
* 🧠 Google Gemini API integration
* 👁️ Gemini Vision for image-based AI assistance
* 🌿 AI-powered crop disease detection
* 🔬 TensorFlow + Keras + MobileNetV2
* 📚 Retrieval-Augmented Generation (RAG)
* 🔎 Agriculture knowledge-base retrieval
* 🗄️ PostgreSQL + pgvector
* 🌦️ Real-time weather information
* 📍 Browser-based geolocation
* 🌐 English, Urdu & Roman Urdu support
* 🔐 JWT-based authentication
* 🔒 bcrypt password hashing
* 📷 Camera and image-upload support
* 👨‍💼 Admin dashboard
* 📊 User and system management
* 🧾 Chat and disease-detection history
* ⚡ FastAPI high-performance backend
* 🎨 React + Material UI frontend
* 🐳 Docker-ready architecture
* ☁️ Cloud deployment support

---

# 🎯 Problem Statement

Agriculture depends heavily on timely decisions regarding:

* Crop diseases
* Pest problems
* Irrigation
* Fertilizers
* Crop management
* Weather conditions
* Plant health
* Agricultural practices

However, farmers may not always have immediate access to agricultural experts or reliable information.

**Agri-Assist AI addresses this problem by bringing multiple intelligent agricultural capabilities into a single digital platform.**

Instead of relying on separate tools, farmers can use one system for:

> **Ask → Analyze → Understand → Recommend → Act**

---

# 💡 Solution

Agri-Assist AI combines several AI and software technologies into one integrated ecosystem.

<img width="1363" height="628" alt="image" src="https://github.com/user-attachments/assets/b7648030-7e45-4725-8555-0df2b4861632" />
<img width="1335" height="643" alt="image" src="https://github.com/user-attachments/assets/76ad234b-ebfb-4ac9-9fca-cc384b52cc8d" />


### Farmer

↓

### React.js Web Application

↓

### FastAPI Backend

↓

### AI / ML / RAG / Weather Services

↓

### Intelligent Agricultural Response

The platform combines:

**Generative AI + Computer Vision + RAG + Weather Intelligence + Agricultural Knowledge**

to provide a more useful agriculture-focused assistant.

---

# ✨ Core Features

## 🤖 1. AI Agricultural Assistant

The platform provides an intelligent conversational assistant powered by **Google Gemini API**.

Users can ask agriculture-related questions such as:

* 🌱 Crop management
* 🦠 Crop diseases
* 🐛 Pest problems
* 💧 Irrigation
* 🌾 Fertilizers
* 🌤️ Weather-related guidance
* 🌿 Plant health
* 🚜 General agricultural practices

The assistant uses agriculture-focused prompting and knowledge retrieval to provide contextually relevant responses.

---
<img width="1139" height="641" alt="image" src="https://github.com/user-attachments/assets/b8aa5245-7a19-4f1d-8097-ae2dd602b29e" />
<img width="1134" height="640" alt="image" src="https://github.com/user-attachments/assets/b89ff46e-71bb-44dc-8035-a2cf12afe20f" />
<img width="1144" height="637" alt="image" src="https://github.com/user-attachments/assets/c058a84e-cbf6-491d-bf68-b824b014d3a1" />


# 🧠 2. Retrieval-Augmented Generation (RAG)

Agri-Assist AI implements a **Retrieval-Augmented Generation pipeline** to improve agricultural question answering.

### RAG Pipeline

```text
User Question
      │
      ▼
Query Processing
      │
      ▼
Embedding Generation
      │
      ▼
Vector Search
      │
      ▼
Agriculture Knowledge Base
      │
      ▼
Relevant Context
      │
      ▼
Gemini AI
      │
      ▼
Context-Aware Response
```

### RAG Components

* Agricultural knowledge documents
* Text extraction
* Text chunking
* Embeddings
* Vector similarity search
* PostgreSQL
* pgvector
* Gemini API
* Prompt engineering

The RAG system allows the AI assistant to retrieve relevant agricultural information before generating an answer.

---

# 🌿 3. Crop Disease Detection

Agri-Assist AI includes an image-based crop disease detection system.

Users can:

* 📷 Capture a crop/leaf image using the browser camera
* 📁 Upload an image from their device
* 🔬 Send the image for AI/ML analysis
* 🦠 Detect the associated crop disease
* 📖 Receive disease information
* 💡 Get basic management guidance

### Detection Pipeline

```text
Crop / Leaf Image
       │
       ▼
Image Upload / Camera
       │
       ▼
FastAPI Backend
       │
       ▼
Image Preprocessing
       │
       ▼
TensorFlow / Keras
       │
       ▼
MobileNetV2
       │
       ▼
Disease Prediction
       │
       ▼
Disease Information
       │
       ▼
Management Guidance
```

### Technologies

* TensorFlow
* Keras
* MobileNetV2
* NumPy
* Pillow

---

# 👁️ 4. Gemini Vision

The platform also integrates **Gemini Vision** for image-based AI interaction.

This enables the AI system to work with visual agricultural information and provide image-aware assistance.

### Example Flow

```text
User
 │
 ├── Text Question
 │
 └── Crop Image
        │
        ▼
   Gemini Vision
        │
        ▼
  AI Interpretation
        │
        ▼
Agricultural Guidance
```

---

# 🌦️ 5. Weather Intelligence

Agri-Assist AI integrates weather information using:

* OpenWeather API
* Browser Geolocation API

The user's browser can provide geographic coordinates, which are then used to retrieve weather information.

### Weather Flow

```text
Farmer Location
      │
      ▼
Geolocation API
      │
      ▼
Latitude / Longitude
      │
      ▼
OpenWeather API
      │
      ▼
Weather Information
      │
      ▼
Agri-Assist AI
```

Weather information can include:

* Temperature
* Humidity
* Weather conditions
* Location-based environmental information

---

# 🌐 6. Multilingual AI

Agri-Assist AI supports:

### 🇬🇧 English

### 🇵🇰 Urdu

### 🗣️ Roman Urdu

The multilingual system combines frontend language management with Gemini's multilingual generation capabilities and agriculture-focused knowledge.

This makes the platform more accessible to users who are more comfortable communicating in Urdu or Roman Urdu.

---

# 🔐 7. Authentication & Security

The application includes a complete authentication system.

### Authentication Features

* User registration
* User login
* Logout
* JWT authentication
* Protected routes
* Token management
* bcrypt password hashing
* Secure API communication
* Input validation

### Authentication Flow

```text
User
 │
 ▼
Register / Login
 │
 ▼
FastAPI
 │
 ▼
Password Verification
 │
 ▼
JWT Token
 │
 ▼
Authenticated Session
 │
 ▼
Protected Resources
```

Sensitive credentials and API keys are managed through environment variables rather than being hard-coded into the source code.

---

# 👨‍💼 8. Admin Dashboard

Agri-Assist AI includes an administrative interface for system management and monitoring.

### Admin Capabilities

* 👥 User management
* 💬 Chat monitoring
* 🌿 Disease detection records
* 📚 Knowledge-base management
* 📊 System statistics
* 🗂️ Application data management

The admin system provides centralized control over important application operations.

---

# 📷 9. Image Handling

The platform supports multiple methods for obtaining agricultural images.

### Camera

The **Browser Camera API** allows users to capture crop or leaf images directly from supported devices.

### File Upload

Users can also upload images from:

* Computer
* Mobile device
* Gallery
* Local storage

### Processing Stack

```text
Browser Camera / File Upload
          │
          ▼
     Multipart Upload
          │
          ▼
       FastAPI
          │
          ▼
        Pillow
          │
          ▼
      NumPy / ML
          │
          ▼
 TensorFlow / MobileNetV2
```

---

# 🏗️ System Architecture

```text
                         ┌───────────────────────┐
                         │         FARMER        │
                         │         USER          │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │      React.js         │
                         │      Frontend         │
                         │                       │
                         │ JavaScript + MUI      │
                         │ React Router          │
                         │ Axios                 │
                         └───────────┬───────────┘
                                     │
                              REST API / Axios
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │       FastAPI         │
                         │       Backend         │
                         │        Python         │
                         └───────────┬───────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
       ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
       │ Gemini API   │      │ TensorFlow   │      │ OpenWeather  │
       │              │      │ Keras        │      │ API          │
       │ Gemini       │      │ MobileNetV2  │      │              │
       │ Vision       │      │              │      │ Weather      │
       └──────┬───────┘      └──────┬───────┘      └──────────────┘
              │                     │
              │                     │
              ▼                     ▼
       ┌─────────────────────────────────────┐
       │       Agriculture Intelligence      │
       │                                     │
       │  RAG + Knowledge Base + Embeddings  │
       │              + pgvector              │
       └──────────────────┬──────────────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    PostgreSQL      │
                │                    │
                │ Users              │
                │ Profiles           │
                │ Chat History       │
                │ Detection History  │
                │ Preferences        │
                │ Vector Data        │
                └────────────────────┘
```

---

# 🛠️ Technology Stack

## Frontend

| Technology         | Purpose                 |
| ------------------ | ----------------------- |
| React.js           | Frontend framework      |
| JavaScript         | Application programming |
| HTML5              | Web structure           |
| CSS3               | Styling                 |
| Material UI        | UI components           |
| React Router       | Client-side navigation  |
| Axios              | API communication       |
| React Context API  | State management        |
| Browser Camera API | Crop image capture      |
| File Upload API    | Image uploading         |
| Geolocation API    | User location           |
| Local Storage      | Local session/settings  |

---

## Backend

| Technology       | Purpose                    |
| ---------------- | -------------------------- |
| Python           | Backend programming        |
| FastAPI          | REST API framework         |
| Uvicorn          | ASGI server                |
| Pydantic         | Data validation            |
| SQLAlchemy       | ORM                        |
| JWT              | Authentication             |
| bcrypt           | Password hashing           |
| Multipart Upload | File handling              |
| CORS             | Cross-origin communication |

---

## Artificial Intelligence

| Technology         | Purpose                     |
| ------------------ | --------------------------- |
| Google Gemini API  | Generative AI               |
| Gemini Vision      | Image-aware AI              |
| Prompt Engineering | AI response optimization    |
| TensorFlow         | Machine learning framework  |
| Keras              | Deep learning API           |
| MobileNetV2        | Crop disease classification |
| NumPy              | Numerical processing        |
| Pillow             | Image processing            |

---

## RAG & Knowledge Base

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| Agriculture Documents | Knowledge source           |
| Text Extraction       | Document processing        |
| Text Chunking         | Knowledge preparation      |
| Embeddings            | Semantic representation    |
| Vector Search         | Relevant context retrieval |
| pgvector              | Vector similarity search   |
| PostgreSQL            | Persistent storage         |
| Gemini                | Response generation        |

---

## Database

### PostgreSQL

Used for persistent application data including:

* Users
* Farmer profiles
* Chat history
* Disease detection history
* Uploaded image information
* Weather/search history
* User preferences
* Vector embeddings

### SQLAlchemy

Used as the application's Object-Relational Mapping layer.

### pgvector

Used for vector storage and similarity search within PostgreSQL.

---

# 📊 Data Flow

The overall application flow can be represented as:

```text
                    USER
                      │
                      ▼
              React.js Frontend
                      │
                      ▼
                Axios / REST
                      │
                      ▼
               FastAPI Backend
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
      Gemini       TensorFlow    OpenWeather
        │             │             │
        ▼             ▼             ▼
       AI           Disease       Weather
    Assistant      Detection     Information
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
               RAG Knowledge Base
                      │
                      ▼
                pgvector Search
                      │
                      ▼
                 PostgreSQL
                      │
                      ▼
              Intelligent Response
                      │
                      ▼
                     USER
```

---

# 📁 Project Structure

A professional modular structure is used to separate frontend, backend, AI, data, and configuration components.

```text
Agri-Assist-AI/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── ...
│
├── backend/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── auth/
│   └── ...
│
├── ai/
│   ├── chatbot/
│   ├── rag/
│   ├── disease_detection/
│   └── ...
│
├── data/
│   └── agriculture/
│
├── tests/
│
├── .gitignore
├── requirements.txt
├── package.json
├── Dockerfile
└── README.md
```

> The exact folder structure may vary slightly depending on the implementation and deployment configuration.

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Astreonix/Agri-Assist-AI.git
```

```bash
cd Agri-Assist-AI
```

---

# 🐍 Backend Setup

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

# ⚛️ Frontend Setup

Install Node.js dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

---

# 🔑 Environment Configuration

Create a local `.env` file containing the required configuration.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key

DATABASE_URL=your_postgresql_connection_string

JWT_SECRET_KEY=your_secret_key
```

### ⚠️ Security Notice

**Never commit `.env` files or API keys to GitHub.**

The `.gitignore` should contain:

```gitignore
.env
.env.*
venv/
.venv/
node_modules/
__pycache__/
```

---

# 🗄️ Database Setup

Agri-Assist AI uses:

```text
PostgreSQL
     +
pgvector
     +
SQLAlchemy
```

The database stores both application information and vector representations used by the RAG pipeline.

Typical database entities include:

```text
Users
Profiles
Chat Sessions
Chat Messages
Disease Detection Records
Uploaded Images
Weather History
User Preferences
Knowledge Documents
Vector Embeddings
```

---

# 🔌 API Architecture

The FastAPI backend exposes REST APIs for communication between the frontend and intelligent services.

Major API categories include:

```text
Authentication
     │
     ├── Register
     ├── Login
     └── Logout

AI Assistant
     │
     ├── Chat
     └── RAG-based Questions

Disease Detection
     │
     ├── Image Upload
     └── Disease Prediction

Weather
     │
     └── Location-based Weather

User
     │
     ├── Profile
     └── Preferences

Admin
     │
     ├── Users
     ├── Records
     └── Statistics
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API documentation through:

### Swagger UI

```text
/docs
```

### OpenAPI

```text
/openapi.json
```

Swagger can be used to test and inspect backend endpoints during development.

---

# 🧪 Testing

The project supports API and application testing using tools such as:

* Postman
* Swagger UI
* Automated testing frameworks
* Backend integration testing

API endpoints can be tested independently before integrating them with the frontend.

---

# 🐳 Docker

The application is designed with containerization in mind.

Docker can be used to package application services and provide a consistent deployment environment.

Typical architecture:

```text
Docker
 │
 ├── Frontend
 │
 ├── Backend
 │
 └── Supporting Services
```

---

# ☁️ Deployment Architecture

The application supports a cloud-oriented deployment architecture.

```text
                  Internet
                     │
                     ▼
              ┌──────────────┐
              │   Vercel     │
              │   Frontend   │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │    Render    │
              │   FastAPI    │
              │   Backend    │
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      PostgreSQL   Gemini    OpenWeather
       + pgvector     API        API
```

### Deployment Technologies

**Frontend**

* Vercel

**Backend**

* Render

**Database**

* Cloud PostgreSQL

**Containerization**

* Docker

---

# 🔒 Security Architecture

Security is considered throughout the application.

### Authentication

```text
JWT Authentication
        +
Protected Routes
```

### Password Security

```text
User Password
      │
      ▼
    bcrypt
      │
      ▼
Hashed Password
      │
      ▼
   Database
```

### API Security

* Environment-based secrets
* JWT authentication
* Password hashing
* CORS configuration
* Input validation
* Protected API endpoints
* Secure configuration management

---

# 📱 User Experience

The frontend is designed around a simple agricultural workflow.

```text
┌─────────────────────────────┐
│       Agri-Assist AI        │
├─────────────────────────────┤
│                             │
│  🤖 Ask AI                  │
│                             │
│  🌿 Detect Disease          │
│                             │
│  🌦️ Weather                │
│                             │
│  📚 Agricultural Knowledge  │
│                             │
│  👤 Profile                 │
│                             │
└─────────────────────────────┘
```

The interface uses **Material UI** to provide a modern and responsive user experience.

---

# 🌍 Why Agri-Assist AI?

Traditional agricultural applications often focus on a single function.

Agri-Assist AI combines multiple intelligent capabilities:

```text
                 AGROTECH
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
      AI           ML           RAG
       │            │            │
       ▼            ▼            ▼
   Chatbot     Disease AI    Knowledge
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
                Weather
                    │
                    ▼
              Smart Assistance
```

This creates a unified agriculture intelligence platform instead of a collection of disconnected tools.

---

# 🎓 Technologies Demonstrated

This project demonstrates practical implementation of:

* Full-stack web development
* React.js
* REST API architecture
* FastAPI
* Database design
* PostgreSQL
* SQLAlchemy
* JWT authentication
* Secure password hashing
* Generative AI
* Prompt engineering
* Computer Vision
* Deep Learning
* TensorFlow
* Keras
* Transfer learning
* MobileNetV2
* Retrieval-Augmented Generation
* Vector databases
* Embeddings
* pgvector
* Multilingual AI
* External API integration
* Geolocation
* Image processing
* Cloud deployment
* Docker
* Git/GitHub

---

# 📈 Future Expansion

Although the current platform is fully functional, the architecture provides room for future expansion, including:

* 📡 IoT-based farm monitoring
* 🌡️ Sensor integration
* 🛰️ Satellite imagery analysis
* 📊 Advanced crop analytics
* 🌾 Yield prediction
* 💰 Market-price intelligence
* 🚜 Precision agriculture
* 📱 Dedicated mobile applications
* 🧠 Additional specialized ML models
* 🌍 Regional agricultural datasets
* 🔔 Smart agricultural alerts

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

### Contribution Workflow

```bash
git clone <repository>
```

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Make your changes and commit:

```bash
git add .
git commit -m "Add: your feature"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Then create a Pull Request.

---

# 👥 Contributors

## Project Owner

### Astreonix

**Project:** Agri-Assist AI

The project is developed as a full-stack AI-powered smart agriculture solution combining software engineering, artificial intelligence, machine learning, and data-driven agriculture.

Additional contributors are recognized through their GitHub contributions.

---

# 📜 License

This project should be distributed according to the license included in this repository.

If no license file currently exists, add an appropriate open-source or proprietary license before allowing external reuse.

---

# 🌱 Vision

> **Empowering farmers with Artificial Intelligence, Machine Learning, and accessible digital agriculture.**

Agri-Assist AI aims to demonstrate how modern AI technologies can be applied to real-world agricultural challenges.

The project brings together:

```text
Artificial Intelligence
        +
Machine Learning
        +
Computer Vision
        +
RAG
        +
Data
        +
Weather Intelligence
        +
Modern Web Engineering
        │
        ▼
   AGRI-ASSIST AI
```

---

# ⭐ Project

**Agri-Assist AI**

### Built with

**React.js • FastAPI • Python • PostgreSQL • pgvector • Gemini AI • TensorFlow • Keras • MobileNetV2 • RAG • OpenWeather • Material UI • Docker**

---

## 🌾 Agri-Assist AI

### *Smart Agriculture. Intelligent Assistance. Better Decisions.*
