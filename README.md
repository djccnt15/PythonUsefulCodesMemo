## Python Useful Codes Memo
- DataFrame_Header.py : control DataFrame column name collectively with lambda
- DataFrame_column_calculating.py : calculating Pandas DataFrame by column
- count_runtime.py : count runtime of the file
- make_folder.py : make folder if working directory has no declared name of folder
- pause.py : pause .py file
- regression_modeling.py : modeling regression easily by using for

## Python Useful Packages Memo
#### Data mining
- Pandas : DataFrame
- Numpy
- Scikit-learn
- Scipy
#### Deeplearning
- tensorflow
- keras
- Pytorch
#### system handling
- os
- sys
#### web handling
- beautifulsoup4 : crawling
- selenium : web browser control, needs webdriver
#### plotting
- matplotlib
- yellowbrick : visualization with machine learning
- ggplot
- seaborn

## pyinstaller
#### make py file to exe file  
basic form

    C:\PyProject\test>pyinstaller --clean --onefile FileName.py
    
make .spec file first and make exe file following the spec file

    C:\PyProject\test>pyi-makespec test.py --onefile --add-binary "chromedriver.exe";"."
    C:\PyProject\test>pyinstaller --clean --onefile test.py

if you have multi level import, pyinstaller won't recognize the hidden-multi level import.    
so you have to make .spec file first, open the file with text editor, and than declare that there are hidden imports in your code.    
look at the changing example below.   

    a = Analysis(hiddenimports=['your_multi_level_imported_packeges'],)

this will make pyinstaller gether all the hidden-multi level import at once.    

#### reference
https://pyinstaller.readthedocs.io/en/stable/index.html   
https://pyinstaller.readthedocs.io/en/stable/spec-files.html
