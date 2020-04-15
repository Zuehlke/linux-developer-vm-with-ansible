
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu2004-desktop"
  
  config.vm.provider "virtualbox" do |vbox, override|
    vbox.name = "My Developer VM"
    vbox.cpus = 4
    vbox.memory = 4096
    vbox.customize ["modifyvm", :id, "--usb", "on"]
    vbox.customize ["modifyvm", :id, "--accelerate3d", "off"]
    vbox.customize ["modifyvm", :id, "--vrde", "off"]
  end

  # vmware specific customizations
  config.vm.provider "vmware_desktop" do |vmware, override|
    vmware.vmx["displayname"] = "My Developer VM"
    vmware.vmx["numvcpus"] = "4"
    vmware.vmx["memsize"] = "4096"
    vmware.vmx["usb.present"] = "TRUE"
    vmware.vmx["usb_xhci.present"] = "TRUE"
  end

  # create new login user
  config.vm.provision "shell", privileged: true, path: 'scripts/setup-vm-user.sh',
    args: "user user"

  # run the actual update-vm provisioning script under the new login user
  #config.vm.provision "shell", privileged: true, keep_color: true, run: "always", inline: <<-EOF
  #  sudo -i -u user ROLE_TAGS=#{ENV['ROLE_TAGS']} /vagrant/scripts/update-vm.sh #{ENV['UPDATE_VM_FLAGS']}
  #  EOF

end
