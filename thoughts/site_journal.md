
## Date: 2026-04-28
**Architect Notes: West Façade 5.6m Layout Generation (Large Windows)**
- **User Constraint:** Rejects "Gallery Sweep" (too dark for future office) and "Vertical Rhythm" (workbench blocking floor-to-ceiling glass). Desires configurations using large square/landscape windows (800x1200mm or 1200x1200mm) that balance light and workshop utility.
- **Canvas Analysis:**
  - Wall Length: 5.43m (internal core).
  - Door: ~1.5m.
  - Remaining Solid Wall: ~3.93m.
  - Windows: 2x large units (1.2m wide each = 2.4m of glass).
  - Remaining SIP column space: ~1.5m to distribute for structural stability.
- **Layout Concept 1: The "Zoned Pavilion" (Asymmetric)**
  - *Layout:* Door offset to the far Left (or Right). The two 1200x1200mm windows are grouped together on the remaining wall, separated by a structural SIP mullion (e.g., 400mm). 
  - *Aesthetic:* Very modern. Creates a distinct "Entrance Zone" and a "Light Zone".
  - *Utility:* Perfect for a workbench. A 1200x1200mm window typically sits at ~900mm off the floor (standard desk/workbench height is 900mm). The workbench can sit flush against the wall *under* the windows, providing a 2.4m+ wide panorama of the garden while working, without blocking the glass.
- **Layout Concept 2: The "Bookend" (Symmetric Glass, Asymmetric Door)**
  - *Layout:* A 1200x1200mm window on the far Left corner, and a 1200x1200mm window on the far Right corner. The 1.5m Door sits between them, but *off-center* (e.g., closer to the left window).
  - *Aesthetic:* Quirky but balanced.
  - *Utility:* Provides distinct workstations. One window for a desk, one window for a machine.
- **Layout Concept 3: The "Grand Wrap" (Corner Bias)**
  - *Layout:* Door pushed to the right. The two 1200x1200mm windows are joined together with almost zero mullion (a direct couple) on the far left corner, acting as one massive 2.4m x 1.2m picture window.
  - *Aesthetic:* Highly architectural, mid-century modern vibe. 
  - *Utility:* Creates a dedicated "viewing gallery" half of the room, leaving the door half completely solid for heavy, messy machinery.
- **Recommendation:** The "Zoned Pavilion" using 1200x1200mm windows is the absolute best solution. It allows a workbench to sit exactly at sill height, providing massive light for a future home office while keeping the door out of the way.

## Date: 2026-04-28
**Architect Notes: West Façade Finalization (Workbench Panorama)**
- **User Decision:** The user selected Option 1: The "Workbench Panorama" (Asymmetric Zoning).
- **Execution:** 
  - Updated the Glazing Schedule in `MASTER_PLAN.md` to specify 2x 1200x1200mm Fixed VIG uPVC windows on the West Elevation.
  - Injected a strict layout logic clause: The 1.5m door is offset to the corner. The two windows are grouped on the remaining wall space, separated by a structural ~400mm SIP mullion.
  - *Sill Height Optimization:* Locked the window placement to align with the door header (2100mm). This explicitly places the window sill at **900mm** off the FFL (Finished Floor Level), perfectly accommodating a standard workbench or office desk underneath without blocking the light.
  - Re-ran validation tests: The 400mm SIP mullion provides the necessary structural shear and load-bearing strength to support the roof without requiring a complex, thermal-bridging steel lintel over the glass.
- **Status:** Blueprints are 100% updated and verified.

## Date: 2026-04-28
**Architect & Foreman Notes: Blueprint Role Separation (Roofing Logistics)**
- **User Request:** The user requested reformatting the Roof Section (2.3) in the Master Plan to match the tabular "Sandwich (Exterior to Interior)" layout of the Wall Section (2.1), and moving all "Lifting Logistics" over to the Workplan.
- **Execution (Master Plan):**
  - Renamed Section 2.3 to `The Roof 'Sandwich' (Exterior to Interior)`.
  - Replaced the narrative breakdown of the 192mm thickness and the malformed table with a clean 5-point Markdown table matching the Wall specification (Waterproofing Deck, Roof Structure, Wall Top Plate, VCL, Internal Ceiling).
  - Deleted the "Lifting Logistics" text from the Master Plan. (The 192mm thickness calculation remains safely documented in Section 2.3.2 below the table).
- **Execution (Workplan):**
  - Updated `Weekend 9: The Roof Lift` in `WORKPLAN.md`.
  - Injected the explicit "CRITICAL LIFTING LOGISTICS" mandate (requiring 600mm panels or a Genie lift to prevent safety failures) directly into the Saturday execution instructions.
- **Result:** The `MASTER_PLAN.md` is now purely the "What" (Material Sandwich), and the `WORKPLAN.md` is the "How" (Execution and Lifting Safety).

## Date: 2026-04-28
**Architect & Foreman Notes: Blueprint Purity (What vs. How vs. Why)**
- **User Request:** Strip "How-to" instructions from the Master Plan and move them to the Workplan. Move architectural/regulatory justifications ("Why") into the Master Plan to defend the "What".
- **Master Plan Updates (The "What" & "Why"):**
  - Scrubbed execution tooling (e.g., "min 6 passes", "Low torque drill, NO impact drivers") from the Fixing Method columns, replacing them with passive structural states (e.g., "Mechanically compacted").
  - Extracted the "3 Critical Failure Points" warning block out of the foundation chapter.
  - Bolstered the "Why" logic in the materials table: Explicitly added the Approved Document B (REI30/REI60) justification directly into the 15mm Fermacell 'Purpose' column, defending why it is specified over standard plasterboard.
- **Workplan Updates (The "How"):**
  - Scrubbed all thermodynamic and architectural theory from the execution weekends (e.g., removed the U-Value trade-off explanation from Weekend 1, removed the Part B Fire Regs lecture from Weekend 14). The instructions are now purely military-style checklists.
  - Injected the explicit tooling requirements (e.g., "minimum 6 overlapping passes") into the corresponding execution days.
  - Injected the "Critical Failure Points" as direct *Foreman Warnings* on the specific execution days (e.g., warning about DPM corner tearing on Weekend 3, hydrostatic blowout on Weekend 4, and Tyvek tape failure on Weekend 8).
- **Result:** The `MASTER_PLAN.md` is a pure engineering/architectural specification (Defending the What with the Why). The `WORKPLAN.md` is a pure chronological execution sequence (The How).
