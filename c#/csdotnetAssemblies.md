# Assemblies

## Combining managed modules into assemblies

a single PE file that represents the logical grouping of files managed PE files: they always use the 32 bit PE file format, not the 64−bit PE file format. On 64−bit Windows systems, the OS loader detects the managed 32−bit PE file and automatically knows to create a 64−bit address space


When you build an EXE assembly, the compiler/linker emits some special information into the resulting assembly’s PE file header and the file’s .text section. When the EXE file is invoked, this special information causes the CLR to load and initialize. The CLR then locates the application’s entry point method and allows the application to start executing. 

Similarly, if an unmanaged application calls LoadLibrary to load a managed assembly, the DLL’s entry point function knows to load the CLR in order to process the code contained within the assembly.

![1](https://6ebcoa.by3302.livefilestore.com/y3msInvUWYmlQWTfxO2xXQ3gg-4tPwdAT__cxyivXLPgn5HS_GhMsWvEpXnfKgpt1_qvWslKAJH8Dq9OPzYKo7ChYdQZTYgd9N40ugZ_dl-Z-GX2zvdKxQLYsPOKD---WdlI0M0d0VMvO1q7DIMr9G6hjK_JS4GDj28IkuT9hnswps?width=787&height=378&cropmode=none)

![2](https://fpnlua.by3302.livefilestore.com/y3mzvjADQSazTtbUSSZ1fr4NVUlrfjwjgcXUCb79t_wNoohxRx8SjrNrqbSdqFwR3jEmz7NGih7vXqwWHMndDFHs6XzF9C4FWRftCE0zA-SMBykCQDMUvpvKNepAhPyo29p1czf4x17Hd21CxPBWQM3il2QYEu3WcotBPaIGbJ3nyQ?width=819&height=644&cropmode=none)


