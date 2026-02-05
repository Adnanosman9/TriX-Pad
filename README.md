<h1 align="center">
  Adnan's 3x3 Macro-Pad
  <br>
</h1>

<h4 align="center">
A custom mechanical macro-pad with OLED screen
</h4>

<div align="center">

![KiCad](https://img.shields.io/badge/KiCad-314CB0?style=for-the-badge&logo=kicad&logoColor=white)
![Fusion 360](https://img.shields.io/badge/Fusion%20360-FF6B00?style=for-the-badge&logo=autodesk&logoColor=white)

</div>

## Key Features

- **Seeed Studio XIAO RP2040** microcontroller
- **KMK Firmware** - CircuitPython
- **OLED Display** - SSD1306 (128×64)
- **3×3 Key Matrix** with diode orientation

## Design

Designed in KiCad and Fusion 360 for PCB and Case

### PCB

Designed in KiCad

**Schematic:**

<img src="Images/MacroPAD PCB Schemetic.png" alt="Schematic" width="800"/>

**PCB :**

<img src="Images/MacroPAD PCB Front.png" alt="PCB Front" width="800"/>

**PCB 3D view**

<img src="Images/PCB 3D.png" alt="PCB 3D" width="800"/>

### Case

Designed in Fusion 360 (This was my first time on CAD)

**Case Assembly:**

<img src="Images/Assembly.png" alt="Case Assembly" width="800"/>

**Case Top:**

<img src="Images/Top case.png" alt="Case Top" width="800"/>

**Case Bottom:**

<img src="Images/MacroPAD Bottom case.png" alt="Case Bottom" width="800"/>

### Final Build

<img src="Images/MacroPAD.png" alt="Final Build" width="800"/>

## Bill of Materials

| Component | Item | Qty | Link |
|-----------|------|-----|------|
| Controller | Seeed Studio XIAO RP2040 | 1 | [🛒](https://keebd.com/products/xiao-rp2040-controller) |
| Switches | MX-Style - Cherry | 9 | [🛒](https://www.aliexpress.com/item/1005008656717678.html) |
| Display | 0.96" SSD1306 OLED | 1 | [🛒](https://www.aliexpress.com/item/1005008754404998.html) |
| Diodes | 1N4148 | 9 | [🛒](https://store.roboticsbd.com/components/1355-1n4148-diode-robotics-bangladesh.html) |
| Keycaps | Blank DSA Keycaps | 9 | [🛒](https://keebd.com/products/ldsa-low-profile-blank-keycaps) |
| PCB | Custom PCB | 1 | [🛒](https://www.nextpcb.com/?code=BanglaGECS) |

*For full URLs and details, see [BOM.csv](BOM.csv)*

## Credits

This project uses:

- [KiCad](https://www.kicad.org/) for PCB design
- [Autodesk Fusion 360](https://www.autodesk.com/products/fusion-360/) for case design
- [KMK Firmware](https://github.com/KMKfw/kmk_firmware) for keyboard functionality
- [Hack Club Blueprint](https://blueprint.hackclub.com/) as guide and inspiration

## License

MIT

---

> GitHub [@Adnanosman](https://github.com/Adnanosman9)
