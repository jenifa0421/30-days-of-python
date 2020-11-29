#1

import mymodule
#BEFORECHANGING
print(mymodule.l)
mymodule.l[0]=7
#AFTER CHANGING
print(mymodule.l)

OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
[1, 2, 3, 4]
[7, 2, 3, 4]

#2
import pandas as pd
s=pd.Series([2,4,5,6,7])
print(s)

OUTPUT
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
0    2
1    4
2    5
3    6
4    7
dtype: int64

#3
import random
print(random.randint(1,100))

OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
20

#4

import sys
print(sys.path)


OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
['C:\\Users\\Home\\PycharmProjects\\pythonProject2', 'C:\\Users\\Home\\PycharmProjects\\pythonProject2', 'C:\\Users\\Home\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\Home\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\Home\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\Home\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\Home\\PycharmProjects\\pythonProject2\\venv', 'C:\\Users\\Home\\PycharmProjects\\pythonProject2\\venv\\lib\\site-packages']

#5

C:\Users\Home>pip install pandas
Collecting pandas
  Downloading pandas-1.1.4-cp39-cp39-win_amd64.whl (8.9 MB)
     |████████████████████████████████| 8.9 MB 3.3 MB/s
Collecting pytz>=2017.2
  Downloading pytz-2020.4-py2.py3-none-any.whl (509 kB)
     |████████████████████████████████| 509 kB 3.3 MB/s
Collecting numpy>=1.15.4
  Downloading numpy-1.19.4-cp39-cp39-win_amd64.whl (13.0 MB)
     |████████████████████████████████| 13.0 MB 30 kB/s
Collecting python-dateutil>=2.7.3
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 6.8 MB/s
Collecting six>=1.5
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: pytz, numpy, six, python-dateutil, pandas
Successfully installed numpy-1.19.4 pandas-1.1.4 python-dateutil-2.8.1 pytz-2020.4 six-1.15.0
WARNING: You are using pip version 20.2.3; however, version 20.2.4 is available.
You should consider upgrading via the 'c:\users\home\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip' command.

C:\Users\Home>pip uninstall pandas
Found existing installation: pandas 1.1.4
Uninstalling pandas-1.1.4:
  Would remove:
    c:\users\home\appdata\local\programs\python\python39\lib\site-packages\pandas-1.1.4.dist-info\*
    c:\users\home\appdata\local\programs\python\python39\lib\site-packages\pandas\*
Proceed (y/n)? y
  Successfully uninstalled pandas-1.1.4