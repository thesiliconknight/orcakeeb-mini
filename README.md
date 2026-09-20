# orcakeeb-mini

A 16-key mechanical macropad featuring a rotary encoder, per-key RGB, and a 0.91-inch OLED screen. The board is built around the Waveshare RP2040-Zero module, which handles the USB-C connection and logic, allowing for a highly compact PCB design. Fully compatible with QMK and KMK (CircuitPython) firmware.

## Pictures

| Top View | Bottom View |
| :---: | :---: |
| ![Board Front](<Images (R)/topbrd.png>) | ![Board Back](<Images (R)/btmbrd.png>) |

## Features

* **Main Controller:** Waveshare RP2040-Zero, providing a dual-core ARM Cortex-M0+ and natively handling USB-C and 3.3V regulation.
* **Switch Matrix:** 4x4 grid supporting 16 TTC low-profile mechanical switches, fully diode-isolated to prevent ghosting.
* **RGB Leds:** 16 reverse-mounted SK6812MINI-E LEDs sitting flush inside the switch cutouts. Powered directly via the 5V VBUS line.
* **Rotary Encoder:** Standard rotary encoder with push-button functionality. Relies on internal RP2040 pull-up resistors and software debouncing.
* **OLED Display:** I2C header for a standard 0.91" SSD1306 OLED module to display active layers, WPM, or custom graphics.

## Components Used

* **Microcontroller:** Waveshare RP2040-Zero Dev-Board
* **Switches:** 16x Cherry MX Switches or similar knock-offs
* **Diodes:** 16x 1N4148 
* **LEDs:** 16x SK6812MINI-E
* **Screen:** 0.91" SSD1306 I2C OLED Module
* **Miscellaneous:** 1x 10µF Ceramic Cap (for main 5V), 16x 0.1µF Caps (LED decoupling), EC11 (or similar knockoffs) Rotary Encoder

## Bill of Materials (BOM)

| Qty | Component | Designators | Unit Price (in INR) | Total Cost (also INR) | Source/Links |
| :---: | :--- | :--- | :---: | :---: | :--- |
| 1 | RP2040-Zero Dev-Board | U1 | 250.00 | 250.00 | [Robu.in](https://robu.in/product/rp2040-zero-for-raspberry-pi-microcontroller-with-soldering/) |
| 1 | 0.91" I2C OLED  | U2 | 212.00 | 212.00 | [Robu.in](https://robu.in/product/blue-oled-display-module/) |
| 1 | EC11 Encoder | SW19 | 47.00 | 47.00 | [Robu.in](https://robu.in/product/m274-360-degree-rotary-encoder-module-brick-sensor/) |
| 15 | SK6812MINI-E RGB LED | D1-D3, D5-D16 | 8.60 | 155.00 | [ETStore](https://www.etstore.in/products/e9974) |
| 15 | Mechanical Switches | SW1-SW12, SW14-SW16 | 18.00 | 360.00 | [StacksKB](https://stackskb.com/store/click-inc-hp-switch-pack-of-10-pre-order/) |
| 1 | Numpad Keycap Set | - | 100.00 | 100.00 | [StacksKB](https://stackskb.com/store/numpad-keycaps/?attribute_variant=Black+Gradient) |
| 15 | 1N4148W Diode | D17-D28, D30-D32 | 0.70 | 14.00 | [Robu.in](https://robu.in/product/1n4148w-sod-123-1206-diodereel-of-3000/) |
| 2 | 10kΩ Resistor  | R3, R4 | 0.86 | 10.00 | [Robu.in](https://robu.in/product/10k-ohm-1-4w-0603-surface-mount-chip-resistor-pack-of-100/) |
| 1 | 10µF Capacitor  | C17 | 1.54 | 10.64 | [Robu.in](https://robu.in/product/tcc0603x5r106k160ct-cctc-smt-ceramic-capacitors-0603-x5r-106k10%c2%b5f%c2%b110-rated-voltage16v-thickness0-80mm-tape/) |
| 1 | 10nF Capacitor  | C22 | 0.50 | 10.29 | [Robu.in](https://robu.in/product/tcc0603x7r103k500cts-cctc-smt-ceramic-capacitors-0603-x7r-103k10nf%c2%b110-rated-voltage50v-thickness0-80mm-tape/) |
| 15 | 100nF Capacitor | C1-C3, C5-C16 | 0.00 | 0.00 | [Robu.in](https://robu.in/product/100nf-0603-surface-mount-multilayer-ceramic-capacitor-pack-of-40/) |
| 5 | Custom PCB | - | 405.00 | 2025.00 | no link see folder |
| | | | **Total:** | **₹3,193.93** (33.29) | |

| Schematic Design |
| :---: |
| ![Schematic Diagram](<Images (R)/schematics_orcakeeb.png>) |

| PCB Top Layer Routing | PCB Bottom Layer Routing |
| :---: | :---: |
| ![Top Routing](<Images (R)/routing_topbrd.png>) | ![Bottom Routing](<Images (R)/routing_btmbrd.png>) |

### Connections
* **VBUS (5V):** Routes power straight from the USB-C port to the main 10µF bulk capacitor, then daisy-chains to the VDD pins of all 16 LEDs. 
* **OLED Header:** Connecetd to pins (SDA) G10 (SCK) G9
* **Encoder:** Connected to Pin G4, and A And B pins to G3 and G2
* **RGB Led Data:** Data IN pins connected to G14
  
## License

This hardware project is open-source and licensed under the CERN Open Hardware Licence Version 2 - Strongly Reciprocal (CERN-OHL-S-2.0). 

You are free to copy, modify, distribute, and manufacture this board for personal or commercial use. However, if you modify these schematic or layout files and distribute your new design, you must release those modifications under this exact same CERN-OHL-S-2.0 license.

This design is shared without any warranty or implied guarantee. Check the LICENSE file for the full legal text.
