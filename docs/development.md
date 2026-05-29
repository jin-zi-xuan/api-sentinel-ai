# Development Guide

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run API

```bash
uvicorn app.main:app --reload
```

## Initialize Database

```bash
python -m app.db.init_db
```

## Run Tests

```bash
pytest
```

## API Response Shape

Successful responses use this structure:

```json
{
  "success": true,
  "code": "OK",
  "message": "Success",
  "data": {}
}
```

Error responses use the same structure with `success` set to `false`.
