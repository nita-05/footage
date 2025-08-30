# 🎬 Footage Flow - AI Video Story Tool

Transform your videos into compelling stories with AI-powered scene generation, emotional analysis, and intelligent tagging.

## ✨ Features

- **🎥 AI Video Processing**: Upload videos and automatically extract audio, frames, and metadata
- **🔍 AI Tagging**: Visual elements are tagged using AI for better organization and search
- **📝 Smart Transcription**: Speech-to-text with word-level timestamps
- **📖 AI Story Generation**: Transform your video into compelling stories with AI-powered scene generation
- **🎭 Inspirational Storytelling**: The tool helps users relive and share uplifting life stories
- **📊 Emotional Journey Option**: Optionally, it can create contrasting stories showing good vs. bad choices
- **🎬 Video Rendering**: Create custom video clips with transitions and effects
- **🔍 Advanced Search**: Search through video content with timestamp-based navigation

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/)
- **FFmpeg** - [Download FFmpeg](https://ffmpeg.org/download.html)

### Simple Setup (3 Steps)

```bash
# 1. Install Python dependencies (with dependency fix)
python install_dependencies.py

# 2. Install frontend dependencies
cd frontend && npm install && cd ..

# 3. Start the application
python start_footage_flow.py
```

### Troubleshooting Dependencies

If you encounter dependency issues (especially NumPy/OpenCV compatibility):

```bash
# Check current dependency status
python check_dependencies.py

# Fix dependency issues
python fix_dependencies.py

# Or do a complete fresh installation
python install_dependencies.py
```



Create a `.env` file in the root directory:

```env
# Google AI API Key (Required)
GEMINI_API_KEY=your_actual_api_key_here

# Backend Configuration
FLASK_ENV=development
FLASK_DEBUG=true
PORT=5000

# Frontend Configuration
VITE_BACKEND_URL=http://localhost:5000
```

#### 4. FFmpeg Installation

**Windows:**
```bash
# Run the automatic installer
python install_ffmpeg.py

# Or manually:
# 1. Download from https://ffmpeg.org/download.html
# 2. Extract to C:\ffmpeg
# 3. Add C:\ffmpeg\bin to PATH
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## 🏃‍♂️ Running the Application

### Option 1: Run Everything Together (Recommended)

```bash
python start_footage_flow.py
```

This will start both backend and frontend servers automatically.

### Option 2: Run Separately

**Backend Only:**
```bash
python start_backend.py
# Backend runs on http://localhost:5000
```

**Frontend Only:**
```bash
python start_frontend.py
# Frontend runs on http://localhost:5173
```

## 🌐 Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000
- **Dashboard**: http://localhost:5173/dashboard

## 🔑 API Keys Setup

### 1. Google Gemini AI (Required)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 2. Features (All Powered by Gemini AI)

The application now works with **only your Gemini API key**:

- **AI Story Generation**: Powered by Google Gemini AI ✅
- **AI Transcription**: Powered by Google Gemini AI ✅
- **AI Visual Tagging**: Powered by Google Gemini AI ✅
- **AI Text Tagging**: Powered by Google Gemini AI ✅
- **Video Processing**: Uses FFmpeg ✅
- **Google Account Login**: Uses Google OAuth (no additional setup needed) ✅

**Note**: All AI features use Gemini API, and Google login works automatically!

## 📁 Project Structure

```
Ai--video--story-main/
├── backend/                 # Flask backend server
│   ├── app.py              # Main Flask application
│   ├── transcribe.py       # Audio transcription service
│   ├── tagging.py          # AI visual tagging service
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend application
│   ├── src/                # Source code
│   ├── package.json        # Node.js dependencies
│   └── vite.config.js      # Vite configuration
├── uploads/                # User uploaded files
├── start_footage_flow.py   # Main startup script
├── start_backend.py        # Backend-only startup
├── start_frontend.py       # Frontend-only startup
├── install_ffmpeg.py       # FFmpeg installer (Windows)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. "FFmpeg not found" Error
```bash
# Windows: Run the installer
python install_ffmpeg.py

# Or add to PATH manually
# Add C:\ffmpeg\bin to your system PATH
```

#### 2. "Module not found" Errors
```bash
# Ensure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

#### 3. Frontend Build Errors
```bash
# Clear node modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
```

#### 4. Port Already in Use
```bash
# Kill processes using ports 5000 or 5173
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

### Performance Issues

- **Large Videos**: The tool works best with videos under 100MB
- **Memory Usage**: Ensure you have at least 4GB RAM available
- **Processing Time**: Complex videos may take several minutes to process

## 🔧 Development

### Backend Development

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run in development mode
cd backend
python app.py
```

### Frontend Development

```bash
cd frontend
npm run dev
```

### Database Management

```bash
# Reset database
rm ai_video_story.db
python -c "from backend.app import init_database; init_database()"
```

## 📊 API Endpoints

- `POST /upload` - Upload video file
- `POST /transcribe` - Transcribe video audio
- `POST /tag` - Generate AI tags for video
- `POST /generate-story` - Generate AI story from video
- `POST /render-story` - Render video with story scenes
- `GET /search` - Search video content
- `GET /videos` - Get all videos
- `GET /video/<id>` - Get specific video

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Review the logs in the terminal
3. Ensure all dependencies are properly installed
4. Verify your API keys are correct

## 🎯 System Requirements

- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8+
- **Node.js**: 16+
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Network**: Internet connection for AI services

---

**Made with ❤️ for content creators and storytellers**
