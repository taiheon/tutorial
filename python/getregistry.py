import sys
import winreg
import subprocess

#=====================================
# get application path of  AcroRd32.exe, Acrobat.exe
#     if Acrobat is installed, use it. else use Reader
#
# key = winreg.HKEY_LOCAL_MACHINE
# subkey pro = SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Acrobat.exe
# subkey reader = SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\AcroRd32.exe
#===================================
def getAcro():
    key = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    try:
        thePath = winreg.QueryValueEx(winreg.OpenKey(key, r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Acrobat.exe'),"Path")
        acro = thePath[0] + 'Acrobat.exe'
        subprocess.call(acro)
        print(acro)
    except:
        try:
            thePath = winreg.QueryValueEx(winreg.OpenKey(hKey,r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\AcroRd32.exe'),"Path")
            acro = thePath[0] + 'AcroRd32.exe'
            print(acro)
        except:
            print("Please install Adobe Reader or Acrobat Pro. exit")
            sys.exit()
    return acro

#================================
# SmartTag URL Protocol
# requires administrator right
#================================
def config_win():
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Classes\intratech-stag' )
        winreg.SetValue(key, '', winreg.REG_SZ, 'Url:Smartag Protocol')
        winreg.SetValueEx(key, 'URL Protocol', 0 , winreg.REG_SZ, '')
        winreg.CloseKey(key)

        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Classes\intratech-stag\shell\open\command' )
#        winreg.SetValue(key,'',winreg.REG_SZ, '"{0}" "%1"'.format(os.normpath(os.path.abspath(sys.executable))))
        winreg.SetValue(key,'',winreg.REG_SZ, r'smarttag_protocolhandler.exce "%1"')
        winreg.CloseKey(key)

    except(OSError, ImportError):
        print(Col.FAIL + ' FAILED to setup registry link for SmartTag scheme!' + Col.OFF)
        sleep(wait_time)
        sys.exit(2)


#-------------------------------------
#config_win()

acro=getAcro()
subprocess.call(acro)