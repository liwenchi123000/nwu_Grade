# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\liwen\\Desktop\\Grade_Search\\PrettyPrint.py', 'C:\\Users\\liwen\\Desktop\\Grade_Search\\xml_list.py', 'C:\\Users\\liwen\\Desktop\\Grade_Search', 'C:\\Users\\liwen\\Desktop\\Grade_Search\\main.py'],
             binaries=[],
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
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
