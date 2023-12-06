import pytest
import os

@pytest.mark.skipif(not os.path.exists('/.dockerenv'), reason = 'only relevant with docker provider')
def test_x11_DISPLAY_is_forwared_to_docker_host_(host):
    x11_display = host.file(f"{os.environ['HOME']}/.bashrc.d/x11-display.bash")
    assert x11_display.exists
    assert x11_display.contains('export DISPLAY=host.docker.internal:0')

@pytest.mark.skipif(not os.path.exists('/.dockerenv'), reason = 'only relevant with docker provider')
def test_systemtctl_replacement_command_is_found_(host):
    assert host.run('which systemctl').rc is 0

@pytest.mark.skipif(not os.path.exists('/.dockerenv'), reason = 'only relevant with docker provider')
def test_systemtctl_replacement_command_reports_version_1_5_4505_(host):
    assert 'systemctl.py 1.5.4505' in host.run('systemctl --version').stdout
