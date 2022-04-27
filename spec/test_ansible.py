
def test_ansible_is_installed_at_version_5_5_0_(host):
    cmd = host.run("pip3 show --disable-pip-version-check ansible")
    assert cmd.rc is 0
    assert "Name: ansible\nVersion: 5.5.0" in cmd.stdout


def test_ansible_core_is_installed_at_version_2_12_5_(host):
    cmd = host.run("pip3 show --disable-pip-version-check ansible-core")
    assert cmd.rc is 0
    assert "Name: ansible-core\nVersion: 2.12.5" in cmd.stdout


def test_ansible_commands_are_found_(host):
    assert host.run('which ansible').rc is 0
    assert host.run('which ansible-playbook').rc is 0


def test_ansible_version_command_reports_core_version_2_12_5_(host):
    assert 'core 2.12.5' in host.run('ansible --version').stdout
