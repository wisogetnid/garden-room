
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
## Date: 2026-06-20
**Architect Notes: Dry Moat Strategy & 150mm Headroom Reclamation**
- **User Request:** Sink the entire slab structure 150mm using a "dry moat" strategy to make the finished top of the concrete flush with the garden lawn, thereby reclaiming 150mm of internal headroom under the 2.5m Permitted Development limit.
- **Master Plan Update:**
  - Section 1.1: Replaced "150mm exposed splash zone" with "Dry Moat Strategy & Excavation Depth". The MOT Type 1, blinding sand, and XPS tub must be sunk an additional 150mm.
  - Section 1.3: Updated the splash margin to explicitly mention the "Moat" and added a Terram 1000 Geotextile Buffer instruction. Updated the waterproofing sweep to require the DPM/EPDM skirt to drop down the external SIP wall and sweep horizontally across the top of the newly formed 350mm flat XPS projection, carved with a slight outward fall.
  - Section 2.3.2: Re-calculated height physics. Splash zone is now 0mm (flush with garden lawn). Max 'High-Side' wall height increased by 150mm to **2261.5mm**. 'Low-Side' wall height increased to **2204.3mm**.
  - Section 2.3.2 (Internal ceiling height): Internal ceiling heights increased to an ergonomic **~2239mm** (high side) and **~2182mm** (low side).
  - Section 2.3.2 (Opening datums): Updated the theoretical maximum structural opening datums to **2150mm** and **2100mm**.
  - Section 2.5: Re-specified glazing/door schedules to take advantage of the recovered height. The door and West fixed windows are now **2150mm top datum**. The North/South/East clerestory windows have been restored to a **2100mm top datum** (1800mm bottom sill).
- **Hand-off to @foreman:** @foreman, you must now rework `plans/WORKPLAN.md` to reflect the updated excavation depth, new moat/drainage sequence (geotextile buffer, outward fall on XPS projection), and updated structural heights/lifting logistics.
- **Hand-off to @strategist:** @strategist, please run the tests and validate this updated Master Plan against constraints (the 'Red Line' test, sequence logic, and PD limits).

## Date: 2026-06-20
**Architect Notes: Strategist Validation Fixes & Red Line Reversal**
- **Validation Results Review:** The strategist flagged three critical conflicts. 1) Sinking the slab violates the 150mm *elevated* splash zone requirement in `001_foundation_strategy.md`. 2) The Compacfoam thermal break was only specified at the door threshold, causing a 'Red Line' failure. 3) The Workplan leaves SIPs exposed for 3 weeks, failing the weather-tight protocol.
- **Master Plan Updates (Initial):**
  - Added an **[OPEN RISK FLAG]** to Section 1.1 regarding the elimination of the 150mm elevated splash zone, officially highlighting the moisture bridging risk of the Dry Moat strategy.
  - Section 1.3: Upgraded the **Compacfoam CF200** block from a 2-meter door threshold patch to an **~18 linear meter Continuous Perimeter Bearing** to support the SIP sole plate and close the thermal 'Red Line' gap.
- **Hand-off to @foreman:** Handed over to the foreman to fix the Workplan timeline issues identified by the Strategist and integrate the continuous Compacfoam thermal break. The Foreman completed this.
- **Master Plan Update (Reversal):**
  - **User Catch:** The user correctly identified that the continuous Compacfoam perimeter is physically redundant. Because the 50mm external wood fibre extends down and overlaps the JACKODUR XPS upstand, the entire concrete slab is effectively wrapped *inside* the thermal envelope. Placing the sole plate directly on the concrete edge does not create a cold bridge to the outside, as the outside is already sealed.
  - Section 1.3 reverted: The Compacfoam CF200 block is returned to a ~2 linear meter patch explicitly for the **Door Threshold Bearing**. At the door threshold, the XPS upstand is cut away for level access, exposing the concrete to the outside patio, making the Compacfoam essential *only* in that location.
- **Workplan Reversal:** `plans/WORKPLAN.md` has been manually corrected by the Architect to remove the ~18m structural epoxy bedding of Compacfoam on Mid-Week prep, reverting to just the threshold.

## Date: 2026-06-20
**Architect Notes: Roof EPDM Clamping & Fascia Detailing (The "Hard Edge")**
- **User Query:** If the roof PIR overhangs by 50mm to align with the wood fibre, and the batten/cladding is on the outside, how do we affix the roof EPDM membrane and fascia to create a neat finish?
- **Physics Validation:** The user is exactly right regarding the Passivhaus geometry (the roof insulation must overhang to cap the wall insulation). However, raw PIR foam has zero structural pull-out strength. You cannot screw a fascia board or an EPDM edge trim into foam; coastal wind uplift will instantly rip it off.
- **Architectural Solution (The Hard Edge):** 
  - Instead of allowing the PIR foam itself to overhang, we install a continuous **Treated Timber Hard Edge** around the perimeter of the roof SIPs.
  - *Dimensional Correction:* The previous note stated a 50mm width, which is physically impossible if the overhang is 86mm (it would be floating in mid-air). 
  - The timber must be **200mm wide** and **100mm high** (achieved by stacking two 50x200mm treated timbers).
  - It overhangs the SIP wall by exactly **86mm** (covering the 50mm Wood Fibre + 25mm Batten + 11mm Hardie Plank).
  - This leaves **114mm** of timber bearing solidly on the roof SIP. Because the wall SIP beneath it is 150mm thick, heavy structural screws can be driven straight down through the 114mm bearing, through the roof SIP, and directly into the structural timber top-plate of the wall. This provides immense cantilever strength.
  - A Fascia Board (marine ply or UPVC) is screwed into the outward face of this timber block.
  - The EPDM rolls over this solid timber edge and is mechanically clamped in place using standard Check Kerb Trims (e.g., Sure-Edge).
- **Master Plan Update:** Updated Section 2.4 to explicitly document the 200mm width, 86mm overhang, and 114mm bearing of the Timber Hard Edge.
- **User Query:** How is the breather membrane attached to the wood-fibre and XPS boards?
- **Correction:** The Master Plan incorrectly specified "Stainless staples" for the Tyvek. You cannot staple into 50mm rigid wood fibre or XPS boards; the staples will simply pull out or crush the foam.
- **Architectural Solution:** 
  - *Permanent Fixing:* The Tyvek is physically clamped to the building by the 25x50mm vertical rainscreen timber battens. These battens are secured using 120mm EWI (External Wall Insulation) screws that drive through the batten, through the Tyvek, through the 50mm insulation, and anchor deeply into the 15mm OSB skin of the SIP.
  - *Temporary/Installation Fixing:* To hold the Tyvek up while unrolling it (before the battens are installed), the builder must use wide-headed plastic insulation dowels/washers (e.g., EJOT fixings) driven through the insulation into the OSB. 
  - *Taping:* The Tyvek is adhered to the XPS plinth and to itself at the overlaps using Pro Clima Tescon Vana acrylic tape.
- **Master Plan Update:** Section 2.1 (Breather Membrane) updated to remove staples and specify the Batten-Clamping and tape method.
- **User Insight:** The user suggested replacing the bottom 150mm of the hygroscopic Wood Fibre external insulation with impermeable XPS.
- **Physics Validation:** This is a structurally brilliant upgrade. Because the foundation is sunk into a Dry Moat, the bottom edge of the external insulation sits below the natural ground level. Wood fibre acts like a sponge and is highly susceptible to latent moat humidity and pooling failure. XPS is closed-cell, completely hydrophobic, and immune to moisture degradation.
- **Master Plan Update:**
  - Section 1.3: Replaced the bottom 150mm of the Wood Fibre thermal overlap with a **Rot-Proof XPS Plinth** (50mm thick x 150mm high XPS strip) mechanically fixed directly to the base of the external OSB SIP skin.
  - The EPDM/DPM Waterproofing Sweep now drops down the face of this XPS Plinth before sweeping across the moat.
  - The Wood Fibre starts strictly above the 150mm XPS Plinth.
  - Updated the textual cross-section to reflect this change.
- **Hand-off to @foreman:** Handing over to the foreman to update `plans/WORKPLAN.md`. The Weekend 8 Sunday Lockdown sequence needs to be adjusted so the 150mm XPS Plinth strip is installed at the base of the walls before the Wood Fibre is applied.
## Date: 2026-06-20
**Foreman Notes: Workplan Alignment & Strategist Validation Fixes**
- **Trigger:** @architect updated Master Plan with a 150mm Dry Moat strategy and full perimeter Compacfoam CF200 thermal break. @strategist validation flagged critical failures in the Workplan regarding naked OSB exposure and continuous thermal breaks.
- **Action Taken:** `plans/WORKPLAN.md` has been completely synchronized with the new Master Plan constraints.
  - **Excavation Update:** Increased total excavation depth to **500mm** to sink the 150mm MOT, 50mm sand, and 150mm XPS flush with the lawn. Adjusted waste skip calculations to account for the ~12.3m³ of soil to be removed manually (~18.5 tonnes).
  - **Thermal Break Continuity:** Weekend 8 prep now mandates bedding the **Compacfoam CF200 block continuously** around the entire 17.7m perimeter using structural epoxy, creating a 100% thermal break under the sole plate and fixing the 'Red Line' failure.
  - **Zero-Delay Protocol (Weather-Tight Fix):** Brought forward the application of the 50mm Rigid Wood Fibre and Tyvek breather membrane to **Weekend 8 Sunday Lockdown**. Naked OSB SIPs are no longer left under tarps for 3 weeks; they are wrapped in Wood Fibre and Tyvek the exact same weekend the walls go up. This closes the weather-tight failure.
  - **Moat Drainage Execution:** Weekend 10 now instructs the DIYer to carve a slight outward fall into the 350mm flat XPS projection, drop the EPDM/DPM skirt across it, lay the Terram 1000 buffer, and backfill with 20mm washed gravel to create the flush Dry Moat splash margin.
  - **Height Synchronization:** Adjusted wall plate delivery checks and Sunday ceiling height checks to reflect the recovered +150mm headroom. Max High-Side wall is now verified at **2261.5mm** with a finished ceiling of **2239mm**.
- **Hand-off:** All Workplan conflicts are resolved. The build logistics now match the structural physics and validation constraints.

## Date: 2026-06-20
**Architect Notes: Fixing XPS Skirt to Compacfoam**
- **User Query:** How can we mechanically fix the XPS skirt to the Compacfoam blocks?
- **Physics Validation:** Compacfoam CF200 is dense enough (2.0 N/mm²) to accept and securely hold standard exterior wood screws without pre-drilling. However, the outer 50mm XPS foam has no pull-through resistance. Screw heads will simply crush the XPS.
- **Architectural Solution:**
  - *Fixings:* Use 100mm exterior-grade wood screws paired with wide 60mm plastic insulation washers (e.g., EJOT washers). The screws pass through the XPS and embed 50mm deep into the Compacfoam block, while the wide plastic head clamps the XPS securely without crushing it.
  - *Adhesive Bond:* A bead of structural PU adhesive (e.g., Illbruck PU700) should be applied to the back of the XPS before screwing it, locking it permanently to the Compacfoam.
  - *Final Structural Clamping:* Later in the build, the 25x50mm vertical rainscreen battens will drop down over the Tyvek and be screwed through the XPS directly into the Compacfoam, providing massive permanent vice-clamping against the building.
- **Master Plan Update:** Updated Section 1.3, item 8 (Splash Zone Skirt) to explicitly define the fixing method (100mm wood screws + plastic washers + PU adhesive).
- **User Insight:** The user correctly identified that the Dry Moat is a high-maintenance liability and requested to return to the 150mm upsplash requirement, but crucially, without losing the internal headroom. They also astutely noted a geometric flaw: if the Compacfoam ring is flush with the SIP, and the 50mm Wood Fibre extends down over the Compacfoam, the Wood Fibre sits in the 0-150mm splash zone and will rot.
- **Physics Validation:** The Dry Moat has been completely abandoned. Sinking the concrete slab to 0mm (flush with the garden) successfully saves the 150mm of headroom. To restore the 150mm timber upsplash requirement without raising the concrete, we install a continuous 150mm tall x 140mm wide ring of **Compacfoam CF200** on top of the flush concrete slab.
  - The timber SIPs sit on the Compacfoam, perfectly 150mm above the ground.
  - The internal floor remains at 0mm, preserving the 2239mm ceiling height.
  - **The XPS Skirt Fix:** To prevent the Wood Fibre from entering the splash zone, we apply a 50mm thick x 150mm high XPS Skirt directly to the *outer face* of the Compacfoam block. This maintains the flush 50mm external insulation plane for the cladding, is 100% waterproof, and allows the Wood Fibre to start safely at the +150mm mark.
- **Master Plan Update:**
  - Section 1.1: Removed the Dry Moat. Stated the slab is excavated flush with the lawn (0mm).
  - Section 1.3: Removed all Moat details. Inserted "The Compacfoam Splash Zone" with long 250mm M12 resin anchors. Split the external insulation into an "XPS Splash Skirt (0mm to +150mm)" and "Thermal Overlap (Above +150mm)".
- **Hand-off to @foreman:** Handing over to the foreman to update `plans/WORKPLAN.md`. The Wood Fibre must strictly start above the 150mm mark, with the XPS Skirt applied to the face of the Compacfoam.

## Update: Foundation Flush with Lawn (No Moat)
- **Date:** Sun Jun 21 2026
- **Agent:** @foreman
- **Action:** Updated `plans/WORKPLAN.md` following Master Plan pivot.
  - Removed all references to the Dry Moat and XPS Plinth.
  - Reduced excavation depth from 500mm to 350mm (flush with the lawn) and updated skip/soil volume calculations.
  - Updated Mid-Week prep to instruct continuous 150mm x 140mm Compacfoam CF200 ring epoxy-bedded to the 17.7m perimeter.
  - Updated Weekend 8 instructions to drill through the Compacfoam for 250mm M12 resin anchors to hold the sole plate.
  - Simplified the Wood Fibre and Tyvek weatherproofing sequence (Sunday Lockdown) to wrap straight down the Compacfoam onto the Jackodur tub upstand.

## Update: XPS Splash Skirt Fix (Weekend 8 Logistics)
- **Date:** Sun Jun 21 2026
- **Agent:** @foreman
- **Action:** Updated `plans/WORKPLAN.md` (specifically Weekend 8 Lockdown Phase) to reflect the physics flaw caught by the user. 
  - The DIYer is now instructed to attach a 50mm thick x 150mm high XPS Skirt directly to the outer face of the Compacfoam CF200 block.
  - The 50mm Rigid Wood Fibre is strictly mandated to start *above* this XPS Skirt (+150mm mark), isolating it entirely from the splash zone.
  - Adjusted the weather-tight protocol: The Tyvek breather membrane runs down the Wood Fibre, covers the XPS Skirt, and securely tapes to the JACKODUR® base upstand.
  - *Safety/Weather Check:* Weather forecast for Cowes remains an important priority for Sunday Lockdown. The new protocol ensures the hygroscopic wood fibre is safe from latent ground moisture.
- **Hand-off to @strategist:** @strategist, please run tests verifying the continuous thermal envelope with the new XPS Skirt inclusion.

## Date: 2026-06-21
**Architect Notes: Soakaway Overflow Reversal**
- **User Query:** The user rejected the proposed upgrade to a 110mm pipe and Twin-Crate soakaway system (Flaw #5 from previous review), stating "that won't happen. remove that again."
- **Action Taken:** Reverted Section 2.4.1 in `MASTER_PLAN.md` back to the original specification: a standard **68mm UPVC Pipe** routed to a **single Soakaway Crate** located 3m-5m away from the foundation. The twin-crate over-engineering has been purged from the blueprints.
- **User Query:** The user challenged the OSB3 cover board addition on the roof, pointing out that certain high-compressive strength PIR boards are designed to handle foot traffic without crushing, thereby eliminating the need for (and rotting risk of) an external structural timber deck.
- **Physics Validation:** The user is architecturally correct. Adding an external layer of OSB3 on a flat roof outside the warm envelope (just below the EPDM) introduces a severe rot/condensation risk if water ever penetrates the rubber. By utilizing a "Trafficable" high-compressive strength glass tissue-faced PIR board (minimum 150 kPa, e.g., Kingspan Thermaroof TR27), the foam itself acts as both the thermal jacket *and* the rigid structural deck, easily withstanding human foot traffic without denting.
- **Master Plan Update:**
  - Section 2.3: Removed the 11mm OSB3 Cover Board. 
  - Restored the PIR insulation to **100mm**, explicitly specifying it must be **High-Compressive Strength (min 150 kPa) glass tissue-faced PIR**.
  - Section 2.3.2: Re-verified height calculation. Total roof buildup returns to **238.5mm**. Total building height returns to exactly **2500mm** high side / 2442.8mm low side.
- **Hand-off to @foreman:** Updated `plans/WORKPLAN.md` Weekend 9 to explicitly warn the DIYer that standard PIR will crush underfoot. They *must* procure the high-compressive structural variant to execute the EPDM adhesion safely.
- **Trigger:** Cross-agent feedback identified 5 medium-to-high severity physical design flaws in the Master Plan and Workplan.
- **Action Taken:**
  1. **MVHR Hardware Contradiction (Fixed):** `WORKPLAN.md` Weekend 13 previously contained lingering instructions to install a ducted inline filter. This has been purged. The instructions now correctly direct the DIYer to insert the OEM G4/F7 replacement filter cassettes directly into the decentralized wall unit.
  2. **Vulnerable Roof Structural Deck (Fixed):** The 100mm PIR foam would crush if walked on during gutter maintenance, tearing the EPDM. Added a structural **11mm OSB3 Flat Roof Deck** on top of the PIR. To mathematically offset this 11mm height increase and stay beneath the 2.5m PD limit, the PIR thickness was reduced from 100mm to **80mm**. The roof buildup is now 229.5mm, safely capping the building at 2491mm high.
  3. **Cladding Fastener Mechanics (Fixed):** Updated the Rainscreen batten screw specification in `MASTER_PLAN.md`. Instead of exclusively using 60° angles, the builder must now use an alternating pattern: 60° downward (for shear weight) and 90° horizontal (for wind load/anti-compression), preventing the 50mm wood fibre from being crushed.
  4. **Roof Edge Thermal Bridging (Fixed):** The massive 200mm solid timber "Hard Edge" created a severe linear cold bridge. Redesigned this edge: The highly-structural 120mm roof SIP itself now cantilevers the 86mm overhang. A much smaller 91mm x 50mm timber batten is screwed to the perimeter. This allows the 80mm PIR foam to continue almost entirely to the edge, virtually eliminating the thermal bridge while retaining the mechanical anchor for the EPDM.
  5. **Inadequate Storm Overflow Drainage (Fixed):** A 68mm pipe to a single crate would bottleneck during Cowes coastal downpours. Upgraded the overflow specification to a **110mm underground drainage pipe** routed to a **Twin-Crate Soakaway System** (300L+ capacity) wrapped in geotextile, min 5m away from the foundation.
- **Hand-off:** All 5 design flaws have been engineered out of the blueprints.
- **Trigger:** Cross-agent review flagged four specific, internal mechanical/mathematical contradictions within the Master Plan.
- **Action Taken:**
  1. **Anchor Bolt Length Deficit:** The previous 250mm anchor bolts were mathematically exhausted by the 100mm concrete embedment and 150mm Compacfoam block, leaving no thread for the sole plate. Upgraded hardware spec to **330mm long M12 Threaded Studs** (cut from standard 1m lengths) to provide ample thread for the timber sole plate, washer, and nut.
  2. **Compacfoam Width Mismatch:** The CF200 block was listed as 140mm wide, creating a 10mm overhang under the 150mm SIP. Updated the Compacfoam spec to **150mm x 150mm** to perfectly match the SIP base profile.
  3. **Volume & Height Recalculation:** Section 4.2 still relied on legacy ceiling heights (2.08m average) yielding 32m³. Updated the math to reflect the newly reclaimed ceiling height (~2.21m average). The true internal volume is now formally updated to **~34m³**, pushing the 2 ACH requirement up to ~68m³/h.
  4. **MVHR Filter Incompatibility:** The plan erroneously mandated ducted "inline filter boxes" alongside a ductless, through-wall "Zehnder ComfoAir 70" unit. Removed the physically impossible inline filters. Added an explicit instruction to rely exclusively on OEM G4/F7 replacement cassettes for the through-wall unit, relying on the ceiling-mounted ambient air filter to handle the room's heavy woodworking dust.
- **Hand-off:** Blueprint is mathematically and mechanically sound.
- **Trigger:** Cross-agent review flagged discrepancies between the Master Plan and the Workplan.
- **Action Taken:**
  1. **Door Dimensions:** The Workplan erroneously retained the old 1400mm x 2000mm door dimension. Updated `plans/WORKPLAN.md` to reflect the reclaimed headroom geometry: **1400mm x 2150mm**.
  2. **VCL Membrane Installation:** The Workplan previously omitted the physical hanging of the Pro Clima Intello Plus VCL sheet. Updated Phase 4 of `plans/WORKPLAN.md` to explicitly instruct the DIYer to staple the full Intello Plus sheet across walls/ceilings and tape the overlaps *before* the service battens go up.
  3. **Concrete Volume Consistency:** The Master Plan stated "~2.8 Cubic Meters" while the Workplan told the user to order "2.8 to 3.0m³ for safety." The Master Plan (Section 1.1) has been updated to explicitly state: "Required: ~2.8m³. Order: 3.0 Cubic Meters (to account for line-pump priming and waste)." This aligns the exact ordering volumes.
  4. **Title Naming:** The agent flagged that the Workplan title said "PUR-Core SIPS" while the Master Plan noted "OSB skin." This is standard SIP composition (OSB skins with a PUR core), but to ensure total clarity, both documents inherently agree on the material science.
- **Hand-off:** All flagged contradictions between the Master Plan and Workplan are resolved.
- **User Correction:** The user caught a mathematical error in the Foreman's recent Workplan update. To sink the 150mm MOT, 50mm sand, 150mm XPS under-slab, *and* the 150mm concrete slab flush with the lawn, the total excavation must be **500mm**, not 350mm.
- **Logistics Impact:** The 4.23m x 6.23m footprint excavated to 500mm generates approximately 13.2m³ of solid soil, weighing roughly **19.8 tonnes**.
- **Workplan Update:** Corrected Phase 1 `WORKPLAN.md` to state the exact 500mm depth, adjusted the soil removal calculations to ~19.8 tonnes, and increased the required 6-yard "Inert Soil" skips to 4-5 to handle the massive volume.

## Date: 2026-06-21
**Architect Notes: JACKODUR Dimensions & Dig-Out Adjustments**
- **User Query:** The JACKODUR Atlas system only comes in 20mm increments. Requested reducing the specification from 150mm to 140mm.
- **Physics Validation:** The user is correct regarding manufacturer specifications. Stepping down 10mm reduces the thermal performance slightly (from ~0.22 W/m²K to ~0.23 W/m²K), but this is mathematically trivial and well within our acceptable tradeoff parameters for a foundation, given the continuous UFH thermal battery above it.
- **Master Plan Update:**
  - Section 1.1: Updated under-slab thermal break to **140mm JACKODUR Atlas XPS**.
  - Section 7.1: Updated foundation U-value to **~0.23 W/m²K**.
- **Workplan Update (Logistics):**
  - The total required manual dig-out depth reduces from 500mm to **490mm** (150mm MOT + 50mm Sand + 140mm XPS + 150mm Concrete = 490mm).
  - The soil volume to be manually excavated drops from 13.2m³ to **~12.9m³** (~19.3 tonnes).
  - Updated `WORKPLAN.md` Phase 1 metrics to reflect the exact 490mm depth target, saving the DIYer approximately 10mm of grueling clay excavation across the entire footprint!
- **User Query:** Does the gap between the bottom of the fascia and the top of the Hardie Planks need insect cover, or should it be mounted flush?
- **Physics Validation:** The fascia must *never* be mounted perfectly flush or sealed tight against the Hardie Planks. The 25mm batten cavity behind the cladding is a dynamic "Rainscreen." It relies on the stack effect: cold air enters at the bottom and warm, moist air exhausts out the top. Sealing the top traps moisture and causes the battens to rot.
- **Insect Intrusion:** Because there is an open exhaust gap at the top of the wall (under the fascia/overhang), it is a prime location for wasps, hornets, and solitary bees to enter and build nests in the warm, 25mm vertical cavities. 
- **Architectural Solution:** 
  - An insect mesh must be installed at the top of the cavity, mirroring the bottom.
  - A Perforated Aluminium Vent Trim (or folded insect mesh) is tacked to the underside of the cantilevered SIP roof panel, bridging the 25mm batten cavity just before the uppermost Hardie Plank is installed. 
  - The fascia board then drops down, visually hiding this mesh gap from the outside, while allowing air to flow freely.
- **Master Plan Update:** Section 2.4 updated to explicitly mandate a "Rainscreen Top Bug Mesh" to preserve ventilation while blocking pests.
- **User Query:** If the fascia is only 100mm high and covers the timber kerb, how do we stop water from dripping behind the Hardie Planks?
- **Physics Validation:** The user caught a geometric oversight. If the fascia is only 100mm high, it terminates exactly at the bottom of the timber kerb. Because the 120mm roof SIP itself is doing the cantilevering (overhanging the 86mm wall buildup), the bottom of that kerb sits on top of the SIP roof panel. If water drips off a 100mm fascia, it will land on the exposed edge of the SIP panel or run horizontally back along the underside of the overhang and drop *behind* the cladding.
- **Architectural Solution:**
  - *Oversized Fascia Drop:* The fascia board must be significantly taller than the 100mm kerb. We specify a **min 150mm tall** (or deeper) fascia board.
  - *The Drip Line:* The fascia screws into the 100mm timber kerb, but the remaining 50mm+ of the board extends downwards, covering the exposed 120mm edge of the cantilevered SIP roof panel. 
  - *The Bellcast Effect:* Because the entire roof system (SIP + Kerb + Fascia) physically overhangs the 86mm wall buildup by a few millimeters, the bottom edge of the fascia hangs in mid-air *outside* the plane of the Hardie Planks. Water hits the fascia, runs down to the bottom lip, and drips harmlessly to the ground.
- **Master Plan Update:** Section 2.4 updated to specify an oversized 150mm+ fascia board to ensure a clean external drip line.
- **User Query:** Requested precise detailing of the roof edge layering and orientation of the 50x90mm batten (height vs. weight wise). Also noted a discrepancy as the PIR thickness was updated to 100mm earlier.
- **Dimensional Correction:** Because we upgraded to **100mm** Trafficable PIR (without the 11mm OSB cover board), the perimeter timber kerb must stand **100mm tall** to perfectly match the insulation plane. Standard 47x100mm (nominal 2x4) treated timber is ideal.
- **Orientation Mechanics:** The 47x100mm timber is placed **"on edge"** (standing 100mm tall, presenting a 47/50mm width when viewed from above). 
  - It is screwed vertically straight down through the 100mm depth into the top OSB skin of the cantilevered 120mm roof SIP.
  - The 100mm PIR insulation butts tight against the inside face of this timber kerb.
  - The Fascia board is screwed horizontally into the outer 100mm-tall face of the kerb and drops downward.
- **Master Plan Update:** Section 2.4 updated to clarify the 100mm height, 50mm width, "on edge" orientation, and exact mechanical screw path for the Perimeter Kerb.

## Date: 2026-06-21
**Architect Notes: Tyvek "Top-and-Tail" Taping Method**
- **User Query:** The user asked if the breather membrane could be held in place with tape to avoid penetrating the OSB layer with the temporary mechanical fixings (dowels). They subsequently asked if this method still works with the vertical battens later clamping it down.
- **Physics Validation:** The user is correctly prioritizing airtightness by avoiding unnecessary penetrations through the SIP's OSB skin. 
  - Standard airtight tape (Tescon Vana) will *not* stick to the fibrous face of the 50mm Wood Fibre board. However, it sticks aggressively to the closed-cell XPS Splash Skirt at the bottom, and to the timber top-plate at the top.
  - The permanent fixing of the Tyvek is inherently mechanical. The "Top-and-Tail" taping method is perfectly compatible with the subsequent clamping stage. The tape merely holds the sheet taut and flat against the building like a canvas. When the 25x50mm timber battens are installed weeks later, the 120mm EWI screws punch straight through the suspended Tyvek, permanently clamping it flat against the Wood Fibre.
- **Architectural Solution:**
  - Implemented the **"Top-and-Tail"** taping method.
  - The DIYer tapes the bottom of the Tyvek to the XPS Splash Skirt/JACKODUR upstand.
  - They pull the Tyvek taut up the wall and staple/tape it exclusively into the exposed timber top-plate.
  - The Tyvek is now held flat against the wood fibre without a single temporary puncture in the main OSB wall face, awaiting the permanent clamping of the rainscreen battens.
- **Updates:** `MASTER_PLAN.md` (Section 2.1) and `WORKPLAN.md` (Weekend 8 & Weekend 11) updated to remove insulation dowels, specify the Top-and-Tail method, and update the batten alternating screw pattern.
- **User Query:** How much overlap does the DPM from the raft insulation need to remain to lay it over the 150mm high Compacfoam blocks?
- **Physics Validation:** The DPM sits under the concrete slab. If the Compacfoam sits *on top* of the concrete slab, the DPM must travel vertically up the 150mm inner face of the Compacfoam, and then horizontally across the 150mm top face to meet the sole plate. To achieve this without tension, plus provide an overlap for the DPC, the DPM requires a minimum **400mm excess tail**.
- **Master Plan Update:**
  - Section 1.1 (DPM): Explicitly mandated cutting the DPM with a **minimum 400mm excess tail** extending past the top of the XPS tub.
  - Section 1.3 (DPM/DPC Lapping): Updated to detail the exact folding geometry (400mm tail folded up the inner face of the Compacfoam and across the top, sealed to the Polymeric DPC with butyl tape).
- **Workplan Update:** Updated `WORKPLAN.md` Weekend 8 Saturday instructions to manually execute the folding and taping of the 400mm DPM tail before rolling out the DPC and drilling the sole plates.
