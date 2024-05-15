import customtkinter
import socket

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
import socket
HOST = '192.168.241.55'
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

root = customtkinter.CTk()
root.geometry("800x600")    

def shoulder_sldr(value):
    value = "sh" + str(value)
    client_socket.send(str(value).encode('utf-8'))
    
def elbow_sldr(value):
    value = "el" + str(value)
    client_socket.send(str(value).encode('utf-8'))

def claw_sldr(value):
    value = "cl" + str(value)
    client_socket.send(str(value).encode('utf-8'))

def vert_sldr(value):
    value = "ve" + str(value)
    client_socket.send(str(value).encode('utf-8'))

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40,padx=60)

label = customtkinter.CTkLabel(master=frame,text="Vert")
label.pack(pady=10)

vert_slider = customtkinter.CTkSlider(master=frame,from_=-1,number_of_steps=2,to=1,command=vert_sldr)
vert_slider.pack(pady=20)

label = customtkinter.CTkLabel(master=frame,text="Shoulder Joint")
label.pack(pady=10)

shoulder_slider = customtkinter.CTkSlider(master=frame,from_=0,number_of_steps=180,to=180,command=shoulder_sldr)
shoulder_slider.pack(pady=20,padx=60)

label = customtkinter.CTkLabel(master=frame,text="Elbow Joint")
label.pack(pady=10)

elbow_slider = customtkinter.CTkSlider(master=frame,from_=0,number_of_steps=180,to=180,command=elbow_sldr)
elbow_slider.pack(pady=20)

label = customtkinter.CTkLabel(master=frame,text="Claw")
label.pack(pady=10)

claw_slider = customtkinter.CTkSlider(master=frame,from_=0,number_of_steps=180,to=180,command=claw_sldr)
claw_slider.pack(pady=20)

root.mainloop()
