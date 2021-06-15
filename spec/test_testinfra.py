
def test_testinfra_is_installed_at_version_6_3_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check pytest-testinfra")
    assert cmd.rc is 0
    assert "Name: pytest-testinfra\nVersion: 6.3.0" in cmd.stdout

def test_pytest_spec_is_installed_at_version_3_2_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check pytest-spec")
    assert cmd.rc is 0
    assert "Name: pytest-spec\nVersion: 3.2.0" in cmd.stdout