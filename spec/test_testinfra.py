
def test_testinfra_is_installed_at_version_5_0_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check testinfra")
    assert cmd.rc is 0
    assert "Name: testinfra\nVersion: 5.0.0" in cmd.stdout

def test_pytest_spec_is_installed_at_version_2_0_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check pytest-spec")
    assert cmd.rc is 0
    assert "Name: pytest-spec\nVersion: 2.0.0" in cmd.stdout