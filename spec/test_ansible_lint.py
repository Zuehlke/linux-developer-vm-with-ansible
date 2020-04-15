
def test_ansible_lint_is_installed_at_version_4_2_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check ansible-lint")
    assert cmd.rc is 0
    assert "Name: ansible-lint\nVersion: 4.2.0" in cmd.stdout

def test_ansible_lint_command_is_found_(host):
    assert host.run('which ansible-lint').rc is 0

def test_ansible_lint_version_command_reports_version_4_2_0_(host):
    assert '4.2.0' in host.run('ansible-lint --version').stdout