ruff:
	poetry run ruff check curl_decode_server --fix

dev:
	FORWARDED_ALLOW_IPS=* \
	poetry run fastapi dev curl_decode_server/server.py --host 0.0.0.0 --port 8009

run:
	FORWARDED_ALLOW_IPS=* \
	poetry run fastapi run curl_decode_server/server.py --port 8009
