import os,shutil as os,sys,re,easygui
from colorama import init,Fore,Back,Style,Cursor
init(autoreset=True)

def roundrect(width, height,text="",color=None):
    if os.get_terminal_size().columns < width:
        width = os.get_terminal_size().columns
    return ("{}╭─{}{}╮\n{}╰{}╯".format(color,text,"─" * (width - 3 - len(text)),("│" + " " * (width - 2) + "│\n")*(height - 2), "─" * (width - 2))+Style.RESET_ALL,width,height)
def RGB(r,g,b):
    return "\033[38;2;{};{};{}m".format(r,g,b)
def visible_length(text):
    # 使用正则表达式匹配ANSI转义序列
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    # 去除ANSI转义序列
    clean_text = ansi_escape.sub('', text)
    # 返回可见字符的长度
    return len(clean_text)
def advprint(text):
    print(text+Cursor.BACK(visible_length(text)),end="")
# 调用函数打印长方形
rect=roundrect(60,5,"ALL OF RESOURCES",RGB(208, 139, 243))
print(rect[0]+Cursor.UP(1)+Cursor.BACK(rect[1]-2),end="")
advprint(Fore.GREEN+"F "+Fore.CYAN+"使用GUI来选择")
print(Cursor.UP(1)+"请输入 .minecraft 路径: ",end="")
mcdir=sys.stdin.read(1)
if mcdir=="w":
    easygui.diropenbox("请选择 .minecraft 路径","All Of Resources")