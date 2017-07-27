# Virtual Memory

1. We will break both address spaces up into “**pages**”.  
2. Typically **4KB** in size, although sometimes large 
3. Use a “**page table**” to map between virtual pages and physical pages. 
4. The processor generates “virtual” addresses 
5. They are translated via “**address translation**” into physical addresses. 
_from <http://cseweb.ucsd.edu/classes/wi11/cse141/Slides/19_VirtualMemory.key.pdf>_ 
6. build a **cache** for the page mapping, but call it a “_translation lookaside buffer_” or “TLB” 
7. TLBs are **small** (maybe 128 entries), **highly-associative** (often fully-associative) caches for page table entries.

![Virtual memory to Physical memory mapping](https://hiqq5q.by3302.livefilestore.com/y3mN3SOY6bgjZ0hcWQf4dTTTMQ9Z2E8Qy8IXJL_VOlQPQ1m9AYygxWyvNnU6SvH1dk2JPT3dlrzV9m96nDEIfSBaqhkPxZw-6C7IOgh9n3MJP9jAwE6zRA08MmvseFLJ8PFYrEbpk_nRlVFtw3VBjcBtWZRm1Ke8RIgd4XyQHcrWsE?width=615&height=424&cropmode=none)

[<<](../OS.md)
|
[home](README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki)

