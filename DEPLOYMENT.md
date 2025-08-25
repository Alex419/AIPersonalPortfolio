# 🚀 Railway Deployment Guide for Alex's AI Portfolio

## 🎯 **Deployment Strategy: Railway for Everything!**

### **Why Railway?**
- ✅ **Single platform** - frontend + backend together
- ✅ **Python/Flask support** - handles your RAG system perfectly
- ✅ **Free tier** - generous limits for students
- ✅ **Easy setup** - connects to GitHub, auto-deploys
- ✅ **Custom domains** - easy to connect `alexgu.dev`
- ✅ **SSL certificates** - included automatically

## 📋 **What We've Prepared:**

### **Production-Ready Files:**
- **`Procfile`**: Tells Railway "run `gunicorn app:app`"
- **`runtime.txt`**: Specifies Python 3.9.18
- **`env.production.example`**: Template for environment variables
- **Updated `app.py`**: Production-ready Flask app
- **Updated `requirements.txt`**: Clean production dependencies

## 🔧 **Railway Deployment Steps:**

### **Step 1: Prepare Your Code**
1. **Commit all changes** to GitHub
2. **Ensure these files exist**:
   - `Procfile`
   - `runtime.txt`
   - `requirements.txt`
   - `app.py`

### **Step 2: Set Up Railway**
1. Go to [railway.app](https://railway.app)
2. **Sign up** with your GitHub account
3. **Create new project** → "Deploy from GitHub repo"
4. **Select your repo**: `AIPersonalPortfolio`

### **Step 3: Configure Environment Variables**
In Railway dashboard, add these environment variables:
```bash
FLASK_ENV=production
GOOGLE_API_KEY=your-actual-google-api-key
SECRET_KEY=your-secret-key-here
```

### **Step 4: Deploy**
1. **Railway auto-detects** Python and Flask
2. **Builds automatically** from your `requirements.txt`
3. **Starts your app** using the `Procfile`
4. **Gives you a URL** like `https://your-app.railway.app`

### **Step 5: Connect Your Domain**
1. **Buy `alexgu.dev`** (from Namecheap, GoDaddy, etc.)
2. **In Railway**: Settings → Domains → Add custom domain
3. **Point DNS** to Railway's servers
4. **SSL certificate** is automatic!

## 🎯 **What Each File Does:**

- **`Procfile`**: "Railway, run `gunicorn app:app` when starting"
- **`runtime.txt`**: "Railway, use Python 3.9.18"
- **`app.py`**: "Flask app that serves your portfolio + chat API"
- **`requirements.txt`**: "Railway, install these Python packages"

## 🚨 **Important Notes:**

1. **Environment Variables**: Never commit your actual API keys!
2. **Database**: Your ChromaDB will be recreated on each deployment
3. **Port**: Railway sets `PORT` automatically
4. **Free Tier**: 500 hours/month, 1GB RAM, 1GB storage

## 🎉 **Benefits of Railway:**

- **One deployment** - everything together
- **Auto-scaling** - handles traffic spikes
- **GitHub integration** - auto-deploys on push
- **Monitoring** - see logs, performance, errors
- **Student-friendly** - generous free tier

## 🚀 **Ready to Deploy!**

Your code is perfectly set up for Railway! Once you deploy, you'll have:
- **Portfolio site** at `alexgu.dev`
- **RAG chatbot** working perfectly
- **Beautiful UI** with your divine orb theme
- **Professional hosting** for recruiters to see

**Questions?** Ask me about any Railway step!
