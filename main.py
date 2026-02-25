'''
=================================
  MAIN ENTRY POINT OF THE PROGRAM.
=================================
'''

import tkinter as tk
from GUI import MiniMathApp

def main():
    root = tk.Tk()
    app = MiniMathApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
