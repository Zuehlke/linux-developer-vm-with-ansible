
# Linux Developer VM Example / Template

[![Circle CI](https://circleci.com/gh/Zuehlke/linux-developer-vm-with-ansible/tree/master.svg?style=shield)](https://circleci.com/gh/Zuehlke/linux-developer-vm-with-ansible/tree/master)

A minimal example / template project for an Ansible-managed Linux Developer VM based on Ubuntu 22.04.

![Linux Developer VM Screenshot](https://github.com/Zuehlke/linux-developer-vm-with-ansible/assets/365744/66854dc6-b7b9-4c8f-a9c4-48457eeaac84)

It's meant to be copy/pasted and filled with life. The `roles/` directory contains the roles
for setting up the VM, the `spec/` directory contains the tests that come along with it.
All your specific customizations go in there!

**NOTE: This is just a bare skeleton template project -- use it as a copy/paste template to kickstart your own developer VM and grow it to your needs**

For the Chef-based equivalent of it, see https://github.com/Zuehlke/linux-developer-vm

## What's included?

### Main tools

These are the main tools included in this [Ubuntu 22.04 Desktop](https://ubuntu.com/download/desktop) based Developer VM:

 * [Git](https://git-scm.com/) - your version control system of choice :)
 * [VSCode](https://code.visualstudio.com/) - as a general purpose (code) editor, e.g. for updating the Ansible roles when working from within the developer VM
 * [Docker](https://www.docker.com/) - as a general purpose container runtime, e.g. for building your applications with a dockerized toolchain

Apart from the above, the following tools are used to set up and maintain this developer VM:

 * [Ansible](https://docs.ansible.com/ansible/latest/index.html) - for managing / installing this developer VM
 * [Ansible-lint](https://github.com/ansible/ansible-lint) - to ensure best practices when adding more Ansible roles
 * [TestInfra](https://testinfra.readthedocs.io/en/latest/) - for verifying that the developer VM is set up correctly

### Tweaks and Settings

Other tweaks and settings worth mentioning:

 * places a `README.md` file on the Desktop to guide first time users after they logged in to the VM
 * sets up `~/.bashrc.d` directory to ease management of bash initialization (e.g. for setting env vars)
 * adds a Git `PS1` shell prompt and configures some useful aliases and settings in `~/.gitconfig`
 * symlinks [`update-vm.sh`](scripts/update-vm.sh) to `/usr/local/bin/update-vm` so it's in the `$PATH` and can be used for updating the VM from the inside (see below)
 * adds `/var/cache/downloads` as a cache directory for downloaded installer files


## Building the VM

### Prerequisites

Minimally, you need [VirtualBox](http://virtualbox.org/wiki/Downloads) and [Vagrant](http://www.vagrantup.com/) (>= 2.4.0) installed.

➡️ if you want to build a VMware .ova image, you will need a [VMware Workstation (Pro) or VMware Fusion](https://www.vmware.com/products/desktop-hypervisor.html) + [Vagrant VMware Provider](https://www.vagrantup.com/vmware) (👉 **works on M1/M2 MacBooks!**).

➡️ if you want to build a Parallels .pvmp image, you will need a [Parallels Desktop (Pro Edition / Business Edition)](https://www.parallels.com/products/desktop/pro/) + [Vagrant Parallels Provider](https://parallels.github.io/vagrant-parallels/docs/) (👉 **works on M1/M2 MacBooks!**).

All other requirements, including Ansible will be installed *inside the Vagrant VM* during provisioning, i.e. you don't need them installed on your host machine.

The steps below can be executed in the same way on Mac, Linux, and Windows.

### Building and Provisioning via Vagrant

Bring up the developer VM:
```
$ vagrant up
```

This will take a while, as it will do quite a few things inside the VM:

 1. set up a new user account using the `setup-vm-user.sh` script
 1. update the VM using `update-vm.sh` script
    1. installs Ansible from PyPi
    1. runs the `site.yml` playbook to install the toolchain and configure the developer VM
    1. checks the roles via `ansible-lint` to ensure best practices
    1. verifies the configuration of the VM via TestInfra 

Watch the vagrant output on the console for seeing progress. At the end you
should see all tests passing:

```
...
    default: ============================= test session starts ==============================
    default: platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    default: rootdir: /home/user/vm-setup
    default: plugins: testinfra-6.3.0, spec-3.2.0
    default: collected 36 items
    default:
    default: spec/test_ansible.py:
    default:   ✓ Ansible is installed at version 2 9 22 [local]
    default:   ✓ Ansible commands are found [local]
    default:   ✓ Ansible version command reports version 2 9 22 [local]
    default:
    default: spec/test_ansible_lint.py:
    default:   ✓ Ansible lint is installed at version 5 0 12 [local]
    default:   ✓ Ansible lint command is found [local]
    default:   ✓ Ansible lint version command reports version 5 0 12 [local]
    default:
    default: spec/test_bashrc_d.py:
    default:   ✓ Bashrc loads files from bashrc d [local]
    default:
    default: spec/test_cache.py:
    default:   ✓ Download cache directory exists [local]
    default:
    default: spec/test_docker.py:
    default:   ✓ Vm user is in docker group [local]
    default:   ✓ Containerd package is installed at version 1 4 6 [local]
    default:   ✓ Containerd version command reports 1 4 6 [local]
    default:   ✓ Docker cli package is installed at version 20 10 7 [local]
    default:   ✓ Docker cli version command reports 20 10 7 [local]
    default:   ✓ Docker engine package is installed at version 20 10 7 [local]
    default:   ✓ Docker engine version command reports 20 10 7 [local]
    default:
    default: spec/test_git.py:
    default:   ✓ Git package is installed [local]
    default:   ✓ Git command is found [local]
    default:   ✓ Git version command reports version 2 x [local]
    default:   ✓ Git shell prompt is configured in bashrc d [local]
    default:   ✓ Git shell prompt is set in the environment [local]
    default:   ✓ Gitconfig configures rebase on pull [local]
    default:   ✓ Gitconfig configures autocrlf input [local]
    default:   ✓ Gitconfig provides alias [local-co-checkout]
    default:   ✓ Gitconfig provides alias [local-ci-commit]
    default:   ✓ Gitconfig provides alias [local-br-branch]
    default:   ✓ Gitconfig provides alias [local-st-status]
    default:   ✓ Gitconfig provides alias [local-unstage-reset HEAD --]
    default:   ✓ Gitconfig provides alias [local-slog-log --pretty=oneline --abbrev-commit]
    default:   ✓ Gitconfig provides alias [local-graph-log --all --oneline --graph --decorate]
    default:
    default: spec/test_testinfra.py:
    default:   ✓ Testinfra is installed at version 6 3 0 [local]
    default:   ✓ Pytest spec is installed at version 3 2 0 [local]
    default:
    default: spec/test_vscode.py:
    default:   ✓ Vscode command is found [local]
    default:   ✓ Vscode version command reports version 1 57 1 [local]
    default:   ✓ Vscode extension is installed [local-zbr
    default:   ✓ Vscode extension is installed [local-ms-azuretools
    default:   ✓ Vscode extension is installed [local-ms-vscode-remote
    default:
    default: ============================== 36 passed in 5.60s ==============================
```

If these are passing as expected, you can continue developing on the Ansible roles within this repo.
Please don't forget to add a test for each new feature you add (see "Contributing")


## Packaging / Exporting the VM

Whenever you feel like distributing a fat VM image rather than a Vagrantfile,
you can package / export it as a VirtualBox image. This might be useful
for distributing the initial version of the developer VM to your dev team,
or simply for preserving checkpoint releases as a binary images.

Let's start from a clean state:
```
$ vagrant destroy -f
$ vagrant up
```

This will provision the VM as usual. Once the provisioning succeeded, we will
do a few cleanup steps before packaging the VM.

First, unmount the /vagrant shared folder:
```
$ vagrant ssh -c "sudo umount /vagrant -f"
```

Then remove the vagrant user account:
```
$ vagrant ssh -c "sudo pkill -KILL -u vagrant"
$ vagrant ssh -c "sudo userdel -f -r vagrant"
```

Finally, shutdown the VM, remove the sharedfolder, and export the VM as an .ova file

For VirtualBox:
```
$ vagrant halt
$ VBoxManage sharedfolder remove "Linux Developer VM" --name "vagrant"
$ VBoxManage modifyvm "Linux Developer VM" --name "Linux Developer VM v0.1.0"
$ VBoxManage export "Linux Developer VM v0.1.0" --output "linux-developer-vm-v0.1.0.ova" --options manifest,nomacs
```

*Windows users*: You may have to either use the full path to `VBoxManage.exe` or add the Virtualbox path to your `Path` environment variable (recommended): Open the system settings (keyboard shortcut `WIN + X` then `y`), click on "Advanced system settings" > tab "Advanced" > button "Environment Variables" and add `C:\Program Files\Oracle\VirtualBox\` to `Path`.

For VMware:
```
$ vagrant halt
$ VMX_FILE=`cat .vagrant/machines/default/vmware_desktop/id`
$ ovftool --name="Linux Developer VM v0.1.0" "$VMX_FILE" linux-developer-vm-v0.1.0.ova
```

For Parallels (via ControlCenter UI):
* shutdown the running VM (via right-click on VM -> Shutdown)
* rename the VM to "linux-developer-vm-v0.1.0_arm64" (via right-click on VM -> Configure... -> Name)
* remove any snapshots (via right-click on VM -> Mange Snapshots... -> Delete)
* export to .pvmp file (via right-click on VM -> Prepare for Transfer)
* locate the .pvmp file (via right-click on VM -> Show in Finder) and upload it

Don't forget to throw away the VM when you are done:
```
$ vagrant destroy -f
```


## Using the Packaged / Exported VM

Consider that not everyone in your team has Vagrant + the necessary plugins installed, so you can just provide them with the exported (yet still updateable) VM image and they are ready to go.

### Obtaining and Starting the VM Image

The latest version of this developer VM can be downloaded as a VM image from here:

 * https://github.com/Zuehlke/linux-developer-vm-with-ansible/releases

After downloading the .ova file you can import it:

* into VirtualBox via `File -> Import Appliance...` (and choose the exported VirtualBox .ova image)
* into VMware Workstation / Fusion via `File -> Import...` (and choose the exported VMware .ova image)
* into Parallels Desktop via `File -> Open...` (and choose the exported Parallels .pvmp image)

Once imported, you can simply start the VM and log in:

 * username: "user"
 * password: "user"

From then on just open a terminal and you will have all of the tools available (see "What's included?").

### Updating the VM

You can run these commands from anywhere inside the developer VM:

 * `update-vm` - update the VM by applying the Ansible roles from the locally checked out repo at `~/vm-setup`
 * `update-vm --pull` - same as above, but update repo before by pulling the latest changes
 * `update-vm --verify-only` - don't update the VM, only run the TestInfra tests
 * `update-vm --provision-only` - don't run the TestInfra tests, only update the vm

### Further Usage Instructions

For general instructions, please refer to the README.md that is placed on the Desktop of the Developer VM:

* [roles/readme/files/README.md](./roles/readme/files/README.md)


## Contributing

 1. Fork the repository on Github
 1. Create a named feature branch (like `feature/add-xyz`)
 1. Implement your changes, add tests
 1. Commit and push
 1. Submit a Pull Request via Github
