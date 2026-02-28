# 🧮 Tkinter Calculator App

A modern desktop calculator built using **Python** and **Tkinter**, designed with clean UI styling, modular architecture, and persistent history storage.

---

## 🚀 Features

✅ Addition  
✅ Subtraction  
✅ Multiplication  
✅ Division (with divide-by-zero protection)  
✅ Power operation  
✅ Square root (with negative number handling)  
✅ Live result display  
✅ Calculation history panel  
✅ Persistent history saved to file  
✅ Clear input & clear history functionality  
✅ Modular structure (GUI separated from logic)

---

## 🏗 Project Structure
calculator_3/
|
|--gui.py
|--calculator_logic.py
|--history.txt
|--main.py
|--assets
|--README.md


### 🔹 `gui.py`
Handles:
- Tkinter UI layout
- Event handling
- Input validation
- History display
- File saving

### 🔹 `calculator_logic.py`
Contains:
- All mathematical functions
- Error handling logic
- Operations dictionary mapping symbols to functions

---

## 🧠 Architecture Design

The application follows a **modular design pattern**:

- GUI layer → Responsible for interface & user interaction  
- Logic layer → Responsible for calculations only  
- Data layer → Stores history in a text file  

This separation improves:
- Maintainability
- Scalability
- Code readability
- Testing capability

---

## ⚙️ How It Works

The application uses a dictionary-based operation dispatcher:

```python
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "**": power,
    "√": sqrt
}

---

💾 History System

-Each calculation is appended to history.txt
-History is displayed in the GUI
-Clear history button resets the display
-File persistence allows session tracking

---

🛡 Error Handling

✔ Empty input detection
✔ ValueError handling
✔ Divide by zero protection
✔ Negative square root protection
✔ File existence validation

---

📦 Requirements

-Python 3.8+
-Tkinter (comes pre-installed with Python)

---

🔮 Future Improvements

-Scrollable history using Text widget
-Dark / Light mode toggle
-Keyboard bindings
-Scientific calculator mode
-JSON-based history storage
-MVC refactoring
-Unit testing with pytest

---

## 👤 Author

Vidushan Pathirana  
University Student | Aspiring Data Scientist  
First GitHub Project 🚀