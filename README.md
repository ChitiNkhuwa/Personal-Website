# Personal Portfolio Website

A Streamlit-based portfolio website showcasing projects, skills, education, and contact information.

## Local Development

### Prerequisites
- Python 3.7 or higher
- pip

### Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd Personal-Website
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

4. Open your browser to `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free & Easy)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app" and select this repository
5. Set the main file path to `streamlit_app.py`
6. Click "Deploy"

Your app will be live at: `https://your-app-name.streamlit.app`

### Option 2: AWS EC2

1. Launch an EC2 instance (Ubuntu recommended)
2. SSH into the instance
3. Install Python and dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install -r requirements.txt
   pip3 install streamlit
   ```
4. Upload your files to the server
5. Run the app:
   ```bash
   streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
   ```
6. Configure security group to allow port 8501

### Option 3: Heroku

1. Create a `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Install Heroku CLI
3. Login: `heroku login`
4. Create app: `heroku create your-app-name`
5. Deploy: `git push heroku main`
6. Visit: `https://your-app-name.herokuapp.com`

### Option 4: Docker

1. Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. Build and run:
   ```bash
   docker build -t portfolio-app .
   docker run -p 8501:8501 portfolio-app
   ```

## Assets

Place your headshot image at `assets/headshot.jpg` to display your photo on the homepage. The app will work without it, but the image section will be empty.

## Customization

Edit `streamlit_app.py` to customize:
- Personal information and bio
- Project descriptions and links
- Skills and expertise
- Education and certifications
- Contact form behavior

## License

MIT

