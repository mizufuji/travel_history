旅行履歴を記録するWEBアプリケーションです。
旅行先・旅行した月をDBに記録し、UIに表示することができます。

■言語:
Python

■構造:
UI・・・Streamlit

APIサーバー・・・FastAPI

Database・・・SQLite3


■ドキュメント構成
```
.
│  app.py
│  sql_app.db
│
├─sql_app
│  │  crud.py
│  │  database.py
│  │  main.py
│  │  models.py
│  │  schemas.py
│  │  __init__.py
```
