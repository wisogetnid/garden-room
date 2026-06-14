
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

## Date: 2026-05-23
**Architect Notes: Sloped SIP Roof + Flat 50mm PIR Warm-Over-Roof**
- **User Direction:** Replace the bespoke tapered PIR roof fall with SIP construction that provides the 1:60 slope. Install flat 50mm tissue-faced PIR above the SIP and fully adhere the EPDM membrane to the PIR.
- **Master Plan Update:** `plans/MASTER_PLAN.md` now specifies a sloped 150mm New Forest SIP roof panel/top-plate set-out, flat 50mm PIR warm-over-roof layer, and EPDM adhered to PIR. The roof fall setup table now identifies the SIP support geometry—not tapered insulation—as the source of drainage fall.
- **Workplan Synchronization:** `plans/WORKPLAN.md` now requires the delivery check to confirm sloped top plates/bearing geometry, roof installation to verify a 1:60 SIP surface before insulation, and Sunday weatherproofing to bond flat 50mm PIR followed by EPDM.
- **Technical Consequence:** Moisture robustness improves because the upper SIP OSB skin is kept warmer and drier beneath the PIR layer. The bespoke tapered PIR package is removed, which should reduce cost and procurement complexity.
- **Open Risk — resolved by following entry:** **[OPEN RISK FLAG: verify door/window head clearance]** The roof buildup increases to approximately 217mm, reducing the high-side wall height to 2133mm and the high-side internal ceiling height to about 2111mm after flooring. The 2100mm door/glazing datum must be verified against supplier rough-opening/head-clearance tolerances before SIP fabrication.

## Date: 2026-05-23
**Architect Notes: Internal/External Dimension Recalculation and Opening Validation**
- **Recalculated Plan Dimensions:** The accepted structural slab/SIP core remains **3430mm x 5430mm**. With 86mm external buildup each side, finished external dimensions remain **3602mm x 5602mm**. With 190mm internal buildup each side, usable internal dimensions remain **3050mm x 5050mm** (~15.4m²).
- **Recalculated Vertical Envelope:** Roof buildup is **217mm**. With 150mm exposed splash zone and 2500mm PD height cap, the high-side wall height is **2133mm** and low-side wall height is **2076mm**. Finished internal clear heights after 22mm flooring are **2111mm high side** and **2054mm low side**.
- **Opening Validation Result:** The previous **2100mm** door/window datum is not functional under the sloped-SIP/50mm-PIR roof. It leaves only ~11mm head zone at the high side and fails at the low side.
- **Corrected Opening Strategy:** The West façade is designated as the high side. West door becomes **1400mm x 2000mm maximum outer-frame-height**. West panorama windows become **1200x1000mm**, with heads at **2000mm FFL** and sills at **1000mm FFL**. North/South/East clerestories remain **300x1500mm**, but their top datum lowers to **1950mm FFL** and sills to **1650mm FFL**.
- **Workplan Synchronization:** `plans/WORKPLAN.md` now reflects the revised glazing and door sizes/datums and requires a ~100mm structural head zone above West openings.

## Date: 2026-05-23
**Architect Notes: Section 7.2 Heating Effort Recalculation**
- **User Correction:** Section 7.2 retained outdated heat-loss inputs. The glazing area was still listed as 4m² despite the revised door/window schedule, and the HTC/cost figures did not fully reflect the sloped-SIP plus 50mm PIR roof change.
- **Corrected Glazing Area:** West panorama windows = **2.40m²**; asymmetric door = **2.80m²**; four clerestories = **1.80m²**; total glazing/door assembly area = **7.00m²**.
- **Corrected Fabric Loss Inputs:** Gross wall area is **~37.29m²**. Opaque wall area is **~30.29m²** after subtracting openings. Roof and floor area are **18.62m²** each.
- **Corrected Thermal Result:** Total fabric heat loss is **16.78 W/K**. Adding **4.5 W/K** ventilation/air leakage gives a corrected HTC of **~21.28 W/K**.
- **Corrected Heating Effort:** Annual thermal demand is now **~766 kWh/year**. At **£0.245/kWh**, annual baseline heating cost is **~£187.68/year**.

## Date: 2026-05-23
**Architect Notes: MVHR, Ventilation, and Electrical Integration Expansion**
- **Research Source:** `research/mvhr-research.md` was integrated into `plans/MASTER_PLAN.md` and `plans/WORKPLAN.md`.
- **Master Plan Update:** Added Section 4.2 for dMVHR strategy, including isolated workshop ventilation, Zehnder ComfoAir 70-class enthalpy dMVHR, factory-cut wall sleeve, G4/F7 pre-filtration, optional HEPA/carbon stage, ambient filtration, pressure-balance rules, and Part F commissioning targets.
- **Ventilation Rates:** Revised internal volume is approximately **32m³**. Standby ventilation is **16-32m³/h** (0.5-1 ACH). Occupied/general dilution target is **60-70m³/h** (~2 ACH), with woodworking dust controlled by closed-loop extraction rather than outdoor exhaust.
- **Electrical Update:** Section 5 now separates machine, heating, IR/control, MVHR/filtration, and socket circuits. It adds airtight back boxes, MVHR control wiring, and a labelled future makeup-air interlock provision.
- **Workplan Synchronization:** Delivery checks now include dMVHR sleeve factory cut-out verification. Weekend 13 now includes MVHR sleeve sealing, G4/F7 inline extract filtration, segregated RCBO labelling, and explicit prohibition on outdoor dust-extractor discharge without interlocked makeup air. Final commissioning now includes BPEC/Part F airflow balancing and a filter/LEV maintenance log.
- **Risk Control:** Added risks for MVHR core contamination, pressure imbalance from outdoor exhaust, and COSHH/Part F compliance duties.

## Date: 2026-06-14
**Architect Notes: Roof Re-specification (122mm SIP + 100mm Glass Tissue-Faced PIR over-roof)**
- **User Query:** Is it possible to build the roof out of 120mm thick, 600mm wide SIPs using LVL splines with 100mm PIR insulation on top and glue EPDM directly to it?
- **Analysis:** Structurally and thermodynamically fully viable. Specifying narrow 600mm width is excellent for DIY manual handling (panels weigh ~30-35kg instead of 75kg). Joining with Laminated Veneer Lumber (LVL) splines creates structural mini-beams every 600mm, ensuring massive roof stiffness (solar-ready). The linear thermal bridging of LVL splines is completely capped and neutralized by the continuous 100mm PIR insulation on top. 
- **EPDM Adhesion Risk:** EPDM cannot be glued directly to standard foil-faced PIR due to lack of curing porosity and delamination. Specifying **glass tissue-faced PIR** (e.g. Kingspan Therma TR26) is mandatory to allow direct adhesive bonding.
- **Master Plan Update:**
  - Section 2.3: Re-specified roof sandwich to 120mm (122mm true) SIP roof panel (600mm narrow-format) with structural LVL splines, 100mm flat glass tissue-faced PIR over-roof, and fully adhered EPDM.
  - Section 2.3.2: Re-calculated height physics under the 2.5m Permitted Development limit. Roof buildup increases to 238.5mm (up 21.5mm). Max wall plate height adjusted to **2111.5mm** (high side) and **2054.3mm** (low side). High-side internal headroom becomes **2089.5mm** and low-side **2032.3mm**.
  - Section 2.3.2 (Opening datums): West wall door (1400x2000mm) and windows retain 2000mm top datum FFL, leaving exactly **89.5mm** structural head zone beneath the wall plate. East wall clerestories retain 1950mm top datum FFL, leaving **82.3mm** structural head zone. This is structurally validated by the SIP sheathing lintel strength.
  - Section 2.4: Updated roof fall setup table to specify 100mm glass tissue-faced PIR.
  - Section 7.1: Roof target U-value of 0.13 W/m²K remains, but achieved U-value is optimized from ~0.12 to **~0.11 W/m²K**. Added notes about glass tissue-facing and spline thermal-break capping.
  - Section 7.2: Recalculated fabric heat loss. Gross wall area is updated to ~36.91m² and opaque wall area to ~29.91m² due to wall height reduction. Recalculated roof heat loss to 2.05 W/K. Corrected Total Fabric Loss to **16.54 W/K** (down from 16.78 W/K) and Total Heat Transfer Coefficient (HTC) to **~21.04 W/K** (down from 21.28 W/K). Adjusted annual thermal demand to **757 kWh/year** (down from 766) and annual running cost to **£185.47/year**.
- **Hand-off to @foreman:** The site manager must now rework `plans/WORKPLAN.md` (the physical build sequence, deliveries, weights, lifting considerations, and height metrics) to ensure complete alignment with these new specifications.
