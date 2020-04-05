# Zippy zip zip

got one archived file.

extract it.

another archived file.

It looks like the flag will be inside a file that is compressed many times, in different archive formats.

The solution would be to install a multi format archive manager (`dtrx`) and to run a script that keep extracting while there is an archive.

```shell
while true; do echo extracting...; dtrx -rf flag.gbip.1; done
```

solved !
