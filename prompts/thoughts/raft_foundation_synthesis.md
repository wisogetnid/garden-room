# Synthesis: Ground-to-Wall Interface on Floating Raft

**Context**: 4x5m Cowes Workshop.
**Foundation Choice**: We are proceeding with a Passivhaus-style floating insulated raft (EPS "tub" filled with a 100mm+ concrete slab reinforced with A193 mesh).
**Issue**: Why add a structural thermal break (like Marmox Thermoblock or Compacfoam) under the sole plate if the entire concrete slab is already wrapped in an EPS tub?

**Architectural Reasoning**:
1. **Flanking / Thermal Bypassing**: The concrete slab, being inside the thermal envelope, acts as a thermal mass equalized with the indoor air temperature (e.g., 20°C). However, the base track (timber) sits right at the edge of the slab. Without a thermal break block, heat travels from the warm room air -> into the concrete slab -> outward toward the cold edge -> up through the solid timber sole plate ($\lambda$ ~0.14 W/mK) -> bypassing the wall's thick PIR/mineral wool insulation. Replacing the timber base track with Compacfoam ($\lambda$ ~0.04 W/mK) severs this flanking path.
2. **Capillary Break / Damp-Proofing (Critical Risk)**: Concrete slabs, especially new ones, hold vast amounts of construction moisture. They can also draw moisture from condensation or internal spills. A standard DPC membrane is thin and easily punctured during timber frame erection. High-density structural thermal breaks (like Marmox Thermoblock or Foamglas) have zero capillarity and are completely impermeable. They act as a fail-safe Damp Proof Course (DPC) precisely where the timber frame is most vulnerable to rotting (the "Splash Zone" equivalent for the base track).
3. **Geometric Alignment (The L-Element Junction)**: In a true passive insulated raft, the external wall insulation needs to align perfectly with the EPS perimeter upstand of the foundation. Often, the structural wall needs to cantilever slightly or sit right on the edge. High-density EPS (Compacfoam) or Marmox allows the structural load to be perfectly positioned over the junction between the soft EPS upstand and the hard concrete, bridging the gap without creating a cold bridge or crushing the soft EPS perimeter.

**Decision for MASTER_PLAN.md**:
- **Foundation**: Floating EPS Insulated Raft (Kore/Jackon style).
- **Ground-to-Wall Interface**: Use a 100mm wide x 65mm high Marmox Thermoblock or Compacfoam strip as the starter track beneath the timber/SIP sole plate.
- **DPC Strategy**: Bed the thermal break block in a continuous bead of flexible polymer sealant (e.g., CT1 or equivalent) to the concrete slab, serving as an indestructible capillary break. Lap the internal VCL over this block.
