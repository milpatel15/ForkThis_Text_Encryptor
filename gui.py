import tkinter as tk
from tkinter import messagebox
import logic


def handle_generate_key():
    new_key = logic.generate_key_str()
    key_entry.delete(0,tk.END)
    key_entry.insert(0,new_key)


def handle_encrypt():
    message = message_entry.get()
    key = key_entry.get()

    if not message or not key:
        messagebox.showwarning("Input Error", "Message and Key fields are required.")
        return
    encrypted_result = logic.encrypt_message(message,key)
    result_text.delete('1.0', tk.END)
    result_text.insert('1.0', encrypted_result)

def handle_decrypt():
    
    encrypted_message = result_text.get('1.0', tk.END).strip()
    key = key_entry.get()

    if not encrypted_message or not key:
        messagebox.showwarning("Input Error", "Result and Key fields cannot be empty.")
        return

    decrypted_result = logic.decrypt_message(encrypted_message, key)
    result_text.delete('1.0', tk.END)
    result_text.insert('1.0', decrypted_result)

def handle_clear():
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result_text.delete('1.0', tk.END)


window  = tk.Tk()
window.title("Password Encryptor and Decryptor")
window.geometry("500x400")
window.resizable(False,False)

frame = tk.Frame(window)
frame.pack(expand=True,fill=tk.BOTH)

#Input Text
input_frame = tk.LabelFrame(frame,padx=5,pady=5)
input_frame.pack(fill="x",padx=10,pady=5)

message_label = tk.Label(input_frame,text="Password/Message:")
message_label.grid(row=0,column=0,sticky="w", pady=(0, 5))

key_label = tk.Label(input_frame,text="Encryption Key:")
key_label.grid(row=2,column=0, sticky="w", pady=(0, 10))

message_entry = tk.Entry(input_frame,width=68)
message_entry.grid(row=1,column=0,sticky="w", pady=(0, 5))

key_entry = tk.Entry(input_frame,width=68)
key_entry.grid(row=3,column=0,columnspan=2, sticky="ew", pady=(0, 10))

key_button = tk.Button(input_frame,text="Generate Key",command=handle_generate_key)
key_button.grid(row=4,column=0,columnspan=2,pady=(0,10))

#Buttons
button_frame = tk.LabelFrame(frame,padx=10,pady=5)
button_frame.pack(fill='x',padx=10,pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt",command=handle_encrypt)
encrypt_button.pack(side="left", padx=50)

decrypt_button = tk.Button(button_frame, text="Decrypt",command=handle_decrypt)
decrypt_button.pack(side="left", padx=50)

clear_button = tk.Button(button_frame, text="Clear",command=handle_clear)
clear_button.pack(side="left", padx=50)

#Result
result_frame = tk.LabelFrame(frame,padx=5,pady=5)
result_frame.pack(fill="both",padx=10,pady=5)

result_label = tk.Label(result_frame,text="Result(Encrypted/Decrypted):")
result_label.grid(row=0,column=0,columnspan=2, sticky="w", pady=(0, 10))

result_text = tk.Text(result_frame,height=5,width=50)
result_text.grid(row=1,column=0,sticky="w",pady=(0,5))

window.mainloop()