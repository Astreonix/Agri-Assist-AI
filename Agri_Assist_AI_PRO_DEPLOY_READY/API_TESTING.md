# API Testing Quick Reference

Base URL local:
http://127.0.0.1:8000

1. Register
POST /api/auth/register
{
  "name": "Ali",
  "email": "ali@example.com",
  "password": "12345678",
  "phone": "03001234567"
}

2. Login
POST /api/auth/login
{
  "email": "ali@example.com",
  "password": "12345678"
}

Copy access_token and use:
Authorization: Bearer TOKEN

3. Profile
GET /api/profile

4. AI Chat
POST /api/chat
{
  "message": "How often should I monitor wheat for pests?",
  "language": "English"
}

5. Fertilizer
POST /api/fertilizer/recommend
{
  "crop": "Wheat",
  "growth_stage": "Vegetative",
  "soil_type": "Loam",
  "farm_size": 2
}

6. Weather
GET /api/weather?lat=31.5204&lon=74.3587

7. Crops
GET /api/crops
Response:
{
  "crops": ["Wheat", "Rice", "Cotton", "Maize", "Tomato", "Potato", "Chili"]
}

8. Crop advice
POST /api/crops/advice
{
  "crop": "Tomato",
  "topic": "irrigation",
  "growth_stage": "flowering",
  "soil_type": "loam"
}

9. Disease
POST /api/disease/analyze
Multipart form:
file = leaf image
