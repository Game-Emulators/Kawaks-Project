## Kawaks
- Kawaks 1.65 Latest version of Kawaks.
- High res Kawaks skin (optional) unzip in the same directory as WinKawaks.exe
- Screen shot preview package 1.32 (optional) 2.7mb (unzip in SSHOTS directory)
- Screen shot preview package upgrade 1.32 to 1.38 (optional) 137kb (unzip in SSHOTS directory)
- Screen shot preview package upgrade 1.38 to 1.42 (optional) 71kb (unzip in SSHOTS directory)

### Support files
- mfc4261.zip Unzip this in C:\WINDOWS\SYSTEM if Kawaks complains about mfc42.dll, msvcrt.dll or msvcirt.dll
- msvcp60.dll Unzip this in C:\WINDOWS\SYSTEM if Kawaks complains about msvcp60.dll
- W95ws2setup.exe Download and install this if you have problems about "Ws2_32.dll" (needed by Kaillera) *DO NOT INSTALL THIS IF - KAWAKS DOESN'T ASK FOR IT*
- redump36.zip A tool to convert old NeoGeo dumps (N10234489.078) to Kawaks compliant dumps (game_p1.rom)

### Links 
- [Kaillera-Game-Server](https://github.com/yaowenxu/Projects/tree/master/Kaillera-Game-Server)
- [WinKawaks](https://www.winkawaks.org/index.htm)
- [Kawaks](http://kawaks.retrogames.com/)
- [Kawaks Project document arrangement](https://www.cnblogs.com/xuyaowen/p/Kawaks-project.html)
- [Game ROMs Collection](https://github.com/Game-Emulators/Kawaks-ROMs)

### WinKawaks structure
```
D:\WinKawaks
   |
   +--blend               -- 
   |
   +--capture             -- Where the Captured file(s) stored
   |
   +--cheats              -- Where the Cheats file(s) stored
   |
   +--eeprom              -- 
   |
   +--ini                 --
   |
   +--lang                -- Language Package
   |  |
   |  |-Arabic.lng
   |  |
   |  |-
   |  |
   |  |-..
   |
   +--lang                -- Language Package
   |
   +--roms                -- As default, Winkawaks scans this folder for roms
   |  |
   |  |-cps1              -- Save as above
   |  |
   |  |-cps2              -- Save as above
   |  |
   |  |-neogeo            -- Save as above
   |
   +--saves               -- 
   |
   +--sshots              -- 
   |
   +--tracklst            -- 
   |
   +--defaultkeysCPS.ini  -- 
   |
   +--DefaultWinKawaksINI.zip  -- The default WinKawaks.ini stored in this archive.
   |
   +--faq.txt             -- Frequently Asked Questions
   |
   +--kailleraclient.dll  -- NetPlay Client dll
   |
   +--sample_ini_files.zip-- Sample ini Files
   |
   +--whatsnew.txt        -- Full Release Log
   |
   +--WinKawaks.exe       -- WinKawaks Main File
```