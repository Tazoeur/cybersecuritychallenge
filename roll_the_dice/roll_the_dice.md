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

## Bruteforce

There is a [way](https://github.com/glv2/bruteforce-luks) to bruteforce it, since there is only 5 char length in the examples, I assumed that the user roll dice to find password.

So let's bruteforce it with parameters :

```shell
bruteforce-luks -s "123456" -t 4 -l 5 -m 5 -v 30 chal.img
```

it didn't work.

We then tried to solve it with some dice cryptography theory.

## dice encryption

```txt
26522
26461
64151
16412
32121
55512
```

2 chains :

```txt
26 52 22 64 61 64 15 11 64 12 32 12 15 55 12
```

```txt
0011010 0110100 0010110 1000000 0111101 1000000 0001111 0001011 1000000 0001100 0100000 0001100 0001111 0110111 0001100
```

and

```txt
22 61 35 66 46 25 54 14 15 26 51 21 21 12 12
```

```txt
0010110 0111101 0100011 1000010 0101110 0011001 0110110 0001110 0001111 0011010 0110011 0010101 0010101 0001100 0001100
```
