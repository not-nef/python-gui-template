rmdir /Q /S dist
pyinstaller main.py --onefile --windowed --collect-data sv_ttk
rmdir /Q /S build
rmdir /Q /S __pycache__
del /Q /S main.spec