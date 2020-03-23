from cx_Freeze import setup, Executable

setup(name = "Snake_Game" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("Snake_Game.py", base = "Win32GUI")])