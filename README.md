# Curl Decode Server

## support for

- bech32 (lnurl)
- bech32m (taproot)
- base32
- base58
- base64
- hex
- sha256
- double sha256

### help page

```console
curl dec.dni.guru
```

### decode lnurl

```console
curl dec.dni.guru/bech32/LNURL1DEQW3
```

### encode lnurl

```console
curl -X PUT dec.dni.guru/bech32/lnurl --data 'https://dni.guru'
```

# Home page

```console
$ curl dec.dni.guru
------------------------------------
Welcome to dni's curl en-/decoder :)
------------------------------------
* bech32 decode (curl dec.dni.guru/bech32/<string>)
* bech32 encode (curl -X PUT dec.dni.guru/bech32/<hrp> --data <string>)
* base32 decode (curl dec.dni.guru/b32/<string>)
* base32 encode (curl -X PUT dec.dni.guru/b32 --data <string>)
* base58 decode (curl dec.dni.guru/b58/<string>)
* base58 encode (curl -X PUT dec.dni.guru/b58 --data <string>)
* base64 decode (curl dec.dni.guru/b64/<string>)
* base64 encode (curl -X PUT dec.dni.guru/b64 --data <string>)
* sha256 hash   (curl -X PUT dec.dni.guru/sha256 --data <string>)
* double sha256 (curl -X PUT dec.dni.guru/2sha256 --data <string>)
------------------------------------
request counter: 0
------------------------------------
about (curl dec.dni.guru/about)
donate (curl dec.dni.guru/donate)

made with 🧡 by dni
```

## run the server

```console
poetry install
make run
```
