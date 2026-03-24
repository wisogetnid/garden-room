# Risk Analysis: Insufficient Concrete Cover for Steel Reinforcement

**Agent:** @strategist
**Topic:** The danger of A252 steel mesh breaching the top 50mm of a 150mm concrete slab.

## 1. The Physics of the "Cover Zone"
In reinforced concrete, the "cover" is the specified distance between the outer surface of the concrete and the nearest surface of the reinforcing steel. For a ground-bearing slab, standard structural engineering (e.g., Eurocode 2 / BS EN 1992-1-1) mandates a strict minimum cover (usually 40mm to 50mm) for several critical reasons.

## 2. The Dangers of Breaching the Top 50mm

### A. The "Spalling" and Corrosion Risk (The Biggest Threat)
Concrete is porous. Even indoors, a concrete floor will absorb ambient moisture (and any liquid spills, workshop chemicals, or water from wet boots). 
*   **The Chemistry:** Concrete is naturally highly alkaline (pH 12-13), which protects steel from rusting. However, over time, carbon dioxide from the air penetrates the concrete, lowering its pH (a process called carbonation). 
*   **The Failure:** If the steel mesh sits only 10mm or 20mm below the surface (instead of the required 50mm), the carbonation front reaches the steel much faster. The steel begins to rust. 
*   **The Explosion:** Rust expands to **up to 6 times the volume** of the original steel. This massive internal expansive force blows the concrete apart from the inside out. The surface of your power-floated floor will literally pop off in chunks (known as "spalling").

### B. Ruining the Power-Float Finish
A power float is a heavy, spinning trowel machine used to create a perfectly smooth, hard-wearing surface on wet concrete.
*   **The Impact:** If the top layer of A252 steel is floating too high (e.g., in the top 20mm), the spinning blades of the heavy power float will strike the steel mesh. 
*   **The Result:** This will violently rip the steel upward, drag it across the wet concrete, tear deep gouges in your floor, and likely damage or break the power float machine. The contractor will have to abandon the smooth finish, leaving you with a rough, uneven floor that is impossible to bond your engineered oak to.

### C. Structural "Punching Shear" Failure
Steel mesh works by absorbing tensile (pulling) forces. In a slab loaded from above (like a 250kg cast-iron table saw), the bottom of the slab experiences tension, while the top experiences compression. 
*   **The Failure:** The top layer of mesh in a double-reinforced slab is primarily there to stop the top surface of the concrete from cracking due to thermal expansion/contraction (especially with Underfloor Heating) and drying shrinkage. If the mesh is too close to the surface, it lacks enough "bite" (concrete embedment) to hold the slab together. Heavy point loads dropped on a thin cover layer can easily punch straight through to the steel.

## 3. The 150mm Slab "Double Sandwich" Geometry Crisis
The @strategist previously flagged a severe tolerance issue in `MASTER_PLAN_SIPS.md`:
*   **Total Slab Thickness:** 150mm
*   **Bottom Cover (Plastic Chairs):** 50mm
*   **Bottom A252 Mesh:** 16mm (8mm wire overlapping 8mm wire)
*   **PEX-a UFH Pipe:** 16mm
*   **Top A252 Mesh:** 16mm (8mm wire overlapping 8mm wire)
*   **Total Stack Height:** 50 + 16 + 16 + 16 = **98mm**
*   **Remaining Top Cover:** 150mm - 98mm = **52mm**

**The Reality:** In a theoretical vacuum, you have 52mm of cover, which perfectly meets the 50mm requirement. In the real world of a muddy site, 8mm steel mesh is rarely perfectly flat; it bows and warps. If the sub-base is uneven by just 5mm, or the mesh bows upward by just 10mm, you instantly lose your 50mm cover. If a heavy contractor steps on the top mesh during the pour and bends it upward, the power float will hit it. 

This is why the 2mm tolerance is a severe risk.
