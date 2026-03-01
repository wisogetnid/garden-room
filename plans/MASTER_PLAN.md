# TECHNICAL SPECIFICATION: Cowes Passivhaus Woodworkshop (4x5m)

**Document Status:** High-Fidelity Construction Roadmap  
**Revision:** v2.0 (Granular Contractor Spec)  

> **⚠️ CRITICAL INFORMATION GAP:** @librarian - The source file `/research/structural_vibration.md` is missing from the repository. The 300mm joist centers and floor build-up below have been engineered based on standard acoustic best practices, but specific point-load deflection data for the exact workshop machines remains unverified.
> **⚠️ CRITICAL INFORMATION GAP:** @librarian - No research data was found regarding "3HP induction motors" in the existing `/research/` files (only 1HP to 1.5HP models were specified). The exact breaker amp rating for the 3HP machines (assumed 16A or 20A Type C) must be formally validated.

---

## 1. Structural Rigidity & Vibration Logic

To achieve the necessary flush threshold with the Cowes patio while preventing the "sounding board" effect of heavy cast-iron machinery, the foundation utilizes a hybrid **Concrete Raft + Decoupled Timber Sub-Floor**.

### 1.1 Foundation & Sub-Floor Build-up
*   **Base Foundation:** Legalett/Isoquick EPS-Insulated Concrete Raft (C25/30 concrete), steel mesh (B500A) with 50mm cover. Power-floated finish.
*   **Vibration Decoupling:** 15mm Vibro-FS high-density rubber isolation pads placed directly onto the concrete slab at 400mm intervals.
*   **Floor Joists:** 100x50mm C24 treated timber joists. 
    *   **Spacing:** Joist centers strictly set to **300mm** to eliminate flex under the point loads of heavy machinery (Table Saw, Planer).
    *   **In-Joist Dampening:** 100mm Rockwool RW3 (60kg/m³) packed tightly between joists.
*   **High-Mass Floor Deck (34mm total thickness):**
    *   *Base Layer:* 22mm P5 Moisture-Resistant Tongue & Groove Chipboard. Glued at joints with D4 polyurethane adhesive.
    *   *Acoustic Core:* 5kg/m² Mass-Loaded Vinyl (MLV) covering the entire floor footprint.
    *   *Top Layer:* 12mm WBP Structural Plywood. Screwed through the MLV into the P5 using 35mm screws (do not screw through to the joists to maintain the acoustic break).
*   **Machine Isolation:** 15mm dense anti-vibration ribbed rubber mats must be placed exactly under the four contact feet of the Table Saw and the Planer-Thicknesser to decouple high-frequency motor chatter from the 12mm Ply deck.
*   **Perimeter Expansion:** A strict 10mm gap must be maintained between the entire sub-floor assembly and the wall framing, filled with a flexible acoustic sealant (e.g., Green Glue Noiseproofing Sealant) to stop flanking noise.

---

## 2. The 'Cowes-Proof' Envelope Detail

### 2.1 Wall-Cladding Schedule (Outside to Inside)
| Layer | Material Specification | Fixing Method / Installation Rules |
| :--- | :--- | :--- |
| **1. Cladding** | James Hardie Fibre Cement Weatherboard (A2 Fire Rated). | 316 Stainless Steel annular ring shank nails (minimum 40mm). Minimum 30mm overlap per board. |
| **2. Battens** | 25x50mm Treated Timber (Class 3). | Fixed vertically at 400mm centers. Secured via 120mm Spax EWI E-X screws driven at a 60° angle through the insulation into the stud. |
| **3. Breather Membrane** | Tyvek UV Facade. | Stapled. Overlaps: 150mm vertical, 100mm horizontal. All seams perfectly taped with Tyvek Acrylic Tape. |
| **4. Continuous Insulation**| 50mm Rigid Wood Fibre or XPS. | Pushed friction-tight; butt joints offset. Held in place by the batten screws above. |
| **5. Sheathing** | 15mm OSB/3. | Fixed with 50mm galvanized ring shank nails at 150mm centers along all edges, 300mm in the field. |
| **6. Structural Studs** | 140x38mm C24 Timber. | Centers strictly 400mm. Double top-plate. Fixed with 90mm framing nails. |
| **7. Acoustic Core** | 140mm Rockwool RW3 (60kg/m³). | Friction fit between studs. No compression, no gaps. |
| **8. VCL (Airtightness)** | Pro Clima Intello Plus Intelligent Membrane. | Tacked with stainless staples. 100mm overlaps. **Every** seam taped with Pro Clima Tescon Vana. |
| **9. Service Cavity** | 25x50mm Treated Timber Battens. | Fixed horizontally at 400mm centers. Used for routing cables. |
| **10. Internal Finish** | 15mm Fermacell "One-Man" Boards (1200x600mm). | Fixed with Fermacell 30mm screws. Edges glued with Fermacell Jointstik (no taping/mudding required). |

### 2.2 Corner Junctions and Window/Door Reveals (VCL Continuity)
Maintaining Passivhaus airtightness at the weak points is mandatory.
*   **Structural Corners:** The Intello Plus VCL must wrap around the internal corners with a minimum 150mm overlap. Do not stretch the membrane tight into the corner; leave a small "slack fold" to accommodate seasonal timber movement. Tape the vertical seam with **Tescon Vana**.
*   **Window/Door Reveals:** At the 1.5 Asymmetric Door and any glazing, the VCL must be connected directly to the aluminum/timber composite frame. Use **Pro Clima Tescon Profil** (a pre-folded corner tape with split backing). Stick one side to the side of the door frame profile, and the other side flat onto the VCL. 

---

## 3. Workshop Infrastructure

### 3.1 Electrical Circuit Schedule
Given the massive inrush current (surge) of heavy woodworking machinery, the sub-main must be carefully balanced. All sockets are surface-mounted, heavy-duty IP66 (dust/moisture proof) located entirely within the 25mm service cavity.

| Circuit Name | Load / Devices | Breaker Specification | Wiring |
| :--- | :--- | :--- | :--- |
| **Main Incomer** | Armored Sub-main from house | 63A Double Pole Isolator | 3-Core SWA (buried 600mm) |
| **Radial 1 (Table Saw)** | 3HP Induction Motor | 20A RCBO - **Type C** | 2.5mm² Twin & Earth |
| **Radial 2 (Planer)** | 3HP Induction Motor | 20A RCBO - **Type C** | 2.5mm² Twin & Earth |
| **Radial 3 (Extraction)**| HVLP Extractor System | 16A RCBO - **Type C** | 2.5mm² Twin & Earth |
| **Ring Main (General)** | Hand tools, battery chargers | 32A RCBO - **Type B** | 2.5mm² Twin & Earth (Ring) |
| **Lighting / MVHR** | LED panels, dMVHR units | 6A RCBO - **Type B** | 1.5mm² Twin & Earth |

*Note: Type C breakers are mandatory for Radials 1-3. A Type C breaker allows surges of 5 to 10 times the rated current for a fraction of a second, preventing nuisance tripping when the heavy 3HP induction stators magnetize.*

### 3.2 Dust Extraction Integration
*   **Extraction Geometry:** 100mm **Rigid Galvanized Steel Ducting**. PVC ducting is strictly forbidden due to static electricity buildup and higher friction losses. Steel ensures a smooth bore to maintain the critical 20-25 m/s air velocity.
*   **Routing:** The main 100mm trunk runs exposed along the ceiling (secured to joists with rubber-lined acoustic pipe clamps). Y-branches (never T-junctions) are used for drops.
*   **Blast Gates:** Cast-aluminum body blast gates with steel sliders installed at every machine drop. Gates must be positioned at chest-height on the vertical drop to maximize the static pressure at the active machine.
*   **Cyclone Pre-separator:** Plumbed directly upstream of the main extractor. 99% of shavings drop into the sealed steel bin, protecting the HEPA filter for internal recirculation.

---

## 4. Bill of Materials (Key Specialist Items)

### 4.1 Foundation & Sub-Floor
| Item | Spec/Size | Qty / Area | Purpose |
| :--- | :--- | :--- | :--- |
| **Vibro-FS Pads** | 15mm Anti-vibration rubber | 120 units | Decouple sub-floor from concrete raft |
| **Floor Joists** | 100x50mm C24 Timber | 55 linear meters | Support deck at 300mm centers |
| **P5 Chipboard** | 22mm x 2400 x 600mm | 20m² | Structural sub-floor base |
| **Mass-Loaded Vinyl**| 5kg/m² MLV roll | 20m² | Primary acoustic mass blocking |
| **WBP Plywood** | 12mm x 2440 x 1220mm | 20m² | Rigid, screwable top deck |

### 4.2 Envelope & Finishes
| Item | Spec/Size | Qty / Area | Purpose |
| :--- | :--- | :--- | :--- |
| **Fibre Cement** | James Hardie Plank (A2 Rated) | 45m² | Coastal, fire-proof cladding |
| **316 SS Nails** | 40mm Annular Ring Shank | 1,500 units | Marine-grade rust prevention |
| **Spax EWI Screws** | 120mm E-X countersunk | 300 units | Secure battens through 50mm insulation |
| **Intello Plus VCL** | 1.5m x 50m roll | 1 roll | Passivhaus intelligent vapour barrier |
| **Tescon Vana Tape**| 60mm x 30m | 6 rolls | Airtight VCL seam taping |
| **Tescon Profil Tape**| 60mm x 30m | 2 rolls | Pre-folded corner/window taping |

### 4.3 Electrical & Climate
| Item | Spec/Size | Qty | Purpose |
| :--- | :--- | :--- | :--- |
| **Type C RCBOs** | 20A & 16A | 3 units | Handle 3HP induction motor inrush |
| **IP66 Sockets** | Double Switched 13A | 10 units | Dust/Moisture proof connection |
| **Ambient Purifier** | Axminster AW15AFS | 1 unit | Ceiling scrub of PM2.5 "dust flour" |
| **dMVHR Units** | Blauberg Vento | 2 units | Continuous fresh air / heat recovery |

---

## 5. Phased Build Schedule (Granular Execution)

*   **Week 1: Groundworks & Raft**
    *   Excavate to stable clay; lay MOT Type 1 and sand blinding.
    *   Lay 1200-gauge DPM.
    *   Assemble EPS raft formwork; set B500A mesh on 50mm chairs.
    *   Pour concrete and power-float the finish.
*   **Weeks 2-5: Concrete Curing Halt**
    *   *MANDATORY:* Absolute halt to allow concrete to off-gas hundreds of liters of moisture.
*   **Week 6: Sub-Floor & Acoustic Base**
    *   Install Vibro-FS pads onto the concrete at 400mm intervals.
    *   Lay out 100x50mm joists at 300mm centers.
    *   Pack joists with 100mm Rockwool.
    *   Install 22mm P5 chipboard (glued joints), roll out MLV, and screw down 12mm Plywood.
*   **Week 7: Wall & Roof Framing**
    *   Erect 140x38mm timber walls with double top-plates.
    *   Install roof joists and 18mm OSB deck.
    *   Install 150mm PIR rigid roof insulation and bond EPDM rubber membrane for immediate weather-tightness.
*   **Week 8: The 'Cowes-Proof' Exterior**
    *   Fix 15mm OSB sheathing to exterior studs.
    *   Friction-fit 50mm external wood fibre insulation.
    *   Wrap entirely in Tyvek UV Facade; tape all overlaps.
    *   Install 25mm battens using Spax EWI screws through to studs.
    *   Nail Fibre Cement cladding using 316 Stainless fasteners.
*   **Week 9: VCL & Internal Insulation**
    *   Install the 1.5 Asymmetric Door with automatic drop seals.
    *   Pack 140mm Rockwool tightly between all studs.
    *   Staple Intello Plus VCL to interior studs. 
    *   *VCL Detailing:* Execute 150mm corner folds, tape all seams with Tescon Vana, and bond door reveals with Tescon Profil.
*   **Week 10: Service Cavity & Electrical 1st Fix**
    *   Install 25mm horizontal battens *over* the VCL.
    *   Electrician runs 2.5mm² T&E for radials and ring main within the 25mm cavity.
    *   Mount 100mm rigid steel ducting to ceiling joists.
*   **Week 11: Internal Boarding & Finishes**
    *   Fix 15mm Fermacell boards to the service battens.
    *   Glue edges with Fermacell Jointstik.
*   **Week 12: 2nd Fix & Commissioning**
    *   Electrician installs IP66 sockets, Type C RCBOs, and tests the circuits (Part P compliance).
    *   Install Dehumidifier, Ambient Purifier, and dMVHR units.
    *   Move in heavy machinery (placing 15mm ribbed mats under feet).
