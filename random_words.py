import random
import tkinter as tk

with open('./words.txt') as f:
    words = f.read().splitlines()

words_4 = [w for w in words if len(w)>= 4]


# Function to return random words based on user input
def get_random_words():
    try:
        # Get the integer from the user input
        num_words = int(entry.get())

        # Ensure the number is valid
        if num_words <= 0:
            result_text.delete(1.0, tk.END)  # Clear previous text
            result_text.insert(tk.END, "Please enter a positive integer.")
            return

        # Get the random words from the list
        random_words = random.sample(words_4, num_words) if num_words <= len(words_4) else words_4
        random_words_disp = "_".join(random_words)

        # Update the Text widget to show the random words
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, random_words_disp)
    except ValueError:
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, "Please enter a valid integer.")


# Set up the Tkinter window
root = tk.Tk()
root.title("Random Word Selector")

# Add a label, entry, and button
label = tk.Label(root, text="Enter the number of random words:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Random Words", command=get_random_words)
button.pack()

# Text widget to display the result, making it selectable and scrollable
result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
result_text.pack()

# Run the Tkinter event loop
root.mainloop()