# Curl Decode Server
## support for
* bech32 (lnurl)
* bech32m (taproot)
* base32
* base58
* base64
* hex
* sha256
* double sha256

## run
```console
poetry install
make run
```


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
