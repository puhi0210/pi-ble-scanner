# Raspberry Pi BLE scanner
Projekt skeniranja naprav BLE z mikroračunanikom Raspberry Pi. Uporabil sem virtualno napravo z operacijskim sistemom Raspbian v okolju VirtualBox na osebnem računalniku.

## Kazalo
- [Virtualizacija Raspbian OS](#VM)
- [Postavitev po korakih](#steps)


## Virtualizacija Raspbian OS <a name=VM></a>
Za postavitev virtualne naprave sem sledil video navodilom na povezavi: https://youtu.be/aUnvG3DFjBM

Za skeniranje naprav bluetooth je v okolju VirtualBox potrebno dodati pravilo za naoravo USB za vmesnik Bluetooth (najdemo ga v Device manager-ju na gostujočem računalniku Windows)

## Postavitev po korakih <a name=steps></a>
V terminalu Raspbery Pi-ja najprej kloniramo ta repozitorij:
```bash
$ git clone https://github.com/puhi0210/pi-ble-scanner.git

$ cd pi-ble-scanner
```

Namestimo orodje pip, libglib2.0-dev in bluepy:
```bash
$ sudo apt-get install python3-pip libglib2.0-dev

$ sudo pip3 install bluepy
```

Nato poženemo program:
```bash
$ sudo python3 ble-scanner.pi
```

