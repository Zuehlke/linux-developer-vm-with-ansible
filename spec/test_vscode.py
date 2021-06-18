import pytest

def test_vscode_command_is_found_(host):
    assert host.run('which code').rc is 0

def test_vscode_version_command_reports_version_1_57_1_(host):
    assert '1.57.1' in host.run('code --version').stdout

@pytest.mark.parametrize('extension', [
    'zbr.vscode-ansible'
])
def test_vscode_extensions_include_defined_extensions_(host, extension):
    installed_extensions = host.run('code --list-extensions').stdout
    assert extension in installed_extensions
