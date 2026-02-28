# Dust Extraction Physics & Strategy: Deep Research

## 1. Executive Summary
For a 50m³ Passivehaus-standard garden workshop in the UK, **venting dust extraction outside is thermally non-viable**. A "High Volume, Low Pressure" (HVLP) cyclone system with M-Class filtration or a specific "High Pressure" CamVac style system is required to recycle air safely.

## 2. The Physics of Air Movement

### 2.1. CFM vs. Static Pressure (SP)
Effective dust collection requires two things:
1.  **Air Speed (Velocity):** To keep chips entrained in the air stream.
    *   **Vertical Runs:** > 4000 FPM (Feet Per Minute).
    *   **Horizontal Runs:** > 3000 FPM.
2.  **Air Volume (CFM):** To capture fine invisible dust at the source.
    *   **Target:** 1000 CFM at the tool hood for fine dust capture (Bill Pentz Standard).
    *   **Reality for 100mm Ducts:** A 100mm (4") duct restricts max flow to ~400 CFM at standard pressures. This is sufficient for "Chip Collection" but marginally effective for "Fine Dust Health Safety".

### 2.2. The 100mm (4") Duct Limitation
*   **Area:** $0.087 \text{ ft}^2$.
*   **Max Flow:** To maintain 4500 FPM (very high speed), flow is only $390 \text{ CFM}$.
*   **Friction Loss:** 100mm duct has high static pressure resistance.
    *   5m run + 2 elbows + 2m flex hose $\approx$ 3-4" WG (Water Gauge) Static Pressure loss.
*   **Implication:** Standard 1HP-2HP "Chip Extractors" (HVLP) cannot pull 1000 CFM through a 100mm pipe. They will stall, airflow drops to <300 CFM, and ducts clog.

## 3. System Types: Cyclone vs. Bag vs. CamVac (UK Specific)

| Feature | Single Stage (Bag) | Two-Stage Cyclone | CamVac (Twin/Triple Motor) |
| :--- | :--- | :--- | :--- |
| **Physics** | Impeller passes chips. Bag filters. | Impeller is post-separation. Cyclone separates. | High Vacuum motors (like shop vacs). |
| **Pressure** | Low Static Pressure (<5" WG). | Medium Static Pressure (8-12" WG). | **High Static Pressure** (>20" WG). |
| **Filtration** | Poor (Standard bags pass <5 microns). | Excellent (HEPA Cartridges). | Excellent (3-stage filtration usually std). |
| **100mm Suitability** | **Poor.** Stalls easily. | **Medium.** Needs 150mm ducting to work well. | **High.** Designed for 100mm ducts. |
| **Noise** | Low (Induction motor). | Medium/High. | High (Brush motors scream). |

**Recommendation:**
*   **Option A (Best Air Quality):** 3HP Cyclone (e.g., Axminster / Harvey) with **150mm (6") ducting** reduced to 100mm only at the tool.
*   **Option B (Best for 100mm Ducting):** CamVac (Twin or Triple motor) style. These generate enough vacuum to pull hard through 100mm pipes, making them ideal for small retrofit pipe runs, though louder.

## 4. Thermal Analysis: Venting vs. Recycling

For a Passivehaus workshop, energy conservation is paramount.

**Calculation: Heat Loss from Venting**
*   **Flow Rate:** 600 CFM ($\approx 0.283 \text{ m}^3/\text{s}$).
*   **Scenario:** Winter ($0^\circ\text{C}$ outside, $18^\circ\text{C}$ inside).
*   **Heat Loss ($P$):**
    $$P = \dot{m} \cdot C_p \cdot \Delta T$$
    $$P = (0.283 \times 1.2 \text{ kg/m}^3) \cdot 1.006 \text{ kJ/kgK} \cdot 18\text{ K}$$
    $$P \approx 6.15 \text{ kW}$$

**Conclusion:** Venting extraction outside sucks **~6kW of heat** out of the room continuously. This would drain a standard home battery in < 2 hours and make heating impossible. **Recycling air with M-Class/HEPA filtration is mandatory.**

## 5. Ducting & Static Electricity

### 5.1. The "Explosion Myth"
*   **Risk:** Sawdust explosions require a concentration of dust in the air ($>30 \text{ g/m}^3$) usually only found inside industrial silos.
*   **Reality:** In a 100mm home workshop system, reaching the Lower Explosive Limit (LEL) is statistically impossible during normal operation.
*   **Real Danger:** Static shocks causing operator surprise/reaction, and dust clinging to the outside of pipes.

### 5.2. Ducting Materials
*   **PVC (Soil Pipe):** Cheap, smooth bore (low friction). High static generation.
    *   *Mitigation:* Run a bare copper wire inside the duct, grounded at the extractor end.
*   **Spiral Galvanized:** Expensive, self-grounding, professional look.
*   **Flex Hose:** **AVOID** as much as possible. High friction (3x resistance of smooth pipe). Use only for final <1m connection.

## 6. Ambient Air Cleaning (The "Polisher")

Even with 99% capture at source, fine dust escapes.
*   **Volume:** $50 \text{ m}^3$.
*   **Target:** 10 Air Changes Per Hour (ACH).
*   **Required CFM:** $(50 \times 10) / 60 \text{ min} \approx 8.3 \text{ m}^3/\text{min} \approx 295 \text{ CFM}$.
*   **Market Units:**
    *   **Record Power AC400:** Rated ~400 CFM. Perfect size.
    *   **Jet AFS-500:** Rated ~500 CFM. Good alternative.
*   **Placement:** Ceiling mounted, 1/3 distance from a wall, to create a toroidal airflow (Coanda effect) that scrubs the whole room.

## 7. Strategic Recommendations for this Build

1.  **Primary Extraction:** Since 100mm ducting is a hard constraint (5m run), a **High-Pressure Vacuum System** (like a CamVac CGV386 or similar Twin-Motor unit) is technically superior to a standard chip collector. It will maintain airflow through the narrow pipe better.
    *   *Alternative:* If space allows 150mm ducting, a 2HP+ Cyclone is quieter and superior.
2.  **Filtration:** Ensure the unit has **HEPA / M-Class** rated filters to safely recycle air.
3.  **Heat Preservation:** Do not install external vents.
4.  **Ambient Unit:** Install a ceiling-mounted unit (e.g., AC400) on a timer to run for 1 hour after work stops.
