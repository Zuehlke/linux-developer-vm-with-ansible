import textwrap
import os

def test_bashrc_loads_files_from_bashrc_d_(host):
    bashrc = host.file(f"{os.environ['HOME']}/.bashrc")
    snippet = textwrap.dedent(
        '''
        # Load *.bash files from ~/.bashrc.d
        for config in "$HOME"/.bashrc.d/*.bash ; do
          . "$config"
        done
        unset -v config
        '''
    )
    assert snippet in bashrc.content_string