# Virtual Memory

1. We will break both address spaces up into “**pages**”.  
2. Typically **4KB** in size, although sometimes large
3. Use a “**page table**” to map between virtual pages and physical pages.
4. The processor generates “virtual” addresses
5. They are translated via “**address translation**” into physical addresses.
> from http://cseweb.ucsd.edu/classes/wi11/cse141/Slides/19_VirtualMemory.key.pdf
6. build a **cache** for the page mapping, but call it a “_translation lookaside buffer_” or “TLB”
7. TLBs are **small** (maybe 128 entries), **highly-associative** (often fully-associative) caches for page table entries.
8. Virtual memory to Physical memory mapping 
![Virtual memory to Physical memory mapping](http://slideplayer.com/slide/5352359/17/images/18/Virtual-to-Physical+Memory+Address+Mapping.jpg)

[<<](../os.md) | [home](../../README.md)