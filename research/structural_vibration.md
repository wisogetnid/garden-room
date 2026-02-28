# Structural Rigidity & Vibration Damping Research

## 1. Executive Summary
This research focuses on optimizing the floor structure for a 4m x 5m garden workshop in Cowes, UK. The goal is to achieve high stiffness (low deflection) for hand tools and potential machinery, effective vibration damping, and Passivehaus-level thermal performance, all while adhering to the constraint of manual material handling via a narrow access path.

## 2. Floor Structure: Solid Joists vs. Engineered I-Joists
### Comparison for 4m Span
| Feature | Solid Timber (C24 47x195mm) | Engineered I-Joist (e.g., Steico/James Hardie, ~240mm depth) |
| :--- | :--- | :--- |
| **Span Capability** | Limits of domestic span at 400mm centers. Likely requires doubling or 300mm centers for workshop stiffness. | Easily spans 4m+ with high stiffness (deflection < L/500). |
| **Weight** | ~5-6 kg/m. Heavy to carry manually over distance. | ~3-3.5 kg/m. Lightweight, easily handled by one person. |
| **Straightness** | Prone to bowing, twisting, and cupping. | Engineered straight and dimensionally stable. |
| **Thermal Bridging** | Significant (solid wood conducts heat). | Minimal (thin 6-9mm hardboard web). Ideal for Passivehaus. |
| **Service Integration** | Drilling holes is limited and weakens the joist. | Pre-punched knockouts or easy-to-cut webs for ducting/cables. |

### Analysis
For a "Passivehaus" ambition, thermal bridging is a critical failure point. Solid joists act as thermal bridges. I-Joists reduce this by ~80% through the web.
*   **Deflection:** A 4m span is the upper limit for standard 195mm solid joists if "workshop stiffness" is desired. I-Joists (220mm-240mm deep) offer superior rigidity.
*   **Access:** Carrying 20+ solid joists (5m long) down a narrow path is exhausting. I-Joists are significantly lighter.

**Recommendation:** **Engineered I-Joists (220mm or 240mm depth) at 400mm centers.**
*   *Confidence:* 5 (Standard for high-performance timber/Passivehaus).
*   *Source:* [Steico Joist Technical Manual](https://www.steico.com/en/products/construction-elements/steicojoist)

## 3. Floor Decking & Torsion Box Construction
A "Torsion Box" creates extreme rigidity by bonding skins to a core grid.
*   **Application:** Instead of building a complex custom grid, use the I-Joist floor as a torsion box.
*   **Method:**
    1.  **Top Skin:** 22mm P5 Chipboard (or 18mm Ply + 18mm Sacrificial layer), glued and screwed to joist flanges.
    2.  **Bottom Skin:** 9mm OSB or similar racking board, glued and screwed to the *bottom* of the I-joists (before insulation, or supporting insulation).
*   **Result:** This "stressed skin" design turns the entire floor assembly into a rigid beam, significantly reducing bounce without complex joinery.

## 4. Vibration Control (Machinery & Hand Tools)
Vibration in timber floors creates noise and interferes with precision work.
*   **Solution:** Decoupling.
*   **Material:** **Sylomer** (by Getzner) is the industrial standard for vibration isolation pads.
    *   *Usage:* Place pads under the feet of heavy benches or machines (lathes, bandsaws).
    *   *Selection:* Match the pad density (Color code: Yellow, Orange, Blue) to the weight of the machine to ensure the correct static load range.
    *   *DIY Alternative:* High-density rubber gym mats (horse stall mats) offer decent damping for general use but lack the specific frequency tuning of Sylomer.
*   *Confidence:* 5 (Industrial Engineering Standard).
*   *Source:* [Getzner Sylomer Technical Data](https://www.getzner.com/en/products/sylomer)

## 5. The "Floating Hearth" (Concrete Pad)
**Question:** Should a 100mm reinforced concrete pad be cast for heavy machinery?
**Analysis:**
*   **Cons:**
    *   **Thermal Bridge:** A concrete slab penetrating the insulated floor is a massive thermal leak, violating Passivehaus principles.
    *   **Logistics:** Mixing ~0.5m³ of concrete (approx 1.2 tonnes) by hand and wheelbarrowing it 30m is feasible but arduous and messy.
    *   **Permanence:** Hard to remove/change layout later.
*   **Pros:** High mass absorbs vibration.

**Recommendation:** **Do NOT cast in-situ concrete.**
*   **Better Alternative:** Create a modular "floating mass" on top of the finished floor.
    *   Layer 1: Rubber damping mat (10-20mm).
    *   Layer 2: Concrete paving slabs (50mm) or thick steel plate.
    *   Layer 3: Machine base.
*   This provides the necessary mass for damping without compromising the thermal envelope or structural timber integration.

## 6. Access Constraints Review
*   **Wheelbarrow Width:** 
    *   I-Joists fit easily.
    *   Sheet materials (1.2m wide) may need to be carried vertically or on a dolly.
    *   Concrete aggregate/sand would require 20-30 wheelbarrow trips per cubic meter. Dry construction is highly preferred.

## Summary of Recommendations for Master Plan
1.  **Floor System:** 240mm Engineered I-Joists @ 400mm centers.
2.  **Insulation:** Blown cellulose or wood fiber batts between I-joists (perfect fit, hygroscopic).
3.  **Deck:** 22mm P5 Chipboard (Glued & Screwed) + Sacrificial Hardboard/OSB layer.
4.  **Vibration:** Sylomer pads for specific machines; Horse stall mats for general standing areas.
5.  **No Wet Concrete:** Use dry mass (pavers/steel) for damping if required.
