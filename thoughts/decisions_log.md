# Decisions Log: Workshop "Philosophy" and Core Choices

## Established Principles (As of Feb 2026)

1. **Acoustics over Space:** The user prioritizes soundproofing over maximizing internal floor space. Open to external continuous insulation to offset internal footprint loss.
2. **Thermal Efficiency First:** High thermal performance (Passivhaus-level) is the priority, accepting higher upfront costs. Dust extraction will utilize an internal recirculation system (with high-grade HEPA and cyclone separation) to preserve the thermal envelope.
3. **Foundation Strategy:** Insulated Concrete Raft. Provides maximum thermal mass, vibration dampening for heavy machinery, and features an explicit 150mm "splash zone" above the external ground level to protect the timber frame from ground moisture and wind-driven rain rebound.
4. **Labor & Logistics:** The user is willing to hire temporary contractors for critical heavy-lifting phases (e.g., moving heavy acoustic boards like Fermacell, or pumping/barrowing concrete on pour day).
5. **Structural Envelope:** Traditional Timber Frame for walls and roof. Chosen for breathability, flexibility, and ease of DIY modification, despite the slower weather-tightness timeline compared to SIPs.
6. **Vapour Management:** A meticulously taped internal Vapour Control Layer (VCL) will be the primary defense against interstitial condensation. This locks the moisture out of the wall structure.
7. **Wall Build-Up:** Single timber frame with external continuous insulation (Twin-stud rejected). Heavy cladding will require engineered structural fixings through the insulation.
8. **Heating Strategy:** The insulated concrete slab will be continuously heated to a baseline temperature to protect tools and act as a thermal battery. This aligns perfectly with future plans for solar+battery.
9. **Roof Design:** "Warm Roof" methodology (insulation entirely *on top* of the timber joists). The user accepts a lower internal ceiling height to safely stay under the 2.5m Permitted Development limit while eliminating roof condensation risks.
10. **Construction Timeline:** A deliberate 4-week halt will be scheduled immediately after pouring the concrete raft to allow full curing and drying before timber framing begins.
11. **Door Access Strategy:** French Doors are strictly eliminated due to acoustic and airtightness failures at the meeting stile. The primary design will utilize an **Asymmetric "1.5" Door system** (1000mm main active leaf + 400mm-600mm bolted slave leaf). This provides Passivhaus-level sealing 99% of the time, while allowing a 1.4m+ clear opening for machinery and 8x4 sheet goods when unbolted. (A premium Lift-and-Slide system is kept as an upgrade option if the budget allows).
12. **Logistics vs Physicality (Concrete):** The user has authorized the £400-£500 budget for a concrete line pump and a small contractor crew for the 2 cubic meter (5-tonne) slab pour. This mitigates the critical risk of physical exhaustion and cold-joints on the 30m wheelbarrow path.
13. **Safety vs Panel Size (Roof Lifting):** The 175mm MgO SIP roof panels (weighing 120kg-150kg) present a severe lifting hazard. The user is evaluating splitting the standard 1200mm panels into 600mm "narrow-format" SIPs (~70kg) and hiring a Material Lift (Genie Lift) to safely winch them onto the 2.5m wall plate.
14. **Heating Optimization (ASHP vs IR):** The high-efficiency ASHP (UFH) will remain the baseline system to provide a cheap, steady-state thermal battery (e.g., 14°C) to protect cast-iron tools and future-proof the space as a home office (passive summer cooling). However, to avoid expensive heating spikes while working, a suspended Infrared (IR) panel will be used for instant, localized radiant heat on the occupant. This IR panel can simply be removed when the space converts to an office.
15. **Flooring Strategy (Workshop vs Office):** The user selected 7mm Heavy-Duty Interlocking PVC Tiles (e.g., Ecotile) over fully-bonded engineered oak or LVT. This prioritizes tool safety (protecting dropped chisels) and machinery point-loads for the current workshop phase. The loose-laid nature allows the tiles to be easily lifted and sold when the space is eventually converted to a premium home office.

## [Date: 2026-04-11] - XPS Floor Insulation Tradeoff (0.13 vs 0.22 W/m²K)
**Context:** Strategist identified that the 150mm XPS slab yields a U-value of 0.22 W/m²K, missing the strict Passivhaus target of 0.15 W/m²K. Achieving 0.13 requires ~260mm XPS.
**Decision:** Option B (Prioritize Logistics). We formally accept the 0.22 W/m²K slab performance as a deliberate tradeoff.
**Reasoning:** The excavation depth (350mm) for 150mm XPS is manageable for a DIY weekend build. Upgrading to 260mm XPS would require nearly 500mm of excavation, drastically increasing soil removal, skip costs, and labor. Since the slab is a continuous thermal mass heated by a highly efficient ASHP, the minor heat loss into the earth is acceptable.

## [Date: 2026-04-11] - Pivot to Internal Electric Flow Boiler
**Context:** The user realized that installing an Air Source Heat Pump (ASHP) would require piercing the Passivhaus SIP envelope for refrigerant lines, introducing major airtightness and moisture vulnerabilities.
**Decision:** Replace the external ASHP with an Internal Electric Flow Boiler (3kW) mounted on the internal wall to heat the wet UFH slab.
**Reasoning:** This approach achieves "zero penetrations" while maintaining the critical concrete thermal battery for machinery stability. The trade-off is a drop in COP from 3.5 to 1.0. However, the Passivhaus energy demand is so low (280 kWh/year) that the running cost only increases from ~£22/year to ~£78/year. The massive upfront capital savings (~£2,000) and elimination of airtightness failure risks make this highly advantageous.

## [Date: 2026-04-11] - Heating Calculation Pivot (HTC vs Passivhaus Shortcut)
**Context:** User astutely noted that because the 150mm XPS floor yields a U-value of 0.22 W/m²K, the building technically misses the Passivhaus standard (≤ 0.15 W/m²K). Therefore, calculating annual demand using the Passivhaus shortcut of 15 kWh/m²a is inaccurate. Additionally, the electricity price used (£0.28) was outdated.
**Decision:** Rewrote the Expected Heating Effort section in the Master Plan using the Heat Transfer Coefficient (HTC) and Heating Degree Days (HDD) methodology to account for the exact U-value of the leaking floor. Updated the electricity price to the recent Ofgem average of £0.245/kWh.
**Result:** Total energy demand recalculates from the theoretical 280 kWh to a realistic **720 kWh/year**. Running costs adjust to **~£176.40/year**. This provides a perfectly accurate expectation for the user.

## [Date: 2026-04-11] - 2.5m PD Height Limit Roof Optimization
**Context:** To maintain the mandatory 150mm concrete splash zone (which raises the FFL +150mm above ground), the remaining height available for the walls and roof to stay under the strict 2500mm Permitted Development limit became dangerously tight. The original plan layered 172mm SIPs + tapered PIR insulation + 18mm OSB, creating a roof nearly 272mm thick, which would have forced the internal ceiling height down to ~2078mm (making standard doors impossible).
**Decision:** Eliminated the Tapered PIR insulation and the 18mm OSB deck completely. Instead, the SIP walls will be factory-cut with a built-in 1:60 pitch (front wall 2161mm, rear wall 2101mm). The flat 172mm roof SIPs sit directly on these pitched walls, and the 1.5mm EPDM is glued directly to the roof SIP's top OSB skin.
**Result:** Total roof buildup thickness is reduced to just 189mm. The highest point of the building hits exactly 2498.5mm, safely clearing the 2500mm PD limit while allowing a 2161mm ceiling height, which perfectly accommodates a standard 2040mm door.

## [Date: 2026-04-12] - Internal Ceiling Height Flooring Correction
**Context:** The previous 2.5m vertical math calculation accurately determined the physical height of the SIP walls (2161mm) but failed to account for the 22mm aesthetic floor buildup (20mm engineered oak + 2mm adhesive) when defining the "Internal Ceiling Height". 
**Decision:** Updated the calculation to explicitly subtract the 22mm floor buildup from the structural wall height to provide the *true* internal ceiling height.
**Result:** The true front internal ceiling height is 2139mm, and the rear is 2079mm. This prompted a structural note change: a standard 2040mm European door leaf would require a ~2100mm rough opening, leaving an unsafe 61mm header. The plan now explicitly mandates a standard UK 1981mm door leaf (rough opening ~2045mm), which safely restores the load-bearing timber header above the door to 116mm.

## [Date: 2026-04-12] - Solar Panel Shading & Roof Insulation Thickness Consideration
**Context:** The Architect noted that downgrading from a 172mm to a 142mm roof SIP incurs a negligible winter heating penalty (~£5/year) but increases the risk of summer overheating. The User countered that planned Solar PV arrays will cover >80% of the flat roof.
**Analysis:** The user is architecturally correct. Solar PV panels mounted on a flat roof act as a continuous primary sun-shield. They absorb the direct shortwave solar radiation and convert it to electricity/heat, while the necessary air gap between the solar panels and the EPDM roof membrane creates a shaded, ventilated buffer. This prevents the primary solar heat from ever reaching the structural roof deck, drastically reducing the required "decrement delay" of the SIP insulation in summer.
**Decision:** Acknowledged that reducing the roof SIP thickness to 142mm (to gain 30mm of internal ceiling height) is a highly viable and safe structural pivot if 80%+ solar coverage is guaranteed. *No changes made to Master Plan currently per user request.*

## [Date: 2026-04-12] - Downgrade Roof SIP to 142mm
**Context:** User confirmed that >=80% of the flat roof will be covered by Solar PV panels. This guaranteed solar shading essentially negates the need for an ultra-thick 172mm SIP core to provide "decrement delay" against summer solar radiation. 
**Decision:** Roof SIP specification downgraded from 172mm to the standard 142mm profile.
**Result:** 
- The physical roof buildup drops from 189mm to 159mm.
- This allows the structural walls to be raised by 30mm while remaining under the 2.5m legal limit.
- Internal ceiling height climbs from 2139mm back up to a comfortable 2169mm.
- The 2191mm structural front wall creates enough clearance for a 96mm timber header, meaning a standard European 2040mm door leaf can be used again!
- The heating requirement (HTC) slightly increases from 20 to 20.6 W/K, causing heating costs to rise trivially from ~£176/year to ~£182/year. This is an exceptional architectural trade-off.

## [Date: 2026-04-12] - Dimension Reduction (3.6m x 5.0m)
**Context:** User requested the room depth be reduced from 5.2m to 5.0m. The footprint reduces from 18.72m² to exactly 18.0m². 
**Decision:** All physical volumes, areas, and heating calculations must be adjusted downwards across both the `MASTER_PLAN.md` and `WORKPLAN.md`.
**Result:** 
- The excavation footprint tightens to 4.4m x 5.8m, saving roughly 0.5 tonnes of manual clay excavation.
- Concrete slab volume required drops slightly to ~2.7m³.
- Perimeter timber, DPC, and skirting lengths drop from 17.6m to 17.2m.
- The external wall surface area drops from ~45m² to ~43m².
- The Heat Transfer Coefficient (HTC) was recalculated with the new surface areas (Wall: 40m², Roof: 18m², Floor: 18m²). The HTC dropped from 20.6 W/K to 19.8 W/K.
- The new expected heating effort drops from 742 kWh to 713 kWh per year, saving the user roughly ~£7/year on their energy bill (£174.68/year).

## [Date: 2026-05-23] - Sloped SIP Roof with Flat 50mm PIR Warm-Over-Roof
**Context:** User requested removal of the bespoke tapered PIR roof package. The roof slope is to be provided by the SIP construction/support geometry, with a flat 50mm PIR board installed above the SIP and EPDM glued directly to the PIR. The stated intent is lower cost and reduced damp risk at the SIP outer layer.
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
