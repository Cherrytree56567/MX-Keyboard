# MX Keyboard
A Keyboard I made for Hackboard. It has a built-in USB C Hub and has Hotswap support.
![gif](https://hc-cdn.hel1.your-objectstorage.com/s/v3/feea19395a16cd392c0e3264e8fdf9a931bc45ca_0001-0180.gif)

## Info
 - 0.25mm Tolerance
 - Black Case

## Features
 - USB C Hub
 - RP2040
 - 61 Keys
 - Cherry MX Switches
 - Kailh Hotswap Sockets

# CAD
Here are some photos of the CAD 3D Print. It uses M2 Threads that are 6mm long on the top (gray part) and a 1.6mm M2 nut on the bottom plate (blue part) to raise the pcb.
I made the USB-C input and output separate so that they won't be confused and I've used Durock V3 Stabilizers for the spacebar, enter and shift keys. When I made my mini
keyboard last time, I made the holes too tight, so when I soldered the keys, if it was slightly tilted, it wouldn't fit in the case. This time, I added a 1.5mm padding.
<br><br>
<img width="1209" height="530" alt="image" src="https://github.com/user-attachments/assets/fb829d36-876a-43fd-81bc-06c7143a02aa" />
<img width="1385" height="616" alt="image" src="https://github.com/user-attachments/assets/db5551cc-8c99-444b-9005-4645d3813d0e" />
<img width="1385" height="584" alt="image" src="https://github.com/user-attachments/assets/33879247-234f-4813-80f1-108fb9d9eaf8" />
<img width="1381" height="582" alt="image" src="https://github.com/user-attachments/assets/65520dfd-f17c-4dca-b1aa-639e3feccfe5" />
<img width="1391" height="603" alt="image" src="https://github.com/user-attachments/assets/a4a17000-f346-4b09-9f8a-0ff0f1c4a65e" />
<img width="1414" height="107" alt="image" src="https://github.com/user-attachments/assets/6e8445e5-855e-4d90-b14f-cdc5fa09e285" />
Here is a photo of pcb and the case put together without the keys.<br><br>
<img width="1599" height="205" alt="image" src="https://github.com/user-attachments/assets/24ccd92f-b4c2-4aff-9768-0d1aa29bf78f" />

# PCB
Here are some photos of the PCB. I've made most of the main components to sit on the top, to prevent electromagnetic interference, and I've also uses ground fills.
The diodes and Kailh Hotswap sockets are placed under the board. The Git Repo was pretty messy because I had multiple revisions of the pcb and the case and I didn't
update some parts like the readme. It should be organised now. The wiring was pretty hard becuase it was my first time making a keyboard. I made a mini keyboard, but
there were some more things to worry about when making a full keyboard. I've used USB 2.0 because dealing with impedences was pretty difficult, and I didn't need a
USB 3.0 port anyway. If you want to take an upclose look at the pcb or the schematic, you can look the pdf's on the root of this repo.
<img width="1682" height="690" alt="image" src="https://github.com/user-attachments/assets/5ff668a7-8595-4cee-9ab9-26315224e7c9" />
<img width="1636" height="646" alt="image" src="https://github.com/user-attachments/assets/d95d703f-b393-4f6c-b14f-346ca70b3765" />
<img width="1590" height="638" alt="image" src="https://github.com/user-attachments/assets/ec551927-fae3-4d8a-92a9-addcd5af26ea" />
<img width="3307" height="2339" alt="pcb_schematic-1" src="https://github.com/user-attachments/assets/8649428c-4ad0-4e85-9810-cb219eaf400f" />

# Firmware
Unfortunatly, I don't know if the code works, because I haven't gotten the PCB yet, but to install it:
 - Install Circuit Python
   - [Download CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)
   - Plug the Keyboard in
   - Drag the .uf2 into the RP2040 Drive
 - Install KMK
   - [Download KMK](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip)
   - Unzip it and copy the `kmk` folder from `kmk_firmware-main` to the CIRCUITPY Drive
 - Install Firmware
   - Copy the Code from [src/main.py](https://github.com/Cherrytree56567/MX-Keyboard/raw/refs/heads/main/src/main.py)
   - Create a new file in the CIRCUITPY Drive called `code.py` and paste it in.

# Building
1. Print out the 3D Print and order the PCB
2. Solder all the parts on the PCB
3. Add the Kailh SMD Keys
4. Add the Durock V3 Stabilizers
5. Push the threads and nuts into the PCB using a Soldering Iron
6. Place the PCB in the case and screw it in
7. Install Firmware
<br>
Here is the JLC Ordering Screen
<img width="1414" height="797" alt="image" src="https://github.com/user-attachments/assets/7aa04b2f-4209-41d5-8223-7ca700c84267" />


# Bill of Materials
> [!NOTE]
> All Prices are in AUD

|Designator                                  |Footprint                                   |Quantity|Value                  |URL                                                       |Price_AUD|
|--------------------------------------------|--------------------------------------------|--------|-----------------------|----------------------------------------------------------|---------|
|C1, C2                                      |0402                                        |2       |15p                    |https://au.mouser.com/ProductDetail/581-04025A150G        |$1.82    |
|C10, C8                                     |0402                                        |2       |1u                     |https://au.mouser.com/ProductDetail/963-MAASL105CD7105MF  |$0.51    |
|C11, C12, C13, C14, C15, C16, C5, C6, C7, C9|0402                                        |10      |100n                   |https://au.mouser.com/ProductDetail/603-CC402KRX7R9BB104  |$0.27    |
|C23, C24                                    |0805                                        |2       |10uF                   |https://au.mouser.com/ProductDetail/81-GRM21BR61C106KE15  |$0.35    |
|C25                                         |0805                                        |1       |100nF                  |https://au.mouser.com/ProductDetail/581-KAF21KR72A104KL   |$0.29    |
|C3, C4                                      |0805                                        |2       |10u                    |https://au.mouser.com/ProductDetail/81-GRM21BR71A106KA3K  |$0.42    |
|D1, D...                                    |Diode_DO-35                                 |61      |Diode                  |https://au.mouser.com/ProductDetail/512-1N4148            |$3.78    |
|D34                                         |1206                                        |1       |SD1206T020S1R0         |https://au.mouser.com/ProductDetail/581-SD1206T020S1R0    |$0.62    |
|J1, J2, J4, J5                              |USB_C_Receptacle_HRO_TYPE-C-31-M-12         |1       |USB_C_Receptacle_USB2.0|https://www.aliexpress.com/item/1005003285152827.html?mp=1|$2.10    |
|R1, R2                                      |0805                                        |2       |5.1K                   |https://au.mouser.com/ProductDetail/667-ERA-2AEB512X      |$0.32    |
|R14, R15, R16, R17, R18, R19                |0805                                        |6       |56K                    |https://au.mouser.com/ProductDetail/667-ERA-6ARB563V      |$3.84    |
|R3, R5                                      |0402                                        |2       |1k                     |https://au.mouser.com/ProductDetail/754-RG1005V-102-WT1   |$6.28    |
|R4                                          |0402                                        |1       |DNF                    |                                                          |$0       |
|R6, R7                                      |0402                                        |2       |27                     |https://www.aliexpress.com/item/1005005433144951.html?mp=1|$0.40    |
|S1                                          |MX_PCB_1.00u                                |65      |Key                    |https://www.aliexpress.com/item/1005003944834891.html?mp=1|$19.10   |
|SW1                                         |SW_Push_1P1T_NO_Vertical_Wuerth_434133025816|1       |SW_Push                |https://au.mouser.com/ProductDetail/710-434133025816      |$0.88    |
|U1                                          |SOIC-16_4.55x10.3mm_P1.27mm                 |1       |SL2.1A                 |https://www.aliexpress.com/item/1005005552905296.html?mp=1|$1.89    |
|U2                                          |SOT-223-3_TabPin2                           |1       |NCP1117-3.3_SOT223     |https://au.mouser.com/ProductDetail/863-NCP1117ST33T3G    |$0.93    |
|U3                                          |SOIC-8_5.23x5.23mm_P1.27mm                  |1       |W25Q128JVS             |https://au.mouser.com/ProductDetail/454-W25Q128JVSIQTR    |$2.96    |
|U4                                          |RP2040-QFN-56                               |1       |RP2040                 |https://au.mouser.com/ProductDetail/358-SC09147           |$1.28    |
|Y1                                          |Crystal_SMD_3225-4Pin_3.2x2.5mm             |1       |ABM8-272-T3            |https://au.mouser.com/ProductDetail/815-ABM8-272-T3       |$1.04    |
|N/A                                         |Standoff                                    |4       |M2X6                   |https://au.mouser.com/ProductDetail/710-970060244         |$1.86    |
|N/A                                         |Nut                                         |12      |Nut                    |https://au.mouser.com/ProductDetail/855-M80-2430000B      |$3.46    |
|N/A                                         |Screw                                       |5       |M2_10mm                |https://www.ebay.com.au/itm/363744921549?var=632961986863 |$3.27    |
|N/A                                         |Socket                                      |70      |Kailh                  |https://www.aliexpress.com/item/1005007225352311.html?mp=1|$3.76    |
|N/A                                         |Stabilizer                                  |1       |Durock_V3_Stabilizers  |https://www.aliexpress.com/item/1005006628741999.html?mp=1|$22.39   |
|N/A                                         |Key_Caps                                    |1       |Black_Line_131         |https://www.aliexpress.com/item/1005007016258336.html?mp=1|$25.98   |
|N/A                                         |PCB                                         |1       |JLC_PCB                |https://jlcpcb.com/                                       |$17.60   |
|N/A                                         |Mouser Shipping                             |1       |Mouser_Shipping        |https://au.mouser.com                                     |$24      |
|N/A                                         |AliExpress Shipping                         |1       |Aliexpress_Shipping    |https://www.aliexpress.com                                |$1.59    |
|N/A                                         |JLCPCB Shipping                             |1       |JLCPCB_Shipping        |https://www.jlcpcb.com                                    |$11.47   |

Total Price: AUD$164.46
