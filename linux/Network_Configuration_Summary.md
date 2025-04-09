# Network Configuration Summary

## 🔧 Overview

This document highlights key responsibilities and accomplishments related to configuring and managing network components on Red Hat Enterprise Linux (RHEL) servers.

## ⚙️ Responsibilities

- Configured and managed network settings on RHEL servers, including:
  - **TCP/IP**
  - **DNS (Domain Name System)**
  - **DHCP (Dynamic Host Configuration Protocol)**
  - **VLANs (Virtual Local Area Networks)**
  - **Firewall Rules**
- Ensured secure and reliable communication across enterprise systems by maintaining optimal network configurations.

## ✅ Outcome

These efforts contributed to:
- Improved system connectivity and uptime
- Enhanced network security through effective firewall configurations
- Streamlined communication across different network segments via VLANs

---

## 🧪 Proof of Concept (PoC)

The following tasks were performed on a RHEL 8 environment to demonstrate the configuration of key networking components:

### ✅ 1. Configure Static IP (TCP/IP)
```bash
nmcli con mod ens33 ipv4.addresses 192.168.1.100/24
nmcli con mod ens33 ipv4.gateway 192.168.1.1
nmcli con mod ens33 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con mod ens33 ipv4.method manual
nmcli con up ens33

## ✅ 2. Setup DNS Resolution
Edit the /etc/resolv.conf file:
~~~
nameserver 8.8.8.8
nameserver 8.8.4.4
~~~

## ✅ 3. Enable and Configure DHCP Server (on server-side)
Install and configure DHCP:
~~~
yum install dhcp-server
vim /etc/dhcp/dhcpd.conf
~~~
### Sample configuration:
~~~
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.150;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8;
}
~~~
### Enable and start the service:
~~~
systemctl enable dhcpd
systemctl start dhcpd
~~~

## ✅ 4. Create VLAN Interface
~~~
nmcli connection add type vlan con-name vlan10 dev ens33 id 10 ip4 192.168.10.2/24 gw4 192.168.10.1
nmcli connection up vlan10
~~~

## ✅ 5. Configure Firewall Rules (using firewalld)

~~~
# Allow SSH
firewall-cmd --permanent --add-service=ssh

# Allow HTTP and HTTPS
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https

# Reload firewall to apply changes
firewall-cmd --reload
~~~


