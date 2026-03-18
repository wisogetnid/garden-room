# The SOP Fidelity & Linter Check
**Type:** Document Formatting / Data Completeness
**Target Agent:** `@general` or `@architect`

## Objective
Verify that all `MASTER_PLAN_*.md` blueprints strictly adhere to the project's formatting conventions, ensuring no variable is left undefined, and that the text is an actionable, high-fidelity Standard Operating Procedure.

## Verification Checklist

### 1. Markdown Table Integrity
- [ ] Do all material specification tables contain exactly these five columns: `| Material Name | Dimensions / Gauge | Fixing Method | Purpose | Estimated Quantity |`?
- [ ] Are all cells within the `Estimated Quantity` column fully populated with realistic approximations (e.g., `~20m²`, `~16 units`, `1 Roll`)? **No empty cells or 'TBD' permitted.**

### 2. Metric Construction Units
- [ ] Are all dimensions strictly expressed in millimeters (mm) for timber, insulation, and piping (e.g., `100mm`, not `10cm` or `4 inches`)?
- [ ] Are all areas expressed in square meters (m²)?
- [ ] Are all thermal performances expressed in Watts per square meter Kelvin (W/m²K)?

### 3. Chronological Phasing
- [ ] Does the `MASTER_PLAN` include a dedicated "Step-by-Step Construction Phases" section at the top?
- [ ] Are these phases numbered chronologically (e.g., `Phase 1: Groundworks & Foundation`, `Phase 2: Drainage & Threshold`)?
- [ ] Do the phases directly correlate with the logistical weekends established in the `WORKPLAN`?

## Failure States (Do Not Pass If:)
- The material tables list "16mm PEX-a Wet UFH Pipework" but the Quantity column is blank.
- The blueprint uses imperial measurements (e.g., "4x2 framing") instead of the exact metric equivalent (e.g., "47x97mm").
- The Master Plan lacks a clear, sequential step-by-step summary.
