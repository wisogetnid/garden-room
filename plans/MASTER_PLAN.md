# TECHNICAL SPECIFICATION: Cowes Passivhaus Woodworkshop (4x5m)

**Document Status:** High-Fidelity Construction Roadmap  
**Revision:** v3.0 (Granular Contractor Spec)  

---

## 1. Structural Execution & Vibration Logic

### 1.1 Foundation Strategy (Clay Soil Adaptation)
*   **Geotechnical Context:** Cowes clay soils exhibit high "shrink-swell" movement in the upper 0.75m–1.0m active zone.
*   **Foundation Type:** **EPS-Insulated Concrete Raft (e.g., Legalett or Isoquick).**
    *   *Execution:* Excavate below the active organic layer. Install a compacted MOT Type 1 sub-base, sand blinding, and a continuous 1200-gauge polythene DPM.
    *   *Formwork & Pour:* Assemble high-compressive-strength EPS perimeter and base insulation (creating a zero-cold-bridge tub). Suspend B500A steel mesh on 50mm chairs to ensure adequate concrete cover against coastal carbonation. Pour and power-float the C25/30 concrete.

### 1.2 Floating Sub-Floor & Vibration Damping
To achieve the flush patio threshold and eliminate the "sounding board" effect of heavy cast-iron machinery, a decoupled floating timber sub-floor is constructed over the concrete raft.
*   **Decoupling Layer:** 15mm Vibro-FS rubber isolation pads placed directly on the concrete at 400mm intervals.
*   **Floor Joists:** 100x50mm C24 treated timber joists. 
    *   *Spacing:* Strictly set to **300mm centers** to provide extreme rigidity against the point loads of a 3HP table saw and planer.
    *   *Cavity:* Packed tightly with 100mm Rockwool RW3 (60kg/m³) for acoustic absorption.
*   **Sub-Floor Decking (34mm total thickness):**
    *   *Base Layer:* **22mm P5** Moisture-Resistant Tongue & Groove Chipboard, joints glued with D4 polyurethane.
    *   *Acoustic Core:* 5kg/m² Mass-Loaded Vinyl (MLV) stapled across the entire footprint.
    *   *Top Layer:* **12mm WBP Structural Plywood**, screwed through the MLV into the P5 board using 35mm screws (screws must *not* penetrate the joists to maintain the acoustic break).
*   **Machinery Isolation:** Industrial-grade **Sylomer® pads** (color-coded to the machine's static weight) must be placed exactly under the four contact feet of the Table Saw and the Planer-Thicknesser to isolate high-frequency motor chatter from the deck.
*   **Perimeter Expansion:** A 10mm gap between the floor deck and the wall framing must be maintained and filled with flexible acoustic sealant.

---

## 2. The 'Cowes-Proof' Envelope Detail

### 2.1 Wall-Cladding Schedule (Outside to Inside)
| Layer | Material Specification | Fixing Method / Installation Rules |
| :--- | :--- | :--- |
| **1. Cladding** | James Hardie Fibre Cement Weatherboard (A2 Fire Rated). | **316 Stainless Steel** annular ring shank nails (min 40mm). Minimum 30mm overlap per board. |
| **2. Battens** | 25x50mm Treated Timber (Class 3). | Fixed vertically at 400mm centers. Secured via 120mm **Spax EWI E-X screws** driven at a 60° angle through the insulation into the structural stud. |
| **3. Breather Membrane** | Tyvek UV Facade. | Stapled. Overlaps: **150mm vertical, 100mm horizontal**. All seams perfectly taped with Tyvek Acrylic Tape. |
| **4. External Insulation**| 50mm Rigid Wood Fibre or XPS. | Pushed friction-tight; butt joints offset. Held in place by the batten screws above. |
| **5. Sheathing** | 15mm OSB/3. | Fixed with 50mm galvanized ring shank nails at 150mm centers on edges, 300mm in the field. |
| **6. Structural Studs** | 140x38mm C24 Timber. | Centers strictly 400mm. Double top-plate. Fixed with 90mm framing nails. |
| **7. Acoustic Core** | 140mm Rockwool RW3 (60kg/m³). | Friction fit between studs. No compression, no gaps. |
| **8. VCL (Airtightness)** | Pro Clima Intello Plus Intelligent Membrane. | Tacked with stainless staples. 100mm overlaps. **Every** seam taped with Pro Clima Tescon Vana. |
| **9. Service Cavity** | 25x50mm Treated Timber Battens. | Fixed horizontally at 400mm centers. |
| **10. Internal Finish** | 15mm Fermacell "One-Man" Boards (1200x600mm). | Fixed with Fermacell 30mm screws. Edges glued with Fermacell Jointstik (no taping/mudding). |

### 2.2 Corner Junctions and Window/Door Reveals
Maintaining Passivhaus airtightness at the weak points is mandatory to prevent interstitial condensation.
*   **Structural Corners:** The Intello Plus VCL must wrap around internal corners with a minimum 150mm overlap. Leave a small "slack fold" to accommodate seasonal timber movement. Tape the vertical seam with **Tescon Vana**.
*   **Door Reveals:** At the 1.5 Asymmetric Door, the VCL must connect directly to the aluminum/timber composite frame. Use **Pro Clima Tescon Profil** (pre-folded corner tape with split backing). Stick one side to the side of the door frame profile, and the other side flat onto the VCL. 

---

## 3. Workshop Infrastructure

### 3.1 Electrical Circuit Schedule
Given the massive inrush current of heavy woodworking machinery (a 3HP induction motor pulls ~13A running, but spikes to **104A** for the first second), standard breakers will experience nuisance tripping.

| Circuit Name | Load / Devices | Breaker Specification | Wiring |
| :--- | :--- | :--- | :--- |
| **Main Incomer** | Sub-main from house | 63A Double Pole Isolator | **16mm² 2-Core SWA** (buried 600mm) |
| **Radial 1 (Table Saw)** | 3HP Induction Motor | 20A RCBO - **Type C** | 2.5mm² Twin & Earth |
| **Radial 2 (Planer)** | 3HP Induction Motor | 20A RCBO - **Type C** | 2.5mm² Twin & Earth |
| **Radial 3 (Extraction)**| HVLP Extractor System | 16A RCBO - **Type C** | 2.5mm² Twin & Earth |
| **Ring Main (General)** | Hand tools, chargers | 32A RCBO - **Type B** | 2.5mm² Twin & Earth (Ring) |
| **Lighting / MVHR** | LED panels, dMVHR | 6A RCBO - **Type B** | 1.5mm² Twin & Earth |

*   **Sub-Main Sizing:** 16mm² SWA is specified (rather than 10mm²) to future-proof the voltage drop for the planned Solar PV + Battery system.
*   **Emergency Stop:** A **Contactor-based E-Stop system** will control Radials 1, 2, and 3. Hitting any wall-mounted mushroom button breaks the 230V control circuit, opening the contactor and killing machine power instantly (leaving lights and general sockets active).
*   **Sockets:** All sockets on the machine radials and ring main must be surface-mounted **IP66 rated** (dust-tight) to prevent combustible dust ingress.

### 3.2 Dust Extraction Integration
*   **Extraction Geometry:** **100mm Rigid Galvanized Steel Ducting**. PVC is strictly forbidden due to static electricity buildup. Steel ensures a smooth bore to maintain the critical 20-25 m/s air velocity required to keep chips entrained.
*   **Routing & Blast Gates:** The main 100mm trunk runs exposed along the ceiling. Y-branches drop down vertically to the machines. Cast-aluminum body blast gates with steel sliders are installed at every drop at chest-height to concentrate static pressure.
*   **The Cyclone:** An Oneida Dust Deputy (or equivalent) plumbed upstream of the main extractor. Spins out 99% of waste.
*   **Secondary Defense:** A ceiling-mounted **Ambient Air Purifier** (e.g., Axminster AW15AFS) to continuously scrub escaped PM2.5 "dust flour" that the cyclone misses, protecting the dMVHR system.

---

## 4. Phased Build Schedule (Solo Execution)

*   **Phase 1: Groundworks & Raft**
    *   Excavate to stable clay; lay MOT Type 1 and sand blinding.
    *   Lay 1200-gauge DPM.
    *   Assemble EPS raft formwork; set B500A mesh on 50mm chairs.
    *   Pour C25/30 concrete and power-float the finish.
*   **Phase 2: Concrete Curing Halt (Weeks 2-5)**
    *   *MANDATORY:* Absolute 4-week halt to allow concrete to off-gas hundreds of liters of moisture.
*   **Phase 3: Sub-Floor & Acoustic Base**
    *   Install Vibro-FS pads onto the concrete at 400mm intervals.
    *   Lay out 100x50mm joists at 300mm centers.
    *   Pack joists with 100mm Rockwool.
    *   Glue/screw 22mm P5 chipboard, roll out 5kg/m² MLV, and screw down 12mm Plywood.
*   **Phase 4: Wall & Roof Framing**
    *   Erect 140x38mm timber walls with double top-plates.
    *   Install roof joists and 18mm OSB deck.
    *   Install 150mm PIR rigid roof insulation and bond EPDM rubber membrane for immediate weather-tightness.
*   **Phase 5: The 'Cowes-Proof' Exterior**
    *   Fix 15mm OSB sheathing to exterior studs.
    *   Friction-fit 50mm external wood fibre insulation.
    *   Wrap entirely in Tyvek UV Facade; tape all overlaps.
    *   Install 25mm battens using Spax EWI screws through to studs.
    *   Nail Fibre Cement cladding using 316 Stainless fasteners.
*   **Phase 6: VCL & Internal Insulation**
    *   Install the 1.5 Asymmetric Door with surface-mounted automatic drop seals.
    *   Pack 140mm Rockwool tightly between all studs.
    *   Staple Intello Plus VCL to interior studs. 
    *   *VCL Detailing:* Execute 150mm corner folds, tape all seams with Tescon Vana, and bond door reveals with Tescon Profil.
*   **Phase 7: Service Cavity & Electrical 1st Fix**
    *   Install 25mm horizontal battens *over* the VCL.
    *   Electrician runs T&E cables for radials/ring main within the 25mm cavity.
    *   Mount 100mm rigid steel ducting to ceiling joists.
*   **Phase 8: Internal Boarding & Finishes**
    *   Fix 15mm Fermacell boards to the service battens.
    *   Glue edges with Fermacell Jointstik.
*   **Phase 9: 2nd Fix & Commissioning**
    *   Electrician installs IP66 sockets, Type C RCBOs, Contactor E-Stop system, and tests circuits (Part P compliance).
    *   Install Dehumidifier, Ambient Purifier, and dMVHR units.
    *   Move in heavy machinery (placing Sylomer pads under feet).
