# Spring 2025 CS 3200 Project Template Repository

This repo is a template for your semester project. It includes most of the infrastructure setup (containers), sample databases, and example UI pages.

---

# 🐶 Project Title: PetCare Companion

A pet healthcare & appointment management platform developed for CS3200 (Spring 2025). This system allows pet owners to manage pet profiles, book appointments with vets and groomers, and track pet health records.

---

## 👥 Team Members
- Ray Zhang (GitHub: [rayrayowo](https://github.com/rayrayowo))
- [其他组员姓名]

---

## 📁 Features Implemented
- 🐾 Pet Overview Page (Streamlit UI)
- 📅 Appointment Booking Page (Streamlit UI)
- 🛠️ GET and POST Flask Routes for `/appointments`
- 💾 Dockerized MySQL + Streamlit + Flask backend
- ✅ Full relational schema using MySQL init scripts

---

## 🚀 How to Run This Project (Quick Start)

```bash
# Step 1: Build and start services
docker-compose up --build

# Step 2: Visit the web app in your browser
http://localhost:8501

# Step 3: Use the prefilled PetOwner login to view pet info or book appointments
```

---

## 🧱 Database Initialization

All SQL scripts are located in:

```bash
/database-files/docker-entrypoint-initdb.d/
```

They are automatically loaded into MySQL container on first startup.

---

## 🧪 API Endpoints (Example)

```bash
GET  /appointments
POST /appointments
```

---