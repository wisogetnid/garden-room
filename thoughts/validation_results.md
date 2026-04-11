# Test Validation Results - Garden Room Project

**Agent:** @strategist
**Date:** Current
**Target Document:** `plans/MASTER_PLAN.md`
**Active Tests:** Complete Suite (`tests/*`)

## Executive Summary
I have run the validation suite against `plans/MASTER_PLAN.md` (v1.1) and cross-referenced all constraints from the `/tests` directory and `thoughts/decisions_log.md`. 

The current master plan is highly detailed but **FAILS** several strict compliance, structural, and linter tests. **Immediate rollbacks or amendments to the Master Plan are required** before we can safely proceed to generating the Workplan.

## 1. Critical Failures (Requires Immediate Amendment)

### 🔴 FAIL: ATEX Dust Extraction Physics (Test 04)
* **Gap:** Section 5.1 specifies 100mm Rigid Galvanized Steel Ducting but completely omits the explicit instruction for an electrician to install and sign off on a **Copper Earth Bonding Strap**.
* **Risk:** High-velocity wood dust travelling through metal creates massive static charge. Without the copper strap, this poses an ATEX explosive risk.

### 🔴 FAIL: Flush Threshold Moisture Defense (Test 05)
* **Gap:** While the Compacfoam CF200 is correctly specified for the doorway threshold, the plan lacks two critical capillary defense mechanisms:
    1. It does not specify an **Aco HexDrain** (or linear channel drain) directly flush against the rendered foundation upstand at the doorway.
    2. It does not specify a liquid-applied **Waterproof Membrane (e.g., RIW Flexiseal)** painted over the XPS upstand and lapping up the Compacfoam block.
* **Risk:** Coastal wind-driven rain can pool at the flush patio threshold and wick into the timber framework.

### 🔴 FAIL: SOP Fidelity & Linter Check (Test 06)
* **Gap:** The document completely lacks a dedicated **"Step-by-Step Construction Phases"** section at the top. 
* **Risk:** The Master Plan must include a chronological, numbered step-by-step summary that correlates with the logistical weekends for the Workplan to ingest.

### 🔴 FAIL: Construction Timeline & Curing Physics (Test 007 / Test 03)
* **Gap:** The Master Plan does not have a timeline or scheduling section that explicitly mandates a concrete curing halt.
* **Risk:** We must explicitly state the requirement to allow the concrete to cure before heavy point loads (like lifting the SIP walls) are applied.

## 2. Structural & Thermal Challenge (U-Value Risk)
**Issue:** Section 7 correctly flags that the 150mm JACKODUR Atlas XPS yields a U-value of **0.22 W/m²K**, which misses the overarching Passivhaus target of **≤ 0.15 W/m²K**.

**Strategic Challenge to User:** 
We have a conflict in our logic. Test 001 explicitly caps the foundation XPS base at 150mm, but Passivhaus demands <0.15 W/m²K (which requires ~260mm XPS).
*   **Option A (Prioritize Thermal):** Upgrade the XPS to 260mm. This will require a much deeper excavation (460mm instead of 350mm) and significantly more spoil removal via skip.
*   **Option B (Prioritize Logistics):** Accept the 0.22 W/m²K slab performance as a deliberate compromise. Since we use a heated thermal mass, the slight efficiency loss is offset by the cheap running costs of the ASHP.

**Recommendation:** We cannot hand this off to the Foreman until the Architect resolves these missing specifications and you make a decision on the XPS thickness tradeoff.
## Date: 2026-04-11
**Strategist Notes: Validation of Internal Electric Flow Boiler Pivot**
- Re-ran validation suite against `MASTER_PLAN.md` following the pivot to a 3kW Internal Electric Flow Boiler.
- **Test 005 (Heating/Flooring):** PASS. 
  - The 3kW Electric Flow Boiler provides more than enough capacity to meet the 1.3kW - 1.8kW peak heating load. 
  - While the COP drops to 1.0, the total 280 kWh/year energy demand is well within the acceptable running cost threshold for an outbuilding.
  - The major benefit of achieving absolute zero envelope penetrations completely mitigates Passivhaus Q50 airtightness risks associated with external ASHP refrigerant lines.
- **Overall Verdict:** PASS. The Master Plan remains structurally and logically sound, and airtightness integrity is vastly improved.
