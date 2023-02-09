# UHF MAX Breakout


UHF MAX Breakout is an advance and compact "Ultra High Frequency" RFID reader that consists of powerful RFID technology designing for a broad range of applications in the defense, healthcare system, banks, offices etc. UHF MAX Breakout has an onboard ThingMagic® M6E Nano UHF RFID Reader that is JADAK’s smallest embeddable module with ultra-low power consumption and tiny form factor. This RFID reader is ideal for battery operated, low-cost, small form factor portable devices.

<img src ="https://github.com/sbcshop/UHF_MAX_Breakout_Software/blob/main/images/UHF%20Breakout.png" />

## Breakout Using With Pi

<img src = "https://github.com/sbcshop/UHF_MAX_Breakout_Software/blob/main/images/Img2.png" />

* For using this break out with Raspberry Pi follow the steps below:

Enable Serial Port for this type ```sudo raspi-config``` in command promt, then go to Interface Options -> Serial Port - > Would you like a login shell to be accessible over ? type "**No**" then Would you like the serial port hardware to be enabled? type "**Yes**"
         
## How to enable the external UFL port in the UHF breakout
<img src = "https://github.com/sbcshop/UHF_MAX_Breakout_Software/blob/main/images/img011.png" />

## Run Using Python (Raspberry Pi) Run below command one by one

First, make sure you have the required packages

 ```pip install Pillow ```

```sudo apt-get install unzip patch xsltproc gcc libreadline-dev python-dev python-setuptools```

Install Mercury API, for this you need to download below repository

https://github.com/gotthardp/python-mercuryapi

 or 
 
```git clone https://github.com/gotthardp/python-mercuryapi.git```

```cd python-mercuryapi```

Give permission to all files

```sudo chmod 777 *```

```make```

The make command will automatically determine which Python version is installed. If both 2.x and 3.x are installed, the 3.x takes precedence. To build and install 2.x you need to explicitly specify the Python interpreter to use:

```sudo make PYTHON=python```

Then, install the module by running

```sudo make install```

which is a shortcut to running

```sudo python setup.py build install```

#### make sure jumper wire is sort between RX-TX0 and TX-RX1
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img10.jpg" />



 ## Run Using Universal Assistant(Via Micro USB)
 # For using UHF MAX Breakout Via Micro USB cable follow the step guide below:
 

**Download Universal Assistant Software From Below Link, And Install The Software**

https://www.jadaktech.com/resources/all-document-libraries/#Universal_Reader_Assistant

**Step 1 - Open the software, Connect UHF HAT To computer via micro usb cable ( make sure jumper wire is sort between U_RX-TX0 and U_TX-RX1 ) as shown in picture, then click on refresh button to refresh the serial port**. ***Jumpur*** should be connected as shown below, when using UHF MAX Breakout via USB:


<img src = "https://github.com/sbcshop/UHF_MAX_Breakout_Software/blob/main/images/Img1.png" />

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img.JPG" />

**Step 2 - Then click next or skip button**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img1.JPG" />

**Step 3 - Then select the baudrate**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img2.JPG" />
        
**Step 4 - Connect**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img3.JPG" />
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img4.JPG" />
         
**Step 5 - Select your region and anteena and go to read**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img6.JPG" />
         
**Step 6 - Now it start read the cards**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img7.JPG" />
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img8.JPG" />

***Note -*** Buzzer is connected to GPIO 17 Pin of raspberry pi


## Documentation

* [UHF MAX Breakout Hardware](https://github.com/sbcshop/UHF_MAX_Breakout_Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [RFID HAT for RaspberryPi](https://shop.sb-components.co.uk/products/rfid-hat-for-raspberry-pi?_pos=3&_sid=59f725ea2&_ss=r)

 ![RFID HAT for RaspberryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/RFIDforPi.jpg?v=1614587676&width=400)

* [RaspberryPi Pico RFID Expansion](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion?_pos=3&_sid=075681430&_ss=r)

 ![RaspberryPi Pico RFID Expansion](https://cdn.shopify.com/s/files/1/1217/2104/products/2_85a5dfb2-96cb-4e0b-ba28-a70af127a4f1.png?v=1613732653&width=400)
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>

