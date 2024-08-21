from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Najdena naprava", dev.addr)
        elif isNewData:
            print("Sprejeti novi podatki iz", dev.addr)

# Initialize the scanner
scanner = Scanner().withDelegate(ScanDelegate())

# Scan for devices for 10 seconds
devices = scanner.scan(10.0)

for dev in devices:
    print("Naprava %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value))