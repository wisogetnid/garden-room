# Research: Glazing & Automation (2026 Trends)

## Executive Summary
For a DIY garden workshop aiming for Passivhaus standards in Cowes, UK (North/North-East facing), **Vacuum Insulated Glazing (VIG)** offers the best balance of thermal performance and manageability (weight/thickness). While **Smart Glass** is evolving, its cost-benefit for a North-facing workshop is low compared to high-performance Low-E coatings. **Integrated Blinds** with Matter support are highly recommended for dust control in a woodworking environment.

---

## 1. High-Spec Glazing: VIG vs. Triple Glazing

### Vacuum Insulated Glazing (VIG) - The 2026 "Game Changer"
*   **Technology:** Two panes of glass separated by a vacuum gap (0.1-0.3mm), kept apart by micro-spacers.
*   **Performance (U-Value):** 0.4 - 0.7 W/m²K (Center pane). Comparable to or better than triple glazing.
*   **Thickness:** Extremely thin (6mm - 10mm total).
*   **Weight:** ~20kg/m² (Similar to single/double glazing).
*   **DIY Implications:** 
    *   **Handling:** significantly lighter than triple glazing, making it feasible for a solo builder.
    *   **Framing:** Requires less depth in timber frames (standard 50-70mm rebates are fine), reducing timber costs and thermal bridging.
*   **Cost:** Higher upfront (~£300-£500/m²), but offset by savings in structural timber and ease of installation.

### Triple Glazing - The Standard Approach
*   **Technology:** Three panes with two gas-filled cavities (Argon/Krypton).
*   **Performance (U-Value):** 0.5 - 0.8 W/m²K.
*   **Thickness:** Bulky (36mm - 44mm typical).
*   **Weight:** ~30kg - 45kg/m² (Heavy!).
*   **DIY Implications:** 
    *   **Handling:** Dangerous for a solo builder to install large units (e.g., patio doors). Requires heavy-duty lifting gear or multiple helpers.
    *   **Framing:** Requires deep rebates and stronger lintels/headers to support the weight.
*   **Cost:** Moderate (~£150-£250/m²).

### Recommendation
**Go with Hybrid VIG (VIG + 1 Low-E pane).**
This combination offers U-values as low as 0.3 W/m²K, remains lighter than triple glazing, and fits standard profiles. For a DIY build with limited access (wheelbarrow only), the weight reduction of VIG is critical.

---

## 2. Smart Glass Trends (2026)

*   **Electrochromic (Dynamic Tinting):** 
    *   *Examples:* Halio, SageGlass.
    *   *Function:* Tints on demand to block glare/heat.
    *   *Pros:* Eliminates blinds, perfect solar control.
    *   *Cons:* Very expensive, complex wiring, slow transition times (though improving).
    *   *Relevance:* Low for North/NE facing. Glare is less of an issue than heat retention.
*   **PDLC (Privacy Glass):**
    *   *Function:* Switches from opaque to transparent.
    *   *Relevance:* Good for privacy from neighbours (West/South), but doesn't offer significant thermal benefits.

---

## 3. Matter-Compatible Motorized Blinds

For a workshop, dust is the enemy. **Integrated Blinds (Between Glass)** are the gold standard.

### Integrated Systems (Sealed Unit)
*   **ScreenLine (Pellini):** Market leader. Magnetic transmission (no holes in glass).
*   **Control:**
    *   *Wired:* 24V motor inside the headrail. Connect to a Matter-compatible relay (e.g., **Shelly Plus 2PM** flashed with Matter firmware or via Home Assistant).
    *   *Solar/Battery:* Rechargeable battery on the frame.
*   **Matter Integration:** 
    *   Use a **Bond Bridge Pro** or **Somfy TaHoma Switch** (Matter bridge) to expose RF blinds to Apple Home/Google Home.
    *   **Eve MotionBlinds** (Thread/Matter) are available as retrofit motors for roller blinds, but less common for *integrated* slats.

### Recommendation
Prioritize **ScreenLine C-System (Wired Motor)** integrated blinds.
*   **Why:** No dust on slats.
*   **Automation:** Wire to a Shelly relay or similar smart switch that supports Matter. This is robust, hardwired (no batteries to charge), and future-proof.

---

## 4. Solar Reflective Coatings (G-Value)

### The Physics
*   **G-Value:** The percentage of solar heat that enters the room (0.0 - 1.0).
*   **Low-E (Emissivity):** Keeps internal heat IN (Winter priority).

### Analysis for Cowes Garden Room
*   **Orientation:** North / North-East.
*   **Solar Gain:** Limited. The "Greenhouse Effect" is less of a risk than in South-facing rooms.
*   **Strategy:**
    *   **DO NOT** use high solar control glass (low g-value like 0.2-0.3) on North windows. You *want* the free solar gain on the few days you get it.
    *   **DO** use high-performance **Soft-Coat Low-E (Planitherm One or similar)**. This reflects ~96% of internal heat back into the room.
    *   **West Facing (Neighbours):** If there are high-level windows, use privacy glass or standard Low-E. Solar gain here is late evening (summer only).

### Cost-Benefit
*   **Solar Control Glass:** Adds ~15-20% to cost.
*   **Benefit:** Negative for North facing (losses free heat).
*   **Verdict:** Skip solar control. Invest in the lowest possible U-value (VIG) instead.

---

## Summary of Recommendations for Master Plan

1.  **Glazing:** Hybrid VIG (Vacuum + Low-E).
    *   *Target U-value:* < 0.5 W/m²K.
    *   *Reason:* Weight saving for DIY installation, superior thermal performance.
2.  **Blinds:** Integrated Magnetic Blinds (ScreenLine).
    *   *Automation:* Hardwired 24V motors controlled via Matter-compatible relays (Shelly/Eve).
    *   *Reason:* Dust-free, zero maintenance.
3.  **Coatings:** High-performance Low-E (e.g., Saint-Gobain Planitherm One).
    *   *Reason:* Maximize heat retention. Avoid solar control coatings on North face.
