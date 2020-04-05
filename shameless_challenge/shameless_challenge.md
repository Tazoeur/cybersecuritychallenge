# The Shameless Challenge

We got only one of the fragmented key.

A search on the famous stackoverflow website give us the other keys.

```txt
4-801ea582a0be05a76de4cedc856f4e552634fe2a76af7f0c53707ce571d9ef3e64a1d1
3-04a95231b8e74550a671ebf35fdda93d960c2d6ebdaad13fa8eeed8c4f83e80f9670f6
2-ee2f118884ce06dda892aff3fa8969c909951d9d510f4bd0fbcdf9fce902ddbc76b1d8
1-d71f07c7f934f73b2dd32b90f57012580b198cd6a6282adece628cd31ba86cbd27c070
```

We first tried to decrypt it ourselve (hense the [shameless.py](data/shameless.py) file) but it didn't work out.

A website did crack it for us and gave us the following twitter account

```txt
https://twitter.com/foryour20792387
```

we then concatenate very posts of that guy and ended up with a massive text.

We splitted the text at every `|` character and a zoom out gave us the key
