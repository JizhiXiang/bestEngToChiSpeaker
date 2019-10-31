@echo off
REM 声明采用UTF-8编码
chcp 65001

echo note
echo 选中中文，按下f1键直接朗读。
echo note
echo 选中英文，按下f2键先翻译成中文，再进行朗读。

python E:\Program_Files\英译中朗读女\auto_read_by_chinese.py
@cmd.exe