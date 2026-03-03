# Rigorous Technical Audit: Cowes Passivhaus Woodworkshop
**Auditor:** Lead Building Inspector & Passivhaus Consultant
**Date:** March 2026
**Target Document:** `plans/MASTER_PLAN.md` (v4.0)

## 1. Critical Vulnerabilities (Red Flags)

### 🔴 1. Structural Logic: The "Extruding" DPC
**The Flaw:** Section 1.3 specifies a "Polymeric DPC bonded to 1200g DPM" under the Compacfoam and sole plate. However, it fails to specify that this must be a **Compression-Rated** DPC. A standard polymeric DPC will physically extrude (squish out) over time under the 2.5-ton static dead-load of the building and the dynamic live-load of the machinery. This will break the moisture seal and loosen the M12 anchor bolts over time, putting the structure at risk during high coastal winds.

### 🔴 2. Structural Logic: Thermal Mass Bonding Failure
**The Flaw:** Section 3.1 correctly removes the floating timber floor to allow the Wet UFH thermal battery to radiate, but specifies gluing an engineered timber/LVT deck directly to the slab. In a woodworking shop, dropping heavy tools or shifting a 250kg cast-iron machine across a fully glued finish will instantly gouge or crack it. Because it is permanently glued to the thermal mass, replacing a damaged section requires grinding the adhesive off the concrete, risking catastrophic damage to the 16mm PEX heating pipes embedded just below the surface.

### 🔴 3. Envelope Integrity: Unsealed dMVHR Penetrations
**The Flaw:** The plan brilliantly updated the dehumidifier to a zero-penetration "Smart Tank" model, and handles electrical sockets with airtight Kaiser boxes. However, it completely ignores the massive penetrations required for the **dMVHR ventilation units** (typically 100mm–150mm core holes straight through the wall). If these punch through the Intello Plus VCL without certified EPDM airtightness collars (e.g., Pro Clima Roflex), the Passivhaus envelope will haemorrhage warm, moist air into the cold exterior wall cavity, causing immediate interstitial rot.

### 🔴 4. Salt-Air Corrosion: The "Galvanized" Trap
**The Flaw:** Section 2.1 mandates 316 Stainless nails for the cladding, but critically specifies **"50mm galv ring shanks"** for the OSB3 sheathing. In the coastal Cowes environment, saline moisture easily penetrates the breathable rain-screen gap. Galvanized fasteners will undergo galvanic corrosion, rust rapidly, and eventually shear off under the immense racking loads of coastal winds. **All** structural fasteners on the cold side of the insulation must be A4 (316) Stainless Steel.

### 🔴 5. Workshop Safety: The "Capacitor" Dust Ducting (ATEX Explosion Risk)
**The Flaw:** Section 5.1 proudly states that the rigid galvanized steel ducting "prevents static electricity sparks." This is a catastrophic misunderstanding of physics. Metal ductwork moving high-velocity particulate *generates* massive static charge. Because it is metal, it conducts this charge, turning the entire pipe into a giant capacitor. Without a dedicated **Static Grounding Strap** (Earth Bonding), it will eventually discharge a high-voltage arc into the PM2.5 wood dust inside the pipe, risking a lethal ATEX dust explosion.

### 🔴 6. Workshop Safety: Missing Machinery "Kill Switch" (NVR)
**The Flaw:** The electrical schedule specifies Type C RCBOs and IP66 sockets, but completely omits a localized **Master Kill Switch** or a **No-Volt Release (NVR) contactor system**. In a professional woodworking environment, if a workpiece binds in the table saw, you cannot rely on running to the wall to unplug an IP66 socket. There must be an emergency stop circuit that kills all heavy machinery instantly without dropping the lighting circuits.

---

## 2. Technical Recommendations

| Vulnerability Area | Required Specification Update | Purpose & Execution |
| :--- | :--- | :--- |
| **Sole Plate DPC** | **Visqueen High-Performance (HP) Compression-Rated DPC**. | Withstands the compressive structural load of the building without extruding, ensuring anchor bolts and the moisture seal remain intact. |
| **Hard-Bonded Floor Risk** | **Heavy-Duty Floating LVT (No Glue)** or **Polished Concrete**. | If an aesthetic deck is desired over the thermal mass, it must be a 'click-lock' floating system to allow for easy repair/replacement without grinding adhesive near embedded UFH pipes. |
| **VCL Penetrations** | **Pro Clima Roflex / Kaflex EPDM Grommets**. | Every pipe (dMVHR cores, UFH manifold) breaching the VCL must pass through a tight-fitting, taped EPDM rubber gasket to maintain absolute Passivhaus airtightness. |
| **OSB Fasteners**| **50mm A4 (316) Stainless Steel Ring Shanks**. | Coastal marine environments destroy zinc/galvanized coatings. All fasteners in the exterior envelope must be 316 Stainless. |
| **Dust Ducting Grounding** | **10mm² Earth Bonding Copper Wire**. | The galvanized steel ductwork must be physically clamped and wired to the main earth terminal in the workshop consumer unit to dissipate static charge safely. |
| **Machinery Safety** | **Contactor-Based E-Stop Circuit**. | A dedicated NVR (No-Volt Release) circuit for the machinery radials, controlled by easily accessible mushroom-head 'Kill Switches' on the walls. |

---

## 3. Required Librarian Deep-Dives

**@librarian - Action Required:** The current plan relies on generalized building data. For a high-fidelity 2026 Passivhaus build in Cowes, we require exact, verified technical data points to fill the remaining 'Black Holes'. Please provide precise data on the following 6 points:

1.  **Coastal Wind-Load Data (Isle of Wight / Cowes):** What is the exact basic wind speed (m/s) and dynamic wind pressure (kN/m²) required by the IOW Council for structural calculations in Cowes (PO31)? We must verify that M12 anchors at 1200mm centers are sufficient.
2.  **UFH Slab Cover Math:** If an aesthetic LVT floor is fully bonded, what is the exact minimum concrete coverage (in mm) required above the 16mm PEX-a UFH pipes to safely allow mechanical surface grinding/repair without risking a puncture?
3.  **Acoustic Assembly Rw Rating:** What is the specific predicted decibel-drop (Rw rating) of our exact wall assembly: *15mm Fermacell + 140mm Rockwool RW3 + 15mm OSB3 + 50mm Wood Fibre + Fibre Cement Cladding*?
4.  **Galvanic Corrosion Rates:** What is the documented failure timeline of standard Galvanized (Zinc-coated) ring shank nails when exposed to coastal saline air in the UK? 
5.  **ATEX / BS 7671 Static Grounding:** What is the specific BS 7671 electrical regulation code for cross-bonding / earth-grounding exposed metallic dust extraction ductwork in a combustible dust environment?
6.  **dMVHR Core Sizing:** What exact diameter core drill (e.g., 100mm, 150mm) is required for the Blauberg Vento dMVHR units, and what specific Pro Clima Roflex grommet size matches it?