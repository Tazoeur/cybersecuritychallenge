# Fake News

An image with a skull and the following strings is given

```txt
HACKED BY PINOCCHIO

GREETZ TO::::MOBYDICK===LILO&STITCH===POCAHONTAS===B-FOOT_BALOO===JIMMY_TWOFEET===DUMBO
```

reference to disney is omnipresent

- bigfoot
- jimmy two shoes

In the registry, I found that the user used a custom DNS : `54.154.165.103`

The ip of the `youtu.be` returned by the dns : `216.58.211.110`

After investigation, it appears that the DNS server also happens to host a `whois` server, wich does not makes sense.

It is possible to query the `whois` server.

```shell
for i in "MOBYDICK" "LILO&STITCH" "POCAHONTAS" "B-FOOT_BALOO" "JIMMY_TWOFEET" "DUMBO" "PINOCCHIO"; do (echo $i | nc 54.154.165.103 43) ; done

echo "HACKED BY PINOCCHIO" | nc 54.154.165.103 43
```

I got some messages like "you are close but no cigar" and others like it, announcing that I've reach a dead end.