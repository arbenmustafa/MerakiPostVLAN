from meraki import meraki

apikey = "yourapikey" #Your API key can be found in the Meraki Dashboard
myOrgs = meraki.myorgaccess(apikey)
orgID = 123456 #Please add your Org ID
networkID = "YourNetworkID"  #Please add your Network ID

vlanID = 51 # this is a sample VLAN number. You can change this to any number that you would like
vlanName = "Python Test VLAN 51" #You can name the vlan anything you would like
vlanSubnet = "192.168.51.0/24"#Make sure you add the Network and your CIDR (i.e. /24)
defaultGateway = "192.168.51.1" #It is listed here as defaultGateway but  in the Dashboard GUI it is shows as MX IP

addVLAN = meraki.addvlan(apikey, networkID, vlanID, vlanName, vlanSubnet, defaultGateway)

print ("Successfully added VLAN")
