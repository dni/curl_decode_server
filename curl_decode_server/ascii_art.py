url = "dec.dni.guru"

spacer = "[38;5;226m" + "-" * 40

footer = f"""
{spacer}
[38;5;226m*[0m bech32 decode ([38;5;082mcurl {url}/bech32/<string>[0m)
[38;5;226m*[0m bech32 encode ([38;5;098mcurl -X PUT {url}/bech32/<hrp> --data https://dni.guru[0m)
[38;5;226m*[0m base32 decode ([38;5;082mcurl {url}/b32/<string>[0m)
[38;5;226m*[0m base32 encode ([38;5;098mcurl -X PUT {url}/b32 --data https://dni.guru[0m)
[38;5;226m*[0m base58 decode ([38;5;082mcurl {url}/b58/<string>[0m)
[38;5;226m*[0m base64 decode ([38;5;082mcurl {url}/b64/<string>[0m)
[38;5;226m*[0m sha256 hash   ([38;5;098mcurl -X PUT {url}/sha256 --data https://dni.guru[0m)
[38;5;226m*[0m double sha256 ([38;5;098mcurl -X PUT {url}/2sha256 --data https://dni.guru[0m)

made with [38;5;196m❤[0m by [38;5;226mdni[0m"""

welcome = f"""{spacer}
[38;5;32mWelcome to dni's univeral decoder :)[0m{footer}"""

not_found = f"""{spacer}
[38;5;32m[38;5;196m404[0m - encoding not found :([0m{footer}"""

error = f"""[38;5;32m[38;5;196mERROR[0m - encoding/decoding failed :("""
