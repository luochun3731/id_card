### 说明：

- 支持随机生成一个（默认）或多个合法的身份证号码
- 支持根据输入的 行政编码+出生日期+性别 生成指定的合法的身份证号码
- 支持根据输入的身份证号码解析身份信息，能校验身份证号码是否合法
- 基于`py2.7` + `tkinter`
- 使用`pyinstaller`打包成单个`exe`文件（`pyinstaller -w -F -p=[project folder] <main py file>`）
