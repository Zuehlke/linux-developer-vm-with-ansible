

# Workshop


## Prerequisites

Make sure prerequisites are installed:

* Git - https://git-scm.com/downloads
* VirtualBox - https://www.virtualbox.org/wiki/Downloads
* Vagrant - https://www.vagrantup.com/downloads

In order to share code and fork the repository a Github account is needed. In case you don't have that yet, it's a good opportunity to create one ;)

In order to save time during the workshop (requires download of ~1.5GB image file) or have a chance to troubleshoot any installation issues before the workshop, please run the following commands upfront:

```
$ git clone https://github.com/Zuehlke/linux-developer-vm-with-ansible
$ cd linux-developer-vm-with-ansible
$ vagrant up --no-provision
$ vagrant destroy -f
```

In case there are any issues with the above commands, please let me know!

## Exercises

### Lab 1: Up and running!

**Goal**: Getting the Developer VM up and running

 * just run `vagrant up` :)

While this is running in the background (might take a few minutes), please continue with lab 2.


### Lab 2: Getting to know the Developer VM Template Project

**Goal**: Get familiarized with the structure of the template project

 * review the existing Ansible in the `roles/` directory
 * review the corresponding Testinfra tests in the `spec/` directory
 * review the output from running `vagrant up` in lab 1
 * check the README file on the VM Desktop (and configure your keyboard layout)


### Lab 3: Make it yours!

**Goal**: Adapt the Dev-VM name in the README + Vagrantfile and switch to your Git repository

 * adapt the `README.md` to describe your VM
 * adapt the VM name in `Vagrantfile`
 * create a new repo under your Github account (or alternatively fork the template repo)
 * switch the origin to point to your repo, then commit your changes and push
 * run `vagrant reload` to have the VM name changed in VirtualBox as well

Example:
```
$ git remote set-url origin https://github.com/tknerr/zdecamp21-developer-vm.git
$ git commit -am "Adapt for ZCamp21 Developer VM"
$ git push origin master
```

### Lab 4: Let's take a snapshot now!

**Goal**: Learn how to take VM snapshots as a rescue point

 * run `vagrant snapshot save start` to create a snapshot of the current VM state
 * do some changes in the VM, e.g. `sudo apt install sl` (yes... I know you want to try `sl` now... ;))
 * revert to previous state `vagrant snapshot restore start` (you can do that any time you borked your system and want to start back over)


### Lab 5: Hands-On! Let's add Cowsay to our toolchain

**Goal**: Write your first Ansible task and Testinfra spec

Let's start TDD-style by writing a failing test first:

 * create a new test spec `spec/test_cowsay.py`
 * use the Testinfra [package module](https://testinfra.readthedocs.io/en/latest/modules.html#testinfra.modules.package.Package) to check that the "cowsay" package is installed
 * run `vagrant provision` to verify that we have a failing test now

Then create a new Ansible role to install the "cowsay" package:

 * create a new Ansible role named "cowsay" under the `roles/` directory
 * use the Ansible (apt module)[https://docs.ansible.com/ansible/2.9/modules/apt_module.html] to install the cowsay package
 * make sure the newly added cowsay role is referenced in `site.yml`, so that Ansible will pick it up
 * run `vagrant provision` to trigger the provisioning and review the Ansible output
 * in the VM, run `cowsay hello` (alternatively, run `vagrant ssh -c "cowsay hello"` on your host)

Additional hints:

 * take a look at the other test specs (e.g. `test_git.py`) for inspiration on further checks you coud add to ensure a proper installation of cowsay
 * you can run `UPDATE_VM_FLAGS=--verify-only vagrant provision` to skip the Ansible provisioning and run only the tests
 * you can run `ROLE_TAGS=cowsay vagrant provision` to run Ansible provisioning only for the "cowsay" role (but ignore all others)
 * you can disable the cows in the Ansible output by setting the `ANSIBLE_NOCOWS=1` env var via the `~/.bashrc.d` mechanism [provided by the bashrc_d role](https://github.com/Zuehlke/linux-developer-vm-with-ansible/pull/11)


### Lab 6: Export your Developer VM for others as an .ova file

**Goal**: Understand how to export the VM as an .ova image so that it can be distributed to the team

 * follow the instructions in the ["Packaging" section](https://github.com/Zuehlke/linux-developer-vm-with-ansible/blob/master/README.md#packaging) to export the .ova image

### Lab 7: Import the Developer VM .ova file and work from there

**Goal**: Run through the VM import process so that you can work from within the imported VM now

 * follow the instructions in the ["Usage" section](https://github.com/Zuehlke/linux-developer-vm-with-ansible#usage)
    * import the .ova image
    * verify that everything works by running the `update-vm` commands
    * review the `~/vm-setup` directory and it's connection to `update-vm`

Notes:
 * this is the point where you should consider sharing the VM .ova image with your team!
 * at this point you do not need Vagrant anymore and can extend the toolchain from within the VM!
 * you need to switch back to Vagrant everytime you want to create a fresh .ova image (and consider having a CI process that regularly builds these .ova images via vagrant)

### Lab 8: Work from within the imported .ova image and grow your toolchain!

Workshop ends here, this is left for you... :)



