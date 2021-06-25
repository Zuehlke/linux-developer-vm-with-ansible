
def test_cowsay_is_installed_(host):
    assert host.package('cowsay').is_installed