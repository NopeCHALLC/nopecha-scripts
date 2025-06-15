import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch


@pytest.fixture
def temp_dir():
    """Create a temporary directory that is cleaned up after the test."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def mock_config():
    """Provide a mock configuration object."""
    config = Mock()
    config.debug = False
    config.timeout = 30
    config.max_retries = 3
    config.base_url = "https://api.example.com"
    return config


@pytest.fixture
def mock_logger():
    """Provide a mock logger for testing."""
    logger = Mock()
    logger.debug = Mock()
    logger.info = Mock()
    logger.warning = Mock()
    logger.error = Mock()
    logger.critical = Mock()
    return logger


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return {
        "id": 1,
        "name": "Test Item",
        "value": 42.0,
        "tags": ["test", "sample"],
        "active": True,
        "metadata": {
            "created": "2024-01-01T00:00:00Z",
            "updated": "2024-01-01T12:00:00Z"
        }
    }


@pytest.fixture
def mock_api_response():
    """Mock API response for testing."""
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"success": True, "data": []}
    response.text = '{"success": true, "data": []}'
    response.headers = {"Content-Type": "application/json"}
    return response


@pytest.fixture
def mock_file_system(temp_dir):
    """Create a mock file system structure."""
    # Create some test files
    (temp_dir / "config.json").write_text('{"key": "value"}')
    (temp_dir / "data").mkdir()
    (temp_dir / "data" / "test.txt").write_text("test content")
    return temp_dir


@pytest.fixture(autouse=True)
def reset_environment(monkeypatch):
    """Reset environment variables for each test."""
    # Clear any test-specific environment variables
    test_env_vars = ["TEST_API_KEY", "TEST_DATABASE_URL", "TEST_DEBUG"]
    for var in test_env_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def mock_database():
    """Mock database connection for testing."""
    db = Mock()
    db.connect = Mock(return_value=True)
    db.disconnect = Mock()
    db.execute = Mock(return_value=[])
    db.commit = Mock()
    db.rollback = Mock()
    return db


@pytest.fixture
def capture_logs():
    """Capture log messages during tests."""
    logs = []
    
    def log_capture(message, level="INFO"):
        logs.append({"message": message, "level": level})
    
    return log_capture, logs


@pytest.fixture
def benchmark_timer():
    """Simple benchmark timer for performance tests."""
    import time
    
    class Timer:
        def __init__(self):
            self.start_time = None
            self.end_time = None
        
        def start(self):
            self.start_time = time.time()
        
        def stop(self):
            self.end_time = time.time()
            return self.end_time - self.start_time
    
    return Timer()