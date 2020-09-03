# -*- mode: python -*-

block_cipher = None


a = Analysis(['McMasterSelenium.py'],
             pathex=['C:\\Users\\jzerez\\Documents\\GitHub\\McMaster-BOM-Maker'],
             binaries=[('./chromedriver_win32/chromedriver.exe', './chromedriver_win32')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='McMasterSelenium',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
