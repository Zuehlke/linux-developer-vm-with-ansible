import pytest
import os

def test_git_package_is_installed_(host):
    assert host.package('git').is_installed

def test_git_command_is_found_(host):
    assert host.run('which git').rc is 0

def test_git_version_command_reports_version_2_x_(host):
    assert 'git version 2.' in host.run('git --version').stdout

def test_git_shell_prompt_is_configured_in_bashrc_d_(host):
    git_ps1 = host.file(f"{os.environ['HOME']}/.bashrc.d/git-ps1.bash")
    assert git_ps1.exists
    assert git_ps1.contains('export PS1=')

def test_git_shell_prompt_is_set_in_the_environment_(host):
    assert '__git_ps1' in host.run('bash -i -c "env | grep ^PS1=; exit \\$?"').stdout


def test_gitconfig_configures_rebase_on_pull_(host):
    __assert_git_config(host, 'pull.rebase', 'true')

def test_gitconfig_configures_autocrlf_input_(host):
    __assert_git_config(host, 'core.autocrlf', 'input')

@pytest.mark.parametrize('shortcut,command', [
    ('co', 'checkout'),
    ('ci', 'commit'),
    ('br', 'branch'),
    ('st', 'status'),
    ('unstage', 'reset HEAD --'),
    ('slog', 'log --pretty=oneline --abbrev-commit'),
    ('graph', 'log --all --oneline --graph --decorate')
])
def test_gitconfig_provides_alias_(host, shortcut, command):
    __assert_git_config(host, f"alias.{shortcut}", command)

def __assert_git_config(host, config_key, expected_value):
    actual_value = host.run(f"git config --global --get {config_key}").stdout.strip()
    assert actual_value == expected_value