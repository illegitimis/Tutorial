---
title: Handle (Sysinternals)
layout: default
nav_order: 15
parent: DevOps
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Handle (Sysinternals)

`Handle` v4.22 [1] — search mode (enabled by specifying a name fragment as a parameter)

```cmd
if exist "$(TargetPath).locked" del "$(TargetPath).locked"
if not exist "$(TargetPath).locked" move "$(TargetPath)" "$(TargetPath).locked"
```

Unlock a file handle locked by SYSTEM or any other active process [2]

```cmd
Handle64.exe > output.txt
```

How to unlock file locked by SYSTEM or app process [3]

```cmd
Handle64.exe -a "C:\Program Files\App"
handle64.exe -p excel.exe
Handle.exe -a C:\Path\To\Resource\That\Is\Locked\Open > Output.txt
handle.exe -c <handleID> -p <processID>
```

Sysinternals Handle tutorial [4] \
`Unlock-File.ps1` [5] \
Unlock file handle gist [6]

[1]: https://docs.microsoft.com/en-us/sysinternals/downloads/handle
[2]: https://www.ryadel.com/en/unlock-file-handle-locked-system-active-process-windows/
[3]: http://woshub.com/unlock-file-locked-windows-system-process/
[4]: https://adamtheautomator.com/sysinternals-handle/
[5]: https://github.com/ztrhgf/useful_powershell_functions/blob/master/Unlock-File.ps1
[6]: https://gist.github.com/rgl/1861f2c6642ab79dd4cae6e488635c1a

[<](./index.md) | [<<](/index.md)
