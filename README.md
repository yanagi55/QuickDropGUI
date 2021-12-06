## Python Drag-and-Drop GUI with wxPython
---
Create a window which able to accept files with Drag-and-Drop

どうしてもファイルのドラッグ&ドロップを使いたいのに、  
簡単に書けるちょうど良いツールが無いので、モジュールとしてまとめます。  

ドラッグ&ドロップを使わないなら、  
大抵は PythonSimpleGUI を使うほうが良いと思います。  


## How to use
---
```python
from simple_drop import get_filelist
paths = get_filelist()

print(paths)
$ ['filepathA', 'filepathB', ...]
```

