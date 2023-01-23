import openai
import tkinter as tk
from tkinter import messagebox

openai.api_key = "sk-D8nm4UyMuHKEEp99pb44T3BlbkFJgRx5IzG48TtKy1uaBiA"


# Get the prediction from GPT-3
def predict_phishing(message):
  # Send the message to GPT-3
  prompt = f'Is this email phishing or legitimate: "{message}"'
  model_engine = "text-davinci-002"
  completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.7,
  )

  prediction = completions.choices[0].text.strip().lower()
  return prediction

# Create the main window
window = tk.Tk()
window.title("Phishing Detector")

# Create the input field
input_field = tk.Text(window, height=5, width=50)
input_field.pack()

# This function will run when you click predict
def predict():
  message = input_field.get("1.0", "end").strip()
  if message:
    prediction = predict_phishing(message)
    messagebox.showinfo("Prediction", f"GPT-3 Response: {prediction}")
  else:
    messagebox.showerror("Error", "Please enter an email message")

# Create the predict button
predict_button = tk.Button(text="Predict", command=predict)
predict_button.pack()

# Open the GUI
window.mainloop()
