# 🏛️ CSR Provincial System Backend (Tawi-Tawi)

Isang robust at secure na **Centralized Service Request (CSR) System** na binuo para sa Provincial Government ng Tawi-Tawi. Ang system na ito ay nagpapadali ng koordinasyon mula sa **Barangay level** hanggang sa **Provincial level**.

## 🚀 Key Features

* **JWT Authentication:** May secure na login system (OAuth2) at "Lock Icon" protection sa bawat endpoint.
* **Multi-Level Routing:** Automated system para sa pag-akyat (escalation) ng mga requests mula sa Barangay -> Municipal -> Provincial.
* **Database Cloud Sync:** Naka-connect sa **Neon PostgreSQL** para sa real-time data storage.
* **API Documentation:** Interactive Swagger UI para sa madaling testing ng mga endpoints.

## 🛠️ Project Structure & Endpoints

| Category | Prefix | Description |
| :--- | :--- | :--- |
| **Authentication** | `/auth` | Login, Register, at User Profile management. |
| **Citizen Services** | `/citizen` | Submission at tracking ng mga service requests. |
| **Barangay Level** | `/barangay` | Initial review at records ng mga requests. |
| **Municipal Level** | `/municipal` | Processing ng mga requests mula sa mga barangay. |
| **Provincial Level** | `/provincial` | Final approval at provincial-wide records. |

## 🏗️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database:** PostgreSQL (Neon.tech)
* **ORM:** SQLAlchemy
* **Security:** JWT, Passlib (Bcrypt for hashing)

## ⚙️ Local Installation & Setup

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/nas010122/crs_backend.git](https://github.com/nas010122/crs_backend.git)
    cd crs_backend
    ```

2.  **Activate Virtual Environment:**
    ```bash
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Application:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **View Docs:**
    Pumunta sa `http://127.0.0.1:8000/docs`

## 👤 Developer
* **Aljan Andy**
* **Mickie Cornelio**
* **Nurusman Nasser**
* *Group: Provincial CSR Project Team*

---
© 2026 Tawi-Tawi Provincial System Project
