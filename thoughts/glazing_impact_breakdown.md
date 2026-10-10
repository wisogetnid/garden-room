# Glazing & Door Impact Breakdown: Triple → Double Re-Specification

**Date:** Sat 10 Oct 2026
**Persona:** @strategist / @architect
**Trigger:** The triple-glazed window quotes alone came to **~£10k**, which is over budget. The user has decided to switch to **double glazing**. This note works out where high-performance glazing (thermal and acoustic) still earns its cost, opening by opening, and gives an assumed price for each choice.

---

## 1. What Drives the Decision

| Driver | Finding | Consequence |
| :--- | :--- | :--- |
| **Regulation** | The building is exempt from the Building Regulations (Schedule 2, Class VI; confirmed by IoW Building Control, MASTER_PLAN §1.0). Part L sets **no** U-value limit for these windows. | Double glazing is not a compliance problem. The thermal spec is a running-cost and comfort choice only. |
| **Heating cost per W/K** | `24h × 1500 HDD ÷ 1000 ÷ SCOP 3.5 × £0.245/kWh` = **£2.52 per W/K per year**. | Each extra W/K of heat loss through glazing costs about £2.50/yr. Thermal savings cannot repay a glazing upgrade costing hundreds of pounds. |
| **Neighbour exposure** | Neighbours are on the **North, South and East** boundaries (1m wall clearance). The **West** façade faces the user's own house. | Acoustic money should go first to the N/S/E openings. |
| **Fence line** | The clerestory head is at 1995mm FFL ≈ **+2087mm absolute** and the sill at ≈ +1787mm, against **1.8m** boundary fences. | The clerestories sit almost entirely **above the fence**, so they have a direct line of sight to the neighbours' gardens. The fence screens the lower wall but does nothing for them. They are small, but they are the most exposed openings. |
| **Wall acoustic baseline** | Wall build-up: 125mm EPS SIP, 15mm Fermacell glued direct, 60mm wood fibre, ventilated cavity, 11mm Hardie VL. Estimated **Rw ≈ 40 dB**, sensitivity case 45 dB. *(Confidence 2/5. EPS-core SIPs have a poor mass-spring-mass resonance and there is no lab test for this exact build-up.)* | A window is "good enough" acoustically once it passes **only a few % of the façade's sound energy**. Going beyond the wall's own Rw gains almost nothing. |
| **Noise source** | Table saw / planer-thicknesser: **~95–105 dB(A) at 1m**, with mostly mid- and high-frequency energy. | Acoustic laminated glass (PVB damping) targets exactly this band. Low-frequency motor hum is a matter for mass and vibration isolation, not glazing. |

---

## 2. Glass Build-Up Catalogue

| Code | Build-up (outer / cavity / inner) | Centre-pane Ug | Glass Rw (Rw+Ctr) | Glass weight | Assumed price vs. Standard double | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **D-STD** | 4mm toughened / 16mm 90% argon, warm edge / 4mm Low-E | ~1.1 W/m²K | ~30–31 dB (~26) | ~20 kg/m² | baseline | 4/5 |
| **D-ASYM** | 6mm toughened / 16mm argon / 4mm Low-E | ~1.1 W/m²K | ~33–35 dB (~30) | ~25 kg/m² | +£15–30/m² | 3/5 |
| **D-SAFE** *(door)* | 6mm toughened / 16mm argon / 6.4mm laminated Low-E | ~1.1 W/m²K | ~35–36 dB (~31) | ~31 kg/m² | +£40–70/m² | 3/5 |
| **D-AC** *(high acoustic)* | 6mm toughened / 16mm argon / **8.8mm acoustic-PVB laminated** Low-E (e.g. Pilkington Optiphon™, Saint-Gobain Stadip Silence®) | ~1.1 W/m²K | **~39–41 dB** (~35) | ~37 kg/m² | **+£60–120/m²** | 3/5 |
| **T-AC** *(previous spec)* | 6T / 16 / 4 / 16 / 8.8 acoustic laminated | ~0.6 W/m²K | ~40–42 dB (~36) *(the plan claimed 42–44)* | ~47 kg/m² | +£150–250/m² over D-STD | 3/5 |

**Key finding:** with the same acoustic laminated inner pane, **asymmetric acoustic double (D-AC) performs within ~1–2 dB of the acoustic triple (T-AC)**. The acoustic benefit comes from the laminated pane and the asymmetric pane thicknesses, not from a third pane. A triple with two identical 16mm cavities can even develop extra mass-spring-mass resonances. Dropping to double therefore costs **almost nothing acoustically**, as long as the acoustic laminated pane is kept where it matters.

---

## 3. Whole-Window Thermal Values (Frame Fraction Matters)

The plan claimed a single **Uw ≈ 0.85 W/m²K** for every unit. That figure is not achievable on a 300 × 1500mm clerestory: a 60–70mm aluminium frame takes up **~45–50 %** of its area, so the frame, not the glass, sets Uw.

| Opening | Area | Frame fraction | Uw triple (realistic) | Uw double | Δ heat loss | Δ running cost |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 4 × Clerestory (300 × 1500) | 1.80m² | ~45–50 % | ~1.4 W/m²K | ~1.8 W/m²K | +0.72 W/K | **+£1.81/yr** |
| 2 × West fixed (1000 × 1000) | 2.00m² | ~25–30 % | ~0.95 W/m²K | ~1.4 W/m²K | +0.90 W/K | **+£2.27/yr** |
| 1 × West door (1400 × 2078) | 2.91m² | ~35–40 % (leaves, meeting stile) | ~1.15 W/m²K | ~1.7 W/m²K | +1.60 W/K | **+£4.03/yr** |
| **Total** | **6.71m²** | | **7.77 W/K** | **10.99 W/K** | **+3.22 W/K** | **≈ +£8/yr** |

*Against the plan's optimistic 5.70 W/K the penalty is +5.29 W/K, or **+£13/yr**. Confidence 3/5. Uw values assume a thermally broken aluminium frame with Uf ≈ 2.0–2.4 and a warm-edge spacer with ψ ≈ 0.04 W/mK. Ask suppliers for the declared Uw per unit size.*

**Condensation check (Weather-Tight / durability):** at 0°C outside and 14°C inside, the double-glazed centre pane sits at ~12°C. A frame edge with **fRsi ≥ 0.70** sits at ≥ 9.8°C, or ~8.9°C at −3°C outside. Dew point at 14°C is **6.2°C at 60 % RH** and **8.6°C at 70 % RH**. **Pass**, provided the humidistat-controlled dehumidifier (MASTER_PLAN §4) keeps RH ≤ 60 %. Make **fRsi ≥ 0.70** and a **warm-edge spacer** mandatory in the specification.

---

## 4. Acoustic Impact by Façade (Composite Sound Reduction)

Composite R = −10·log₁₀( Σ Sᵢ·10^(−Rᵢ/10) ÷ S_total ). Installed window Rw is taken as **glass Rw − 2 dB** to allow for frame and perimeter losses. The door Rw is seal-limited. The **"Share"** column is the window's share of the sound energy that gets through that façade.

| Façade (neighbour?) | Option | Façade R (wall 40 dB) | Window share | Façade R (wall 45 dB) | Window share |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **East** (neighbour, 2 clerestories, 0.9m² of 10.67m²) | D-STD | 37.5 dB | 48 % | 39.5 dB | 74 % |
| | D-ASYM | 38.7 dB | 32 % | 41.5 dB | 59 % |
| | **D-AC** | **39.8 dB** | **13 %** | **43.7 dB** | **32 %** |
| | T-AC (old) | 40.0 dB | 8 % | 44.3 dB | 23 % |
| **North / South** (neighbour, 1 clerestory, 0.45m² of 7.48m²) | D-STD | 38.1 dB | 39 % | 40.5 dB | 67 % |
| | **D-AC** | **39.8 dB** | **9 %** | **44.1 dB** | **24 %** |
| | T-AC (old) | 40.0 dB | 6 % | 44.5 dB | 17 % |

| West façade (own house; 2.0m² windows + 2.91m² door of 10.95m²) | Façade R (wall 40) | Energy share wall / windows / door |
| :--- | :--- | :--- |
| D-STD windows + standard-sealed door (Rw ≈ 31) | 33.5 dB | 12 / 41 / 47 % |
| D-STD windows + **high-seal door** (Rw ≈ 35) | 34.9 dB | 17 / 57 / 26 % |
| **D-AC windows** + standard-sealed door | 35.3 dB | 19 / 10 / **72 %** |
| **D-AC windows + high-seal door** | **37.7 dB** | 33 / 17 / 50 % |
| T-AC windows + triple door, high seal (old spec) | 38.0 dB | 35 / 12 / 53 % |

**Readings:**
1. On every neighbour-facing façade, **D-AC gets to within 0.2–0.6 dB of the old triple spec**, which is inaudible.
2. With **D-STD** the clerestories pass **40–75 %** of the sound energy on the neighbour façades. They become the weak link, and they sit above the fence. This is the one place where "standard" glazing really costs acoustic performance.
3. On the West façade **the door dominates**. Its seals (compression gaskets, multi-point lock, threshold/drop seal) are worth more dB than any glass upgrade. A triple-glazed door adds nothing over a well-sealed double-glazed door.
4. Operational rule, free of charge: **the door stays shut while machines run.** An open 2.9m² door puts the façade at about 0 dB.

---

## 5. Per-Opening Impact Breakdown (Decision Table)

Price deltas are **assumed** (window-company pricing, Isle of Wight, Oct 2026, confidence 2/5). Confirm them with **line-item re-quotes**. "Standard" = D-STD (D-SAFE for the door). "High" = D-AC.

| Opening | Qty / area | Neighbour exposure | Thermal: High vs Std | Acoustic: High vs Std (façade) | Assumed price Δ, High vs Std | Saving vs old triple (same frame) | **Recommendation** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **N clerestory** | 1 / 0.45m² | **High.** Above fence, ~1m from boundary, direct line of sight | Same Ug; 0 W/K | **+1.7 dB** (window share 39 % → 9 %) | +£30–60 (small IGU, minimum-charge driven) | −10–20 % of unit price | **HIGH (D-AC)** |
| **S clerestory** | 1 / 0.45m² | **High.** As North | 0 W/K | **+1.7 dB** | +£30–60 | −10–20 % | **HIGH (D-AC)** |
| **E clerestories** | 2 / 0.90m² | **High.** As North; also shares the façade with the dMVHR terminal | 0 W/K | **+2.3 dB** (48 % → 13 %) | +£60–120 | −10–20 % | **HIGH (D-AC)** |
| **West fixed windows** | 2 / 2.00m² | Low–Medium. Face own house; sound spreads round to N/S gardens | 0 W/K | +1.8 dB with standard door; **+2.8 dB with high-seal door** | +£90–180 | −10–20 % | **HIGH (D-AC)** recommended: low cost, and the laminated inner pane protects against workbench and kickback impact. *Downgrade candidate:* D-ASYM saves ~£60–120 at a cost of ~2 dB on the West façade. |
| **West door** (1.5 leaf) | 1 / 2.91m² | Low–Medium. Own-house side, but the **largest and leakiest** opening | Double vs triple: +1.6 W/K (+£4/yr) | Glass upgrade D-SAFE → D-AC: ≤ +1 dB (seal-limited). **Seal upgrade: +3–4 dB** | Glass: +£130–260 (**not recommended**). Seals: **+£100–250** (drop seal / threshold seal, gasket spec) | −£200–400 vs triple door | **STANDARD glass (D-SAFE)**. Put the money into **seals**. |

**Recommended package vs. old triple spec:** thermal **+£8/yr**; acoustic **−0.2 to −0.6 dB** on the neighbour façades (inaudible); price **≈ −10–20 % of the window quote (~£1.0–2.0k off £10k)**, plus **~£200–400** off the door.

---

## 6. Price Reality Check: Bigger Levers Than Glass

**[OPEN RISK FLAG: double glazing alone will not halve the quote.]** For small, bespoke, marine-grade aluminium units, the IGU is only ~20–30 % of the unit price. Frame fabrication, Qualicoat Seaside coating, per-unit minimum charges and delivery to the island make up most of it. Expect the triple → double switch to save **~£1.0–2.0k** on a £10k quote. If the target is closer to £5–6k, these levers move more money:

| Lever | Assumed price impact | Trade-off | Confidence |
| :--- | :--- | :--- | :--- |
| **Ask for line-item quotes** (per unit, glass build-up, coating class, delivery) | n/a, but it shows where the £10k actually goes | None | – |
| **No 316 hardware on fixed lights.** The six fixed units have no handles or locks; check the quote is not charging for them | Small, £0–300 | None | 3/5 |
| **Fixed lights in uPVC** (salt-immune, Uf ≈ 1.2–1.3) while the door stays marine aluminium | **−40–60 % on the six fixed units** | Wider sightlines on the 300mm clerestories (~10–20 % less glass); looks different from the alu door; anthracite foil finish only. Thermally *better* than alu on the clerestories | 2/5 |
| **Trade aluminium system from a local fabricator** (e.g. Stylish Windows Trade & DIY Centre, Newport) instead of a premium bespoke supplier | −20–35 % | Confirm the Qualicoat Seaside / marine coating class and warranty for a coastal site | 2/5 |
| **Single active leaf + fixed glazed sidelight** (e.g. 900 + 500 fixed) instead of a 1.5 door | −£300–800 | Loses the full 1400mm opening for machinery delivery. Removes the leaky meeting stile, so it **gains** airtightness and acoustics | 2/5 |
| **Retrofit secondary glazing later** (DIY 6mm acrylic or polycarbonate inside the 236mm reveal, ~100mm gap) | £30–60 per clerestory | Upgrade path of **+8–12 dB** if a neighbour complains. This makes "standard" glazing a recoverable decision | 3/5 |

*Not recommended:* resizing or dropping openings. The SIP openings are factory-cut and the opening geometry has already been coordinated with the dMVHR pier (§4.2.1).

---

## 7. Recommended Specification (Carried into MASTER_PLAN §2.7)

1. **All six fixed lights (4 clerestories + 2 West):** D-AC asymmetric acoustic double, 6mm toughened / 16mm argon, warm edge / 8.8mm acoustic-PVB laminated Low-E. Ug ≈ 1.1, glass Rw ≥ 39 dB. **One glass spec for every fixed light.**
2. **Door:** D-SAFE double, 6mm toughened / 16mm argon / 6.4mm laminated Low-E. Ug ≈ 1.1, Ud ≈ 1.6–1.8. **Seal package mandatory:** continuous EPDM compression gaskets at every leaf edge and the meeting stile, multi-point cam lock, and a threshold seal or automatic drop seal compatible with the flush +92mm threshold.
3. **Frames:** thermally broken, marine-grade aluminium (Qualicoat Seaside) remains the baseline. **[OPEN: uPVC fixed lights]** are a user choice once line-item quotes are in hand.
4. **Mandatory performance:** frame **fRsi ≥ 0.70**, warm-edge spacer, declared Uw per unit size, and glazing rebate deep enough for the **30.8mm** D-AC unit.

## 8. Self-Verification (AGENTS.md §4; `/tests` retired, run by hand)

* **Red Line:** the change only alters the IGU and frame Uw. Installation position, airtight tape (Tescon Vana to the reveals) and the external insulation return are unchanged. **Pass.**
* **Weather-Tight:** same install week (Week 7). D-AC units are lighter than triple (~37 vs ~47 kg/m²), so handling is easier. **Pass.**
* **Condensation:** fRsi ≥ 0.70 with RH ≤ 60 % → **Pass** (§3).
* **Sequence:** no change. **Pass.**
* **Open:** Zehnder Dn,e,w is still needed to rank the dMVHR against the East clerestories (MASTER_PLAN §4.2.1).

---

## 9. Revision (10 Oct 2026, later): Single-Leaf Door, No Acoustic Door Glass

**User decision:** no acoustic glazing on the door. The asymmetric 1.5 door is replaced by a **single leaf**.

### 9.1 Door Thermal Impact

Same basis as before: £2.52 per W/K per year. The narrower ~1100mm opening gives back ~0.62m² of SIP wall (U 0.18).

| Door option | Door area | Ud | Door + infill wall | Running cost/yr | vs old 1.5 door |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Old asymmetric 1.5, double glazed (1400 wide) | 2.91m² | ~1.7 | 4.95 W/K | £12.47 | – |
| **Single leaf, fully glazed, standard double (adopted)** | 2.29m² | ~1.6 | **3.77 W/K** | **£9.50** | **−£3/yr** |
| Single leaf, half-glazed | 2.29m² | ~1.3 | 3.08 W/K | £7.77 | −£5/yr |
| Single leaf, solid insulated panel (e.g., Hörmann ThermoSafe class) | 2.29m² | ~1.0 | 2.40 W/K | £6.04 | −£6/yr |

**Reading:** the door's thermal performance is worth **under £7/yr** between the best and worst options. Choose it on **daylight, security and price**, not heat loss. The real thermal gain from going single-leaf is **airtightness**: no meeting stile, and four-sided gasket compression. Comfort is unaffected; the door is not next to a seated workstation.

### 9.2 Door Acoustic Impact

Taking the acoustic laminate out of the door glass costs ≤1 dB (the door is seal-limited). Removing the meeting stile **gains** about the same back. West façade composite R with D-AC windows: door Rw 30 → 35.2 dB, door Rw 32 → 36.5 dB, door Rw 34 (with drop seal) → 37.6 dB. This façade faces the user's own house, so the result is accepted.

### 9.3 Leaf Widths (UK)

| Category | Typical leaf | Doorset (outer frame) | Clear opening | Source / confidence |
| :--- | :--- | :--- | :--- | :--- |
| Off-the-shelf composite / uPVC doorsets | 736–816mm | 840 / 920mm | ~680–760mm | Wickes Door-Stop range (4/5) |
| Made-to-order composite / uPVC | up to ~1000mm | ~1100mm | ~900mm | Composite max ~1000 × 2300mm (3/5); uPVC similar, leaves sag above this |
| Made-to-order aluminium (residential door systems) | up to ~1200mm | ~1300mm | ~1100mm | e.g., AZ-45 single leaf max 1200 × 2360mm (3/5) |

**Adopted:** ~1000mm aluminium leaf, ~1100mm doorset, ~900mm clear. Going to 1200mm in aluminium is possible but means heavier hinges, more leaf sag and a higher price for ~200mm more clear width. **[OPEN RISK FLAG: confirm the largest machine fits through ~900mm clear before the SIP order.]**

### 9.4 uPVC Durability in Cowes (Coastal Solent)

| Factor | Effect at Cowes | Mitigation in the spec |
| :--- | :--- | :--- |
| **Salt spray on the profile** | uPVC is non-metallic and does not react with salt. This is its main advantage over aluminium, which depends on its powder coat (Qualicoat Seaside) staying intact. | None needed beyond washing down 2× a year. |
| **Hidden steel reinforcement** | Galvanised steel inside the chambers is sealed from rain but can corrode where drainage slots or cut ends are exposed. Fixed lights carry little reinforcement. | Ask for galvanised (not bare) reinforcement and drainage slots that don't expose the steel. |
| **Hardware (door/opening units)** | The **weakest point** on the coast: zinc/steel hinges and locks pit within a few years. | Hardware to **BS EN 1670 Grade 5** salt-spray resistance or 316 stainless. Not relevant to fixed lights. |
| **UV and heat** | South- and west-facing frames degrade fastest. **Dark foils (anthracite) on the West façade** reach 60–70°C in afternoon sun, which risks bowing, foil lift and gasket shrinkage. White profiles chalk slightly but stay stable. | White, or a heat-reflective foil (e.g., Renolit Exofol with solar-reflective technology), on the West face. Profiles to **BS EN 12608 Class A** with a long-life UV-stabilised formulation (Rehau, VEKA, Deceuninck, Kömmerling class). |
| **Gaskets** | EPDM / TPE gaskets harden and shrink after ~15–20 years. | Specify **replaceable** (not co-extruded) gaskets. |
| **Lifespan** | Good-quality uPVC: **~20–35 years**. Marine-coated aluminium: **~40+ years** if the coating is maintained. | uPVC suits the six fixed lights (no hardware, small spans). **Keep the door in aluminium:** leaf width (uPVC sag above ~1000mm), hardware load and security favour it. |

**Verdict:** uPVC holds up well in Cowes for **fixed lights in white or heat-reflective finish**. Avoid dark foils on the West façade and avoid uPVC for the wide door leaf. Confidence 3/5. Sources: REHAU coastal guidance (sadecor.co.za); uPVC lifespan summaries; manufacturer data to be confirmed at quote stage.

### 9.5 Revision: Half-Glazed Door Adopted (Summer Solar Gain)

**User decision:** a half-glazed leaf, to limit direct West sun heating the room in summer. Upper vision panel ~0.75m² (4T/16Ar/4T Low-E); lower solid insulated aluminium infill panel.

| Metric | Fully glazed leaf | **Half-glazed leaf (adopted)** |
| :--- | :--- | :--- |
| Glass area | ~1.55m² | ~0.75m² |
| Peak summer solar gain through the door (West, ~550 W/m², g ≈ 0.6) | ~510W | **~250W** |
| Ud / heat loss | ~1.6 / 3.66 W/K | **~1.3 / 2.98 W/K** |
| Running cost | £9.20/yr | **£7.50/yr** |

~260W less peak gain is significant in a 31m³ room with high internal gains from machines; it is about a quarter of a small ASHP's cooling output. Winter solar gain lost is negligible (low sun, a West façade, and a 12–14°C setpoint). The West fixed windows keep their external blinds. Whole building: HTC **25.16 W/K**, **£63.40/yr**.

### 9.6 Revision: 900mm Leaf Adopted

**User decision:** a **900mm leaf** (~1000mm doorset, ~800mm clear). A narrower leaf tolerates small frame movement and racking with less binding and sags less on its hinges. The user has confirmed the machinery fits, which closes the access flag.

| Metric | 1000mm leaf, half-glazed | **900mm leaf, half-glazed (adopted)** |
| :--- | :--- | :--- |
| Door area / glass | 2.29m² / ~0.75m² | **2.08m² / ~0.65m²** |
| Peak summer solar gain through the door | ~250W | **~215W** |
| Door heat loss | 2.98 W/K | **2.70 W/K** |
| SIP opening / right corner pillar | ~1100 / 739mm | **~1000 / 839mm** (~699mm visible internal wall) |

Whole building: openings 5.88m², HTC **24.92 W/K**, 897 kWh, **£62.79/yr**.

---

## 10. Cost Ballpark: Adopted Setup (10 Oct 2026)

**Setup:** 4 × uPVC fixed clerestories 300 × 1500 and 2 × uPVC fixed West 1000 × 1000, all D-AC (6T/16Ar/8.8 acoustic lam), white or heat-reflective foil on the West. 1 × aluminium half-glazed single door, 900mm leaf, standard double glazing, insulated lower panel, 316 hardware. **Supply only, DIY install** (per WORKPLAN Week 7). Confidence **2/5**: web benchmarks, not quotes.

| Item | Basis | Ballpark |
| :--- | :--- | :--- |
| uPVC fixed clerestory, standard double, white | Small bespoke unit, minimum-charge driven; fixed 1200 × 1200 supply-only benchmark £200–300 | £120–200 each |
| + acoustic lam upgrade per clerestory | 8.8mm acoustic lam pane £90–180/m², min 0.5m² charge per pane | +£45–90 each |
| **4 × clerestories** | | **£660–1,160** |
| uPVC fixed West 1000 × 1000, standard double | Supply-only benchmark | £180–280 each |
| + acoustic lam upgrade (~0.72m² glass) | as above | +£65–130 each |
| + heat-reflective foil (if not white) | ~15–25 % uplift | +£30–60 each |
| **2 × West windows** | | **£490–940** |
| **Aluminium door**, 900mm leaf, half-glazed, insulated panel, marine coating, 316 / Grade 5 hardware, 3D hinges | Supply-only alu singles from ~£920 (900mm) up to £3.3–4.0k (premium ranges) | **£1,200–2,500** |
| Optional automatic drop seal | Surface-mounted | £80–150 |
| Install sundries | Expanding foam tapes, Contega / Tescon Profil, packers, frame fixings for 7 openings | £250–450 |
| Delivery to the Isle of Wight | Bespoke delivery ~£70 mainland plus Solent premium | £100–300 |
| **Total, supply only** | | **≈ £2,800–5,500** (central ~£3,800) |
| *If fitted by an installer* | ~£80–150 per window, £200–400 for the door | *+£700–1,300* |

**Compared with the triple quote:** ~£10k for the windows alone (door extra) → **~£3–5.5k for windows *and* door**. Most of the saving comes from the uPVC frames and supply-only purchase, not from dropping the third pane.

**Sources:** [less.co.uk window costs](https://less.co.uk/home-improvements/windows/cost); [Just Value Doors stocked/bespoke windows](https://www.justvaluedoors.co.uk/stocked-windows); [trade2base window installation costs](https://www.trade2base.com/blog/window-installation-costs-uk); [8.8mm acoustic laminate cut to size](https://buyglass.co/?p=32202); [Saint-Gobain Stadip Silence](https://www.saint-gobain-glass.co.uk/stadipr-silence); [900mm aluminium single door](https://homebuilddoors.co.uk/products/900mm-white-heritage-aluminium-single-door); [Doors Direct 2U aluminium door pricing](https://doorsdirect2u.co.uk/?p=174441); [Self Build entrance door costs](https://www.self-build.co.uk/how-to-cost-an-entrance-door).
