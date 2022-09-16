# hubitat_unifiProtect

This provides various driver capabilities for Hubitat with UniFi Protect systems. Supported devices include:
* cameras (Motion and ImageCapture capabilities, as well as Smart Detect for supported cameras)
* doorbells (Motion, Notification (LCD screen message), and PushableButton (for doorbell button presses))
* lights (Motion, Switch, and SwitchLevel (for dimming the light))
* *more capabilities may be added over time.*
<br><br>

Most of this implementation is based on the work shared here:

* https://github.com/hjdhjd/homebridge-unifi-protect

Special thanks to @Bago for their troubleshooting help.

# Manual Installation instructions:

* **Note:** this step is not required as of Hubitat platform version 2.2.8.143 and hubitat_unifiProtect version 1.3.0.
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
* Utilize Motion (from cameras, doorbells, and lights) and PushableButton (from doorbell) events, according to whatever is supported by your devices
* Use ```on()```, ```off()```, and ```setLevel()``` on lights
* Use the ```take()``` command on camera devices to take a snapshot from the main lens of the camera
    * A text attribute, ```displayImage``` will contain an HTML data URL to display the image on Dashboards.  A generic *Attribute* tile will render this for you.
    * Note that this may be a very large image, so if page loads or other performance suffers the ```clearImages()``` command can be used to flush the data
* Use the ```takePicture()``` command for capturing snapshots from camera devices that have multiple lenses, like the G4 Doorbell Pro.  
* Use the ```setRecordingMode(mode)``` on camera devices to modify the recording mode.  Supported modes: "always", "never", and either "motion" or "detections" (try both to see which is correct) depending on your version of UniFi Protect.
* Use the ```deviceNotification()``` command on doorbell devices to print a message to the LCD screen
    * Messages are limited to 30 characters by the UniFi Protect system

# Disclaimer

I have no affiliation with any of the companies mentioned in this readme or in the code.
