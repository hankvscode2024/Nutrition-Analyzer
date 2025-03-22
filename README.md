# 📌 Nutrition Analyzer
_A Django-based web app for analyzing nutritional values of food items._

---

## **🛠 Features**
✅ Fetches nutritional data using **Calories Ninja API**  
✅ Displays **calories, proteins, fats, and carbs** for any food item  
✅ Visualizes nutritional data using **charts**  
✅ Simple and interactive web UI  

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**
Open a terminal (or Command Prompt) and run:  
```bash
git clone https://github.com/hankvscode2024/Nutrition-Analyzer.git
cd Nutrition-Analyzer
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**
#### For Windows:
```powershell
python -m venv env
env\Scripts\activate
```
#### For macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

---

### **3️⃣ Install Dependencies**
Run the following command inside the project directory:  
```bash
pip install -r requirements.txt
```

---

### **4️⃣ Set Up Environment Variables**
Create a **.env** file in the project root and add:  
```plaintext
API_KEY=<your_calories_ninja_api_key>
DEBUG=True
```
Replace `<your_calories_ninja_api_key>` with your **Calories Ninja API Key**.

---

### **5️⃣ Apply Migrations**
```bash
python manage.py migrate
```

---

### **6️⃣ Run the Development Server**
```bash
cd calorie_counter
python manage.py runserver
```
Now, open **http://127.0.0.1:8000/** in your browser.

---

## **🎯 Usage Guide**
1️⃣ Enter a food item in the search bar (e.g., "Banana, Egg, Milk")  
2️⃣ Click **Analyze** to fetch and display the nutrition facts  
3️⃣ View **calories, proteins, fats, and carbs** in a clean UI  
4️⃣ Check **charts** for easy visualization  

---

## **🔧 Troubleshooting**
- If `python` is not recognized, try `python3` instead.
- If dependencies fail, run:
  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
- If API calls fail, verify your **API Key** in `.env`.

---

## **🤝 Contributing**
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Make your changes and commit (`git commit -m "Added new feature"`)  
4. Push the changes (`git push origin feature-branch`)  
5. Open a **Pull Request**  

---

## **📄 License**
This project is licensed under the **MIT License**.
