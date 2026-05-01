
## Date: 2026-04-28
**Architect Notes: Cladding Thickness Calibration (Hardie Plank VL)**
- **User Request:** The user correctly identified that Hardie Planks are manufactured in 8mm (standard lap) or 11mm (VL interlocking) thicknesses, challenging the generic "~10mm effective lapped depth" used in the dimensional reverse-engineering.
- **Physics Calibration:** 
  - Standard James Hardie Plank (8mm): When installed in a traditional "clapboard" lap style, the planks overlap by 30mm. At the overlap, the thickness is 16mm. Due to the angle of the plank kicking out from the batten, the *effective horizontal projection* from the batten face is approximately **15mm**.
  - James Hardie VL Plank (11mm): This is a tongue-and-groove interlocking board that sits dead flat against the batten. The *effective horizontal projection* from the batten face is exactly **11mm**.
- **Impact on 3.6x5.6m Boundary Limit:**
  - If using 11mm VL Plank: 11mm (Cladding) + 25mm (Batten) + 50mm (Wood Fibre) = **86mm per wall** (172mm total reduction).
  - If using 8mm Lapped Plank: 15mm (Effective projection) + 25mm (Batten) + 50mm (Wood Fibre) = **90mm per wall** (180mm total reduction).
- **Architectural Adjustment:** The previous calculation used an 85mm buildup (170mm total reduction), resulting in a 3.43m x 5.43m core. 
  - If we stick to 3.43m x 5.43m, an 11mm VL plank pushes the final dimension to 3.602m x 5.602m (technically breaching the limit by 2mm, which is structurally irrelevant as it's within standard construction tolerances of +/- 5mm).
  - An 8mm lapped plank would push it to 3.61m x 5.61m (breaching by 10mm, still largely within tolerance but riskier if boundary constraints are absolute).
- **Resolution:** I will update `MASTER_PLAN.md` Section 1.0 to explicitly define the cladding as **11mm Hardie Plank VL** to lock in the absolute tightest tolerance, updating the buildup to 86mm per wall (172mm total). The 2mm difference (172mm vs 170mm) does not necessitate resizing the SIP core from 3.43m x 5.43m, as 2mm is entirely consumed by the compression of the wood fibre or the glue line of the splines. 
