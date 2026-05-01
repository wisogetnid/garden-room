import re

# ------------- UPDATE MASTER_PLAN.md -------------
with open("plans/MASTER_PLAN.md", "r") as f:
    mp = f.read()

dimensional_section = """
### 1.0 Dimensional Reverse-Engineering (Outer Cladding to Core)
**Objective:** The User requested the absolute maximum *external* dimensions (from James Hardie cladding to James Hardie cladding) to be exactly **3.6m x 5.6m**. To achieve this, we must reverse-engineer the required size of the SIP structural framework and the concrete slab.

*   **External Envelope Buildup (Per Wall):**
    *   James Hardie Fibre Cement Plank (effective lapped depth): ~10mm
    *   Rainscreen Timber Batten: 25mm
    *   Rigid Wood Fibre External Insulation: 50mm
    *   *Total External Projection beyond SIP core:* **85mm per wall**
*   **Total Dimensional Reduction:** 85mm x 2 walls = **170mm reduction per axis**.
*   **Required SIP Framework & Concrete Slab Size:**
    *   Width: 3600mm - 170mm = **3430mm (3.43m)**
    *   Length: 5600mm - 170mm = **5430mm (5.43m)**
*   **Final Usable Internal Space (Accounting for internal Fermacell & battens):**
    *   SIP Core (150mm) + Service Batten (25mm) + Fermacell (15mm) = 190mm internal buildup per wall.
    *   Usable Internal Width: 3430mm - (190mm x 2) = **3050mm (3.05m)**
    *   Usable Internal Length: 5430mm - (190mm x 2) = **5050mm (5.05m)**
    *   *Final Internal Usable Footprint:* **15.4 m²**

*(Note: All structural orders—Concrete, SIPs, and XPS—must be executed to the 3.43 x 5.43m dimensions, NOT 3.6 x 5.6m).*

"""

# Inject section 1.0 before 1.1
mp = mp.replace("### 1.1 Groundworks & Slab Execution", dimensional_section + "### 1.1 Groundworks & Slab Execution")

# Replacements in MASTER_PLAN
mp = mp.replace("20.16m²", "18.6m²")
mp = mp.replace("18.4 linear meters", "17.7 linear meters")
mp = mp.replace("~46m² coverage", "~39m² coverage")
mp = mp.replace("~46m² wall coverage", "~39m² wall coverage")
mp = mp.replace("~3.1 Cubic Meters", "~2.8 Cubic Meters")
mp = mp.replace("~12 Bulk Bags (approx. 10.2 tonnes)", "~10 Bulk Bags (approx. 8.5 tonnes)")
mp = mp.replace("~3 Bulk Bags (approx. 2.5 tonnes)", "~2.5 Bulk Bags (approx. 2.1 tonnes)")
mp = mp.replace("~26m² Sheet", "~22m² Sheet")
mp = mp.replace("~20m² (actually ~18.6m²)", "~15.4m² (Internal Usable)") # fixing floor
mp = mp.replace("~20 boards", "~26 boards")
mp = mp.replace("~12 boards", "~14 boards")
mp = re.sub(r"Walls \(42m² x 0\.16\) = 6\.72 W/K", "Walls (34.1m² x 0.16) = 5.45 W/K", mp)
mp = re.sub(r"Roof \(18\.6m² x 0\.17\) = 3\.42 W/K", "Roof (18.6m² x 0.17) = 3.16 W/K", mp)
mp = re.sub(r"Floor \(18\.6m² x 0\.22\) = 4\.43 W/K", "Floor (18.6m² x 0.22) = 4.10 W/K", mp)
mp = re.sub(r"Total Fabric Loss = 17\.77 W/K", "Total Fabric Loss = 15.91 W/K", mp)
mp = re.sub(r"~5\.2 W/K", "~4.5 W/K", mp)
mp = re.sub(r"~22\.97 W/K", "~20.41 W/K", mp)
mp = re.sub(r"\[22\.97\]", "[20.41]", mp)
mp = re.sub(r"826 kWh/year thermal demand", "735 kWh/year thermal demand", mp)
mp = re.sub(r"826 kWh of electricity per year", "735 kWh of electricity per year", mp)
mp = re.sub(r"£202\.37 per year", "£180.07 per year", mp)

# Update ceiling height math text
mp = mp.replace("short 3.6m width", "short 3.43m SIP width")
mp = mp.replace("3600 ÷ 60 = 60mm", "3430 ÷ 60 = 57mm")
mp = mp.replace("60mm drop", "57mm drop")
mp = mp.replace("2098mm wall", "2101mm wall")
mp = mp.replace("2076mm", "2079mm")
mp = mp.replace("2098mm", "2101mm")

with open("plans/MASTER_PLAN.md", "w") as f:
    f.write(mp)

# ------------- UPDATE WORKPLAN.md -------------
with open("plans/WORKPLAN.md", "r") as f:
    wp = f.read()

wp = wp.replace("18.6m²", "18.6m²") # Make sure to catch previous if exist
wp = wp.replace("20.16m²", "18.6m²")
wp = wp.replace("3.6x5.6m tub", "3.43x5.43m tub")
wp = wp.replace("4.4m x 6.4m footprint", "4.23m x 6.23m footprint")
wp = wp.replace("4.4x6.4m footprint", "4.23x6.23m footprint")
wp = wp.replace("~9.8m³ of solid soil (~14.7 tonnes)", "~9.2m³ of solid soil (~13.8 tonnes)")
wp = wp.replace("Total waste: ~16.7 tonnes / ~13.9m³", "Total waste: ~15.8 tonnes / ~13.2m³")
wp = wp.replace("9,856-liter swimming pool", "9,222-liter swimming pool")
wp = wp.replace("~3.1m³ (or ~3.3m³ for safety)", "~2.8m³ (or ~3.0m³ for safety)")
wp = wp.replace("~3.0m³ (or ~3.3m³ for safety)", "~2.8m³ (or ~3.0m³ for safety)")
wp = wp.replace("16.4m of perimeter", "15.7m of perimeter")
wp = wp.replace("18.4m of expensive Compacfoam", "17.7m of expensive Compacfoam")
wp = wp.replace("18.4 linear meters", "17.7 linear meters")
wp = wp.replace("17.2m of expensive", "17.7m of expensive") # Catch any old

with open("plans/WORKPLAN.md", "w") as f:
    f.write(wp)

