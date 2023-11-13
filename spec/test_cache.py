
def test_cache_downloads_directory_exists_(host):
    assert host.file('/var/cache/downloads').is_directory