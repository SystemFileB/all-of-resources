from cx_Freeze import setup, Executable
from aor import version

# 定义构建选项
build_exe_options = {
    "packages": ["tkinter","os","zipfile","shutil","threading","time","json","webbrowser","aor.core"],
    "excludes": [],
    "include_msvcr": True,
}

# 定义可执行文件
executables = [
    Executable(
        "aor/tkgui.py",
        target_name="aortk.exe",
        base="Win32GUI",  # 这将隐藏控制台窗口
    )
]

# 运行 setup
setup(
    name="AOR",  # 替换为你的应用程序名称
    version=version.version,
    description="All Of Resources",
    options={"build_exe": build_exe_options},
    executables=executables
)