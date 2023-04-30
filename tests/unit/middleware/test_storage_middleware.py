from griptape.artifacts import TextArtifact
from griptape.drivers import MemoryStorageDriver
from griptape.middleware import StorageMiddleware
from tests.mocks.mock_tool.tool import MockTool


class TestStorageMiddleware:
    def test_constructor(self):
        mw = StorageMiddleware(
            driver=MemoryStorageDriver()
        )

        assert mw.name == "StorageMiddleware"

        mw = StorageMiddleware(
            name="MyMiddleware",
            driver=MemoryStorageDriver()
        )

        assert mw.name == "MyMiddleware"

    def test_process_output(self):
        mw = StorageMiddleware(
            name="MyMiddleware",
            driver=MemoryStorageDriver()
        )

        assert mw.process_output(MockTool().test, TextArtifact("foo")).value.startswith(
            'Output of "MockTool.test" was stored in storage "MyMiddleware" with entry ID'
        )
