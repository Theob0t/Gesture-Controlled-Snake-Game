from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5"],
                     "optimize": 2}

setup(name = "Snake_Game" ,
      version = "0.1" ,
      description = "" ,
      options = {"build_exe": build_exe_options},
      data_files=[('data', ['./data/score.txt','./data/logo.jpg'])],
      executables = [Executable("Snake_Game.py", base = "Win32GUI")])