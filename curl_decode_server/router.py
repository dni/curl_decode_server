from base64 import b32decode, b32encode, urlsafe_b64decode, urlsafe_b64encode
from hashlib import sha256

from base58 import b58decode, b58encode
from bech32 import bech32_decode, bech32_encode, convertbits
from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse

from .ascii_art import about, donate, welcome

router = APIRouter()

@router.get("/")
async def root() -> PlainTextResponse:
    return PlainTextResponse(welcome)

@router.get("/about")
async def about_() -> PlainTextResponse:
    return PlainTextResponse(about)

@router.get("/donate")
async def qr() -> PlainTextResponse:
    return PlainTextResponse(donate())

@router.get("/bech32/{data}")
async def bech32(data: str) -> PlainTextResponse:
    _, _data = bech32_decode(data)
    if not _data:
        raise ValueError("Invalid Bech32 data")
    bech32_data = convertbits(_data, 5, 8, False)
    if not bech32_data:
        raise ValueError("Invalid Bech32 data")
    decoded = bytes(bech32_data).decode("utf-8")
    return PlainTextResponse(decoded)


@router.put("/bech32/{hrp}")
async def api_bech32_encode(hrp: str, data: str = Body(...)) -> PlainTextResponse:
    _data = convertbits(data.encode(), 8, 5, True)
    if not _data:
        raise ValueError("Invalid data")
    encoded = bech32_encode(hrp, _data)
    return PlainTextResponse(encoded)


@router.get("/b32/{data}")
async def api_b32_decode(data: str) -> PlainTextResponse:
    decoded = b32decode(data.encode()).decode()
    return PlainTextResponse(decoded)


@router.put("/b32")
async def api_b32_encode(data: str = Body(...)) -> PlainTextResponse:
    encoded = b32encode(data.encode())
    return PlainTextResponse(encoded.decode())


@router.get("/b64/{data}")
async def api_b64_decode(data: str) -> PlainTextResponse:
    decoded = urlsafe_b64decode(data)
    return PlainTextResponse(decoded)


@router.put("/b64")
async def api_b64_encode(data: str = Body(...)) -> PlainTextResponse:
    encoded = urlsafe_b64encode(data.encode())
    return PlainTextResponse(encoded)


@router.get("/b58/{data}")
async def api_b58_decode(data: str) -> PlainTextResponse:
    decoded = b58decode(data)
    return PlainTextResponse(decoded)


@router.put("/b58")
async def b58_encode(data: str = Body(...)) -> PlainTextResponse:
    encoded = b58encode(data)
    return PlainTextResponse(encoded)


@router.get("/sha256/{data}")
async def sha256_hash(data: str) -> PlainTextResponse:
    hashed = sha256(data.encode()).hexdigest()
    return PlainTextResponse(hashed)


@router.get("/2sha256/{data}")
async def double_sha256(data: str) -> PlainTextResponse:
    hashed = sha256(sha256(data.encode()).digest()).hexdigest()
    return PlainTextResponse(hashed)
