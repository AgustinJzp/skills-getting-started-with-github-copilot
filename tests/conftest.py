import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


# Snapshot of the original in-memory activities to restore before each test
_ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    # Restore the in-memory activities before each test
    activities.clear()
    activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)
