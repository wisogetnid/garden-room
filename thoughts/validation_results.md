# Validation Results: Master Plan vs Tests
**Run Date:** 2026-08-22
**Agent:** @strategist
**Blueprint Version:** `MASTER_PLAN.md` (v1.1 - SIPs Structural Execution)

## Executive Summary
The current `MASTER_PLAN.md` represents a significant architectural pivot—moving from an insulated concrete raft to a ground-screw suspended timber floor, and from an electric flow boiler (UFH) to an Air-to-Air Heat Pump (ASHP). As a result of these major design evolution changes, multiple tests are currently failing. 

The Strategist flags these architectural gaps for review: either the underlying textual tests must be formally updated/retired to align with newly authorized trade-offs, or the `MASTER_PLAN.md` requires revisions to adhere to the strict project constraints.

## Gap Report & Test Failures

### 1. Foundation & Moisture Detailing (Tests 001, 01, 03, 05) - **[FAIL]**
* **Concrete vs Timber:** Test 001 and Test 03 explicitly require an Insulated Concrete Raft (150mm slab in a 390mm pit) with a Compacfoam splash block and strict concrete curing timelines. The Master Plan violates this by specifying a zero-concrete Ground Screw foundation with a suspended timber/PIR floor.
* **Rot Risk at Threshold:** Test 01 (Thermal Red Line) and Test 05 (Flush Threshold Moisture) mandate a Compacfoam CF200 sole plate/submarine layer to prevent capillary wicking and thermal bridging. The Master Plan specifies a 47x150mm C24 timber sole plate and a C24 timber riser block at the door threshold, directly triggering a failure state for rot risk at the flush patio transition.

### 2. Heating System (Test 005) - **[FAIL]**
* **UFH vs ASHP:** Test 005 strictly mandates an Internal Electric Flow Boiler for Underfloor Heating (UFH) within a concrete slab. The Master Plan abandons this constraint, specifying a 2.5kW Air-to-Air Heat Pump (Mini-Split AC) instead.

### 3. Door Access Strategy (Test 004) - **[FAIL]**
* **French Doors:** Test 004 dictates that "French Doors are strictly eliminated due to acoustic and airtightness failures." However, Section 2.7 of the Master Plan conditionally permits a high-performance French Door, violating the strict prohibition.

### 4. Dust Extraction & ATEX Fire Safety (Tests 006, 04) - **[FAIL]**
* **Ducting & Grounding:** Tests 006 and 04 (Boundary Fire Safety) require a fixed dust extraction system utilizing Rigid Galvanized Steel Ducting and a Copper Earth Bonding Strap to prevent explosive static electricity (ATEX compliance). The Master Plan ignores this requirement, explicitly stating "No fixed ducting network required" and substituting a standalone extractor without grounded ducting.

### 5. Weather-Tight Sequence Conflict (Test 02) - **[FAIL]**
* **Vapour vs Rain Protection:** Test 02 mandates a "Zero-Delay Protocol" to apply the Tyvek breather membrane immediately to the OSB SIPs to prevent coastal moisture damage. The Master Plan intentionally contradicts this instruction (Section 2.3), warning that applying Tyvek before the external wood fibre will create a moisture trap (vapour dam). This creates an irreconcilable conflict between logistical rain protection and building physics.

## Passed Tests

* **Test 002 (Roof Structure) - [PASS]:** The plan uses a warm roof SIP methodology and strictly complies with the ≤ 2.5m Permitted Development height limit (Peak height is specified at 2480mm on the high side).
* **Test 003 (Wall Build-up & Vapour) - [PASS]:** Continuous insulation (60mm Wood Fibre over 150mm SIP) is specified, alongside meticulously taped internal VCL (Tescon Vana).
* **Test 06 (SOP Fidelity Linter) - [PASS]:** Document formatting is excellent. Markdown tables follow the precise 5-column requirement, material quantities are robustly populated without empty cells, metric units are strictly used, and clear chronological construction phasing is outlined.

## High-Impact Questions & Next Steps
To resolve these failures, decisions must be made:

1. **The Foundation Pivot:** Was the shift to ground screws intentional to bypass the logistical nightmare of a concrete pour? If yes, I will update Tests 001, 03, and 005. 
2. **The Sole Plate Danger:** The use of C24 timber at the threshold (instead of Compacfoam) introduces a significant rot risk and thermal bridge. **Recommendation:** Instruct the Architect to immediately update the `MASTER_PLAN.md` to swap the C24 base plates for Compacfoam CF200.
3. **The Membrane Catch-22:** How do we protect the OSB SIPs from sudden coastal rain without creating a vapour trap behind the wood fibre? **Recommendation:** Instruct the Foreman to use heavy-duty emergency tarps during erection until the Wood Fibre and Tyvek are applied sequentially. Update Test 02 to reflect this new SOP.
4. **Door & Dust Compliance:** Remove the French Door allowance from the Master Plan and confirm whether we are officially dropping the fixed galvanized ATEX ducting in favor of a standalone unit. 
