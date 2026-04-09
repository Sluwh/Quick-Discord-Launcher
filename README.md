# Quick Discord Launcher

Small utility to launch Discord on Windows without dealing with broken shortcuts after updates.

### Why this exists?
Discord installs itself into folders named `app-1.x.x`. When it updates, Windows shortcuts often break because they point to an old version folder that no longer exists. This launcher finds the latest version folder automatically and starts the app from there.

### How it works
1. Scans `%LOCALAPPDATA%/Discord` for folders starting with `app-`.
2. Sorts them to find the highest version.
3. Launches `Discord.exe` and exits immediately.

### Installation
- Download the latest `.exe` from the [Releases](https://github.com/Sluwh/Quick-Discord-Launcher/releases) section.
- Put it anywhere and pin it to your taskbar.

### Building from source
If you want to build it yourself, you'll need Python and `customtkinter`.
```powershell
pip install customtkinter Pillow pyinstaller
./build.ps1
```

The executable will be generated in the `dist/` folder.
