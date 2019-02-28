# Cryptography GCP Cloud Function

GCP Cloud function that can create a encryption key, encrypt and decrypt data with a key. Utilizes python `cryptography` library and has a basic UI for testing.

## REST API

JSON REST API that returs `{data: str}` object.

| Method | Route | Payload | Info |
| ------ | ----- | --------| ---- |
| `GET`  | `/cryptography` |  | Render UI
| `POST`  | `/cryptography` | `{action: "get_key"}` | Creates a secret key
| `POST`  | `/cryptography` | `{action: "encrypt", key: str, data: str}` | Encrypts data with a key
| `POST`  | `/cryptography` | `{action: "decrypt", key: str, data: str}` | Decrypts data with a key
