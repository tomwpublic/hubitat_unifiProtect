# hubitat_unifiProtect

This provides various driver capabilities for Hubitat with UniFi Protect systems. Supported devices include cameras (Motion and ImageCapture capabilities) and doorbells (Motion and PushableButton capabilities).  More capabilities may be added over time.

Note that this package requires a companion server that can run the python HTTP server script (server.py).  You can run this just about anywhere, including a Raspberry Pi or desktop PC.

Most of this implementation is based on the work shared here:

* https://github.com/hjdhjd/homebridge-unifi-protect

Special thanks to @Bago for their troubleshooting help.

# Manual Installation instructions:

* On the external Python-enabled machine, execute the script *server.py*.
    * This needs to be running continuously in order for events to be properly decoded
* In the *Drivers Code* section of Hubitat, add the unifiProtectController, unifiProtectCamera, and unifiProtectDoorbell drivers.
* In the *Devices* section of Hubitat, add a *New Virtual Device* of type UniFi Protect Controller.
* On the configuration page for the newly created *Device*, enter these details and Save:
    * username and password for your UniFi Protect controller
    * the IP address of your UniFi Protect controller
    * the IP address and port number of your Python server
        

# Usage instructions:

* Use ```createChildDevices()``` to create specific instances for all known devices (from the 'bootstrap' *Device States* entry)
* Utilize Motion (from cameras and doorbells) and PushableButton (from doorbell) events, according to whatever is supported by your devices
* Use the ```take()``` command on camera devices to take a snapshot
    * A text attribute, ```displayImage``` will contain an HTML data URL to display the image on Dashboards.  A generic *Attribute* tile will render this for you.
    * Note that this may be a very large image, so if page loads or other performance suffers the ```clearImages()``` command can be used to flush the data

# Disclaimer

I have no affiliation with any of the companies mentioned in this readme or in the code.
