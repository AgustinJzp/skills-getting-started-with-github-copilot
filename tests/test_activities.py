from urllib.parse import quote


def test_get_activities(client):
    r = client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_updates_participants(client):
    email = "newstudent@mergington.edu"
    path = f"/activities/{quote('Chess Club')}/signup?email={email}"
    r = client.post(path)
    assert r.status_code == 200

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_duplicate_returns_400(client):
    email = "duplicate@mergington.edu"
    path = f"/activities/{quote('Programming Class')}/signup?email={email}"
    r1 = client.post(path)
    assert r1.status_code == 200

    r2 = client.post(path)
    assert r2.status_code == 400


def test_signup_nonexistent_returns_404(client):
    path = f"/activities/{quote('Nonexistent')}/signup?email=test@x.com"
    r = client.post(path)
    assert r.status_code == 404
