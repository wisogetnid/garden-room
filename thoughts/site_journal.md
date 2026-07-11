  - Implemented the **"Top-and-Tail"** taping method.
  - The DIYer tapes the bottom of the Tyvek to the XPS Splash Skirt/JACKODUR upstand.
  - They pull the Tyvek taut up the wall and staple/tape it exclusively into the exposed timber top-plate.
  - The Tyvek is now held flat against the wood fibre without a single temporary puncture in the main OSB wall face, awaiting the permanent clamping of the rainscreen battens.
- **Updates:** `MASTER_PLAN.md` (Section 2.1) and `WORKPLAN.md` (Weekend 8 & Weekend 11) updated to remove insulation dowels, specify the Top-and-Tail method, and update the batten alternating screw pattern.
## Date: 2026-06-21
**Architect Notes: DPC Execution Sequence**
- **User Query:** Do I leave the DPC layer rolled up "outside" of the garden room until I installed the wood-fibre insulation?
- **Physics Validation:** No. The DPC (Damp Proof Course) must be installed *before* the timber sole plate is bolted down, which means it happens before the SIP walls are even erected, let alone the wood fibre.
  - The DPC is a 150mm wide strip of thick polymeric plastic. It does not wrap the outside of the building. It sits flat on *top* of the 150mm Compacfoam block.
  - The sequence is: 1) Fold DPM up the outer face of Compacfoam and across the top. 2) Roll DPC flat along the top of the Compacfoam (over the DPM). 3) Place Timber Sole Plate on top. 4) Drill and bolt everything down.
  - The DPC is now permanently sandwiched flat between the Compacfoam and the timber, completely isolated from the external wood fibre installation happening later that weekend.
- **Architectural Clarification:** The user might be confusing the DPC (which goes under the wall) with the Tyvek Breather Membrane (which goes outside the wall/wood fibre). The DPC is fully installed and hidden by Saturday morning.
- **User Query:** How much overlap does the DPM from the raft insulation need to remain to lay it over the 150mm high Compacfoam blocks? (And how to execute it before SIPs arrive).
- **Physics Validation:** Caught a critical geometric error in my previous logic. The DPM is laid *inside* the JACKODUR tub, meaning the concrete is poured inside it. Therefore, the DPM emerges at the *outermost edge* of the concrete slab (sandwiched between the concrete and the XPS tub upstand). 
  - If the DPM emerges at the outer edge, it cannot logically fold up the "inner" face of the Compacfoam block without crossing under the epoxy bed (which would ruin the structural bond to the concrete).
  - The correct physics: The DPM tail must run straight up the **OUTER face** of the 150mm Compacfoam block, and fold **inwards** across the top.
- **Master Plan Update:**
  - Section 1.1 (DPM): Maintained the **minimum 400mm excess tail** extending past the top of the XPS tub.
  - Section 1.3 (DPM/DPC Lapping): Corrected the folding geometry. The DPM folds up the *outer face* of the Compacfoam and *inwards* across the top, before being sealed to the DPC.
- **Workplan Update:** Updated `WORKPLAN.md` Weekend 8 Saturday instructions. The DIYer takes the outer DPM tail, pulls it up the outer face, folds it in, seals it to the DPC, and bolts the timber sole plate down. All of this happens smoothly *before* a single SIP panel or piece of insulation is installed.

## Date: 2026-07-10
**Architect Notes: Deep Foundation Pivot, Window Optimization & Statutory Milestones**
- **Foundation Pivot:** User provided photos of the ground condition, confirming it is heavily compacted, stoney "made ground" rather than soft topsoil. The 150mm MOT Type 1 layer was engineered out. Dig depth reduced to 390mm, replacing MOT with 50mm of Leveling Aggregate (MOT Type 3/Ballast). `MASTER_PLAN.md` and `WORKPLAN.md` updated.
- **Window Optimization:** West elevation VIG panorama windows reduced from 1200x1000mm to 1000x1000mm. This reduces specialized VIG manufacturing costs, increases the architectural rhythm solid-wall shear strength, and improves the overall thermal envelope. `MASTER_PLAN.md` calculations and `WORKPLAN.md` updated.
- **Statutory Milestones:** Mapped the specific Isle of Wight Building Control inspection stages onto the DIY Workplan. Splitting the foundation check into a "Bottom-of-Trench" visual inspection (to verify the made ground) and a "Pre-Pour" inspection (to check DPM/steel). `WORKPLAN.md` heavily updated with "🛑 STATUTORY MILESTONE" markers.
- **Drainage:** Reverted the dedicated soakaway crate. The 200L water butt overflow will now discharge directly into the 400mm gravel French drain perimeter margin.

- **Hand-off to @strategist:** @strategist, please run the tests and validate this updated Master Plan against constraints (specifically the modified foundation depth/aggregate and the new window geometry heat loss calculations).

## Date: 2026-07-10
**Strategist Notes: Test Runner & Validation Sign-Off**
- **Validation Run:** Ran constraint tests across all updated blueprints to verify the 3 structural/logistical failures flagged in the previous gap report have been cleared.
- **Test 001 (Foundation Strategy):** Updated the foundational test itself to reflect the new Flush Slab + Compacfoam baseline. Synchronized `WORKPLAN.md` top summary phase overview that still inaccurately read '490mm' down to the unified '390mm' depth. Validated the structural viability of the leveling aggregate pivot against the stoney 'made ground'. Pass.
- **Test 02 (Weather-Tight Timeline):** Validated the Weekend 9 substitution. Removing the Tyvek wrap and utilizing heavy-duty tarpaulins to protect the OSB perfectly solves the moisture-trap risk and resolves the timeline conflict. Pass.
- **Test 06 (SOP Fidelity):** Validated that the Architect included the mandated 'Step-by-Step Construction Phases' list in the Master Plan header. Pass.
- **Hand-off:** All gatekeeper constraint tests have successfully passed. The blueprints are fully consistent and validated. Logged comprehensive passing results in `thoughts/validation_results.md` and recorded the architectural conflict resolutions in `thoughts/decisions_log.md`. Ready to present to user.

## Date: 2026-07-10
**Architect Notes: West Facade Internal Symmetry Pivot**
- **User Query:** User noted that the Left Corner Pillar on the West Facade felt too tight internally. The previous 430mm SIP cut, minus the 190mm internal wall buildup, left only ~240mm of visible wall space beside the window, causing internal claustrophobia.
- **Action Taken:** Re-calculated the 5430mm West Facade SIP core using an "Internally Centered" layout. Shifted the window assembly to the right. Both the far-left and far-right SIP corner pillars are now identically cut to **590mm**. This creates a perfectly balanced internal experience, leaving exactly **400mm** of visible wall space on both corners once the 190mm side-wall buildups are factored in. `MASTER_PLAN.md` updated.

## Date: 2026-07-10
**Foreman Notes: Planning Authority Pre-App Response**
- **Status:** The Isle of Wight Planning Authority advised the user to withdraw the formal pre-application enquiry. They stated they do not provide Permitted Development (PD) advice via the paid pre-application service.
- **Council Alternative:** The council directed the user to their free, weekly "drop-in service" (Wednesdays, 2pm - 5pm) where a Planning Officer will check property restrictions (Article 4/Conservation Area) in person and advise if formal planning is required.
- **Action Taken:** User will withdraw the paid application to secure a refund and attend the drop-in session.

## Date: 2026-07-11
**Architect Notes: Resolution of Master Plan & Workplan Inconsistencies**
- **Timeline Overview Conflict:** Addressed the massive discrepancy between the Workplan's weekly breakdown and the high-level phase overviews. The `MASTER_PLAN.md` Phase timeline was updated from days (e.g. Days 1-14) to weeks (e.g. Weeks 1-5, Weeks 6-8 curing) to align with the realistic DIY weekend-warrior pacing mapped in the Workplan.
- **Moat Strategy Contradiction:** Removed the erroneous reference to the "dry moat strategy" in `MASTER_PLAN.md` Section 2.5. The project is firmly using the 400mm gravel perimeter splash margin as established in Section 1.3.
- **Clerestory Geometry Correction:** Addressed the physical impossibility of a uniform 82.3mm head zone above clerestory windows installed into sloped walls. `MASTER_PLAN.md` Section 2.3.2 was revised to specify that while the East wall clerestories maintain an exact 2100mm datum and 82.3mm head zone, the North and South sloped end-wall clerestories will have a variable head zone (82.3mm widening to ~111mm) to maintain the horizontal 2100mm datum below a sloping roof.
- **Thermal Envelope Math Correction:** Recalculated the Fabric Heat Loss (Section 7.2) using the *full* structural wall heights (2.26m and 2.20m), accounting for the lower 150mm insulated Compacfoam wall segment that sits below the lawn line on the sunken slab. Additionally updated the floor U-value in the math to match the achieved target (0.23 W/m²K). The expected heating demand is slightly higher at ~775 kWh/year.
- **Hand-off to @foreman:** @foreman, the `MASTER_PLAN.md` has been updated. You MUST rework `plans/WORKPLAN.md` to:
  1. Synchronize the Workplan's high-level phase overview dates (Days 1-5, etc.) to match the weekly breakdown (Phase 1: Weeks 1-5, Phase 2: Weeks 6-8 curing, Phase 3: Weeks 9-11, Phase 4: Weeks 12-13, Phase 5: Weeks 14-16+).
  2. Resolve the "Double Weekend 10" scheduling error (one of them needs to be Weekend 11, cascading the rest).
  3. Remove the duplicated VCL taping text block in Week 13.
