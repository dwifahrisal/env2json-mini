# env2json

Kecil, satu file, gak ada dependency. Ubah `.env` jadi `env.json`:

```bash
python3 env2json.py .env config.json
```

Atau output ke stdout kalau argumen kedua dikosongin. Support baris komentar `#` dan value pakai kutip.
