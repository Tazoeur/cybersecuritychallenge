# Roll the dice

> Employee is gone. The only thing he left behind was this paper on his desk with a few numbers on it. We tried to look at his hard drive, but all the bits look random.
>
> Piece of paper:
> 26522
> 26461
> 64151
> 16412
> 32121
> 55512

The following command can be used to extract a mountable image

```shell
sudo cryptsetup open --type luks chal.img desired-name
```

but it requires a password...

There is a [way](https://github.com/glv2/bruteforce-luks) to bruteforce it, since there is only 5 char length in the examples, I assumed that the user roll dice to find password.

So let's bruteforce it with parameters :

```shell
bruteforce-luks -s "123456" -t 4 -l 5 -m 5 -v 30 chal.img
```
