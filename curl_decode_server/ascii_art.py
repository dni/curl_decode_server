from io import StringIO

from qrcode import QRCode

url = "dec.dni.guru"
lnaddress = "dni@600.wtf"
nostr = "https://njump.me/nprofile1qqspe9xqk3zh0m05z5yaguaf9k0hk67qfcawqlmstecfc2vek8f7qaqx0juux"
github = "https://github.com/dni"
repo = "https://github.com/dni/curl_decode_server"
x = "https://x.com/dnilabs"


spacer = "[38;5;226m" + "-" * 44 + "[0m"

footer = """
made with [38;5;196m❤[0m by [38;5;226mdni[
"""

help = f"""
{spacer}
[38;5;226m*[0m bech32 decode ([38;5;082mcurl {url}/bech32/<string>[0m)
[38;5;226m*[0m bech32 encode ([38;5;098mcurl -X PUT {url}/bech32/<hrp> --data <string>[0m)
[38;5;226m*[0m base32 decode ([38;5;082mcurl {url}/b32/<string>[0m)
[38;5;226m*[0m base32 encode ([38;5;098mcurl -X PUT {url}/b32 --data <string>[0m)
[38;5;226m*[0m base58 decode ([38;5;082mcurl {url}/b58/<string>[0m)
[38;5;226m*[0m base58 encode ([38;5;098mcurl -X PUT {url}/b58 --data <string>[0m)
[38;5;226m*[0m base64 decode ([38;5;082mcurl {url}/b64/<string>[0m)
[38;5;226m*[0m base64 encode ([38;5;098mcurl -X PUT {url}/b64 --data <string>[0m)
[38;5;226m*[0m sha256 hash   ([38;5;098mcurl -X PUT {url}/sha256 --data <string>[0m)
[38;5;226m*[0m double sha256 ([38;5;098mcurl -X PUT {url}/2sha256 --data <string>[0m)
{spacer}
about ([38;5;082mcurl {url}/about[0m)
donate ([38;5;082mcurl {url}/donate[0m)
{footer}"""

welcome = f"""{spacer}
[38;5;32mWelcome to dni's curl en-/decoder :)[0m{help}"""

not_found = f"""{spacer}
[38;5;32m[38;5;196m404[0m - encoding not found :([0m{help}"""

error = """[38;5;32m[38;5;196mERROR[0m - encoding/decoding failed :("""

about = f"""
[38;5;32msocials[0m
{spacer}
[38;5;226m*[0m nostr ([38;5;082m{nostr}[0m)
[38;5;226m*[0m github ([38;5;082m{github}[0m)
[38;5;226m*[0m x ([38;5;082m{x}[0m)
{spacer}
[38;5;226m*[0m repository ([38;5;082m{repo}[0m)
{footer}"""

def donate():
    qr = QRCode()
    qr.add_data(f"lightning:{lnaddress}")
    f = StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    qr_ascii = f.read()
    return f"""{qr_ascii}{spacer}
Lightning address: [38;5;082m{lnaddress}[0m
{spacer}
{footer}"""
