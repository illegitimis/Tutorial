---
title: SQL LocalDB
layout: default
nav_order: 17
parent: SQL
grand_parent: Data
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# SQL LocalDB

c:\Program Files\Microsoft SQL Server\130\Tools\Binn\SqlLocalDB.exe \
c:\Program Files\Microsoft SQL Server\150\Tools\Binn\SqlLocalDB.exe

```cmd
sqllocaldb.exe i
MSSQLLocalDB
sqllocaldb.exe i MSSQLLocalDB
Name:               MSSQLLocalDB
Version:            15.0.4153.1
Shared name:
Auto-create:        Yes
State:              Stopped

sqllocaldb.exe start MSSQLLocalDB
LocalDB instance "MSSQLLocalDB" started.
Instance pipe name: np:\\.\pipe\LOCALDB#5F469504\tsql\query

sqllocaldb.exe stop "MSSQLLocalDB"
LocalDB instance "MSSQLLocalDB" stopped.
```

Configure the Windows Firewall to allow SQL Server access [1]:

```cmd
netsh firewall set portopening protocol = TCP port = 1433 name = SQLPort mode = ENABLE scope = SUBNET profile = CURRENT
netsh firewall set portopening protocol = UDP port = 1434 name = SQLPort mode = ENABLE scope = SUBNET profile = CURRENT

netsh advfirewall firewall add rule name = SQLPort dir = in protocol = tcp action = allow localport = 1433 remoteip = localsubnet profile = DOMAIN
netsh advfirewall firewall add rule name = SQLPort dir = in protocol = udp action = allow localport = 1434 remoteip = localsubnet profile = DOMAIN
```

Getting started with SQL Server 2017 Express LocalDB [2]

```powershell
New-NetFirewallRule -DisplayName "SQLServer default instance" -Direction Inbound -LocalPort 1433 -Protocol TCP -Action Allow
New-NetFirewallRule -DisplayName "SQLServer Browser service" -Direction Inbound -LocalPort 1434 -Protocol UDP -Action Allow
```

---

C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Data

```powershell
Get-Service | ?{ $_.DisplayName -like "SQL Server (*" }
```

```cmd
AzureStorageEmulator.exe init -sqlinstance . -server MSSQLSERVER
```

[1]: https://learn.microsoft.com/en-us/sql/sql-server/install/configure-the-windows-firewall-to-allow-sql-server-access?view=sql-server-ver16
[2]: https://www.mssqltips.com/sqlservertip/5612/getting-started-with-sql-server-2017-express-localdb/

[<](./index.md) | [<<](/index.md)
