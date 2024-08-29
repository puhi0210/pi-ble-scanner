from bluepy.btle import Scanner, DefaultDelegate

# Maximalni RSSI za določanje bližine neprave
minRSSI = -70

# Class za skeniranje
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Najdena naprava", dev.addr)
        elif isNewData:
            print("Sprejeti novi podatki iz", dev.addr)

# Inicializacija skenerja
scanner = Scanner().withDelegate(ScanDelegate())

# Skeniraj naprave Bluetooth 10 s
devices = scanner.scan(10.0)

st_naprav = len(devices)



# Izpis
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Skeniranje končano.")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Vse naprave:\n")

for dev in devices:
    print("Naprava %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value))
    print("\n")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Naprave z lokalnim imenom:\n")

for dev in devices:
    if any("Local Name" in desc for (_, desc, _) in dev.getScanData()):
        print("Naprava %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            if "Local Name" in desc:
                print("  %s = %s" % (desc, value))
        print("\n")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


devicesNearBy = []

for dev in devices:
    if dev.rssi >= minRSSI:
        devicesNearBy.append(dev)

print("Število zaznanih naprav:", len(devices), "\n")
print("Število naprav v bližini (RSSI večji od %s dB): %s\n" % (minRSSI, len(devicesNearBy)))
