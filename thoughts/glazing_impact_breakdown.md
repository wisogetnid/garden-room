# Glazing & Door Impact Breakdown

**Date:** Sat 10 Oct 2026 (consolidated after all same-day revisions)
**Persona:** @strategist / @architect
**Trigger:** The triple-glazed window quotes alone came to **~£10k**, which is over budget. The user switched to **double glazing** and asked for the thermal, acoustic and price impact of each opening. This document is the **current adopted specification**, and it is mirrored in `plans/MASTER_PLAN.md` §2.7, §7.1 and §7.2. Superseded options are listed in §11 for traceability only.

---

## 0. Adopted Specification (Summary)

| Opening | Qty / size | Frame | Glass | Uw (whole unit) | Rw (fitted, assumed) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fixed clerestories** (N ×1, S ×1, E ×2) | 4 × 300 × 1500mm (1.80m²) | **uPVC**, white, BS EN 12608 Class A, glazed directly into the frame (no dummy sash) | **D-AC:** 6mm toughened / 16mm argon, warm edge / 8.8mm acoustic-PVB laminated Low-E | ~1.5 W/m²K | ~38 dB |
| **West fixed windows** | 2 × 1000 × 1000mm (2.00m²) | **uPVC**, white or heat-reflective foil (no dark standard foil on the West) | **D-AC** (as above) | ~1.3 W/m²K | ~38 dB |
| **West entrance door** | 1 × **single leaf, 900mm**; opening ~1000 × 2080mm (2.08m²); ~800mm clear | **Thermally broken marine aluminium** (Qualicoat Seaside), 316 / BS EN 1670 Grade 5 hardware, 3D-adjustable hinges | **Half-glazed:** upper vision panel ~0.65m², **D-STD** 4mm toughened / 16mm argon / 4mm toughened Low-E; lower insulated aluminium infill panel (≥28mm) | ~1.3 W/m²K | ~32 dB (~34 with optional drop seal) |

**No side panel.** The SIP door opening is cut to the single-leaf doorset (~1000mm). The West façade uses an even rhythm: door (right / South end, seen from outside) and two windows, all ~1000mm, separated by four equal 481mm piers. The inner piers land over ground screws P07 / P11 (see MASTER_PLAN §2.7). The door mid-rail sits at ~1080mm FFL, level with the window sills. The door is made to order to suit the ~1000mm SIP opening after the SIP drawings are confirmed (decision 25 Oct 2026).

**Supplier check (25 Oct 2026):** the IOW Glass estimate (4/18Ar/6.8 acoustic lam, REHAU TOTAL70, Smart Systems door) is assessed against this spec in **§12**. The Master Plan now uses ~1.5 W/m²K for every unit (HTC 25.24 W/K, ~£63.60/yr); §0–§11 keep the earlier figures for traceability.

**Whole building:** glazed and door area **5.88m²**, area-weighted Uw **~1.36 W/m²K**, glazing heat loss **8.00 W/K**, HTC **24.54 W/K** (after the 2026-10-11 taller-wall revision), **~£62/yr** heating. Cost ballpark **≈ £2.8–5.5k supply only** (§9).

---

## 1. What Drives the Decision

| Driver | Finding | Consequence |
| :--- | :--- | :--- |
| **Regulation** | The building is exempt from the Building Regulations (Schedule 2, Class VI; confirmed by IoW Building Control, MASTER_PLAN §1.0). Part L sets **no** U-value limit for these windows. | Double glazing is not a compliance problem. The thermal spec is a running-cost and comfort choice only. |
| **Heating cost per W/K** | `24h × 1500 HDD ÷ 1000 ÷ SCOP 3.5 × £0.245/kWh` = **£2.52 per W/K per year**. | Each extra W/K of heat loss through glazing costs about £2.50/yr. Thermal savings cannot repay a glazing upgrade costing hundreds of pounds. |
| **Neighbour exposure** | Neighbours are on the **North, South and East** boundaries (1m wall clearance). The **West** façade faces the user's own house. | Acoustic money goes first to the N/S/E openings. |
| **Fence line** | The clerestory head is at 1997mm FFL ≈ **+2037mm absolute** and the sill at ≈ +1737mm, against **1.8m** boundary fences. | The clerestories sit almost entirely **above the fence**, with a direct line of sight to the neighbours' gardens. They are small but the most exposed openings. |
| **Wall acoustic baseline** | 125mm EPS SIP, 15mm Fermacell glued direct, 60mm wood fibre, ventilated cavity, 11mm Hardie VL. Estimated **Rw ≈ 40 dB**, sensitivity case 45 dB. *(Confidence 2/5. EPS-core SIPs have a poor mass-spring-mass resonance and there is no lab test for this build-up.)* | A window is "good enough" once it passes **only a small share of the façade's sound energy**. Going beyond the wall's own Rw gains almost nothing. |
| **Noise source** | Table saw / planer-thicknesser: **~95–105 dB(A) at 1m**, with mostly mid- and high-frequency energy. | Acoustic laminated glass (PVB damping) targets exactly this band. Low-frequency motor hum is a matter for mass and vibration isolation. |

---

## 2. Glass Build-Up Catalogue

| Code | Build-up (outer / cavity / inner) | Centre-pane Ug | Glass Rw (Rw+Ctr) | Glass weight | Assumed price vs. D-STD | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **D-STD** | 4mm toughened / 16mm 90% argon, warm edge / 4mm toughened Low-E | ~1.1 W/m²K | ~30–31 dB (~26) | ~20 kg/m² | baseline | **Adopted: door vision panel** |
| D-ASYM | 6mm toughened / 16mm argon / 4mm Low-E | ~1.1 W/m²K | ~33–35 dB (~30) | ~25 kg/m² | +£15–30/m² | Not used |
| **D-AC** | 6mm toughened / 16mm argon / **8.8mm acoustic-PVB laminated** Low-E (e.g., Pilkington Optiphon™, Saint-Gobain Stadip Silence®) | ~1.1 W/m²K | **~39–41 dB** (~35) | ~37 kg/m² | **+£60–120/m²** | **Adopted: all six fixed lights** |
| T-AC | 6T / 16 / 4 / 16 / 8.8 acoustic laminated (triple) | ~0.6 W/m²K | ~40–42 dB (~36) | ~47 kg/m² | +£150–250/m² | Withdrawn on cost |

**Key finding:** with the same acoustic laminated inner pane, **D-AC double performs within ~1–2 dB of the T-AC triple**. The acoustic benefit comes from the laminated pane and the asymmetric pane thicknesses, not from a third pane. The laminated inner pane also holds the glass together if it is hit (kickback, long boards), which suits the workbench windows.

---

## 3. Thermal Impact by Opening

uPVC frames have a lower Uf (~1.2–1.3) than thermally broken aluminium (~2.0–2.4). This matters most on the 300mm clerestories, where the frame is ~45–50% of the unit area.

| Opening | Area | Uw adopted | Heat loss | Running cost | Old triple-alu spec (realistic Uw) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4 × uPVC clerestory | 1.80m² | ~1.5 W/m²K | 2.70 W/K | £6.80/yr | ~1.4 → 2.52 W/K |
| 2 × uPVC West fixed | 2.00m² | ~1.3 W/m²K | 2.60 W/K | £6.55/yr | ~0.95 → 1.90 W/K |
| 1 × alu half-glazed door, 900mm leaf | 2.08m² | ~1.3 W/m²K | 2.70 W/K | £6.80/yr | 1400 × 2078 1.5-door, ~1.15 → 3.35 W/K |
| Extra solid wall from the narrower door opening | 0.83m² | 0.18 W/m²K | 0.15 W/K | £0.38/yr | – |
| **Total** | | **~1.36 W/m²K** (openings) | **8.15 W/K** | **≈ £20.50/yr** | **7.77 W/K** |

**Reading:** the adopted double-glazed set comes within **~0.4 W/K (≈ £1/yr)** of the original triple-glazed aluminium spec. The penalty from dropping the third pane is recovered by the uPVC frames, the single-leaf door and the half-glazed leaf. *Confidence 3/5. Ask suppliers for the declared Uw per unit size.*

**Condensation check:** at 0°C outside and 14°C inside, the double-glazed centre pane sits at ~12°C. A frame edge with **fRsi ≥ 0.70** sits at ≥ 9.8°C, or ~8.9°C at −3°C outside. Dew point at 14°C is **6.2°C at 60% RH** and **8.6°C at 70% RH**. **Pass**, provided the humidistat-controlled dehumidifier (MASTER_PLAN §4) keeps RH ≤ 60%. uPVC frames typically reach fRsi ≥ 0.75. Make fRsi ≥ 0.70 and a warm-edge spacer mandatory.

---

## 4. Acoustic Impact by Façade (Composite Sound Reduction)

Composite R = −10·log₁₀( Σ Sᵢ·10^(−Rᵢ/10) ÷ S_total ). Fitted window Rw is taken as **glass Rw − 2 dB**. The door Rw is seal-limited. **"Share"** is that element's share of the sound energy getting through the façade.

### 4.1 Neighbour Façades (Clerestories)

| Façade | Option | Façade R (wall 40 dB) | Window share | Façade R (wall 45 dB) | Window share |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **East** (2 clerestories, 0.9m² of 10.67m²) | D-STD | 37.5 dB | 48% | 39.5 dB | 74% |
| | **D-AC (adopted)** | **39.8 dB** | **13%** | **43.7 dB** | **32%** |
| | T-AC (withdrawn) | 40.0 dB | 8% | 44.3 dB | 23% |
| **North / South** (1 clerestory, 0.45m² of 7.48m²) | D-STD | 38.1 dB | 39% | 40.5 dB | 67% |
| | **D-AC (adopted)** | **39.8 dB** | **9%** | **44.1 dB** | **24%** |
| | T-AC (withdrawn) | 40.0 dB | 6% | 44.5 dB | 17% |

### 4.2 West Façade (Own House; 2.0m² Windows + 2.08m² Door of 10.95m²)

| Option | Façade R (wall 40) | Share wall / windows / door |
| :--- | :--- | :--- |
| D-STD windows + door Rw 32 | 34.4 dB | 17 / 50 / 33% |
| D-AC windows + door Rw 30 (poorly adjusted seals) | 35.5 dB | 22 / 10 / 67% |
| **D-AC windows + single-leaf door Rw 32 (adopted)** | **36.7 dB** | 30 / 14 / 57% |
| D-AC windows + door Rw 34 (optional drop seal) | 37.8 dB | 38 / 17 / 45% |

**Readings:**
1. On every neighbour façade, **D-AC is within 0.2–0.6 dB of the triple spec**, which is inaudible.
2. With D-STD the clerestories would pass **40–75%** of the neighbour-façade sound energy and become the weak link above the fence. That is why they keep the acoustic laminate.
3. On the West façade **the door dominates**. Its seals and their adjustment are worth more than any glass upgrade, so the door glass is plain D-STD. The single leaf has no meeting stile, which removes the worst leak path of the old 1.5 door.
4. Operational rule: **the door stays shut while machines run.**

**Rough meaning:** a façade at ~40 dB brings a ~100 dB(A) planer down to the **low 60s dB(A) just outside the wall**, falling further with distance and behind the fences. *Very rough; confidence 2/5.*

---

## 5. Per-Opening Decision Table

| Opening | Neighbour exposure | Adopted | Acoustic effect vs D-STD | Thermal effect | Assumed price Δ vs D-STD glass |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **N clerestory** | **High.** Above fence, ~1m from boundary | uPVC + D-AC | **+1.7 dB** façade (window share 39% → 9%) | 0 (same Ug) | +£45–90 |
| **S clerestory** | **High.** As North | uPVC + D-AC | **+1.7 dB** | 0 | +£45–90 |
| **E clerestories ×2** | **High.** As North; shares the façade with the dMVHR terminal | uPVC + D-AC | **+2.3 dB** (48% → 13%) | 0 | +£90–180 |
| **West fixed ×2** | Low–Medium. Face own house | uPVC + D-AC | +2.3 dB West façade | 0 | +£130–260 |
| **West door** | Low–Medium. Own house side, but the largest opening | Alu single leaf 900mm, half-glazed D-STD | Seal-limited; acoustic glass would add ≤1 dB, so it is not used | Half-glazed: −0.6 W/K vs fully glazed | baseline |

---

## 6. Door: Single Leaf, 900mm, Half-Glazed (No Side Panel)

### 6.1 Leaf Width

The **leaf** is the opening part; the **frame** (doorset) is the fixed outer part.

| Category | Typical leaf | Doorset (outer frame) | Clear opening | Source / confidence |
| :--- | :--- | :--- | :--- | :--- |
| Off-the-shelf composite / uPVC doorsets | 736–816mm | 840 / 920mm | ~680–760mm | Wickes Door-Stop range (4/5) |
| Made-to-order composite / uPVC | up to ~1000mm | ~1100mm | ~900mm | Composite max ~1000 × 2300mm (3/5) |
| Made-to-order aluminium | up to ~1200mm | ~1300mm | ~1100mm | e.g., AZ-45 single leaf max 1200 × 2360mm (3/5) |
| **Adopted** | **900mm, aluminium** | **~1000mm** | **~800mm** | User confirmed the machinery fits |

**Why 900mm:** a narrower leaf changes less across its width for the same frame movement, and it sags less on its hinges. This suits a building on a ground-screw foundation that may see small movement. Aluminium leaves are routinely made at 900mm, well inside every system's limits.

### 6.2 Glazing Ratio and Thermal / Solar Impact (900mm leaf, 2.08m²)

| Leaf option | Glass area | Ud | Heat loss | Running cost | Peak summer solar gain (West, ~550 W/m², g ≈ 0.6) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fully glazed | ~1.35m² | ~1.6 | 3.32 W/K | £8.38/yr | ~445W |
| **Half-glazed (adopted)** | **~0.65m²** | **~1.3** | **2.70 W/K** | **£6.81/yr** | **~215W** |
| Solid insulated | 0 | ~1.0 | 2.08 W/K | £5.24/yr | ~0W |

**Reading:** the options differ by only ~£3/yr on heating, so the choice comes down to **summer overheating and daylight**. The half-glazed leaf cuts peak door solar gain by ~230W, which matters in a 31m³ room that already has machine heat. It still keeps a vision panel at standing eye height (mid-rail ~1080mm FFL, level with the window sills).

### 6.3 Movement-Tolerant Installation (Small Foundation Movement)

The aluminium frame is stiff and springs back. It does not absorb movement: it rides with the opening or, if fixed rigidly, gets loaded until the leaf binds, the gaskets lose compression or the mitred corner cleats open. Rigid tilting of the whole SIP wall is largely harmless, because frame and leaf tilt together. The damaging case is the opening going **out of square**.

| Measure | Specification | What it absorbs |
| :--- | :--- | :--- |
| Installation gaps | ~10mm at each jamb, **~15mm at the head**; sill fully bedded and packed on the continuous SIP sole plate | ~10mm before the frame is loaded |
| Fixings | Jamb fixings only (3 per jamb, packer behind each); **no rigid fixing through the head** (sliding or slotted restraint or head clip) | Head of the opening can move freely |
| Seals across the gap | Pre-compressed expanding foam tape (e.g., illbruck TP600); internal Pro Clima Contega SL / Tescon Profil with a **~10mm movement fold at the head**; no gun-foam-only seals | Weather and airtightness kept while moving |
| Hardware | **3D-adjustable hinges** (±2–3mm) and **adjustable lock keeps** | ~2–3mm of out-of-square, by adjustment alone |
| Monitoring | Record the opening diagonals and sill level at install; re-measure after the first winter and summer | Change ≤3mm: adjust hinges and keeps. >3mm or recurring: check ring-beam levels at the screw heads |

---

## 7. uPVC Durability in Cowes (Coastal Solent)

| Factor | Effect at Cowes | Mitigation in the spec |
| :--- | :--- | :--- |
| **Salt spray on the profile** | uPVC is non-metallic and does not react with salt. Aluminium, by contrast, depends on its powder coat staying intact. | Wash down 2× a year. |
| **Hidden steel reinforcement** | Galvanised steel in the chambers can corrode where drainage slots or cut ends are exposed. Fixed lights carry little reinforcement. | Galvanised (not bare) reinforcement; drainage slots that don't expose the steel. |
| **Hardware** | Not applicable: the fixed lights have no hardware. (The aluminium door has 316 / Grade 5 hardware.) | – |
| **UV and heat** | South- and west-facing frames degrade fastest. **Dark foils on the West** reach 60–70°C, which risks bowing and foil lift. White profiles chalk slightly but stay stable. | White, or a heat-reflective foil (e.g., Renolit Exofol with solar-reflective technology), on the West. Profiles to **BS EN 12608 Class A** (Rehau / VEKA / Deceuninck / Kömmerling class). |
| **Thermal expansion** | uPVC expands ~3× more than aluminium: a 1500mm clerestory moves ~4mm over a 40°C swing. | 10–12mm perimeter gap with expanding foam tape; fix to the profile maker's expansion guidance. |
| **Gaskets** | They harden and shrink after ~15–20 years. | **Replaceable** (not co-extruded) gaskets. |
| **Lifespan** | Good-quality uPVC: **~20–35 years**. Marine-coated aluminium: **~40+ years**. | uPVC for the six fixed lights; **aluminium for the door** (leaf width, hardware load, security). |

---

## 8. Upgrade Paths and Open Items

* **Secondary glazing (if a neighbour complains):** DIY 6mm acrylic or polycarbonate inside the 236mm reveal with a ~100mm gap adds **~8–12 dB** per clerestory, for £30–60 each.
* **Optional automatic drop seal on the door:** ~+1 dB on the West façade (door Rw 32 → 34), £80–150.
* **Door width (resolved 25 Oct 2026):** the SIP opening stays ~1000mm and the bespoke doorset is made to it. Before the SIP order, only confirm the door system gives ~800mm clear in that opening; if it can't, widen the opening and spread the difference equally across the four 481mm piers.
* **[OPEN] CAD drawings** still show the 1400mm door. Update them before the SIP order.
* **[OPEN] Zehnder Dn,e,w:** still needed to rank the dMVHR terminal against the East clerestories (MASTER_PLAN §4.2.1).

---

## 9. Cost Ballpark: Adopted Setup

**Supply only, DIY install** (per WORKPLAN Week 7). Confidence **2/5**: web benchmarks, not quotes. Validate with itemised quotes.

| Item | Basis | Ballpark |
| :--- | :--- | :--- |
| uPVC fixed clerestory 300 × 1500, standard double, white | Small bespoke unit, minimum-charge driven; fixed 1200 × 1200 supply-only benchmark £200–300 | £120–200 each |
| + D-AC acoustic lam upgrade per clerestory | 8.8mm acoustic lam pane £90–180/m², min 0.5m² charge per pane | +£45–90 each |
| **4 × clerestories** | | **£660–1,160** |
| uPVC fixed West 1000 × 1000, standard double | Supply-only benchmark | £180–280 each |
| + D-AC acoustic lam upgrade (~0.72m² glass) | as above | +£65–130 each |
| + heat-reflective foil (if not white) | ~15–25% uplift | +£30–60 each |
| **2 × West windows** | | **£490–940** |
| **Aluminium door**, single 900mm leaf, half-glazed D-STD, insulated lower panel, marine coating, 316 / Grade 5 hardware, 3D hinges (**no side panel**) | Supply-only alu singles from ~£920 (900mm) up to £3.3–4.0k (premium ranges) | **£1,200–2,500** |
| Optional automatic drop seal | Surface-mounted | £80–150 |
| Install sundries | Expanding foam tapes, Contega / Tescon Profil, packers, frame fixings for 7 openings | £250–450 |
| Delivery to the Isle of Wight | Bespoke delivery ~£70 mainland plus Solent premium | £100–300 |
| **Total, supply only** | | **≈ £2,800–5,500** (central ~£3,800) |
| *If fitted by an installer* | ~£80–150 per window, £200–400 for the door | *+£700–1,300* |

**Compared with the triple quote:** ~£10k for the windows alone (door extra) → **~£3–5.5k for windows and door**. Most of the saving comes from the uPVC frames and supply-only purchase, not from dropping the third pane.

**Sources:** [less.co.uk window costs](https://less.co.uk/home-improvements/windows/cost); [Just Value Doors stocked/bespoke windows](https://www.justvaluedoors.co.uk/stocked-windows); [trade2base window installation costs](https://www.trade2base.com/blog/window-installation-costs-uk); [8.8mm acoustic laminate cut to size](https://buyglass.co/?p=32202); [Saint-Gobain Stadip Silence](https://www.saint-gobain-glass.co.uk/stadipr-silence); [900mm aluminium single door](https://homebuilddoors.co.uk/products/900mm-white-heritage-aluminium-single-door); [Doors Direct 2U aluminium door pricing](https://doorsdirect2u.co.uk/?p=174441); [Self Build entrance door costs](https://www.self-build.co.uk/how-to-cost-an-entrance-door); [AZ-45 single-leaf door](https://www.bimobject.com/en-au/morad/product/az-45-single-leaf-door); [Wickes composite doorsets](https://www.wickes.co.uk/Door-Stop-2-Panel-1-Square-Anthracite-Grey-Left-Hand-GRP-Composite-Door---920-x-2100mm/p/311418); [REHAU coastal guidance](https://sadecor.co.za/interior-design-blog/hardware-decorative/doors/rehau-coastal-weather-is-a-test-for-windows-and-doors).

---

## 10. Self-Verification (AGENTS.md §4; `/tests` retired, run by hand)

* **Red Line:** installation position and airtight tapes are unchanged; a movement fold is added at the door head, and the narrower door opening adds solid insulated wall. **Pass.**
* **Weather-Tight:** same install week (Week 7). Expanding foam tape is the primary weather seal on every frame. D-AC units (~37 kg/m²) are lighter than triple (~47 kg/m²). **Pass.**
* **Condensation:** fRsi ≥ 0.70 with RH ≤ 60% → **Pass** (§3).
* **Sequence:** no change. **Pass.**

---

## 11. Decision History (10 Oct 2026, superseded options)

1. Triple acoustic glazing (T-AC) in marine aluminium throughout → **withdrawn on cost** (~£10k for the windows).
2. D-AC double in marine aluminium for the fixed lights, with a **1400mm asymmetric 1.5 door** (D-SAFE glass and an acoustic seal package) → door superseded.
3. Single-leaf door options considered: a 1000mm leaf in a ~1100mm opening, and a single leaf plus fixed side panel filling the 1400mm opening → **side panel rejected**; opening cut to the doorset instead.
4. Acoustic glazing in the door → **dropped** (seal-limited, faces own house).
5. Fully glazed leaf → **half-glazed** (summer solar gain).
6. 1000mm leaf → **900mm leaf** (movement tolerance; machinery access confirmed by user).
7. Aluminium fixed lights → **uPVC fixed lights** (cost, salt immunity, lower Uf).

---

## 12. IOW Glass Estimate: Thermal & Acoustic Recalculation (25 Oct 2026)

**Source:** `comms/quotes/iow-glass_windows-door.txt` (estimate, valid 14 days). **£3,450 + VAT (£4,140 inc)**, supply and delivery only. That is within the §9 ballpark (central ~£3,800). Fitting team optional at £750 + VAT/day.
**Persona:** @strategist. **Status:** MASTER_PLAN §2.7 / §7 now use **~1.5 W/m²K for every unit** (scenario B below, 26 Oct 2026) and describe the glass generically (acoustic laminated inner pane, glass Rw ≥ 39 dB). The quote itself is not yet accepted.

### 12.1 Quoted vs Adopted Specification

| Item | Adopted (§0) | IOW Glass estimate | Delta |
| :--- | :--- | :--- | :--- |
| Fixed-light frame | uPVC, BS EN 12608 Class A, galvanised reinforcement, replaceable gaskets, direct-glazed | **REHAU TOTAL70**, white/white, Class A, galvanised reinforcement, direct-glazed; gasket arrangement "to be confirmed" | Match (confirm replaceable gaskets). TOTAL70 takes glass up to 44mm. |
| Fixed-light glass | 6T / 16 Ar / **8.8** acoustic lam Low-E, 30.8mm, ~36 kg/m² | **4 Low-E / 18 (Ar "to be confirmed") / 6.8 acoustic lam**, black warm edge, 28.8mm, ~25 kg/m² | Thinner, lighter unit; argon not yet committed |
| Glass acoustic rating | Rw ≥ 39 dB (assumed 39–41), Rw+Ctr ~35 | **Rw (C;Ctr) = 39 (−2;−6) → Rw+C 37, Rw+Ctr 33** (supplier figure, no test report) | Meets the ≥ 39 floor, at its bottom; ~2 dB lower at low frequency |
| Fixed-light Uw | Clerestory ~1.5, West ~1.3 | "~1.5 or better" for all six | West units possibly +0.2 |
| Door | Thermally broken marine alu, 900mm leaf, half-glazed 4T/16Ar/4T, Ud ~1.3 | **Smart Systems** thermally broken alu, half-glazed over insulated panel, low threshold; Ud "~1.5 or better"; leaf width, glass and hardware not yet stated | +0.2 W/m²K; coastal coating spec and 316 hardware not named |
| Solar control | None (external blinds) | None | Match |

### 12.2 Thermal Recalculation

Uw per unit to BS EN ISO 10077-1: `Uw = (Ag·Ug + Af·Uf + lg·ψ) ÷ Aw`. Assumes ~65mm visible frame per side, Uf 1.3 (sensitivity 1.4), ψ 0.045 W/mK (black warm-edge spacer in uPVC). Ug: 1.1 with argon + soft-coat Low-E (ε ≤ 0.03), **1.4 if air-filled**. *Confidence 3/5: REHAU publishes no fixed-frame Uf; get the declared Uw per unit size.*

| Glass fill | Clerestory 1500 × 300 (52% glass) | West 1000 × 1000 (76% glass) |
| :--- | :--- | :--- |
| **Argon, Ug 1.1** | **1.50** (1.55 at Uf 1.4) | **1.31** (1.33) |
| Argon, Ug 1.0 (e.g., Planitherm One class) | 1.45 | 1.23 |
| **Air, Ug 1.4** | **1.66** (1.71) | **1.53** (1.56) |

So the quote's "~1.5" matches the clerestory calculation with argon. For the West units it's a blanket figure: with argon they should come out ~1.3. Without argon they don't, which is why argon has to go in the formal spec.

Whole-building effect (base: MASTER_PLAN §7.2, glazing 8.00 W/K, HTC 24.42 W/K, 1,500 HDD, SCOP 3.5, £0.245/kWh):

| Scenario | Clere / West / Door Uw | Glazing loss | Δ | HTC | Thermal demand | Heating cost | Δ cost |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Current plan | 1.5 / 1.3 / 1.3 | 8.00 W/K | – | 24.42 W/K | 879 kWh | £61.55/yr | – |
| **A. Quote, argon confirmed (calculated)** | 1.5 / 1.3 / 1.5 | **8.42 W/K** | **+0.42** | **24.84 W/K** | 894 kWh | **£62.60/yr** | **+£1.05** |
| B. Quote as written (all ~1.5) | 1.5 / 1.5 / 1.5 | 8.82 W/K | +0.82 | 25.24 W/K | 909 kWh | £63.60/yr | +£2.05 |
| C. Air-filled, door 1.5 | 1.66 / 1.53 / 1.5 | 9.17 W/K | +1.17 | 25.59 W/K | 921 kWh | £64.48/yr | +£2.95 |
| D. Air-filled, door 1.6 (worst) | 1.66 / 1.53 / 1.6 | 9.38 W/K | +1.38 | 25.80 W/K | 929 kWh | £65.01/yr | +£3.45 |

**Reading:** at worst ~£3.50/yr more heating and **~+25W** on the 1.1–1.4kW peak load (1.38 W/K × ~17K). Area-weighted opening Uw moves from 1.36 to 1.43 (A) or 1.50 (B). The heat pump sizing doesn't change.

**Condensation (§3):** Ug unchanged with argon and the same warm-edge spacer, so the check still passes at RH ≤ 60%. Air fill lowers the centre-pane surface temperature by ~1°C (~11°C at 0°C outside), still above the 8.6°C dew point at 70% RH. Frame fRsi ≥ 0.70 still has to be declared.

### 12.3 Acoustic Recalculation

Same method as §4: fitted Rw = glass Rw − 2 → **37 dB** (was 38). Wall Rw 40 dB (sensitivity 45 dB). Door stays seal-limited at Rw 32.

| Façade | Wall 40: adopted → quote | Window share | Wall 45: adopted → quote | Window share |
| :--- | :--- | :--- | :--- | :--- |
| **East** (2 clerestories) | 39.8 → **39.65 dB** (−0.15) | 13% → 16% | 43.7 → **43.4 dB** (−0.35) | 32% → 37% |
| **North / South** (1 clerestory) | 39.85 → **39.75 dB** (−0.1) | 9% → 11% | 44.1 → **43.8 dB** (−0.25) | 24% → 29% |
| **West** (2 windows + door Rw 32) | 36.75 → **36.6 dB** (−0.15) | wall / windows / door 29 / 17 / 55% | – | – |
| West, door seals poorly adjusted (Rw 30) | 35.4 dB | 22 / 13 / 66% | – | – |
| West, optional drop seal (Rw 34) | 37.6 dB | 36 / 21 / 43% | – | – |

**Readings:**
1. **Saw / planer noise (mid-high frequency, Rw / Rw+C is the right metric): −0.1 to −0.35 dB** at the neighbour façades. Inaudible (about 1 dB is the smallest change people notice; 3 dB is clearly noticeable). The clerestories remain a minority path; the wall still dominates.
2. **Low-frequency noise (dust extractor and motor hum; Rw+Ctr):** glass Rw+Ctr 33 vs ~35. The lighter unit (25 vs 36 kg/m²) moves the mass-air-mass resonance from ~160 Hz to ~180 Hz. At the façade this is still only ~−0.3 dB, because the EPS SIP wall is weak at low frequency too. Low-frequency hum is handled by machine isolation (§3.2) and keeping the extractor away from the N/S/E walls, not by glass.
3. **West:** the door is still the dominant path (55%). Ask for the Smart Systems door's tested Rw or its seal arrangement, and keep the drop-seal option open. The low threshold is the weakest seal line.
4. **The Rw 39 (−2;−6) is a supplier figure for this build-up, with no test report.** A 4/16/6 acoustic unit is commonly listed at the same 39 (−2;−6), so the figure is plausible. Ask for the glass maker's datasheet (Pilkington Optiphon / Saint-Gobain Stadip Silence) for 4/18/6.8.
5. **Secondary glazing upgrade path (§8) unchanged**: +8–12 dB per clerestory if a neighbour complains.

**Side effect (handling):** a West 1000 × 1000 unit's glass drops from ~27kg to ~19kg, so DIY glazing is easier (WORKPLAN Week 7).

### 12.4 Verdict & What to Pin Down in the Formal Quote

**Verdict:** accept the glass and frame spec in principle. Thermally it costs ≤ £3.50/yr and acoustically ≤ 0.35 dB, both negligible against the §9 saving and well inside the "Rw ≥ 39" requirement in MASTER_PLAN §2.7. To stop scenario C/D happening, these go in the formal quote:

1. **Argon fill (≥ 90%) committed**, not "to be confirmed", plus **soft-coat Low-E** (ε ≤ 0.03; declared Ug ≤ 1.1).
2. **Declared Uw per unit size** (1500 × 300 and 1000 × 1000) and the door's whole-unit Ud; **frame fRsi ≥ 0.70**.
3. **Glass datasheet / test report** for the 4/18/6.8 Rw 39 (−2;−6).
4. **Replaceable (not co-extruded) gaskets** confirmed (§7).
5. **Door:** system name (e.g., Alitherm range), frame made to the ~1000mm SIP opening after the SIP drawings are confirmed; **before the SIP order, only confirm the system gives ~800mm clear in that opening** (§8), vision-panel glass (4T/16Ar/4T Low-E or better), **coastal finish spec** (Qualicoat Seaside or equivalent marine pretreatment), **316 / BS EN 1670 Grade 5 hardware**, 3D-adjustable hinges, multi-point lock, threshold seal detail at the +40mm FFL, and the drop-seal option price.
6. **Sizes = structural opening minus fitting gaps.** The estimate lists the windows at the nominal SIP opening sizes (1500 × 300, 1000 × 1000), which leaves no installation gap. Order the frames ~20mm smaller than the confirmed SIP openings (e.g., ~1480 × 280, ~980 × 980). On a 300mm clerestory that costs ~20mm of visible glass; the alternative is cutting the clerestory openings 20mm taller (head zone 179.7 → ~160mm, still above the ~80–90mm minimum).
7. **Cills / drainage** (excluded, priced separately): agree the detail before ordering. It is not a thermal or acoustic issue, but it affects the head-of-cladding weathering at every opening.

**If adopted:** MASTER_PLAN §2.7 (D-AC → 4/18Ar/6.8 acoustic lam, glass Rw 39 (−2;−6), Ud ~1.5), §7.1 (area-weighted ~1.43) and §7.2 (glazing 8.42 W/K, HTC 24.84 W/K, 894 kWh, ~£62.60/yr, scenario A) need updating. The WORKPLAN only changes if IOW Glass fits.

**Sources:** quote above; [REHAU TOTAL70 brochure](https://www.rehau.com/downloads/419572/rehau-total70-brochure.pdf) (glass up to 44mm); [Copeland planning doc, REHAU TOTAL70 Uw calc](https://www.copeland.gov.uk/sites/default/files/planning-applications/energy_efficient_windows_millom_u_value.pdf) (1.34 W/m²K, 4/20Ar/4 casement); [BuildHub acoustic DGU thread](https://forum.buildhub.org.uk/topic/42967-acoustic-double-glazing-units) (4/18/6.8 offer; 4/16/6 listed at 39 (−2;−6)); [Smart Systems Alitherm 400 doors (NBS)](https://source.thenbs.com/product/alitherm-400-doors/siQKUbhtnW7nGc5gEFveHF/h6QFf14DcUFFGGMkSr5tPH); [Smart Visoglide Plus (NBL)](https://www.nationalbimlibrary.com/en/smart-systems-ltd/visoglide-plus-patio-doors/?lo=en) (alu systems ~1.5–1.6 W/m²K).
