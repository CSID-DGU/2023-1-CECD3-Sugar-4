from cx_Freeze import setup, Executable

setup(
    name="SugarProject",
    version="1.0",
    description="De-identify your privacy",
    executables=[Executable("sugar.py")],
    packages=["app","app.Model","app.gui"],
    include_files=[],
)