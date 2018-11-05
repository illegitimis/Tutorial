# NPM

- update **npm** to latest version 

```cmd
npm install npm@latest -g
```

- **upgrade npm windows**. Elevated PowerShell.

```ps
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
npm install --global --production npm-windows-upgrade
npm-windows-upgrade
```

- find local package 

```sh
npm list -g | grep 'autorest'
npm list -g --depth 0
npm uninstall -g autorest ms-rest-azure @microsoft.azure/autorest-core @microsoft.azure/autorest.csharp @microsoft.azure/autorest.modeler
```

- search remote package

```sh
npm search autorest
npm info autorest versions
```

[<<](../JS.md) | [home](../../README.md)