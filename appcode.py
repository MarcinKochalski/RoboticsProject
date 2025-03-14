import tkinter as tk
from tkinter import messagebox
import serial
import time

# Bluetooth port ve baud hızı ayarları
BLUETOOTH_PORT = "COM6"  # Doğru port adresi
BAUD_RATE = 9600

# Global seri bağlantı
bt_connection = None

# Bluetooth'a bağlanma fonksiyonu
def connect_bluetooth():
    global bt_connection
    try:
        bt_connection = serial.Serial(BLUETOOTH_PORT, BAUD_RATE)
        time.sleep(2)
        messagebox.showinfo("Connected", f"HC-05'e {BLUETOOTH_PORT} connected!")
    except Exception as e:
        messagebox.showerror("Error of Connection", f"Bluetooth is not connected: {e}")

# Komut gönderme fonksiyonu
def send_command(command):
    global bt_connection
    if bt_connection and bt_connection.is_open:
        try:
            bt_connection.write((command + "\n").encode())
            print(f"Command sent: {command}")
        except Exception as e:
            messagebox.showerror("error", f"Cannot sent the message: {e}")
    else:
        messagebox.showerror("no connection", "Connect the bluetooth first")

# Tkinter arayüzü
def create_gui():
    root = tk.Tk()
    root.title("HC-05 Kontrol Paneli")
    root.geometry("600x600")
    root.configure(bg="red")

    button_font = ("Arial", 18, "bold")

    # Bluetooth bağlantı düğmesi
    btn_connect = tk.Button(root, text="CONNECT BLT", font=button_font, bg="green", fg="black", width=12, height=2,
                            command=connect_bluetooth)
    btn_connect.place(x=220, y=20)

    # Komut butonları
    btn_stop = tk.Button(root, text="STOP", font=button_font, bg="blue", fg="black", width=12, height=2,
                         command=lambda: send_command("STOP"))
    btn_stop.place(x=220, y=120)

    btn_start = tk.Button(root, text="MOVE", font=button_font, bg="orange", fg="black", width=12, height=2,
                          command=lambda: send_command("START"))
    btn_start.place(x=220, y=200)

    btn_forward = tk.Button(root, text="↑", font=button_font, bg="yellow", fg="black", width=5, height=2,
                            command=lambda: send_command("FORWARD"))
    btn_forward.place(x=270, y=300)

    btn_left = tk.Button(root, text="←", font=button_font, bg="yellow", fg="black", width=5, height=2,
                         command=lambda: send_command("RIGHT"))
    btn_left.place(x=80, y=400)

    btn_right = tk.Button(root, text="→", font=button_font, bg="yellow", fg="black", width=5, height=2,
                          command=lambda: send_command("LEFT"))
    btn_right.place(x=450, y=400)

    btn_backward = tk.Button(root, text="↓", font=button_font, bg="yellow", fg="black", width=5, height=2,
                             command=lambda: send_command("BACKWARD"))
    btn_backward.place(x=270, y=500)

    # Adding Center Wheel button (move it down to avoid overlap)
    btn_center = tk.Button(root, text="CENTER WHEEL", font=button_font, bg="purple", fg="white", width=15, height=2,
                           command=lambda: send_command("CENTER"))
    btn_center.place(x=190, y=400)  # Adjust y to avoid overlap with other buttons

    root.mainloop()

if __name__ == "__main__":
    create_gui()
