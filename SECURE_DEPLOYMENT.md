# 🔐 SECURE DEPLOYMENT GUIDE

## ⚠️ IMPORTANT: API Keys for Deployment

**Your API keys have been secured and removed from the repository. Use these keys ONLY in your deployment platform environment variables.**

## 🔑 Your API Keys (For Deployment Only)

### Google OAuth
- **GOOGLE_CLIENT_ID:** `724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com`
- **GOOGLE_CLIENT_SECRET:** `a1654bf6b8d952823796bc1401c8171abd3d691404738a39ce1bf2c4996d7f3d`

### Gemini AI
- **GEMINI_API_KEY:** `AIzaSyCGON4hUzN2oHJAEOzSTSmFdXVs_UHFCNs`

## 🚀 Deployment Instructions

### Backend Deployment (Render.com)

1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect repository: `nita-05/footage`
4. Configure:
   - **Name:** `footage-flow-backend`
   - **Build Command:** `cd backend && pip install -r requirements.txt`
   - **Start Command:** `cd backend && gunicorn --config gunicorn.conf.py app:app`
   - **Plan:** Free

5. **Add Environment Variables:**
   ```
   PORT=10000
   FLASK_ENV=production
   GOOGLE_CLIENT_ID=724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=a1654bf6b8d952823796bc1401c8171abd3d691404738a39ce1bf2c4996d7f3d
   GEMINI_API_KEY=AIzaSyCGON4hUzN2oHJAEOzSTSmFdXVs_UHFCNs
   ```

### Frontend Deployment (Vercel.com)

1. Go to [vercel.com](https://vercel.com)
2. Create new project
3. Import repository: `nita-05/footage`
4. Configure:
   - **Framework Preset:** Vite
   - **Root Directory:** `./frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`

5. **Add Environment Variables:**
   ```
   VITE_BACKEND_URL=https://your-backend-url.onrender.com
   VITE_GOOGLE_CLIENT_ID=724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com
   ```

## 🔒 Security Measures Implemented

✅ **API keys removed from repository**  
✅ **Template files secured**  
✅ **Environment variables protected**  
✅ **Sensitive files in .gitignore**  
✅ **Secure deployment guide created**  

## 📝 Local Development

For local development, create a `.env` file in the `backend` directory with your API keys.

## 🎯 Next Steps

1. Deploy backend to Render with the environment variables above
2. Deploy frontend to Vercel with the environment variables above
3. Test your deployed application
4. Share your app URL

**Your repository is now secure and ready for deployment!**
