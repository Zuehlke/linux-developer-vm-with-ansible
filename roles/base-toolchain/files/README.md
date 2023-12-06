# README

Hi! Welcome to the "My Developer VM".

## Overview

This Developer VM provides the toolchains required to develop on "your project".

The latest version of the this VM can be downloaded here:

 * https://github.com/Zuehlke/linux-developer-vm-with-ansible/releases

## Basic Usage and Setup

### Notes on the User Account

Currently you can log in with the following user only:

 * username: "user"
 * password: "user"


### Configuring the Keyboard Layout and Timezone

The first thing you might want to do is configuring the keyboard layout according to your preference:

 * go to "Settings" -> "Region & Language" -> "Input Sources", then click the "+" button to add your preferred keyboard layout

Also, you may want to configure the timezone correctly:

 * go to "Settings" -> "Date & Time", then click on "Time Zone" and select your current timezone


### Initial Git Setup

Since you will be developing with Git, there are a few things you need to set up.
First, configure your name and email in `~/.gitconfig`:

 * run `git config --global user.name "<Firstname> <Lastname>"` to set your real name
 * run `git config --global user.email "<firstname>.<lastname>@example.com"` to set your email address


### Updating the Developer VM

This developer VM is configured via Ansible and provides a simple update mechanism:

 * run `update-vm` to re-apply the current configuration
 * run `update-vm --pull` to pull latest changes and apply the updated configuration
 * run `update-vm --verify-only` to test the current configuration (does not update)
 * run `update-vm --provision-only` - don't run the tests, only update the configuration
