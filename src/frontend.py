import customtkinter as tk
from main import generate_email_content, send_email
import threading

# Function to handle the confirm button click event
def confirm_button_clicked():
    # Get the values from the entry fields
    name = name_entry.get()
    email = email_entry.get()
    context = context_textbox.get("1.0", "end-1c")  # Get all text from the textbox

    # Create a data structure to store the values
    data = {
        'Name': name,
        'Email': email,
        'Context': context
    }
    send_email(data, email_textbox.get("1.0", tk.END))
    

# Function to handle the generate button click event
def generate_button_clicked():
    # Get the values from the entry fields
    name = name_entry.get()
    email = email_entry.get()
    context = context_textbox.get("1.0", "end-1c")  # Get all text from the textbox

    # Create a data structure to store the values
    data = {
        'Name': name,
        'Email': email,
        'Context': context
    }
    email_textbox.delete("1.0", tk.END)
    email_textbox.insert("1.0", generate_email_content(data))

def start_generate_button_clicked():
    threading.Thread(target=generate_button_clicked).start()

# Create the main window
window = tk.CTk()
window.title("Email Generator")

# Create a frame for better layout control
frame = tk.CTkFrame(window)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Create the name label and entry
name_label = tk.CTkLabel(frame, text="Your Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.CTkEntry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Create the email label and entry
email_label = tk.CTkLabel(frame, text="Recipient Email:")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry = tk.CTkEntry(frame)
email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Create the context label and textbox
context_label = tk.CTkLabel(frame, text="Context:")
context_label.grid(row=2, column=0, padx=10, pady=10, sticky="ne")
context_textbox = tk.CTkTextbox(frame, width=300, height=100)
context_textbox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Create the email label and textbox
email_label = tk.CTkLabel(frame, text="Email:")
email_label.grid(row=3, column=0, padx=10, pady=10, sticky="ne")
email_textbox = tk.CTkTextbox(frame, width=300, height=150)
email_textbox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Create a frame for the buttons
button_frame = tk.CTkFrame(frame)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

# Create the confirm button
confirm_button = tk.CTkButton(button_frame, text="Confirm", command=confirm_button_clicked, hover_color="green")
confirm_button.grid(row=0, column=0, padx=10, pady=10)

# Create the generate button
generate_button = tk.CTkButton(button_frame, text="Generate", command=start_generate_button_clicked, hover_color="green")
generate_button.grid(row=0, column=1, padx=10, pady=10)

# Start the main event loop
window.mainloop()