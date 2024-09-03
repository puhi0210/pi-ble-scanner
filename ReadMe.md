# Raspberry Pi BLE scanner
Projekt skeniranja naprav BLE z mikroračunanikom Raspberry Pi. Uporabil sem virtualno napravo z operacijskim sistemom Raspbian v okolju VirtualBox na osebnem računalniku.

## Kazalo
- [Virtualizacija Raspbian OS](#VM)
- [Postavitev po korakih](#steps)
- [Viri](#sources)


## Virtualizacija Raspbian OS <a name=VM></a>
Za postavitev virtualne naprave sem sledil video navodilom na povezavi: https://youtu.be/aUnvG3DFjBM

Za skeniranje naprav bluetooth je v okolju VirtualBox potrebno dodati pravilo za napravo USB za vmesnik Bluetooth (najdemo ga v Device manager-ju na gostujočem računalniku Windows). Na gostujočem OS je dobro tudi izključiti Bluetooth.

## Postavitev po korakih <a name=steps></a>
V terminalu Raspbery Pi-ja najprej kloniramo ta repozitorij:
```bash
$ git clone https://github.com/puhi0210/pi-ble-scanner.git

$ cd pi-ble-scanner
```
Skopirati je potrebno datoteko .env in nastaviti vrednosti spremenljivk:
```bash
$ sudo cp template.env .env

$ sudo nano .env
```


Namestimo orodje pip, libglib2.0-dev, bluepy, paho-mqtt:
```bash
$ sudo apt-get install python3-pip libglib2.0-dev

$ sudo pip3 install bluepy paho-mqtt python-dotenv
```

Nato poženemo program:
```bash
$ sudo python3 ble-scanner.pi
```


## Viri <a name=sources></a>
- Virtualizacija Raspbian v okolju VirtualBox: https://youtu.be/aUnvG3DFjBM
- Uporaba protokola MQTT s python knjižnico Pacho-MQTT in Mosquito MQTT brokerjem: https://medium.com/@potekh.anastasia/a-beginners-guide-to-mqtt-understanding-mqtt-mosquitto-broker-and-paho-python-mqtt-client-990822274923