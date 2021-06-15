
def test_vscode_apt_sources_list_exists_(host):
    assert host.file('/etc/apt/sources.list.d/packages_microsoft_com_repos_vscode.list').exists

def test_vscode_apt_key_defined_(host):
    assert 'Microsoft (Release signing) <gpgsecurity@microsoft.com>' in host.run('apt-key list').stdout

def test_vscode_command_is_found_(host):
    assert host.run('which code').rc is 0

def test_vscode_version_command_succeeds_(host):
    assert host.run('code --version').rc is 0
