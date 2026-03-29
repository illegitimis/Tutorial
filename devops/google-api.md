# Google API

## Sheets

- Register project
  - *Google Developers Console* [1] & mine [2]
  - APIs & Services Credentials [3]
  - Authorization OAuth 2.0: legacy v3 [4]
  - migration [5]
  - ASP MVC OAuth 2.0 guide [6] This document describes OAuth 2.0, when to use it, how to acquire client IDs, and how to use it with the Google API Client Library for .NET.
- Sheets API _v4_
  - home [7] & intro [8]
  - .Net quickstart [9]
  - Google API Client Libraries > .NET [10] Get Started
  - Google.Apis.Sheets.v4 [11] Client Library
  - C# DOCS [12] Google Sheets API v4
  - sheets-api-explorer [13], sample rest call batchclear [14]
  - source code [15] for all generated c# strong types
  - basic writing [16]
- Sheets _backend_
  - josdeweger/SheetToObjects [17] A simple *fluent* library which aims to provide developers with an easy solution to _map_ sheets (Google Sheets, Microsoft Excel, csv) to a model/_POCO_. `Install-Package SheetToObjects.Adapters.GoogleSheets`.
  - KozTv/GoogleSheetsDatabase [18] Use your Google Sheet as a  key-value storage DB. `Install-Package GoogleSheetsDatabase`. Values are serialized to JSON to be human-readable and easily editable using standard Google Sheets web interface.
  - commercial `CData.GoogleSheets`. Read, Write, and Update Google Sheets through easy-to-use bi-directional drivers.
- Apps Script
  - Advanced Sheets Service [19] lets you access the Sheets API using Apps Script.
  - apps-script guides rest quickstart dotnet [20]
- Get _file contents_ as JSON
  - `docs.google.com: <Spreadsheet Key [21]>/edit#gid=0`
  - `spreadsheets.google.com: [List|Cells [22]]/<SPREADSHEET_KEY>/public/values?alt=json` gets first sheet _only_
  - _sheet_ fitness [23] sample
  - atom feed fitness [24]
  - Simple example of retrieving JSON feeds from Spreadsheets Data API [25].
  - sample feeds cells [26]

## Sheetsu

- Sheetsu test sheet [27]
- Sheetsu api sample [28]
- Sheetsu docs [29]

## Google Cloud

- API rate limits [30]
- Cloud Memorystore [31] Fully-managed in-memory data store service for Redis.
- dbs [32]
- Managing Notifications [33]
- JSON API authorize requests [34]

## Drive

- Drive.v3 home [35]
- `Install-Package Google.Apis.Drive.v3`
- googleapis/google-api-dotnet-client [36]

[1]: https://console.developers.google.com/flows/enableapi?apiid=sheets.googleapis.com&pli=1
[2]: https://console.developers.google.com/apis/credentials?authuser=1&project=gsheetsapiv4tria-1547050376693
[3]: https://console.developers.google.com/apis/credentials?project=pristine-atom-166920
[4]: https://developers.google.com/sheets/api/v3/authorize
[5]: https://developers.google.com/sheets/api/guides/migration
[6]: https://developers.google.com/api-client-library/dotnet/guide/aaa_oauth#web-applications-aspnet-mvc
[7]: https://developers.google.com/sheets/api/
[8]: https://developers.google.com/sheets/api/guides/concepts
[9]: https://developers.google.com/sheets/api/quickstart/dotnet
[10]: https://developers.google.com/api-client-library/dotnet/get_started
[11]: https://www.nuget.org/packages/Google.Apis.Sheets.v4/
[12]: https://developers.google.com/resources/api-libraries/documentation/sheets/v4/csharp/latest/
[13]: https://developers.google.com/apis-explorer/#p/sheets/v4/
[14]: https://developers.google.com/apis-explorer/#p/sheets/v4/sheets.spreadsheets.values.batchClearByDataFilter
[15]: https://github.com/googleapis/google-api-dotnet-client/blob/master/Src/Generated/Google.Apis.Sheets.v4/Google.Apis.Sheets.v4.cs
[16]: https://developers.google.com/sheets/api/samples/writing
[17]: https://github.com/josdeweger/SheetToObjects
[18]: https://github.com/KozTv/GoogleSheetsDatabase
[19]: https://developers.google.com/apps-script/advanced/sheets
[20]: https://developers.google.com/apps-script/guides/rest/quickstart/dotnet
[21]: https://docs.google.com/spreadsheets/d/<SPREADSHEET_KEY
[22]: https://spreadsheets.google.com/feeds/[list|cells
[23]: https://docs.google.com/spreadsheets/d/1kVelhej2C99mIAZmNFxtY9oSL7OaHKCFfD1lfbVL6Rk/edit#gid=0
[24]: https://spreadsheets.google.com/feeds/list/1kVelhej2C99mIAZmNFxtY9oSL7OaHKCFfD1lfbVL6Rk/od6/public/values?alt=json
[25]: https://developers.google.com/gdata/samples/spreadsheet_sample
[26]: https://spreadsheets.google.com/feeds/cells/1kVelhej2C99mIAZmNFxtY9oSL7OaHKCFfD1lfbVL6Rk/od6/public/values?alt=json
[27]: https://docs.google.com/spreadsheets/d/1WTwXrh2ZDXmXATZlQIuapdv4ldyhJGZg7LX8GlzPdZw/edit#gid=0
[28]: https://sheetsu.com/apis/v1.0/020b2c0f
[29]: https://docs.sheetsu.com/
[30]: https://cloud.google.com/compute/docs/api-rate-limits
[31]: https://cloud.google.com/memorystore/
[32]: https://cloud.google.com/products/#databases
[33]: https://cloud.google.com/resource-manager/docs/managing-notifications
[34]: https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing
[35]: https://developers.google.com/drive/v3/web/about-sdk
[36]: https://github.com/googleapis/google-api-dotnet-client


[<<](./index.md) | [home](../README.md)
