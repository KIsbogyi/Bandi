import pythoncom, pyHook

def uMad(event):
    return False

hm= pyHook.HookMananger()
hm.MouseAll=uMad
hm.keyAll=uMad
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()
    
