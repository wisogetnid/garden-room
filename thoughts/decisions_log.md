**Decision:** `plans/MASTER_PLAN.md` now specifies a sloped 150mm roof SIP set to 1:60, topped by 50mm flat tissue-faced PIR and fully adhered 1.5mm EPDM. `plans/WORKPLAN.md` now requires verification of the sloped top plates/bearing geometry on delivery and installation of flat PIR rather than tapered PIR.
**Result:** The upper SIP OSB skin is kept warmer and drier, reducing moisture risk. Roof U-value improves to approximately 0.12 W/m²K. The trade-off is reduced internal ceiling height; the 2100mm door/glazing datum now carries an open head-clearance risk requiring supplier verification before SIP fabrication.

## [Date: 2026-05-23] - Glazing and Door Datum Reduction after Roof Recalculation
**Context:** The sloped SIP plus 50mm PIR roof build-up leaves a high-side finished internal height of 2111mm and a low-side finished internal height of 2054mm. A 2100mm door/glazing datum is therefore structurally non-functional.
**Decision:** West façade is fixed as the high side. Door outer-frame height reduces to 2000mm maximum. West panorama windows reduce from 1200x1200mm to 1200x1000mm, with heads at 2000mm and sills at 1000mm. North/South/East clerestories remain 300x1500mm but lower to a 1950mm top datum.
**Result:** The design preserves approximately 100mm structural head zone above factory-cut openings while retaining functional access, workbench-compatible West sill height, and high-level clerestory lighting.

## [Date: 2026-05-23] - Section 7.2 Heat-Loss Recalculation after Opening Changes
**Context:** Revised glazing and door geometry increased the transparent/opening area to 7.00m², while the roof U-value improved to approximately 0.12 W/m²K. Section 7.2 still contained the previous 4m² glazing input and outdated HTC/cost values.
**Decision:** Recalculate Section 7.2 using gross wall area ~37.29m², opaque wall area ~30.29m², roof/floor area 18.62m², glazing/door assembly area 7.00m², wall U=0.16, roof U=0.12, floor U=0.22, glazing U=0.80, and ventilation/air leakage allowance 4.5 W/K.
**Result:** Fabric heat loss is now 16.78 W/K. Total HTC is **~21.28 W/K**. Annual thermal demand is **~766 kWh/year**, costing **~£187.68/year** at £0.245/kWh.

## [Date: 2026-05-23] - MVHR and Electrical Integration Expansion
**Context:** `research/mvhr-research.md` identified that an airtight woodworking workshop requires decoupled ventilation, multi-stage filtration, pressure-balance management, Part F commissioning, and COSHH-aware LEV maintenance.
**Decision:** Add a dedicated dMVHR strategy to the Master Plan: Zehnder ComfoAir 70-class enthalpy dMVHR, factory-cut sleeve, G4/F7 inline extract filtration, optional HEPA/carbon stage, ambient filtration, closed-loop dust extraction, and explicit makeup-air requirement for any future outdoor exhaust mode. Expand electrical schedule with separated RCBOs for machines, heating, IR/controls, MVHR/filtration, and sockets.
**Result:** The plan now preserves airtightness and pressure balance while providing fresh air, humidity control, and dust-core protection. Execution now requires Part F/BPEC balancing and filter/LEV maintenance logging.

## [Date: 2026-06-20] - Dry Moat Strategy & Validation Conflicts
**Context:** The `MASTER_PLAN.md` incorporated a "Dry Moat Strategy", sinking the slab an additional 150mm (flush with the garden lawn) to respect the 2.5m Permitted Development limit while increasing internal headroom to support a 2100mm datum.
**Decision:** We are logging a validation failure. This change inherently conflicts with `Test 001 (Foundation Strategy)` which strictly mandates a 150mm *elevated* splash zone above ground level to protect the timber frame. Additionally, the plan places the main timber sole plate directly on the concrete slab without a continuous thermal break (failing the Red Line test), and leaves OSB SIPs naked for 3 weeks (failing the Weather-Tight sequence test).
**Result:** These conflicts must be officially resolved or accepted as trade-offs. The Architect must address the thermal bridging, and the Foreman must adjust the `WORKPLAN.md` sequence to apply Tyvek immediately on Day 1 of wall erection.

## [Date: 2026-07-10] - Flush Slab Strategy, Compacfoam & Validation Conflicts
**Context:** The Architect updated `MASTER_PLAN.md` with a shallower 390mm foundation excavation, engineering out the MOT Type 1 in favor of 50mm leveling aggregate due to made ground. The slab is poured flush to the garden lawn (0mm FFL), and a 150mm Compacfoam block is used as the thermal/splash zone plinth. West windows were reduced to 1000x1000mm.
**Decision:** Validated against constraint tests. The Compacfoam securely bridges the Red Line thermal gap and PD heights perfectly hit 2500.0mm. However, these changes trigger massive logistical failures:
1. `WORKPLAN.md` (Foreman's schedule) still dictates a 490mm excavation and 150mm MOT Type 1, which contradicts the Architect's made-ground decision.
2. The `MASTER_PLAN.md` explicitly forbids Tyvek direct application to naked OSB SIPs (mandating it over the Wood Fibre), yet the `WORKPLAN.md` demands it for the Weekend 9 Sunday Lockdown.
3. `MASTER_PLAN.md` lacks the mandated "Step-by-Step Construction Phases" linter requirement.
**Result:** These architectural updates are mathematically sound but logistically broken. The `WORKPLAN.md` must be rewritten to match the foundation physics, and a critical decision must be made regarding the "Weekend 9 Sunday Lockdown": *How do we protect naked OSB over the weekend if we cannot apply Tyvek until the Wood Fibre is installed?*

## [Date: 2026-07-10] - Resolution of Validation Conflicts (The Gatekeeper Sign-Off)
**Context:** The previous gap report generated 3 actionable failures involving excavation depths, Tyvek sequence physics, and Markdown linting in the Master Plan.
**Decision:** 
1. `Test 001 (Foundation Strategy)` was updated to formally codify the "Flush Slab + Compacfoam" paradigm. The Architect and Foreman synchronized the `WORKPLAN.md` completely to a 390mm depth manual excavation, utilizing leveling aggregate instead of MOT Type 1.
2. `Test 02 (Weather-Tight Timeline)` was resolved by substituting the Weekend 9 Sunday Lockdown Tyvek wrap with heavy-duty tarpaulins. The Tyvek is now accurately scheduled for Week 11 over the external Wood Fibre insulation, preventing a dual-membrane trap.
3. `Test 06 (SOP Fidelity Linter)` was resolved by inserting the "Step-by-Step Construction Phases" summary at the top of the `MASTER_PLAN.md`.
**Result:** All validation tests pass successfully. The High-Fidelity SOP accurately reflects Passivhaus physics, logistical viability for the weekend-warrior, and strict adherence to Part B and Part L building regulations.

## [Date: 2026-10-07] - dMVHR: Back to Zehnder ComfoAir 70 with Internal Build-Out
**Context:** The 27 Sep switch to the Blauberg Vento Maxi-Air was driven by the ComfoAir 70's 275mm minimum wall (ours is 236mm). A single reversing Blauberg unit is a poor fit for an airtight envelope (Blauberg recommend paired, opposite-phase installation).
**Decision:** Revert to the Zehnder ComfoAir 70. Zehnder support confirmed a local wall build-out is the correct fix and that an internal build-out is acceptable. Spec: 60mm internal build-out (wall 296mm at the unit), 270mm factory core, +1616.7mm axis datum, square cladding cut-out behind the 380 × 376mm outside panel.
**Result:** Continuous balanced ventilation from one penetration, 70m³/h ceiling (2 ACH restored), no change to footprint or rainscreen. Open before SIP order: East-wall pier width vs 740mm side clearance, spline clearance at the core, extract-side F7, Dn,e,w.

## [Date: 2026-10-07] - Swiftfix Lamination Screws; NFS Erects and Wraps the Shell
**Decision:** (1) Swiftfix 8 × 140mm A4 countersunk TX40 (ETA-11/0283) replaces the SPAX A2 for the beam lamination — engineer-approved, UK-stocked. (2) New Forest SIPs supply and erect the shell including all structural connections, and wrap it in a temporary breather membrane to cover a weather hold while the user is away on work commitments.
**Result:** DIY sole plate, wall erection and roof lift are removed from the Workplan. New risk: the temporary membrane's UV limit and its poor performance on a 1:60 roof — the roof is done first after the hold.

## [Date: 2026-10-10] - Glazing: Triple → Asymmetric Acoustic Double
**Context:** Triple-glazed window quotes came to ~£10k (windows only). The building is Building Regs exempt, so there is no Part L glazing limit.
**Decision:** All six fixed lights use asymmetric acoustic double glazing (6T/16Ar/8.8 acoustic lam, glass Rw ≥ 39 dB). The door uses safety double glazing (6T/16Ar/6.4 lam) plus a mandatory seal package (compression gaskets, meeting-stile seal, threshold/drop seal). Frames stay thermally broken marine alu for now, with uPVC fixed lights left open as a cost lever.
**Result:** Heating +~£8–13/yr (HTC 27.02 W/K, £68/yr). The neighbour-façade acoustic loss is ≤0.6 dB. Assumed saving ~£1.0–2.0k on the windows plus ~£200–400 on the door. Full breakdown: `thoughts/glazing_impact_breakdown.md`.

## [Date: 2026-10-10] - Door: Single Leaf, No Acoustic Glass
**Context:** The door's acoustic performance is limited by its seals, and the door faces the user's own house. The 1.5 door's meeting stile was the worst air and sound path.
**Decision:** Single-leaf thermally broken alu door, ~1000mm leaf / ~1100mm frame, standard 4T/16Ar/4T double glazing. SIP opening reduced 1400 → ~1100mm; the right corner pillar is now 739mm.
**Result:** HTC 25.84 W/K, £65.11/yr (−£3/yr vs the 1.5 door). Better airtightness. Clear access drops to ~900mm (open flag: check machinery fits).

## [Date: 2026-10-10] - Door: Half-Glazed Leaf
**Decision:** The single-leaf door becomes half-glazed (upper vision panel, insulated lower panel) to limit West summer solar gain.
**Result:** Peak door solar gain ~510W → ~250W; Ud ~1.3; HTC 25.16 W/K; £63.40/yr.

## [Date: 2026-10-10] - Door: 900mm Leaf
**Decision:** 900mm single leaf (~1000mm frame, ~800mm clear), chosen for tolerance to small frame movement. Machinery access confirmed by the user. The right West corner pillar becomes 839mm.
**Result:** HTC 24.92 W/K, £62.79/yr; peak door solar gain ~215W.

## [Date: 2026-10-10] - uPVC Fixed Lights; Aluminium Door Movement Detail
**Decision:** Fixed lights in uPVC (white or heat-reflective on the West); door in marine aluminium. The door frame is installed with movement gaps, jamb-only fixings and adjustable hardware so small foundation movement is taken up by adjustment, not by the frame.
**Result:** HTC 24.18 W/K, £60.93/yr. The triple → double penalty is effectively recovered.
