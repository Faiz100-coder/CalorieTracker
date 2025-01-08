# CalorieTracker
The Food Calorie Tracker &amp; Gym Assistant is an intuitive web application designed to help users make informed dietary and fitness choices. This tool empowers individuals to track their calorie intake and plan their workouts effectively, ensuring they stay on top of their fitness goals.

# Food Calorie Counter

The Food Calorie Counter is a web application that helps users identify the calorie content of food through image recognition and provides recommendations for maintaining a healthy diet. The project is built using Django, Python, and integrates APIs for nutritional data.

---

## Features

- **Calorie Burn Suggestions:** Displays activities to burn consumed calories.
- **API Integration:** Fetches detailed nutritional data for various food items.
- **User-Friendly Interface:** Intuitive design for easy navigation and interaction.

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (or any configured database)
- **APIs:** Used for nutritional data retrieval

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended)

---

## Installation and Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
https://github.com/your-username/food-calorie-counter.git
cd food-calorie-counter
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```


---

## API Integration

This project uses external APIs to fetch nutritional data. Make sure to:

1. Sign up for an API key (e.g., Edamam, Nutritionix, or any other API).
2. Add your API key to the `.env` file (or directly in settings if you prefer):

```plaintext
API_KEY=your_api_key_here
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
![image](https://github.com/user-attachments/assets/f0315c71-b620-4fe6-a74b-fd8b4f41cbaf)
![image](https://github.com/user-attachments/assets/fb80a33c-d64b-4f91-93f9-973e3081aeca)

![image](https://github.com/user-attachments/assets/0a95274a-94eb-410f-b3f9-b04d9ee11ac7)
![image](https://github.com/user-attachments/assets/290b8b45-78cb-4c30-8bd9-a61299cbead6)


