import tkinter as tk
from tkinter import messagebox

# Define the chatbot's responses and shoe recommendations
responses = {
    "intro": "Hello! I'm your shoe recommendation chatbot. Let's find your perfect pair of shoes.",
    "ask_size": "What is your shoe size? (Enter a number)",
    "ask_use_case": "Where do you plan to wear the shoes? (e.g., running, hiking, casual)",
    "recommendation": "Based on your inputs, here are some shoe options:",
    "end": "Thank you for using our chatbot! Enjoy your new shoes!",
    "error_size": "Please enter a valid shoe size (numeric value).",
    "error_use_case": "Please enter a use case for the shoes (e.g., running, hiking, casual).",
}

shoe_recommendations = {
    "running": [
        {"name": "Nike Air Zoom Pegasus", "sizes": ["7", "8", "9", "10", "11"]},
        {"name": "Adidas Ultraboost", "sizes": ["8", "9", "10", "11", "12"]},
        {"name": "Brooks Ghost", "sizes": ["7", "8", "9", "10", "11"]},
    ],
    "hiking": [
        {"name": "Merrell Moab 2", "sizes": ["7", "8", "9", "10", "11"]},
        {"name": "Salomon X Ultra 3", "sizes": ["8", "9", "10", "11", "12"]},
        {"name": "Columbia Newton Ridge", "sizes": ["7", "8", "9", "10", "11"]},
    ],
    "casual": [
        {"name": "Converse Chuck Taylor", "sizes": ["7", "8", "9", "10", "11"]},
        {"name": "Vans Old Skool", "sizes": ["8", "9", "10", "11", "12"]},
        {"name": "Adidas Superstar", "sizes": ["7", "8", "9", "10", "11"]},
    ],
}

# Function to handle the "Recommend" button click
def recommend_shoes():
    shoe_size = shoe_size_entry.get()
    use_case = use_case_entry.get().lower()

    if not shoe_size.isdigit():
        messagebox.showerror("Error", responses["error_size"])
        return

    if not use_case:
        messagebox.showerror("Error", responses["error_use_case"])
        return

    if use_case in shoe_recommendations:
        recommended_shoes = []
        for shoe in shoe_recommendations[use_case]:
            if shoe_size in shoe["sizes"]:
                recommended_shoes.append(shoe["name"])
        if recommended_shoes:
            recommendation_label.config(
                text=f"{responses['recommendation']} (Size {shoe_size}, {use_case}):\n{', '.join(recommended_shoes)}"
            )
        else:
            recommendation_label.config(text=f"No matching shoes found for Size {shoe_size}, {use_case}.")
    else:
        recommendation_label.config(text="Sorry, we don't have recommendations for that use case.")

# Create the GUI window
window = tk.Tk()
window.title("Shoe Recommendation Chatbot")

# Create and configure GUI elements
intro_label = tk.Label(window, text=responses["intro"])
intro_label.pack()

shoe_size_label = tk.Label(window, text=responses["ask_size"])
shoe_size_label.pack()
shoe_size_entry = tk.Entry(window)
shoe_size_entry.pack()

use_case_label = tk.Label(window, text=responses["ask_use_case"])
use_case_label.pack()
use_case_entry = tk.Entry(window)
use_case_entry.pack()

recommend_button = tk.Button(window, text="Recommend", command=recommend_shoes)
recommend_button.pack()

recommendation_label = tk.Label(window, text="")
recommendation_label.pack()

end_label = tk.Label(window, text=responses["end"])
end_label.pack()

# Run the GUI application
window.mainloop()
