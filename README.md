# tri-func_V 2.0😄

现代软件工程第二段开发

### 开发要求：

将tri-func中的UI替换为本组的UI

### 运行环境：

- python 3.0以上

- 所需python包：tkinter和math

### 项目实现：

#### 修改内容：

- 删除原项目中“+”，“-”，“*”，“/"的四则运算

- 修改原项目中用“=”显示结果为直接点击tri-func中的“sin”，“cos”，“arcsin”和“arctan”出运算结果

- UI 2.0中将不再出现弧度制的转换功能

#### 修改办法：

- 由于1.0版本中0-9的输入与本组项目0-9输入方式不同，且数字输入代码在main函数中，故新建一个main 2.0函数文件，修改0-9的输入方式

- 将本组UI代码中tri-func没有的功能button删除并重新排版

- 调用tri-func项目中的arcsin.py, arctan.py, cos.py, sin.py文件中响应的函数于本组UI生成UI 2.0版本
