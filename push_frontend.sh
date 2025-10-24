#!/bin/bash
# Script để push Frontend code lên GitHub

echo "🚀 Pushing Frontend code to GitHub..."

# Add all files
git add .

# Commit changes
git commit -m "Update PoS Frontend - Ready for Vercel deployment"

# Add remote origin
git remote add origin https://github.com/surp29/Frontend_PoS.git

# Push to main branch
git branch -M main
git push -u origin main

echo "✅ Frontend code pushed successfully!"
