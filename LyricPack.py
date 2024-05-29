from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "syncedlyrics", "glob", "cutlet", "time", "re", "unidic_lite", "rapidfuzz"],
    "include_files": [r"C:\Users\Aria\AppData\Local\Programs\Python\Python312\Lib\site-packages\unidic_lite\dicdir"]
}

setup(name="Lyric Finder", version="1.0", description="Lyric Finder", options={"build_exe": build_exe_options}, executables=[Executable("Lyric Find.py")])