# MusicPop-ups

# 项目描述

本项目的目标是创建一个 Python 应用程序，它可以分析给定的音频文件，检测其中的重音点，并在播放音频时，根据这些重音点弹出具有随机内容和图片的弹窗。

## 功能

- **音频分析**：使用 `librosa` 库来检测音频文件中的重音点。
- **弹窗提示**：使用 `tkinter` 库在重音点出现时弹出提示窗口。
- **随机内容**：弹窗内容从预定义的列表中随机选择。
- **随机图片**：弹窗有 20% 的概率附带一张图片 `image.png`。

## 依赖库

- `librosa`：用于音频分析。
- `sounddevice`：用于播放音频。
- `tkinter`：用于创建弹窗。
- `numpy`：用于数据处理。

## 安装依赖

确保你已安装了所需的 Python 库。可以通过以下命令安装：

```bash
pip install librosa sounddevice numpy
```

## 使用方法

1. **准备音频文件**：
   - 确保你的音频文件是 MP3 格式，并将其命名为 `audio.mp3` 或更改代码中的文件路径以匹配你的文件名。

2. **准备图片文件**：
   - 确保 `image.png` 图片文件存在于与脚本相同的目录中。

3. **运行主程序**：
   - 运行 `main.py` 以生成用于播放音频和弹窗提示的子脚本。

   ```bash
   python main.py
   ```

4. **运行生成的子脚本**：
   - 运行生成的 `generated_script.py` 来播放音频并显示弹窗。

   ```bash
   python generated_script.py
   ```

## 代码说明

- **`main.py`**：主程序，负责生成 `generated_script.py` 子脚本。
  - `analyze_beats(audio_path)`：分析音频文件中的重音点。
  - `generate_script(audio_path, output_script_path)`：生成带有弹窗功能的 Python 脚本。
  - `main(audio_path)`：主函数，设置音频文件路径并生成脚本。

- **`generated_script.py`**：由 `main.py` 生成，用于播放音频并弹出提示窗口。

## 注意事项

- 确保 Python 环境已正确配置，并已安装所有必要的依赖库。
- 图片文件 `image.png` 需要放在脚本所在目录，以便弹窗可以正确加载图片。
- 
---

如果你有任何问题或建议，请联系项目维护者。(其实项目维护者是个fvv，这些所有代码都是GPT-4o写的)

    ```
    我们的口号是！咕咕咕！
    ```

