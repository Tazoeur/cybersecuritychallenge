# Tea 2

> What is this sticky note doing here?
>
> What does "NamingIsTheOriginOfAllParticularThings." even mean..?

I googled `NamingIsTheOriginOfAllParticularThings`, arrived [here](https://twitter.com/hashtag/namingistheoriginofallparticularthings?src=hash), followed the bitly [2B4rm18](https://www.instagram.com/p/BtE3ZZWnAlX/).

I saved the image on the data folder under the name `Dxy2XvzWwAA5vX1.jpeg`.

There is an url with a login form [here](http://34.255.185.219:1906/).

It's exactly the same dump as Tea 1

trying to get some file to work with

```shell
$ for i in $(ls); do strings $i; done | grep -rn -A 2 -B 2 -i 'username'

Binary file 0x70a66000_dump.data matches
Binary file 0x70f0d000_dump.data matches
Binary file 0x70dde000_dump.data matches
Binary file 0x71862000_dump.data matches
```

a fraction of a query that looks interesting

```shell
$ for i in $(ls); do strings $i; done | grep -A 2 -B 2 -i 'username'

e1_interleaving=
+isBehindAT()
```

no time

141520091305