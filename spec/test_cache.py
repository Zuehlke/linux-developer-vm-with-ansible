
def test_cache_dir_downloadsectory_exists_(host):
    assert host.file('/var/cache/downloads').is_directory