def test_add_some(non_empty_db):
    assert non_empty_db.count() > 0
