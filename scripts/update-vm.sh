#!/bin/bash

# fail early
set -e -o pipefail

# variables
REPO_ROOT=~/vm-setup
ANSIBLE_VERSION=2.9.22

# exports
export ANSIBLE_FORCE_COLOR=true

check_ansible() {
  big_step "Checking Ansible..."
  if [[ $(ansible --version | grep "$ANSIBLE_VERSION") ]]; then
    echo "Ansible $ANSIBLE_VERSION already installed"
  else
    step "Installing Ansible version $ANSIBLE_VERSION"
    sudo apt-get update
    sudo apt-get install python3-pip -y
    # use the -H flag to so pip uses /root/.cache and does not leave root-owned files inside ~/.cache
    sudo -H pip3 install ansible==$ANSIBLE_VERSION
  fi
}

check_git() {
  big_step "Checking Git..."
  if [[ $(which git) ]]; then
    echo "Git already installed"
  else
    step "Installing Git"
    sudo apt-get update
    sudo apt-get install git -y
  fi
}

copy_repo_and_symlink_self() {
  big_step "Copying repo into the VM..."
  if mountpoint -q /vagrant; then
    step "Copy /vagrant to $REPO_ROOT"
    rsync -avh --progress /vagrant/ $REPO_ROOT/ --delete --exclude-from /vagrant/.gitignore
    step "Fixing permissions..."
    chmod 0755 "$REPO_ROOT/scripts/update-vm.sh"
    step "Symlinking 'update-vm' script"
    sudo ln -sf $REPO_ROOT/scripts/update-vm.sh /usr/local/bin/update-vm
  else
    echo "Skipped because /vagrant not mounted"
  fi
}

update_repo() {
  big_step "Pulling latest changes from git..."
  cd $REPO_ROOT
  git pull
}

update_vm() {
  big_step "Updating the VM via Ansible..."
  cd $REPO_ROOT

  # append extra vars and role tags if exist
  local role_tags=$([[ -n "$ROLE_TAGS" ]] && echo "--tags $ROLE_TAGS" || echo "")
  local extra_vars=$([[ -f "site.local.yml" ]] && echo "--extra-vars @site.local.yml" || echo "")

  step "trigger the Ansible run with $role_tags and $extra_vars"
  /usr/local/bin/ansible-playbook -i "localhost," -c local site.yml -vv $role_tags $extra_vars
}

verify_vm() {
  big_step "Verifying the VM..."
  cd $REPO_ROOT

  step "run ansible linting"
  ansible-lint --force-color

  step "run integration tests"
  py.test --color=yes --spec spec/*.py
}

big_step() {
  echo -e "\n=====================================\n>>>>>> $1\n=====================================\n"
}
step() {
  echo -e "\n\n>>>>>> $1\n-------------------------------------\n"
}

#
# main flow
#
if [[ "$1" == "--verify-only" ]]; then
  verify_vm
else
  check_git
  check_ansible
  copy_repo_and_symlink_self
  [[ "$1" == "--pull" ]] && update_repo
  update_vm
  [[ "$1" == "--provision-only" ]] || verify_vm
fi
