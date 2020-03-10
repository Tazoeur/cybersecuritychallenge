# Coding puzzle

original string

```txt
MTcxMWJmOTU5YTBjZGQwNzMwYTNhOWU1ZWQwYzY3YzJ9TTI1MjcwMVBNME01ME0wUVFQMjBMODczNzhONU84UTR7TkROZTU3ZTYzNmE5Nzk2NDUzNjJjOTZlMzJlZWFjNTg5NTE
```

add padding to make it base64 decodable

```txt
$ echo "MTcxMWJmOTU5YTBjZGQwNzMwYTNhOWU1ZWQwYzY3YzJ9TTI1MjcwMVBNME01ME0wUVFQMjBMODczNzhONU84UTR7TkROZTU3ZTYzNmE5Nzk2NDUzNjJjOTZlMzJlZWFjNTg5NTE=" | base64 --decode

1711bf959a0cdd0730a3a9e5ed0c67c2}M252701PM0M50M0QQP20L87378N5O8Q4{NDNe57e636a979645362c96e32eeac58951
```

the string `NDN` is the ceaser cypher of `CSC` and it looks like it was written backward.

So backflip the `M252701PM0M50M0QQP20L87378N5O8Q4` part and apply same ceasar decode as the one needed to convert `NDN` to `CSC` and tada

```txt
CSC{M252701PM0M50M0QQP20L87378N5O8Q4}
```
