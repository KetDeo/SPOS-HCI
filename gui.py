import tkinter as tk
from tkinter import ttk

# Function to handle button click
def submit_form():
    selected_radio = radio_var.get()
    entered_text = entry_box.get()
    is_checked = upload_video_var.get()
    from_language = from_var.get()
    to_language = to_var.get()
    
    result_text = f"Radio: {selected_radio}\n" \
                  f"Text: {entered_text}\n" \
                  f"Checked: {is_checked}\n" \
                  f"From: {from_language}\n" \
                  f"To: {to_language}"
    
    result_label.config(text=result_text)

# Function to show/hide widgets based on radio button selection
def toggle_widgets():
    if radio_var.get() == "Indian Sign Language Translation":
        # Hide the text box and show the checkboxes
        label3.grid_remove()
        entry_frame.grid_remove()
        upload_video_checkbox.grid()
        upload_photo_checkbox.grid()
    else:
        # Show the text box and hide the checkboxes
        label3.grid()
        entry_frame.grid()
        upload_video_checkbox.grid_remove()
        upload_photo_checkbox.grid_remove()

# Function to handle cancel button
def cancel_action():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Sensory Harmony")
root.configure(bg="#F5ECDF")  # Set background color

# Set up custom styles for the Combobox to match font color and size
style = ttk.Style()
style.configure("TCombobox",
                foreground="#606676",  # Font color
                font=("Arial", 14),    # Font size
                background="#FFFFFF")  # Background color of the combobox

# Label for Sensory Harmony in big letters and #BEC6A0 color
header_label = tk.Label(root, text="Sensory Harmony", font=("Arial", 24), fg="#BEC6A0", bg="#F5ECDF")
header_label.grid(row=0, column=0, columnspan=4, pady=20)

# Labels for options and input fields
label2 = tk.Label(root, text="Translation Options:", font=("Arial", 14), fg="#606676", bg="#F5ECDF", anchor='w')
label2.grid(row=1, column=0, padx=10, pady=(10, 5), sticky='w')

# Radio buttons for translation options with matching font size
radio_var = tk.StringVar(root)

# Align radio buttons vertically in the same row as the label
radio1 = ttk.Radiobutton(root, text="Indian Sign Language Translation", variable=radio_var, value="Indian Sign Language Translation", command=toggle_widgets)
radio1.config(style="Custom.TRadiobutton")
radio2 = ttk.Radiobutton(root, text="Language to Language Translation", variable=radio_var, value="Language to Language Translation", command=toggle_widgets)
radio2.config(style="Custom.TRadiobutton")

# Adjusted grid positions to align with the label
radio1.grid(row=1, column=1, padx=5, pady=(30, 24), sticky='w')
radio2.grid(row=1, column=3, padx=5, pady=(30, 24), sticky='w')

# Custom style for radio buttons and checkboxes
style.configure("Custom.TRadiobutton", font=("Arial", 14), background="#F5ECDF", foreground="#606676")
style.configure("Custom.TCheckbutton", font=("Arial", 14), background="#F5ECDF", foreground="#606676")
style.configure("Custom.TButton", font=("Arial", 14), background="#F5ECDF", foreground="#606676", relief="flat")

# Labels for "From" and "To" languages
from_label = tk.Label(root, text="From:", font=("Arial", 14), fg="#606676", bg="#F5ECDF", anchor='w')
from_label.grid(row=2, column=0, padx=10, pady=(5, 0), sticky='w')

to_label = tk.Label(root, text="To:", font=("Arial", 14), fg="#606676", bg="#F5ECDF", anchor='w')
to_label.grid(row=2, column=2, padx=10, pady=(5, 0), sticky='w')

# Drop-down for "From" languages with matching font color and size
from_var = tk.StringVar(root)
from_var.set("Indian Sign Language")  # default value for "From"
from_languages = ["Indian Sign Language", "English", "Spanish", "French", "German"]
from_menu = ttk.Combobox(root, textvariable=from_var, values=from_languages, style="TCombobox")
from_menu.grid(row=2, column=1, padx=5, pady=(5, 0), sticky='w')

# Drop-down for "To" languages with matching font color and size
to_var = tk.StringVar(root)
to_var.set("English")  # default value for "To"
to_languages = ["English", "Spanish", "French", "German", "Mandarin"]
to_menu = ttk.Combobox(root, textvariable=to_var, values=to_languages, style="TCombobox")
to_menu.grid(row=2, column=3, padx=5, pady=(5, 0), sticky='w')

# Text box label
label3 = tk.Label(root, text="Enter the text:", font=("Arial", 14), fg="#606676", bg="#F5ECDF", anchor='w')
label3.grid(row=4, column=0, padx=10, pady=(10, 5), sticky='w')

# Frame to simulate rounded entry box
entry_frame = tk.Frame(root, bg="#FFFFFF", bd=1, relief="flat")
entry_frame.grid(row=4, column=1, padx=5, pady=(5, 10), columnspan=1, sticky='w')

# Text box (Entry)
entry_box = tk.Entry(entry_frame, width=30, borderwidth=0, bg="#FFFFFF", fg="#606676")  # Width set for square shape
entry_box.pack(padx=10, pady=5)

# Text box border simulation
entry_frame.pack_propagate(0)  # Prevent frame from resizing
entry_frame.config(width=250, height=50)  # Set size for the text box

# Checkboxes for uploading video and photo
upload_video_var = tk.IntVar()
upload_video_checkbox = ttk.Checkbutton(root, text="Upload Video", variable=upload_video_var, style="Custom.TCheckbutton")
upload_video_checkbox.grid(row=3, column=2, padx=10, pady=(5, 5), sticky='w')

upload_photo_var = tk.IntVar()
upload_photo_checkbox = ttk.Checkbutton(root, text="Upload Photo", variable=upload_photo_var, style="Custom.TCheckbutton")
upload_photo_checkbox.grid(row=3, column=1, padx=10, pady=(5, 5), sticky='w')

# Initially hide the checkboxes
upload_video_checkbox.grid_remove()
upload_photo_checkbox.grid_remove()

# Frame for the Translate and Cancel buttons
button_frame = tk.Frame(root, bg="#F5ECDF")
button_frame.grid(row=10, column=0, columnspan=4, pady=20)

# Translate button with custom style
translate_button = ttk.Button(button_frame, text="Translate", style="Custom.TButton", command=submit_form)
translate_button.pack(side=tk.LEFT, padx=10)

# Cancel button with custom style
cancel_button = ttk.Button(button_frame, text="Cancel", command=cancel_action, style="Custom.TButton")
cancel_button.pack(side=tk.LEFT, padx=10)

# Label to display the results
result_label = tk.Label(root, text="", anchor="w", bg="#F5ECDF", fg="#606676")
result_label.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky='w')

# Start the GUI loop
root.mainloop()


