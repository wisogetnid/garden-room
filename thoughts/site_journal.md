
## Date: 2026-04-28
**Architect Notes: Clerestory Window Datum Line Calibration**
- **User Query:** Are all clerestory windows at the same height?
- **Current Blueprint Logic:** Yes. The Master Plan (Section 2.5) explicitly states: *"The 300x1500mm fixed windows must be factory-cut into the SIPs at a high datum line (e.g., top edge aligned with the door header)."* 
- **The Door Header Height:** The door header is at 2100mm from Finished Floor Level (FFL).
- **The Mathematics of the Clerestories:**
  - Top Edge: 2100mm.
  - Height of Window: 300mm.
  - Bottom Sill: 2100mm - 300mm = **1800mm**.
- **Aesthetic Continuity:** This means that the top edges of the two 1200x1200mm West windows, the top edge of the 1400mm door, and the top edges of all four clerestory windows across the East, North, and South facades form a single, unbroken horizontal ring (a "Datum Line") exactly 2100mm off the floor. The bottom sills of all the clerestories sit exactly at 1800mm off the floor, leaving 1.8m of solid usable wall space below them globally.
- **Action:** Confirm this directly to the user, as the ASCII already perfectly reflects this (the top of the clerestories hits the 2.10m line, and the bottom hits the 1.80m line in the text drawings).

## Date: 2026-05-23
**Architect Notes: Boundary-Control Dimension Correction and Section 2.5 Deduplication — SUPERSEDED DIMENSIONALLY BY NEXT ENTRY**
- **User Correction:** Section 2.5 contained a duplicated West Façade 'Workbench Panorama' paragraph. Section 1.0 also rounded the true 172mm external projection reduction to 170mm, producing a 3430mm core that would finish at 3602mm externally if the 3.6m boundary clearance is absolute.
- **Master Plan Update:** `plans/MASTER_PLAN.md` was temporarily corrected to **3428mm x 5428mm** for SIP framework, concrete slab, and XPS tub. This dimensional decision is superseded by the following entry because the user later accepted a 2mm external oversail.
- **Geometry Consequences:** Usable internal dimensions are now **3048mm x 5048mm** (~15.39m²). The roof fall calculation is corrected to **3428 ÷ 60 = 57.1mm**. Roof span references now use 3428mm.
- **Glazing Text Update:** The duplicate Section 2.5 West Façade paragraph was removed; the 400mm rhythm and 900mm sill height remain stated once.
- **Workplan Synchronization:** `plans/WORKPLAN.md` was updated to use the **3428mm x 5428mm** tub, **4.228m x 6.228m** excavation footprint, ~9.22m³ soil excavation, and ~2.79m³ concrete pour volume.
- **Self-Verification:** Red Line test remains unchanged because the 50mm wood-fibre-to-XPS overlap is unaffected. Weather-tight sequence remains unchanged. Sequence test remains valid: groundworks, cure halt, SIP erection, Tyvek wrapping, and roof waterproofing still occur in physical order.

## Date: 2026-05-23
**Architect Notes: Accepted 2mm External Oversail and Reversion to Rounded Slab Order**
- **User Direction:** The user confirmed that a 2mm increase in finished external envelope is acceptable and instructed the concrete slab dimensions to be **3430mm x 5430mm**.
- **Master Plan Update:** `plans/MASTER_PLAN.md` now treats **3430mm x 5430mm** as the accepted SIP framework, XPS tub, and concrete slab order size. The resulting finished cladding-to-cladding dimensions are documented as **3602mm x 5602mm**.
- **Geometry Consequences:** Usable internal dimensions return to **3050mm x 5050mm** (~15.4m²). The roof span and tapered fall references now use **3430mm**, with 1:60 fall calculated at approximately **57.2mm**.
- **Workplan Synchronization:** `plans/WORKPLAN.md` now uses the **3430mm x 5430mm** tub, **4.23m x 6.23m** excavation footprint, ~9.22m³ soil excavation, ~9,224L open-excavation rain capacity, and ~2.8m³ concrete pour volume.
- **Self-Verification:** Red Line test remains intact; the envelope junction details are unchanged. Weather-tight sequence remains intact. Sequence test remains valid: excavation, XPS tub, DPM, mesh/UFH, pour, cure halt, SIP erection, and immediate weather protection remain in correct order.
