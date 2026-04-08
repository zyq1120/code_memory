import pygetwindow as gw

windows = gw.getAllWindows()
for i, win in enumerate(windows):
    if win.title:
        print(f"{i}: {win.title}")
