# The Boundary Fire Safety & ATEX Test
**Type:** Compliance & Workshop Physics
**Target Agent:** `@architect`

## Objective
Verify that the `MASTER_PLAN_[System].md` successfully navigates the strict 2024-2026 Approved Document B UK Building Regulations (Fire Safety), specifically for structures built <1m from a residential boundary, and handles the dangerous physics of high-velocity wood dust (ATEX explosion risk).

## Verification Checklist

### 1. The <1m Boundary Rule (Approved Document B)
- [ ] If specifying an OSB-faced SIP structure: Does the internal envelope explicitly include a non-combustible Type F equivalent fire-boarding (e.g., 15mm Fermacell) to achieve the mandatory REI30/REI60 fire resistance?
- [ ] If specifying a Magnesium Oxide (MgO) SIP structure: Is there explicit confirmation that the A1 non-combustible panels natively satisfy the boundary regulation?
- [ ] Is the external cladding specified as an A2 non-combustible material (e.g., James Hardie Fibre Cement Plank)?

### 2. ATEX Dust Extraction Physics
- [ ] Are the primary extraction trunks specified as Rigid Galvanized Steel Ducting (smooth bore) rather than PVC, to prevent dangerous static electricity buildup from high-velocity wood dust?
- [ ] Is there an explicit instruction for the Electrician to install and sign-off on a **Copper Earth Bonding Strap** directly bolted to the galvanized ducting to safely ground the massive static charge?
- [ ] Are the electrical machine breakers specifically mapped as **20A Type C RCBOs** to handle the massive 100A+ inrush surge of 3HP induction motors without nuisance tripping?

## Failure States (Do Not Pass If:)
- A garden room built <1m from the boundary utilizes standard combustible OSB interior panels and timber cladding.
- The workshop extraction system specifies 100mm PVC piping without an internal bare copper wire grounded to earth.
- The consumer unit specifies standard Type B breakers for heavy 3HP table saws.
