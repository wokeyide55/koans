from distutils.core import setup
import py2exe

setup(
    options={
        'py2exe': {
            'bundle_files': 1,  # 包含所有文件
            'compressed': True  # 压缩文件
        }
    },
    windows=[{
        'script': 'learn1.py' # 替换为您的脚本文件名
        #'icon_resources': [(1, "heart.ico")]  # 可选：添加图标文件
    }],
    zipfile=None,
)
