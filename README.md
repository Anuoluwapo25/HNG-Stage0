# HNG12 Public API - Stage 0 Task

## Description
This Django REST API returns:
- Registered email
- Current datetime in ISO 8601 format
- GitHub repository URL

## API Endpoint
### GET `/`
#### Response
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}

##  🛠️Technology Stack
Backend: Django REST Framework (Python)
Deployment: Render
CORS Handling: Django CORS Headers
🚀 Live API URL
Base URL: 

Try it in your browser or via a tool like Postman:

curl -X GET https://your-app-name.onrender.com/

🏗️ Project Setup (Run Locally)
1️⃣ Clone the Repository

git clone https://github.com/Anuoluwapo25/HNG-Stage0
cd Hng-stage0

2️⃣ Create a Virtual Environment
python -m venv venv
Activate the virtual environment:
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start the Server
python manage.py runserver
Now, open http://127.0.0.1:8000/ in your browser.

🚀 Deployment Guide (Render)
1️⃣ Install Gunicorn
pip install gunicorn

2️⃣ Create requirements.txt
pip freeze > requirements.txt

3️⃣ Push to GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Anuoluwapo25/HNG-Stage0
git push -u origin main

4️⃣ Deploy on Render
Go to Render.
Create a New Web Service.
Connect your GitHub repository.
Set Start Command:

gunicorn hng12.wsgi:application
Deploy! 🚀

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

