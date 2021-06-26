
# Linux Developer VM Example / Template

A minimal example / template project for an Ansible-managed Linux Developer VM.

![Linux Developer VM Screenshot](https://user-images.githubusercontent.com/365744/122089607-3721ff80-ce07-11eb-801e-661715e95aaa.png)

It's meant to be copy/pasted and filled with life. The `roles/` directory contains the roles
for setting up the VM, the `spec/` directory contains the tests that come along with it.
All your specific customizations go in there!

**NOTE: This is just a bare skeleton template project -- use it as a copy/paste template to kickstart your own developer VM and grow it to your needs**

For the Chef-based equivalent of it, see https://github.com/Zuehlke/linux-developer-vm

## What's included?

### Main tools

These are the main tools included in this developer VM:

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


## Usage

### Obtaining and Starting the VM Image

The latest version of this developer VM can be downloaded as a VM image from here:

 * https://github.com/Zuehlke/linux-developer-vm-with-ansible/releases

After downloading the .ova file you can import it into VirtualBox via `File -> Import Appliance...`.
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


## Building and Packaging the VM

### Prerequisites

You only need [VirtualBox](http://virtualbox.org/wiki/Downloads) and [Vagrant](http://www.vagrantup.com/) installed.

If you want to build a VMware .ova image, you will need a [VMware Workstation (Pro) or VMware Fusion](https://www.vmware.com/products/desktop-hypervisor.html) + [Vagrant VMware Plugin](https://www.vagrantup.com/vmware).

All other requirements, including Ansible will be installed *inside the Vagrant VM* during provisioning, i.e. you don't need them installed on your host machine.

### Building

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
    default: platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    default: rootdir: /home/user/vm-setup
    default: plugins: testinfra-6.3.0, spec-3.2.0
    default: collected 8 items
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
    default: spec/test_testinfra.py:
    default:   ✓ Testinfra is installed at version 6 3 0 [local]
    default:   ✓ Pytest spec is installed at version 3 2 0 [local]                    [100%]
    default:
    default:
    default: ============================== 8 passed in 28.56s ==============================
```

If these are passing as expected, you can continue developing on the Ansible roles within this repo.
Please don't forget to add a test for each new feature you add (see "Contributing")

### Packaging

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

For VMware:
```
$ vagrant halt
$ VMX_FILE=`cat .vagrant/machines/default/vmware_desktop/id`
$ ovftool --name="Linux Developer VM v0.1.0" "$VMX_FILE" linux-developer-vm-v0.1.0.ova
```

Don't forget to throw away the VM when you are done:
```
$ vagrant destroy -f
```

## Contributing

 1. Fork the repository on Github
 1. Create a named feature branch (like `feature/add-xyz`)
 1. Implement your changes, add tests
 1. Commit and push
 1. Submit a Pull Request via Github
