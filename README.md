# 📦 All Of Resources
一个工具可以从client.jar和.minecraft/assets文件夹提取minecraft所有资源的工具  
请勿分发使用这个程序提取出来的资源，这些资源仅用作资源包的开发，我不会对此承担任何责任

这个程序的图标使用了[IconPark](https://iconpark.oceanengine.com/official)的箱子图标，这个部分使用[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)授权

## 🛠️ 安装
1. 使用pip安装
    ```bash
    pip install all-of-resources
    ```
    运行
    ```bash
    # Flutter界面
    aor

    # Tk界面
    aortk
    ```

2. 针对Windows的二进制文件
   直接下载并解压Release的`all-of-resources_1.00_windows.7z`文件，然后运行`aortk.exe`  
   
   谁知道怎么打包Flutter界面的aor.exe呀，我`flet build windows`打包不了，欢迎提交PR帮一下我！

## 🖼️ 截图
| ![](./screenshot1.png) | ![](./screenshot2.png) |
| :--------------------: | :--------------------: |
|       Tkinter界面      |       Flutter界面       |

## 📓 更新日志
### 1.10.4
- 修复安卓版本直接启动不了了！
- 这个Bug太离谱了

### 1.10.3
⚡没有Bug，只有特性⚡
- 修复了安卓11+用不了的问题，好奇怪呀
- 缩短了关于文字
- 移除了Herobrine

### 1.10.2
- 不小心上传了1.10.1，然后没有放icon.png这个文件，这个版本修复

### 1.10.1
- 手机的图标有点不对劲 (flet默认图标)... 我给他修了
- 现在手机端分离了apk，armabi和arm64两个架构使用了不同的安装包，减小了apk的大小

### 1.10
- 分离了前后端
- 添加了flet前段以支持手机
- 移除了Herobrine

### 1.00
- 第一个版本