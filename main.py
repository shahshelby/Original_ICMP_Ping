import PyInstaller.__main__

# Your script file name
script_name = 'testping.py'

# Run PyInstaller
PyInstaller.__main__.run([
    '--onefile',        # Create a single executable file
    '--windowed',       # No console window (for GUI apps); omit for console apps
    script_name         # The script you want to compile
])