
 🔐 Password Strength Checker (Python)

📌 Project Overview

This project is a **Password Strength Checker** built using **Python**.
It checks how strong a password is based on **common security rules** and classifies it as **Very Weak, Weak, Medium, Strong, or Very Strong**.

This project helps beginners understand:

* String handling
* Conditional logic
* Loops
* Real-world validation logic used in applications

🎯 Objective

To analyze a user-entered password and determine its strength using **industry-standard rules** such as:

* Length of password
* Use of uppercase letters
* Use of lowercase letters
* Use of numbers
* Use of special characters

🧠 How It Works (Project Flow)

User enters password
        ↓
Check password length
        ↓
Check uppercase letters
        ↓
Check lowercase letters
        ↓
Check digits
        ↓
Check special characters
        ↓
Calculate score
        ↓
Display password strength


This flow represents the **core logic frame** of the project.

🛠 Tools & Technologies Used

* **Language:** Python 3
* **IDE:** PyCharm / VS Code / Any Python IDE
* **Libraries:** None (only built-in Python functions)


📋 Password Rules Used

| Rule              | Description                 |
| ----------------- | --------------------------- |
| Minimum length    | At least 8 characters       |
| Uppercase letter  | At least one capital letter |
| Lowercase letter  | At least one small letter   |
| Digit             | At least one number         |
| Special character | At least one symbol         |

Each rule adds **1 point** to the password score.
## 📊 Strength Classification Logic

| Score | Password Strength |
| ----- | ----------------- |
| 2 | Very Weak         |
| 5 | Strong            |
| 10| Very Strong       |

---
 💻 Program Features

* Accepts user input securely
* Validates password using multiple conditions
* Calculates strength score
* Displays clear feedback
* Easy to understand and modify

 ▶️ Sample Output
Enter your password: Sharmi@1

Password Strength: Very Strong Password

 📂 Project Structure

password-strength-checker/
│
├── password_checker.py
└── README.md

🚀 How to Run the Project

1. Make sure Python is installed
2. Clone or download the repository
3. Open terminal in project folder
4. Run the file:

 📚 Concepts Learned

* Python string methods (`isdigit()`, `isupper()`, `islower()`)
* Conditional statements
* Loops
* Input validation
* Real-world security rules

## 👩‍💻 Author

SHAMRILA JONES S
