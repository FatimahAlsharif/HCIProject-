import tkinter as tk
from tkinter import ttk, messagebox
import io
import contextlib


class SelfCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Self Code")
        self.root.geometry("600x500")
        self.root.configure(bg="#E2CADB")  # Background color

        self.selected_language = "Python"  # Default language
        self.login_screen()

    def clear_screen(self):
        """Removes all widgets from the current screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        """Displays the login screen."""
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Arial", 20), bg="#E2CADB", fg="#0E1B48").pack(pady=20)
        tk.Label(self.root, text="Username:", bg="#E2CADB", fg="#87A7D0").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#E2CADB", fg="#87A7D0").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(
            self.root, text="Login", command=self.validate_login, bg="#C18DB4", fg="white", width=15
        ).pack(pady=20)

    def validate_login(self):
        """Validates login and shows the welcome screen."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            self.welcome_screen(username)
        else:
            messagebox.showerror("Error", "Please enter both username and password.")

    def welcome_screen(self, username):
        """Displays the welcome screen."""
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome, {username}!", font=("Arial", 18), bg="#E2CADB", fg="#0E1B48").pack(pady=20)

        buttons = [
            ("Choose Language", self.choose_language),
            ("Exercises", self.show_exercises),
            ("Tutorials", self.show_tutorials),
            ("Feedback", self.feedback_screen),
        ]

        for text, command in buttons:
            tk.Button(
                self.root, text=text, command=command, bg="#C18DB4", fg="white", width=20
            ).pack(pady=10)

    def choose_language(self):
        """Allows the user to choose a programming language."""
        def save_language():
            self.selected_language = language_choice.get()
            messagebox.showinfo("Language Selected", f"Language changed to {self.selected_language}")
            language_window.destroy()

        language_window = tk.Toplevel(self.root)
        language_window.title("Choose Language")
        language_window.geometry("300x200")
        language_window.configure(bg="#E2CADB")

        tk.Label(language_window, text="Select Programming Language:", bg="#E2CADB", fg="#87A7D0").pack(pady=20)
        language_choice = ttk.Combobox(language_window, values=["Python", "Java", "C++"], state="readonly")
        language_choice.set(self.selected_language)
        language_choice.pack(pady=10)

        tk.Button(language_window, text="Save", command=save_language, bg="#C18DB4", fg="white").pack(pady=20)

    def show_exercises(self):
        """Displays exercises for the selected language."""
        exercises_window = tk.Toplevel(self.root)
        exercises_window.title("Exercises")
        exercises_window.geometry("600x500")
        exercises_window.configure(bg="#E2CADB")

        tk.Label(
            exercises_window,
            text=f"Exercises in {self.selected_language}",
            font=("Arial", 16),
            bg="#E2CADB",
            fg="#0E1B48",
        ).pack(pady=20)

        exercises = [
            "Print 'Hello, World!'",
            "Find the sum of two numbers.",
            "Reverse a string.",
        ]

        for index, ex in enumerate(exercises):
            tk.Button(
                exercises_window,
                text=f"Exercise {index + 1}: {ex}",
                command=lambda i=index: self.run_exercise(i + 1),
                bg="#C18DB4",
                fg="white",
                width=40,
            ).pack(pady=10)

    def run_exercise(self, exercise_number):
        """Displays the code writing screen for the chosen exercise."""
        exercise_window = tk.Toplevel(self.root)
        exercise_window.title(f"Exercise {exercise_number}")
        exercise_window.geometry("600x500")
        exercise_window.configure(bg="#E2CADB")

        exercises = {
            1: {"description": "Print 'Hello, World!'", "expected_output": "Hello, World!\n"},
            2: {"description": "Find the sum of two numbers (e.g., 2 + 3).", "expected_output": "5\n"},
            3: {"description": "Reverse the string 'Hello'.", "expected_output": "olleH\n"},
        }

        exercise = exercises[exercise_number]
        tk.Label(
            exercise_window,
            text=f"Exercise {exercise_number}: {exercise['description']}",
            bg="#E2CADB",
            fg="#0E1B48",
            wraplength=500,
        ).pack(pady=10)

        code_input = tk.Text(exercise_window, height=15, width=60)
        code_input.pack(pady=10)

        def check_code():
            user_code = code_input.get("1.0", tk.END).strip()
            if self.selected_language == "Python":
                try:
                    # Redirect stdout to capture output
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        exec(user_code)
                    result = output.getvalue()
                    if result == exercise["expected_output"]:
                        messagebox.showinfo("Success", "Correct Output!")
                    else:
                        messagebox.showerror("Error", f"Incorrect Output!\nExpected: {exercise['expected_output']}\nGot: {result}")
                except Exception as e:
                    messagebox.showerror("Error", f"Error in your code: {str(e)}")
            else:
                messagebox.showinfo(
                    "Info",
                    f"Code checking is only available for Python. Write your {self.selected_language} code here.",
                )

        tk.Button(
            exercise_window, text="Submit", command=check_code, bg="#C18DB4", fg="white"
        ).pack(pady=10)

    def show_tutorials(self):
        """Displays tutorials for the exercises."""
        tutorials_window = tk.Toplevel(self.root)
        tutorials_window.title("Tutorials")
        tutorials_window.geometry("600x500")
        tutorials_window.configure(bg="#E2CADB")

        tk.Label(
            tutorials_window,
            text=f"Tutorials in {self.selected_language}",
            font=("Arial", 16),
            bg="#E2CADB",
            fg="#0E1B48",
        ).pack(pady=20)

        tutorials = {
            "Python": [
                "1. Hello, World! - Use print('Hello, World!') to print a string.",
                "2. Sum of two numbers - Use variables and the '+' operator.",
                "3. Reverse a string - Use slicing: string[::-1].",
            ],
            "Java": [
                "1. Hello, World! - Use System.out.println('Hello, World!');.",
                "2. Sum of two numbers - Use int variables and the '+' operator.",
                "3. Reverse a string - Use a loop or StringBuilder.reverse().",
            ],
            "C++": [
                "1. Hello, World! - Use std::cout << 'Hello, World!';.",
                "2. Sum of two numbers - Use int variables and the '+' operator.",
                "3. Reverse a string - Use a loop or std::reverse().",
            ],
        }

        tutorial_list = tutorials.get(self.selected_language, ["No tutorials available."])
        for tut in tutorial_list:
            tk.Label(tutorials_window, text=tut, bg="#E2CADB", fg="#87A7D0", wraplength=500, anchor="w").pack(pady=5)

    def feedback_screen(self):
        """Displays the feedback screen."""
        feedback_window = tk.Toplevel(self.root)
        feedback_window.title("Feedback")
        feedback_window.geometry("400x300")
        feedback_window.configure(bg="#E2CADB")

        tk.Label(feedback_window, text="We value your feedback!", bg="#E2CADB", fg="#0E1B48", font=("Arial", 16)).pack(pady=20)
        feedback_text = tk.Text(feedback_window, height=10, width=40)
        feedback_text.pack(pady=10)

        def submit_feedback():
            feedback = feedback_text.get("1.0", tk.END).strip()
            if feedback:
                messagebox.showinfo("Feedback Received", "Thank you for your feedback!")
                feedback_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter your feedback before submitting.")

        tk.Button(
            feedback_window, text="Submit Feedback", command=submit_feedback, bg="#C18DB4", fg="white"
        ).pack(pady=20)


# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = SelfCodeApp(root)
    root.mainloop()