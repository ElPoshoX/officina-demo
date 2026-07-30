from demo_officina import version


def test_version_is_string() -> None:
    assert isinstance(version(), str)
    assert version() != ""
