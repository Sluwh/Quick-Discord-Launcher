# Build Script for Discord Launcher
$LogoPath = ".\discord_logo.png"
$IconPath = "$env:LOCALAPPDATA\Discord\app.ico"
$LauncherPath = ".\launcher.py"

pyinstaller --noconfirm --onefile --windowed `
    --icon "$IconPath" `
    --add-data "$($LogoPath);." `
    --collect-all customtkinter `
    --name "Quick Discord Launcher" `
    "$LauncherPath"
