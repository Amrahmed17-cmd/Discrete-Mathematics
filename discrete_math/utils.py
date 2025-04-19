import os
import platform

def clear_screen():
    """Clear the console screen based on OS"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def pause():
    """Simulate system pause for cross-platform compatibility"""
    input("\nPress Enter to continue...") 