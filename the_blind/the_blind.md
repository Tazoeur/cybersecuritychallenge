# The blind

The only data we have is a blank file.

The global selection of the file shows that there is some data in there, composed only with space or tabulation.

The solution is to :

- search spaces and replace them with a '0'
- search tabluations and replace theme with a '1'

This should give us the following sequence :

```text
0001111101
0001100100
0001101110
000110001
0001101100
0001100010
0001011111
0001111001
0001101100
000110011
0001110100
000110011
0001101100
0001110000
0001101101
000110000
0001100011
0001011111
0001001101
0001100001
0001011111
000110001
0001111011
0001000011
0001010011
0001000011
```

Which is the ascii code for

```text
}dn1lb_yl3t3lpm0c_Ma_1{CSC
```

That needs to be reverted to obtain the final flag.
