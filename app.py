import sys
import os

def main():
    print("--- Python Minimal Console App ---")
    print(f"OS: {sys.platform}")
    print(f"Current Dir: {os.getcwd()}")

    name = input("Enter your name: ")
    print(f"Hello, {name}! This is a standalone binary.")

    input("\nPress Enter to exit...")  # ← これを追加

if __name__ == "__main__":
    main()
