# Foreground vs Background threads

_Thread pool threads are  background threads._

Concerning exception behavior, no difference exists between background and foreground threads: **Unhandled exceptions in either of them terminate the entire process**.

The only altered behavior of a background thread is that _it won’t keep the process from being terminated after all foreground threads have quit_. 
In other words, **a foreground thread can keep a process alive until it exits**, whereas a background thread can’t. 

[<<](../parallel.md) 
| 
[home](https://github.com/illegitimis/Tutorial) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 