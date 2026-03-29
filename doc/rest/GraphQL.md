# GraphQL

- big issue: overfetching vs new endpoint
- 1 + n queries => data loaders and batch
- how it works, and how to use it [graphql.org learn] | [landscape] | Current Working [draft]

## official C#

`GraphQL` .NET server/client [implementations]

git | package | doc | examples | desc
---|---|---|---|---
[graphql-dotnet] | [GraphQL] | [graphql-dotnet.github.io] | [graphql-dotnet-examples] | continuator of [lmynsberge/graphql-dotnet-netcore]
[graphql-client] | [GraphQL.Client] | - | [GraphQL.Client.Example] | A GraphQL Client for .NET Standard 
[graphql-platform] | [HotChocolate] | [chillicream] | [fetching-from-rest]; [fetching-from-databases]; [dataloader] | Hot Chocolate GraphQL server for .NET, the Strawberry Shake GraphQL client for .NET and Nitro the awesome Monaco based GraphQL IDE. 
[graphql-net] | [GraphQL.Net] | [chkimes] | - | Convert `GraphQL`  and `IQueryable`. netFx only. obsolete

## courses

- Creating GraphQL APIs with ASP.Net Core for Beginners [udemy](https://github.com/mehtanilay10/GraphQL-Demo)
- [fiyazhasan] 12 blog posts
- glenn block _API Development in .NET with GraphQL_ [linkedin](https://www.linkedin.com/learning/api-development-in-dot-net-with-graphql/running-on-mac-and-linux) 2018
- _GraphQL & Caching_: The Elephant in the Room [blog](https://apisyouwonthate.com/blog/graphql-and-caching-the-elephant-in-the-room) 2019
- roland guijt _Building GraphQL APIs with ASP.NET Core_ [pluralsight](https://www.pluralsight.com/courses/building-graphql-apis-aspdotnet-core) 2021 [git](https://github.com/RolandGuijt/PluralsightGraphQL)
- Build Scalable APIs using GraphQL and Serverless [msbuild video](https://azure.microsoft.com/en-us/resources/videos/build-2019-build-scalable-apis-using-graphql-and-serverless/) 2019

## tools

- GitHub _GraphQL API_ [explorer]
- [create-graphless] CLI that generates the code you need for running Graphql with Azure Functions
- [fastify] Fast and low overhead web framework, for `Node.js`

[graphql-dotnet]: https://github.com/graphql-dotnet/graphql-dotnet
[graphql-dotnet.github.io]: https://graphql-dotnet.github.io/docs/getting-started/introduction
[graphql-dotnet-examples]: https://github.com/graphql-dotnet/examples
[lmynsberge/graphql-dotnet-netcore]: https://github.com/lmynsberge/graphql-dotnet-netcore
[GraphQL]: https://www.nuget.org/packages/GraphQL
[graphql-net]: https://github.com/ckimes89/graphql-net
[GraphQL.Net]: https://www.nuget.org/packages/GraphQL.Net
[chkimes]: https://github.com/chkimes/graphql-net/tree/master/docs/introduction
[graphql-platform]: https://github.com/ChilliCream/graphql-platform
[HotChocolate]: https://www.nuget.org/packages/HotChocolate/15.1.0-rc.1
[graphql-client]: https://github.com/graphql-dotnet/graphql-client
[GraphQL.Client]: https://www.nuget.org/packages/GraphQL.Client
[GraphQL.Client.Example]: https://github.com/graphql-dotnet/graphql-client/tree/master/examples/GraphQL.Client.Example
[chillicream]: https://chillicream.com/docs/hotchocolate/v14
[fetching-from-rest]: https://chillicream.com/docs/hotchocolate/v15/fetching-data/fetching-from-rest
[fetching-from-databases]: https://chillicream.com/docs/hotchocolate/v15/fetching-data/fetching-from-databases
[dataloader]: https://chillicream.com/docs/hotchocolate/v14/fetching-data/dataloader
[graphql.org learn]: https://graphql.org/learn/
[graphql-dotnet.github.io-migration4]: https://graphql-dotnet.github.io/docs/migrations/migration4
[landscape]: https://landscape.graphql.org/
[draft]: https://spec.graphql.org/draft/
[fiyazhasan]: https://fiyazhasan.me/tag/graphql/
[explorer]: https://docs.github.com/en/graphql/overview/explorer
[create-graphless]: https://github.com/simonaco/create-graphless
[fastify]: https://github.com/fastify/fastify 
[implementations]: https://graphql.org/code/#c-net
