import bank

DB_FILE = "db.json"

data = {
    "users": {
        "alice": {
            "password": "test123",
            "balance": 0.0,
            "transactions": []
        }
    }
}


# ================ DB TESTS =============

def test_load_db():
    assert isinstance(bank.load_db(), dict)


def test_save_db(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db(data)

    assert bank.load_db() == data

# ================= REGISTER ==================

def test_register(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    monkeypatch.setattr("builtins.input", lambda _: "alice")
    monkeypatch.setattr("getpass.getpass", lambda _: "123")

    bank.register()

    db = bank.load_db()

    assert "alice" in db["users"]
    assert db["users"]["alice"]["password"] == "123"
    assert db["users"]["alice"]["balance"] == 0.0
    assert db["users"]["alice"]["transactions"] == []


# ================ LOGIN ================

def test_login_success(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 0.0,
                "transactions": []
            }
        }
    })

    monkeypatch.setattr("builtins.input", lambda _: "alice")
    monkeypatch.setattr("getpass.getpass", lambda _: "123")

    result = bank.login()

    assert result == "alice"


# ================== SHOW BALANCE ===================


def test_show_balance(tmp_path, monkeypatch, capsys):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 50.0,
                "transactions": []
            }
        }
    })

    bank.show_balance("alice")

    captured = capsys.readouterr()

    assert "50.00" in captured.out


# =================== READ AMOUNT ==================

def test_read_amount_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "10")

    assert bank.read_amount("Amount: ") == 10.0

# ====================== ADD TRANSACTION ==================


def test_add_transaction():
    user = {"transactions": []}

    bank.add_transaction(user, {"type": "deposit", "amount": 100})

    tx = user["transactions"][0]

    assert tx["type"] == "deposit"
    assert tx["amount"] == 100
    assert "at" in tx


# ================ DEPOSIT =====================

def test_deposit(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 50.0,
                "transactions": []
            }
        }
    })

    monkeypatch.setattr("builtins.input", lambda _: "10")

    bank.deposit("alice")

    db = bank.load_db()

    assert db["users"]["alice"]["balance"] == 60.0



# ================== WITHDRAW ======================


def test_withdraw_success(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 100.0,
                "transactions": []
            }
        }
    })

    monkeypatch.setattr("builtins.input", lambda _: "30")

    bank.withdraw("alice")

    db = bank.load_db()

    assert db["users"]["alice"]["balance"] == 70.0


def test_withdraw_insufficient(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 10.0,
                "transactions": []
            }
        }
    })

    monkeypatch.setattr("builtins.input", lambda _: "50")

    bank.withdraw("alice")

    db = bank.load_db()

    assert db["users"]["alice"]["balance"] == 10.0



# ====================== TRANSFER =====================


def test_transfer_success(tmp_path, monkeypatch):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 100.0,
                "transactions": []
            },
            "bob": {
                "password": "456",
                "balance": 50.0,
                "transactions": []
            }
        }
    })

    monkeypatch.setattr("builtins.input", lambda _: "bob")
    monkeypatch.setattr("bank.read_amount", lambda _: 30)

    bank.transfer("alice")

    db = bank.load_db()

    assert db["users"]["alice"]["balance"] == 70.0
    assert db["users"]["bob"]["balance"] == 80.0



# ====================== HISTORY =======================


def test_history_empty(tmp_path, monkeypatch, capsys):
    path = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(path))

    bank.save_db({
        "users": {
            "alice": {
                "password": "123",
                "balance": 0.0,
                "transactions": []
            }
        }
    })

    bank.show_history("alice")

    captured = capsys.readouterr()

    assert "No transactions yet." in captured.out