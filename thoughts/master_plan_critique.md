# Rigorous Technical Audit: Cowes Passivhaus Woodworkshop
**Auditor:** Lead Building Inspector & Passivhaus Consultant
**Date:** March 2026
**Target Document:** `plans/MASTER_PLAN.md` (v4.0)

## 1. Critical Vulnerabilities (Red Flags)

### 🔴 Structural Wind Uplift & Foundation Anchoring
**The Flaw:** The plan details a heavy concrete raft and a timber frame, but entirely omits the mechanical connection between the two. Cowes is a high-wind coastal zone. Without specified anchor bolts tying the sole plate to the concrete slab, the structure is vulnerable to severe wind uplift and racking. Furthermore, the plan specifies a "polymeric DPC" but fails to mandate a *compression-rated* DPC. Standard DPC will extrude (squish out) under the weight of the timber frame, breaking the damp seal and loosening the anchor bolts.

### 🔴 Localized Sub-Floor Deflection (The 250kg Point Load)
**The Flaw:** The plan specifies 100x50mm C24 joists on Vibro-FS isolation pads at 400mm spacing, topped with 34mm of decking. However, placing a 250kg cast-iron planer (a massive dynamic live-load) on this floating floor risks localized crushing of the Vibro-FS pads. The joists themselves won't span 4m (they rest on the slab via pads), but the *pads* must be rated for the concentrated point load, or the floor will dip and permanently deform under the machinery, ruining tool calibration.

### 🔴 Unsealed VCL Penetrations (Passivhaus Failure)
**The Flaw:** The plan correctly specifies "Kaiser Airtight Grommet Boxes" for electrical sockets in the service cavity. However, it completely ignores the massive penetrations required for the **dMVHR units** (approx. 100mm-150mm holes) and the **Dehumidifier permanent condensate drain**. If these punch through the Intello Plus VCL without certified EPDM airtightness grommets, the Passivhaus airtightness fails entirely, inviting severe interstitial condensation.

### 🔴 Galvanic & Coastal Corrosion Overlap
**The Flaw:** The plan specifies 316 Stainless Steel for the cladding nails and vermin mesh. However, it specifies "120mm Spax EWI E-X screws" for the external battens and "Galvanized Steel" for the internal dust ducting. Standard EWI screws are often heavily zinc-plated (Wirox) but *not* A4 stainless. In a marine environment, zinc coating will aggressively corrode, causing the heavy external cladding to shear off.

### 🔴 Dust Extraction Static Grounding (Explosion Risk)
**The Flaw:** The plan specifies rigid galvanized steel ducting to "prevent static electricity sparks (unlike PVC)." This is a dangerous half-measure. While steel *conducts* static electricity, it does not *dissipate* it unless the entire ducting network is physically **Earth Bonded** (grounded) to the electrical system. Without an earth strap, the metal ducting becomes a massive capacitor capable of discharging a high-voltage spark into a cloud of PM2.5 wood dust (ATEX explosion risk).

---

## 2. Technical Recommendations & Rectifications

| Vulnerability Area | Required Material / Specification Update | Purpose & Execution |
| :--- | :--- | :--- |
| **Foundation Anchoring** | **M12 A4 (316) Stainless Anchor Bolts** embedded 100mm into the concrete slab via chemical resin. Max 1200mm centers. | Physically ties the timber frame to the high-mass concrete raft to resist coastal wind uplift and shear forces. |
| **Sole Plate DPC** | **Visqueen High-Performance (HP) Compression-Rated DPC**. | Withstands the compressive structural load of the building without extruding, ensuring anchor bolts remain tight. |
| **Point-Load Isolation** | **High-Load Sylomer® Strips (Brown or Red)**. | Standard Vibro-FS pads will crush under the 250kg planer. Specific high-load elastomer pads must be substituted directly beneath machinery footprints. |
| **VCL Penetrations** | **Pro Clima Roflex / Kaflex EPDM Grommets**. | Every pipe (MVHR, dehumidifier drain) or cable breaching the VCL must pass through a tight-fitting, taped EPDM rubber gasket to maintain absolute airtightness. |
| **Exterior Batten Fasteners**| **Spax EWI Screws (A4 / 316 Stainless ONLY)**. | Coastal marine environments destroy zinc/galvanized coatings. All fasteners penetrating the rain-screen gap must be A4 stainless. |
| **Dust Ducting Grounding** | **10mm² Earth Bonding Copper Wire**. | The galvanized steel ductwork must be physically clamped and wired to the main earth terminal in the workshop consumer unit to dissipate static charge safely. |

---

## 3. Required Librarian Deep-Dives

**@librarian - Action Required:** The current plan relies on generalized UK building data. For a high-fidelity 2026 Passivhaus build in Cowes, we require exact, verified technical data points to fill the remaining 'Black Holes' in our engineering logic.

Please research and provide specific data on the following 5 points:

1.  **Coastal Wind-Load Data (Isle of Wight / Cowes):** What is the required basic wind speed (m/s) and dynamic wind pressure (kN/m²) for structural calculations in Cowes, PO31? We need this to verify if M12 anchors at 1200mm centers are sufficient.
2.  **Elastomer Deflection Rates (Getzner Sylomer):** Find the exact static load limit (in N/mm²) for standard "Vibro-FS" pads versus "Sylomer Brown/Red" pads to support a 250kg dynamic load over a 0.5m² footprint without exceeding 10% deflection.
3.  **Acoustic Assembly Rw Rating:** What is the specific predicted decibel-drop (Rw rating) of our exact wall assembly: *15mm Fermacell + 140mm Rockwool RW3 + 15mm OSB3 + 50mm Wood Fibre + Fibre Cement Cladding*?
4.  **A4 (316) EWI Screw Availability:** Confirm the availability, brand, and shear-strength of 120mm A4 (316) stainless steel screws designed specifically for External Wall Insulation (EWI) over timber studs in the UK market.
5.  **ATEX / BS 7671 Static Grounding:** What is the specific BS 7671 electrical regulation code for cross-bonding / earth-grounding exposed metallic dust extraction ductwork in a combustible dust environment?