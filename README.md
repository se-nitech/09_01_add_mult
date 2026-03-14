# unittestのサンプル

起動

```bash
docker compose build
docker compose up -d
```

assertを用いたテスト

```bash
docker compose exec mypython python assert_add.py
```

unittestを用いたユニットテスト

```bash
docker compose exec mypython python -m test_add
docker compose exec mypython python -m unittest test_add.py
```

カバレッジの計算

```bash
docker compose exec mypython python -m unittest test_add_final.py
docker compose exec mypython coverage run test_add_final.py
docker compose exec mypython coverage report
docker compose exec mypython coverage html
docker compose exec mypython coverage xml
```

テストスイートの実行

```bash
docker compose exec mypython coverage run test_compute.py
```

pytestを用いたユニットテスト

```bash
docker compose exec mypython pytest test/test_compute1.py
docker compose exec mypython pytest test/test_compute2.py
```

停止

```bash
docker compose down
```
