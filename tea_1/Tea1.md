# Tea 1

unzip the `dump.zip`

A quick string scrapping allows us to get the flag :

```shell
for i in $(ls); do strings $i; done | grep -i csc
```

and the following flag appears : `CSC{TheCupOfHumanity...}`
