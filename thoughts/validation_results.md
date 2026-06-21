# Gap Report & Validation Status

**Date:** 2026-06-20
**Event:** Dry Moat Strategy Integration & Validation
**Status:** **FAILED (CRITICAL CONFLICTS IDENTIFIED)**

## Overview
A full validation run was executed against the updated `MASTER_PLAN.md` and `WORKPLAN.md`. While the new "Dry Moat Strategy" achieves the goal of respecting the 2.5m Permitted Development limit while maximizing internal headroom (allowing a 2100mm datum), it inherently conflicts with multiple explicit constraints in the `/tests` folder. 

## Test Suite Results

### 1. Test 001 (Foundation Strategy) & PD Limits: FAIL (Conflict)
*   *Requirement:* `001_foundation_strategy.md` explicitly requires the 150mm concrete slab to sit elevated above ground level to create a strict 150mm splash zone for the timber frame.
*   *Conflict:* The `MASTER_PLAN.md` sinks the slab an additional 150mm (flush with the garden lawn) using the "Dry Moat Strategy" to stay under the 2.5m Permitted Development (PD) limit. 
*   *Result:* PD compliance is achieved, but the Foundation test fails due to the loss of the elevated splash zone. The dry moat replaces it, but the test must be formally updated if this trade-off is accepted.

### 2. Test 01 ('Red Line' Thermal Continuity): FAIL
*   *Requirement:* The external wall insulation must seamlessly meet the foundation perimeter insulation, and the timber sole plate must be replaced by a thermally broken material (e.g., Compacfoam CF200).
*   *Conflict:* The `MASTER_PLAN.md` specifies Compacfoam *only* for the Door Threshold Bearing. The remainder of the 150mm New Forest SIP wall sits on a "Pre-Machined Timber Sole Plate" which bears directly on the concrete slab, separated only by DPC/DPM. This creates a linear thermal bridge along the entire perimeter, bypassing the external wall insulation.

### 3. Test 02 ('Weather-Tight' Sequence): FAIL
*   *Requirement:* The logistical sequence MUST mandate immediate application of a breather membrane (Tyvek) on the same day the OSB SIP panels are erected. (Zero-Delay Protocol).
*   *Conflict:* The `WORKPLAN.md` explicitly states the OSB SIPs are erected on Weekend 8 but left naked and protected only by "massive heavy-duty tarps" until Weekend 11, when the Tyvek is finally applied. This violates the Failure State: "instructs the builder to leave naked OSB SIPs exposed for an entire week while waiting for breather membranes."

## Conclusion & Next Steps
The plans currently fail the Red Line continuity and the Weather-Tight sequence constraints. The Dry Moat Strategy succeeds in complying with the PD limit but breaks the existing Foundation Strategy test. 

**Required Actions:**
1. Update `MASTER_PLAN.md` to run Compacfoam (or equivalent structural thermal break) continuously around the entire perimeter sole plate, not just the doorway.
2. Adjust `WORKPLAN.md` to bring the Tyvek wrapping forward to Weekend 8 (immediately following panel erection) instead of Weekend 11.
3. Either update `tests/001_foundation_strategy.md` to officially accept the Dry Moat trade-off in place of the elevated splash zone, or redesign the roof to accommodate the original 150mm splash block while maintaining the 2.5m PD limit.