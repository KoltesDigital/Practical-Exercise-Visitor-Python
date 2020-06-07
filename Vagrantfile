Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider :virtualbox do |vb|
    vb.name = "Practical Exercise - TeTask"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y libclang1 python3 python3-pip
  SHELL
end
