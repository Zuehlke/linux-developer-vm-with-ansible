
def test_testinfra_is_installed_at_version_9_0_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check pytest-testinfra")
    assert cmd.rc is 0
    assert "Name: pytest-testinfra\nVersion: 9.0.0" in cmd.stdout

def test_pytest_spec_is_installed_at_version_3_2_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check pytest-spec")
    assert cmd.rc is 0
    assert "Name: pytest-spec\nVersion: 3.2.0" in cmd.stdout

def test_pytest_html_formatter_is_installed_at_version_4_1_1_(host):
    cmd = host.run("pip3 show --disable-pip-version-check pytest-html")
    assert cmd.rc is 0
    assert "Name: pytest-html\nVersion: 4.1.1" in cmd.stdout