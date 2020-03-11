from secretsharing import SecretSharer, base64_chars

shares = [
    "1-d71f07c7f934f73b2dd32b90f57012580b198cd6a6282adece628cd31ba86cbd27c070",
    "2-ee2f118884ce06dda892aff3fa8969c909951d9d510f4bd0fbcdf9fce902ddbc76b1d8",
    "3-04a95231b8e74550a671ebf35fdda93d960c2d6ebdaad13fa8eeed8c4f83e80f9670f6",
    "4-801ea582a0be05a76de4cedc856f4e552634fe2a76af7f0c53707ce571d9ef3e64a1d1",
]

solverclass = SecretSharer
# solverclass.secret_charset = base64_chars

print(solverclass.recover_secret(shares))
