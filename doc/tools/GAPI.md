# Google API

## Sheets

- Register project
  - [*Google Developers Console*](https://console.developers.google.com/flows/enableapi?apiid=sheets.googleapis.com&pli=1)
  - APIs & Services [Credentials](https://console.developers.google.com/apis/credentials?project=pristine-atom-166920)
  - Authorization OAuth 2.0: legacy [v3](https://developers.google.com/sheets/api/v3/authorize)
  - [migration](https://developers.google.com/sheets/api/guides/migration)
  - [ASP MVC OAuth 2.0 guide](https://developers.google.com/api-client-library/dotnet/guide/aaa_oauth#web-applications-aspnet-mvc) This document describes OAuth 2.0, when to use it, how to acquire client IDs, and how to use it with the Google API Client Library for .NET.
- Sheets API _v4_
  - [home](https://developers.google.com/sheets/api/)
  - [.Net quickstart](https://developers.google.com/sheets/api/quickstart/dotnet)
  - [Google API Client Libraries > .NET](https://developers.google.com/api-client-library/dotnet/get_started) Get Started
  - [Google.Apis.Sheets.v4](https://www.nuget.org/packages/Google.Apis.Sheets.v4/) Client Library
  - [C# DOCS](https://developers.google.com/resources/api-libraries/documentation/sheets/v4/csharp/latest/) Google Sheets API v4
  - [sheets-api-explorer](https://developers.google.com/apis-explorer/#p/sheets/v4/)
  - [source code](https://github.com/googleapis/google-api-dotnet-client/blob/master/Src/Generated/Google.Apis.Sheets.v4/Google.Apis.Sheets.v4.cs) for all generated c# strong types
  - [basic writing](https://developers.google.com/sheets/api/samples/writing)
- Sheets _backend_
  - [josdeweger/SheetToObjects](https://github.com/josdeweger/SheetToObjects) A simple *fluent* library which aims to provide developers with an easy solution to _map_ sheets (Google Sheets, Microsoft Excel, csv) to a model/_POCO_. `Install-Package SheetToObjects.Adapters.GoogleSheets`.
  - [KozTv/GoogleSheetsDatabase](https://github.com/KozTv/GoogleSheetsDatabase) Use your Google Sheet as a  key-value storage DB. `Install-Package GoogleSheetsDatabase`. Values are serialized to JSON to be human-readable and easily editable using standard Google Sheets web interface.
  - commercial `CData.GoogleSheets`. Read, Write, and Update Google Sheets through easy-to-use bi-directional drivers.
- Apps Script
  - [Advanced Sheets Service](https://developers.google.com/apps-script/advanced/sheets) lets you access the Sheets API using Apps Script.
  - [apps-script guides rest quickstart dotnet](https://developers.google.com/apps-script/guides/rest/quickstart/dotnet)
- Get _file contents_ as JSON
  - `https://docs.google.com/spreadsheets/d/<SPREADSHEET_KEY>/edit#gid=0`
  - `https://spreadsheets.google.com/feeds/[list|cells]/<SPREADSHEET_KEY>/public/values?alt=json` gets first sheet _only_
  - _sheet_ [fitness](https://docs.google.com/spreadsheets/d/1kVelhej2C99mIAZmNFxtY9oSL7OaHKCFfD1lfbVL6Rk/edit#gid=0) sample
  - atom feed [fitness](https://spreadsheets.google.com/feeds/list/1kVelhej2C99mIAZmNFxtY9oSL7OaHKCFfD1lfbVL6Rk/od6/public/values?alt=json)
  - [Simple example of retrieving JSON feeds from Spreadsheets Data API](https://developers.google.com/gdata/samples/spreadsheet_sample).

## Sheetsu

- [Sheetsu test sheet](https://docs.google.com/spreadsheets/d/1WTwXrh2ZDXmXATZlQIuapdv4ldyhJGZg7LX8GlzPdZw/edit#gid=0)
- [Sheetsu api sample](https://sheetsu.com/apis/v1.0/020b2c0f)
- [Sheetsu docs](https://docs.sheetsu.com/)

## Google Cloud

- [API rate limits](https://cloud.google.com/compute/docs/api-rate-limits)
- [Cloud Memorystore](https://cloud.google.com/memorystore/) Fully-managed in-memory data store service for Redis.
- [dbs](https://cloud.google.com/products/#databases)
- [Managing Notifications](https://cloud.google.com/resource-manager/docs/managing-notifications)
- JSON API [authorize requests](https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing)

## Drive

- [Drive.v3 home](https://developers.google.com/drive/v3/web/about-sdk)
- `Install-Package Google.Apis.Drive.v3`
- [googleapis/google-api-dotnet-client](https://github.com/googleapis/google-api-dotnet-client)

[<<](../tools.md) | [home](../../README.md)