# Workshop Electrical Systems Research

**Date:** 2026-02-28
**Topic:** Workshop Electrical Systems, Motor Loads, Sub-Main Feed, Safety Systems
**Status:** DRAFT

## 1. Regulatory Framework: BS 7671 (The Wiring Regulations)

The electrical installation must comply with **BS 7671:2018+A2:2022** (Requirements for Electrical Installations, IET Wiring Regulations 18th Edition). While a 2026 update is anticipated (potential 19th Edition or Amendment 3), the core principles for safety and workshop environments remain robust.

Key considerations for a garden workshop include:
- **Part P (Building Regulations):** Notification to building control is required for new circuits or a new consumer unit in a garden building.
- **Section 705 (Agricultural and Horticultural Premises):** While not strictly agricultural, the outdoor nature and potential for livestock/damp environments in some garden contexts make these relevant (e.g., RCD protection).
- **Chapter 41 (Protection against Electric Shock):** 30mA RCD protection is mandatory for socket outlets <32A.
- **Chapter 42 (Protection against Thermal Effects):** Prevention of fire, particularly relevant in a wood workshop with combustible dust.

## 2. Induction Motor Characteristics & Circuit Protection

### The Problem: Inrush Current
A 3HP (2.2kW) single-phase induction motor has specific starting characteristics:
- **Full Load Current (FLC):** Approx. 13A - 14A at 230V.
- **Locked Rotor Current (LRC/Inrush):** Typically 6 to 8 times FLC.
  - Calculation: 13A * 8 = **104A**.
- **Duration:** This surge lasts for a few cycles to a few seconds depending on the inertia of the load (e.g., a heavy cast iron table saw blade).

### Breaker Selection (MCB Types)
Miniature Circuit Breakers (MCBs) have different instantaneous tripping curves (magnetic trip):
- **Type B:** Trips at 3x to 5x rated current ($I_n$).
  - For a 32A circuit: 96A - 160A.
  - *Risk:* A 104A inrush is within the trip range. Nuisance tripping is highly likely.
- **Type C:** Trips at 5x to 10x rated current ($I_n$).
  - For a 32A circuit: 160A - 320A.
  - *Suitability:* The 104A inrush is well below the instant trip threshold. This is the standard choice for workshop circuits with motors.
- **Type D:** Trips at 10x to 20x rated current ($I_n$).
  - *Suitability:* Generally reserved for transformers, X-ray machines, or industrial welding equipment. Excessive for a 3HP motor and may require a lower earth fault loop impedance ($Z_s$) to ensure disconnection times are met (0.4s).

**Recommendation:** Use **Type C MCBs** for all machine circuits. Ensure the Earth Fault Loop Impedance ($Z_s$) at the furthest socket is low enough to satisfy the max $Z_s$ for Type C breakers (e.g., typically < 0.68Ω for 32A Type C, though RCD protection allows higher $Z_s$ for earth fault protection, overcurrent protection still requires consideration).

## 3. Sub-Main Feed Calculation

**Scenario:**
- **Supply:** 230V Single Phase
- **Load:** 40A (Design current $I_b$) - Approx 9.2kW allowed load.
- **Length:** 25 meters
- **Cable Type:** Steel Wire Armoured (SWA) - XLPE Insulation (90°C), typically terminated to 70°C switchgear.

### Voltage Drop Limits
- **Lighting:** 3% (6.9V)
- **Other Uses:** 5% (11.5V)
- **Goal:** Minimize drop to <3% ideally for efficiency and stability of motors.

### Option A: 10mm² 2-Core SWA
- **Voltage Drop (r):** 4.4 mV/A/m
- **Calculation:**
  $$ VD = \frac{4.4 \times 40 \times 25}{1000} = 4.4 \text{ Volts} $$
- **Percentage:** $(4.4 / 230) * 100 = 1.9\%$
- **Current Carrying Capacity (CCC):** ~73A (Clipped Direct). 40A is well within limits.

### Option B: 16mm² 2-Core SWA
- **Voltage Drop (r):** 2.8 mV/A/m
- **Calculation:**
  $$ VD = \frac{2.8 \times 40 \times 25}{1000} = 2.8 \text{ Volts} $$
- **Percentage:** $(2.8 / 230) * 100 = 1.2\%$
- **Current Carrying Capacity (CCC):** ~94A.

### Recommendation
**10mm² SWA** is technically sufficient and cost-effective. It keeps voltage drop well below 3% (4.4V vs 11.5V limit).
*However*, considering the future plan for **Solar PV and Battery Storage**, 16mm² is strongly recommended. It allows for:
- Higher export currents without raising voltage at the inverter (voltage rise problem).
- Future EV charging (7kW continuous load).
- Lower resistance = less energy wasted as heat (efficiency goal).

## 4. Emergency Stop (E-Stop) Integration

### Regulatory Context
BS 7671 Section 537.3.3 requires devices for emergency switching.
- **Requirement:** Must interrupt the supply to all live conductors (Phase & Neutral).
- **Location:** Readily accessible.

### Strategy: Shunted Trip vs. Contactor
For a dedicated workshop, a "Master Stop" system is safer than relying on individual machine plugs.

1.  **Shunt Trip:** A mechanical accessory fitted to the main switch/MCCB in the consumer unit.
    - *Pros:* Cuts power to the entire board.
    - *Cons:* Requires a specific consumer unit that supports it; can be clunky to reset.
2.  **Contactor System (Recommended):**
    - A specific "Machine Power" circuit (e.g., ring or radial) is fed through a Normally Open (NO) contactor.
    - The control circuit (230V or 24V) runs through a series of Normally Closed (NC) E-Stop buttons (mushroom head, twist-to-reset).
    - **Operation:** Hitting *any* E-Stop breaks the control circuit, the contactor opens, and machines lose power.
    - **Safety Feature:** "No-Volt Release" - If power fails and comes back, the machines do not restart automatically; the contactor must be manually reset (Start button).

**Recommendation:** Implement a contactor-based system for the machine circuits. Lighting and general convenience sockets (charging drills, radio) should remain on a separate, non-E-Stop circuit so you aren't left in the dark when an E-Stop is hit.

## 5. Dust Protection (IP Ratings)

### Wood Dust Hazards
- **Fire Risk:** Fine dust is combustible.
- **Electrical Faults:** Dust ingress can bridge conductors, causing tracking and short circuits.

### IP66 Sockets
- **Ingress Protection (IP) 66:**
  - **First Digit (6):** Dust-tight. No ingress of dust.
  - **Second Digit (6):** Protected against powerful water jets (useful for washdown, though less relevant inside).
- **Standard Sockets (IP2X):** Allow dust to settle inside the backbox and mechanism.

### Placement Strategy
1.  **Workbenches:** Use IP66 switched sockets. The flap covers protect unused sockets from settling dust.
2.  **Fixed Machines:** Use **Rotary Isolators** (IP65/66) for hard-wired connections or Commando sockets (IEC 60309) which are robust and prevent accidental pull-out.
3.  **Height:** Mount sockets at 1200mm+ to be above bench height and out of the "splash zone" of floor sweepings.
4.  **Cleaning:** Vacuum (do not blow) dust from electrical fittings regularly.

## Summary Checklist
- [ ] **Supply Cable:** 16mm² 2-Core SWA (Future-proof for Solar/EV).
- [ ] **Consumer Unit:** Metal-clad (fire rated), with SPD (Surge Protection).
- [ ] **Machine Circuits:** 32A Radials with **Type C** MCBs/RCBOs.
- [ ] **RCD Protection:** 30mA Type A (or Type F/B for variable speed drives).
- [ ] **Emergency Stop:** Contactor-based system controlling machine circuits only.
- [ ] **Accessories:** IP66 rated sockets and rotary isolators for machines.
