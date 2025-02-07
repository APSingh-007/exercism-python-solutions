# Exercism Python Solutions

This repository contains my solutions to the exercises from the  **Python track** on **Exercism**. Each folder represents a different exercise with its corresponding solution.

## 📁 **Repository Structure**

```
exercism-python-solutions/
│-- exercise_name-1/
│   ├── solution.py
│   ├── solution_test.py
│-- exercise_name-2/
│   ├── solution.py
│   ├── solution_test.py
│-- ...
│-- .gitignore
|-- requirements.txt
│-- README.md
``` 

- Each **exercise folder** contains:
    
    - `solution.py` → My implementation of the exercise.
        
    - `test_solution.py` → Test cases for the solution.
        

## 🚀 **How to Use**

1. Clone the repository:
    
    ```
    git clone https://github.com/APSingh-007/exercism-python-solutions.git
    ```
    
2. Create and activate virtual environment and install the requirements:
    
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
        
3. Navigate to exercise directory and run tests to validate the solution:
    
    ```
    cd <exercise_name>
    python3 -m pytest -o markers=task' <test_solution.py>
    ```

## 📌 **.gitignore**

This repository ignores unnecessary files and directories inside each exercise's directory using `.gitignore`, including:

```
.venv/
__pycache__/
.exercism/
.pytest_cache/
help.md
```

## 🏆 **Progress**

I am continuously working on completing all exercises on the python track. Check back for updates!

## 💡 **Contributing**

If you have better solutions or improvements for mine, please fork the repo and open a pull request. It will help me get more feedback and learn more.

## 📜 **License**

This repository is licensed under the **MIT License**. Feel free to use this code anywhere.
