import os
import subprocess
import glob
import sys
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

# Configuration
DISCORD_PATH = os.path.join(os.environ['LOCALAPPDATA'], 'Discord')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

LOGO_PATH = resource_path("discord_logo.png")

def get_latest_discord_version():
    app_folders = glob.glob(os.path.join(DISCORD_PATH, 'app-*'))
    if not app_folders:
        return None
    # Sort by folder name (app-X.X.X) - usually version works well with string sort if formatted correctly
    # or parse version numbers
    app_folders.sort(key=lambda x: [int(d) for d in x.split('-')[-1].split('.')])
    return app_folders[-1]

def launch_discord():
    latest_dir = get_latest_discord_version()
    if latest_dir:
        exe_path = os.path.join(latest_dir, 'Discord.exe')
        if os.path.exists(exe_path):
            subprocess.Popen([exe_path], start_new_session=True)
            return True
    return False

class DiscordLauncherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quick Discord Launcher - v1.0")
        self.geometry("400x320")
        self.resizable(False, False)
        
        # Discord dark theme colors
        self._set_appearance_mode("dark")
        self.configure(fg_color="#23272a")

        # Center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (320 // 2)
        self.geometry(f"400x320+{x}+{y}")

        # Try to set icon
        try:
            self.iconbitmap(os.path.join(DISCORD_PATH, "app.ico"))
        except:
            pass

        # Logo
        if os.path.exists(LOGO_PATH):
            logo_image = Image.open(LOGO_PATH)
            logo_image = logo_image.resize((150, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = tk.Label(self, image=self.logo_photo, bg="#23272a")
            self.logo_label.pack(pady=(30, 10))
        
        # Label/Button-style indicator
        self.btn = ctk.CTkButton(
            self, 
            text="STARTING DISCORD    >", 
            width=300, 
            height=50, 
            corner_radius=25,
            fg_color="#36393f",
            hover_color="#36393f",
            text_color="white",
            font=("Arial", 18, "bold")
        )
        self.btn.pack(pady=20)

        # Launch after 1 second
        self.after(500, self.do_launch)

    def do_launch(self):
        if launch_discord():
            self.after(1000, self.destroy)
        else:
            self.btn.configure(text="DISCORD NOT FOUND", fg_color="#f04747")
            self.after(3000, self.destroy)

if __name__ == "__main__":
    app = DiscordLauncherApp()
    app.mainloop()
