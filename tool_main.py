import asyncio
from bleak import BleakScanner

async def main():
    print("Scanning for nearby BLE devices...\n")
    devices = await BleakScanner.discover(timeout=8.0)

    print("Number of devices found:", len(devices))
    print("-" * 40)
    for device in devices:
        print("Device Name :", device.name or "Unknown Device")
        print("Address     :", device.address)
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())