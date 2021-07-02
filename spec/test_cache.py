
def test_download_cache_directory_exists_(host):
    assert host.file('/var/cache/downloads').is_directory