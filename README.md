# Low-Power Embedded IoT System Power Consumption Analysis

This project investigates the **power consumption, current consumption, and wake-up behavior** of an **Arduino Nano RP2040 Connect** under different operating conditions.

The system was developed using **MicroPython** and evaluated through experimental measurements during sensor processing, Wi-Fi communication, and low-power operation.

## 🔧 Test Setup

Measurements were performed using:

* Arduino Nano RP2040 Connect
* DC power supply
* Oscilloscope
* 10 Ω shunt resistor
* Breadboard and wiring

The voltage drop across the shunt resistor was measured to determine current consumption.


## ⚡ Operating Modes

The system was evaluated under different operating conditions:

* Normal processing
* Temperature sensing
* Wi-Fi data transmission
* Beacon operation
* Sleep mode
* Wake-up from sleep

## 📡 Wi-Fi Communication

Temperature data was acquired and transmitted over Wi-Fi to a webpage available on the local network.

Oscilloscope measurements of the 10 Ω shunt resistor were used to evaluate current consumption during different operating modes.


## 💤 Wake-Up Measurement

The measured wake-up time from sleep mode was:

**1.14 seconds**

## 📊 Results

| Operating Mode     | Measured Current |
| ------------------ | ---------------: |
| Wi-Fi Transmission |       **124 mA** |
| Beacon Mode        |       **118 mA** |
| Normal Processing  |        **40 mA** |
| Sleep Mode         |      **15.6 mA** |

The measurements were performed with a **12 V supply**. The measurements show significantly higher current consumption during Wi-Fi-related operation compared with normal processing. The oscilloscope voltage profiles across the shunt resistor were used to characterize the current behavior during changes between operating modes.


## 📁 Repository Structure

Low-Power_Embedded_IoT_System_Power_Consumption_Analysis/
│
├── src/
├── images/
│   └── voltage_profile_wifi.png
└── README.md


## 🛠️ Tools & Technologies

* Arduino Nano RP2040 Connect
* RP2040
* MicroPython
* Wi-Fi
* Oscilloscope
* DC power supply
* Current and power measurement
* Experimental data analysis

## 🎯 Key Learning

This project provided practical experience in **embedded system development, low-power analysis, oscilloscope-based measurements, and experimental evaluation of power consumption**.
