import tkinter as tk

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

key_button = tk.Button(input_frame,text="Generate Key")
key_button.grid(row=4,column=0,columnspan=2,pady=(0,10))

#Buttons
button_frame = tk.LabelFrame(frame,padx=10,pady=5)
button_frame.pack(fill='x',padx=10,pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt")
encrypt_button.pack(side="left", padx=50)

decrypt_button = tk.Button(button_frame, text="Decrypt")
decrypt_button.pack(side="left", padx=50)

clear_button = tk.Button(button_frame, text="Clear")
clear_button.pack(side="left", padx=50)

#Result
result_frame = tk.LabelFrame(frame,padx=5,pady=5)
result_frame.pack(fill="both",padx=10,pady=5)

result_label = tk.Label(result_frame,text="Result(Encrypted/Decrypted):")
result_label.grid(row=0,column=0,columnspan=2, sticky="w", pady=(0, 10))

result_text = tk.Text(result_frame,height=5,width=50)
result_text.grid(row=1,column=0,sticky="w",pady=(0,5))

window.mainloop()