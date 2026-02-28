# **Integrated Dust Extraction and Atmospheric Management Strategies for High-Performance Garden Workshops**

The construction of a bespoke wood workshop within the constraints of a garden room project in Cowes, UK, represents a sophisticated engineering challenge that intersects building physics, industrial hygiene, and renewable energy management. The objective of achieving a Passivhaus standard in a 20-square-meter structure—characterized by extreme airtightness and high thermal efficiency—creates a fundamental paradox when introduced to the requirements of woodworking dust extraction. Traditional dust collection relies on the rapid displacement of large volumes of air to entrain and transport particulate matter. In a sealed environment with a volume of approximately 50 cubic meters, the activation of a standard industrial extractor can induce significant pressure differentials, potentially compromising the building envelope or disrupting the delicate balance of mechanical ventilation systems.1 Furthermore, the specific geographic context of the Isle of Wight introduces high ambient humidity, which poses a persistent threat of corrosion to precision hand tools unless atmospheric controls are meticulously integrated into the extraction strategy.1

## **Aerodynamic Fundamentals of Particulate Capture**

To design an effective extraction system for a small-scale workshop, it is necessary to categorize wood waste into two distinct aerodynamic regimes: bulk chip collection and fine dust extraction. These regimes are managed by High Volume, Low Pressure (HVLP) systems and Low Volume, High Pressure (LVHP) systems, respectively. The distinction is not merely one of scale but of fluid dynamics. HVLP systems, such as the Charnwood W691 or the Rutlands wall-mounted units, utilize large-diameter impellers to move massive quantities of air at relatively low static pressures, typically ranging from 1,000 to 3,000 cubic meters per hour.5 These are essential for machines like planer-thicknessers or table saws, where the volume of waste produced per second is high and the particles are relatively large and heavy.7  
Conversely, LVHP systems, often represented by high-performance vacuum extractors like the Festool CTL MIDI or Fein Dustex series, generate intense suction pressure but move a smaller total volume of air. These systems are optimized for handheld power tools—sanders, routers, and biscuit joiners—where the extraction ports are small (27mm to 36mm). In these instances, high static pressure is required to overcome the resistance of the narrow aperture and the internal baffling of the tool to capture dust at the point of origin.7

### **Comparative Performance Metrics of Extraction Regimes**

| Parameter | HVLP (High Volume Low Pressure) | LVHP (Low Volume High Pressure) |
| :---- | :---- | :---- |
| Typical Airflow | $1,000 \- 3,000$ m³/h | $150 \- 250$ m³/h |
| Static Pressure | $1,500 \- 3,000$ Pa | $20,000 \- 25,000$ Pa |
| Optimal Hose Diameter | $100$ mm to $150$ mm | $27$ mm to $50$ mm |
| Waste Type | Large chips, shavings, coarse sawdust | Microscopic dust, sanding flour |
| Primary Tool Support | Planer, Table Saw, Bandsaw | Sanders, Routers, Mitre Saws |
| Motor Type | Induction (Quiet, Continuous) | Universal/Brushless (High RPM) |

5  
The physical law governing these systems is the relationship between velocity ($V$), flow rate ($Q$), and cross-sectional area ($A$), expressed as $V \= Q/A$. For effective transport of woodworking waste, air velocity within the ductwork must be maintained at a level that prevents the settling of particles. Generally, a velocity of $20$ to $25$ meters per second (approx. 4,000 to 4,500 feet per minute) is required for horizontal runs of 100mm ducting to keep chips entrained.14 In a small 4m by 5m workshop, the short duct runs reduce friction losses, but the high velocity required means that even a compact extractor like the Charnwood W625 will exert a noticeable influence on the room's internal pressure.5

## **The Passivhaus Constraint: Airtightness and Pressure Equilibrium**

A Passivhaus-standard workshop is designed to minimize uncontrolled air infiltration, often targeting an $n\_{50}$ value of $0.6$ air changes per hour (ACH). In a 50m³ room, this equates to a leakage rate of only 30m³ per hour at a pressure of 50 Pascals.2 When an HVLP extractor moving 2,000m³/h is activated, it attempts to evacuate forty times the entire room volume every hour.3 If the air is vented to the exterior—a common practice in traditional workshops to eliminate fine dust—the building will experience rapid depressurization. This vacuum will force air through any available path, potentially causing structural whistling, drawing in moisture from the Cowes maritime environment, or back-drafting any combustion appliances if present.3  
The solution in a high-performance building is either internal recirculation or a balanced makeup air system. Recirculation involves filtering the air to a high standard and returning it directly to the workshop space. This preserves the thermal energy already invested in heating the room and maintains neutral pressure.11 However, recirculation demands a much higher standard of filtration. Basic bag extractors often filter only to 5 or 30 microns, which is insufficient for health; microscopic "dust flour" (PM2.5) remains airborne and is simply redistributed by the extractor's exhaust.6

### **Mechanical Ventilation with Heat Recovery (MVHR) Integration**

To maintain air quality without losing heat, the workshop must utilize a Mechanical Ventilation with Heat Recovery (MVHR) system. For a single-room garden workshop, decentralised units (dMVHR) are often the most practical choice. These units, such as the Vent-Axia Lo-Carbon Tempra or Blauberg Vento, operate on a "push-pull" cycle. A regenerative ceramic heat exchanger captures thermal energy from the outgoing stale air and then transfers it to the incoming fresh air during the intake phase.20  
In the context of wood dust, the MVHR system is not intended to handle the primary extraction load but rather to provide the background air exchange required for human health and humidity control. The dust extraction system must be treated as a separate, high-intensity local exhaust ventilation (LEV) loop.11 To protect the sensitive heat exchanger and filters of the MVHR unit, the primary extraction must be highly effective at the source. If the dust extraction is vented externally, the MVHR system must be interlocked with the extractor to provide balanced makeup air, though this is mechanically complex for a DIY project.3

## **Filtration Standards and Respiratory Protection**

Wood dust is officially recognized as a Group 1 carcinogen, linked to cancers of the nasal cavity and sinuses.18 In a confined 20m² space, the concentration of fine particulate matter can reach hazardous levels within minutes of using a sander or router. The Health and Safety Executive (HSE) in the UK recommends the use of M-Class or H-Class extraction for professional woodworking.9

### **Classification of Extraction Filtration**

| Class | Capture Efficiency | Typical Application |
| :---- | :---- | :---- |
| L (Low) | $\> 99\\%$ | General cleaning, non-toxic dusts |
| M (Medium) | $\> 99.9\\%$ | Hardwoods, MDF, sanding flour |
| H (High) | $\> 99.995\\%$ | Asbestos, lead, highly toxic pathogens |
| HEPA (H13) | $\> 99.95\\%$ at $0.3 \\mu m$ | Recirculating air in airtight spaces |

9  
For the Cowes garden room, an M-Class extractor equipped with a HEPA filter is the essential minimum for internal recirculation. Units such as the Numatic TRM240 or the Festool CTM MIDI offer the necessary certification. These machines use multi-stage filtration: a high-efficiency bag to capture the bulk of the waste, a secondary filter to protect the motor, and a final HEPA stage to ensure the air returning to the workshop is cleaner than the air it removed.9  
Furthermore, ambient air purifiers, such as the Axminster Workshop AW15AFS, serve as a critical secondary defense. These ceiling-mounted units continuously circulate the workshop's air, pulling it through fine filters to capture the "escaped" dust that the source extractors missed.11 For a 50m³ room, an air filter should provide at least six to ten air changes per hour (300 to 500 m³/h) to effectively maintain low background dust levels.11

## **Tool-Specific Extraction Strategies**

The garden room context, primarily focused on hand tools but requiring support for occasional power tool use, dictates a hybrid extraction approach. The restricted site access—a 30m path only "wheelbarrow wide"—means that any equipment must be modular or compact enough for manual transport.1

### **LVHP Extractors for Handheld Power Tools**

Portable extractors are the backbone of a small workshop. The Fein Dustex and Festool MIDI series are particularly favored for their quiet operation and compact footprint.9 A key feature for the Cowes workshop is "auto-start" functionality, where the vacuum activates automatically when the connected power tool is switched on. This not only ensures 100% compliance with dust capture but also manages energy consumption, which is critical for the future solar and battery phase of the project.9  
For tools like mitre saws, which are notoriously difficult to extract from, a dual-port strategy is often necessary. A high-pressure vacuum line is connected to the blade guard port, while a larger HVLP hood is positioned behind the machine to catch the "overspray" of chips.7

### **HVLP Solutions for Stationary Machinery**

Despite the hand tool focus, machines like a planer-thicknesser or a bandsaw require the high volumetric flow of an HVLP system. The Charnwood W690 (1HP) or W625 are suitable for single-machine extraction in small spaces.5 However, floor space is at a premium in a 4m x 5m room. Wall-mounted extractors, such as the Rutlands R8578, provide a compelling solution by utilizing vertical space.6 These units offer airflows of approximately 870 m³/h, sufficient for most hobbyist stationary tools, while maintaining a footprint that does not interfere with workbenches or assembly areas.6

| Model | Power | Airflow | Noise | Best Use Case |
| :---- | :---- | :---- | :---- | :---- |
| Charnwood W625 | 0.5 HP | 850 m³/h | \~80 dB | Bandsaws, small benchtop tools |
| Rutlands R8578 | 1.0 HP | 870 m³/h | 78 dB | Wall-mounted, space-saving stationary |
| Charnwood W691 | 2.0 HP | 2,000 m³/h | \~85 dB | Planer-thicknessers, multi-machine |
| Record Power CamVac | 1-3 kW | Variable | Variable | Fine dust, high-pressure collection |

5  
The Record Power CamVac series offers a unique alternative; it is a vacuum-based system (LVHP) that utilizes multiple high-speed motors to achieve high static pressure across a 100mm inlet. This makes it particularly effective at capturing fine dust from machines that usually require HVLP airflow, though it is louder than traditional induction motor systems unless the exhaust is muffled or vented outside.8

## **Cyclone Pre-Separation: Efficiency and Maintenance**

A significant operational challenge in a small workshop is the frequency of filter maintenance. Wood shavings from a planer can fill a standard vacuum bag in minutes, and the fine dust quickly "blinds" (clogs) the expensive HEPA filters required for recirculating systems.9 Cyclone pre-separators, such as the Oneida Dust Deputy or the various DIY designs, mitigate this by using centrifugal force to spin out up to 99% of the waste before it reaches the extractor's filter.33  
The physics of cyclone separation involves the creation of a high-velocity vortex. As the dust-laden air spirals downward, the inertia of the heavier particles forces them to the outer wall of the cone, where they lose velocity and fall into a collection bin. The cleaned air then reverses direction and exits through the center of the vortex.33 For the Cowes project, a mobile cyclone unit mounted on a 20-liter or 55-liter drum and paired with an M-Class vacuum provides the most versatile solution.30 This setup can be moved around the shop, keeping the primary extractor's filter clean for hundreds of hours of use and making waste disposal as simple as emptying a bucket.33

### **Cyclone Efficiency Curves**

| Particle Size | Separation Efficiency | Implication |
| :---- | :---- | :---- |
| $\> 50 \\mu m$ (Shavings) | $99.9\\%$ | Minimal impact on secondary filter |
| $10 \- 50 \\mu m$ (Sawdust) | $98 \- 99\\%$ | Filter life extended 50x to 100x |
| $1 \- 10 \\mu m$ (Fine Dust) | $90 \- 95\\%$ | Significant capture, but filter needed |
| $\< 0.5 \\mu m$ (Smoke/Flour) | $\< 50\\%$ | Dangerous particles pass through |

33  
Research indicates that the performance of a cyclone is highly dependent on airflow velocity. If the airflow drops (due to a clogged downstream filter), the vortex weakens, and the separation efficiency for fine particles collapses.33 Therefore, a recirculating system in an airtight shop must include a pressure gauge or "filter full" indicator to ensure the user knows when the system's safety is compromised.30

## **Ducting Design for the 4m x 5m Footprint**

The layout of the ducting system is as critical as the choice of extractor. In a small workshop, the goal is to minimize static pressure loss, which is caused by friction against the duct walls and turbulence at bends.14

### **Engineering Guidelines for Ductwork**

1. **Duct Material:** Smooth-walled rigid pipe, such as PVC or galvanized steel, is significantly more efficient than flexible hose. Flexible hose should be limited to the final meter of connection to the tool, as its corrugated interior can have three times the friction of smooth pipe.14  
2. **Bend Geometry:** 90-degree elbows should be avoided. Instead, two 45-degree elbows with a short straight section between them should be used to create a "long radius" bend. This maintains the laminar flow of air and prevents heavy chips from impacting the wall and losing velocity.14  
3. **Static Electricity Management:** PVC pipe in a dry woodworking environment can build up a significant static charge. While the risk of a dust explosion in a hobbyist shop is statistically low, the static shocks can be painful and interfere with sensitive electronics or solar inverters. A common mitigation is to wrap a copper wire around the exterior of the pipe and ground it to the extractor chassis.39  
4. **Blast Gates:** In a system with a single extractor, blast gates must be used to ensure that 100% of the airflow is directed to the active tool. In an airtight room, leaving multiple gates open will "starve" the system, reducing air velocity below the point required for particle transport and leading to clogs in the main trunk.14

The compact 20m² layout of the Cowes workshop allows for a simple "main trunk" design. By placing the extractor in a central location along one of the 5m walls, the furthest machine would be no more than 3 to 4 meters away, ensuring high performance even from a modest 1HP motor.5

## **Acoustical Management in the Garden Context**

Noise is a primary constraint for the garden room, particularly when working in the evenings or bordering neighboring fences.1 Universal motors, found in most shop vacuums and the CamVac series, are high-RPM machines that produce a piercing whine often exceeding 90 dB.17 Induction motors, used in Charnwood and Rutlands stationary extractors, are inherently quieter, producing a lower-frequency hum at approximately 75 to 80 dB.6

### **Noise Mitigation Strategies**

To achieve a "conversation-level" noise profile, the extractor can be housed in a soundproof enclosure. This enclosure must be designed with a "baffle box" for the air intake and exhaust. A baffle box uses multiple internal 90-degree turns lined with acoustic foam to trap sound waves while allowing air to pass through freely.17

| Acoustic Treatment | Decibel Reduction | Implementation Notes |
| :---- | :---- | :---- |
| Baffle Box Intake | $10 \- 15$ dB | Must maintain cross-sectional area to prevent overheating |
| Mass-Loaded Vinyl (MLV) | $15 \- 20$ dB | Line internal walls of the extractor closet |
| Decoupling Mounts | $5 \- 8$ dB | Use rubber vibration isolators for wall-mounted units |
| Induction Motor Choice | $10 \- 15$ dB | Baseline improvement over universal motors |

6  
For the Cowes workshop, placing the extractor inside a cupboard lined with double-layered acoustic plasterboard and utilizing a long-radius baffle for the exhaust would allow the unit to be operated in the evening without disturbing neighbors.17 It is essential to ensure the motor has adequate cooling; many extractors rely on the air they are pulling through the hose to cool the motor, but the radiant heat from the motor casing can still build up in a small sealed enclosure.17

## **Atmospheric Control: Humidity and Tool Preservation**

The Isle of Wight's maritime climate presents a high risk of "rust flash" on cast iron tool tables and carbon steel hand tools. The Passivhaus building envelope provides a primary barrier, but the movement of air during extraction can introduce moisture-laden air if not handled correctly.1

### **Psychrometrics and Workshop Humidity**

Relative Humidity (RH) is a function of air temperature. As air cools, its capacity to hold moisture decreases, causing the RH to spike. In a well-insulated workshop that is heated during the evening and allowed to cool at night, the RH can easily exceed 70%, the threshold for active corrosion on steel.4  
While MVHR systems help by providing constant air movement and filtering out some external particles, they do not inherently act as dehumidifiers. They simply exchange the internal air for external air. If the external air in Cowes is at 90% RH, the internal air will quickly approach that level unless it is heated or actively dehumidified.4  
A dedicated compressor-based dehumidifier is the most effective tool for a garden workshop. These units not only remove moisture but also release a small amount of latent heat as a byproduct of the condensation process, aiding the workshop's thermal balance.48 For the 50m³ Cowes workshop, a unit capable of extracting 10 to 12 liters per day, fitted with a permanent drain through the wall, would maintain the RH at a stable 45% to 50%, ideal for wood seasoning and tool protection.1

## **Solar and Battery Power Integration**

The plan to incorporate solar panels and a battery system dictates a "low-surge" electrical strategy. Induction motors, while quiet and reliable, have a high starting torque that requires a significant inrush current—often five to seven times the running amperage.50 A 1.5kW extractor with a running current of 6 Amps might spike to 30 Amps for the first second of activation.

### **Managing Surge on an Off-Grid/Hybrid Inverter**

1. **Inverter Sizing:** The system must utilize a "low-frequency" inverter with a high surge rating (typically 300% of its nominal capacity) to handle the startup of the extractor while other tools are in use.50  
2. **Soft Starters:** Installing a soft-start module on the extractor's motor can reduce the inrush current by 50% to 70%, allowing a smaller inverter to manage the load.52  
3. **Sequential Activation:** Utilizing an automated system like iVac that introduces a delay between the extractor starting and the tool starting prevents a synchronized surge that could trip the battery's protection circuit.53  
4. **Dust on Panels:** In a woodworking context, fine dust can settle on the exterior solar panels, significantly reducing their output. An autonomous dust removal system or a regular cleaning schedule is required to ensure the battery bank remains charged.55

For the Cowes project, a 48V battery system paired with a 5,000W inverter would provide sufficient headroom for a 2HP extractor and a table saw, provided they are not activated at the exact same moment.52

## **Automation and Small-Shop Workflow**

In a 20m² workshop, every square meter of floor space must be utilized effectively. Automation of the dust extraction system is not just a luxury but a method of ensuring that safety protocols are followed during every cut, especially during short evening sessions.31

### **Automated Blast Gates and Triggers**

Wireless triggers, such as those from iVac or the various DIY Arduino-based solutions, use current sensors clamped to the power tool cords. When the sensor detects current, it sends a signal to the central extractor and the relevant motorized blast gate.53 For the DIY builder, using RC servos to actuate wooden blast gates is a popular and cost-effective approach that integrates well with small-scale ducting.31

| Feature | Manual Blast Gate | Automated (iVac) | Automated (DIY/Servo) |
| :---- | :---- | :---- | :---- |
| Activation | Physical slide | Current sensing (Wireless) | Microcontroller (Wired/IR) |
| Reliability | High (no electronics) | High (professional grade) | Variable (builder dependent) |
| Cost | Low (£10 \- £20) | High (£100 \- £150 per drop) | Moderate (£30 \- £50 per drop) |
| Space Impact | Slide sticks out | Compact housing | Requires servo mounting |

31  
The inclusion of an "Always Open" gate is a critical safety feature for high-performance extractors. This ensures that the extractor always has a path for airflow, preventing the motor from overheating or the vacuum from collapsing the ductwork if all other gates are closed.53

## **Integrated Strategy for the Cowes Garden Workshop**

The research into the specific constraints of the Cowes garden room—Passivhaus standards, restricted access, high humidity, and future solar power—points toward a highly specific, tiered extraction and atmospheric control strategy.

### **Primary Extraction System**

For stationary machinery (planer, bandsaw, mitre saw), the optimal solution is a wall-mounted 1HP to 1.5HP induction motor extractor, such as the Rutlands R8578 or a compact Charnwood unit. This should be mounted on an internal partition wall to minimize sound transmission to the building envelope and neighboring fences. To satisfy the Passivhaus requirement for thermal retention, the unit must utilize a high-efficiency cartridge filter (0.5 to 1 micron) and a final HEPA stage to allow for 100% internal recirculation.

### **Portable Extraction and Pre-Separation**

For handheld tools and general cleanup, an M-Class portable extractor with auto-start capability (e.g., Fein Dustex 25L) is recommended. This unit should be paired with a high-efficiency cyclone pre-separator (e.g., Dust Deputy) mounted on a modular trolley. This modularity is essential for transport down the narrow 30m access path and for easy maintenance within the workshop. The cyclone will capture 99% of the waste, protecting the vacuum's expensive HEPA filters from the high dust loads of routing and sanding.

### **Ventilation and Climate Control**

Background air quality and moisture management must be handled by a decentralised dMVHR system. A pair of units, such as the Blauberg Vento, should be installed on opposite walls to ensure balanced cross-ventilation. To protect the precision hand tools from Isle of Wight humidity, a standalone compressor dehumidifier should be operated during non-working hours to maintain a stable 45% RH. The heat from this unit will contribute to the Passivhaus thermal goals during the winter months.

### **Electrical and Control Integration**

To support the future transition to solar power, all extraction units should be fitted with soft-starters or chosen for their low-surge characteristics. A wireless automation system (e.g., iVac Pro) will manage the extraction drops, ensuring that the system is only active when necessary and preventing simultaneous motor starts that could overwhelm the battery inverter.  
This integrated approach ensures that the workshop remains a safe, quiet, and thermally stable environment, allowing the craftsman to focus on the precision of hand tools while maintaining the highest standards of modern building performance. By treating dust extraction not as an add-on but as a fundamental component of the building's mechanical design, the Cowes garden room can achieve true Passivhaus excellence without compromising on the requirements of a functional woodworking studio.

#### **Works cited**

1. workshop-research-context.md  
2. Mechanical Heat Recovery and Ventilation | Self Build Blog Passive ..., accessed February 28, 2026, [https://selfbuild.blog/tag/mechanical-heat-recovery-and-ventilation/](https://selfbuild.blog/tag/mechanical-heat-recovery-and-ventilation/)  
3. MHVR and high volumes of dust \- Green Building Forum, accessed February 28, 2026, [https://www.greenbuildingforum.co.uk/newforum/comments.php?DiscussionID=9780](https://www.greenbuildingforum.co.uk/newforum/comments.php?DiscussionID=9780)  
4. MVHR, room humidity and drying out \- Green Building Forum, accessed February 28, 2026, [https://www.greenbuildingforum.co.uk/newforum/comments.php?DiscussionID=12703](https://www.greenbuildingforum.co.uk/newforum/comments.php?DiscussionID=12703)  
5. Top 5 Dust Extractors for Small Workshops \- Woodworking Machinery, accessed February 28, 2026, [https://www.ukwoodworkingmachinery.co.uk/post/top-5-dust-extractors-for-small-workshops](https://www.ukwoodworkingmachinery.co.uk/post/top-5-dust-extractors-for-small-workshops)  
6. Wall-Mount Dust Extractor | Next Day Delivery – Rutlands Limited, accessed February 28, 2026, [https://www.rutlands.com/products/wall-mount-dust-extractor](https://www.rutlands.com/products/wall-mount-dust-extractor)  
7. Woodworking Dust Extraction: How to Choose the Right System \- Hammer Roo, accessed February 28, 2026, [https://hammerroo.com.au/blogs/ideas-advice/woodworking-dust-extraction-how-to-choose-the-right-system](https://hammerroo.com.au/blogs/ideas-advice/woodworking-dust-extraction-how-to-choose-the-right-system)  
8. Understanding Dust Collection \- Parkerville Wood Products, accessed February 28, 2026, [https://parkervillewoodproducts.com/understanding-dust-collection/](https://parkervillewoodproducts.com/understanding-dust-collection/)  
9. Advice on dust extractors for a small hobbyist shed operation \[UK\] : r/woodworking \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/woodworking/comments/zxkz11/advice\_on\_dust\_extractors\_for\_a\_small\_hobbyist/](https://www.reddit.com/r/woodworking/comments/zxkz11/advice_on_dust_extractors_for_a_small_hobbyist/)  
10. Portable Dust Extractors \- Data Powertools Ltd, accessed February 28, 2026, [https://www.datapowertools.co.uk/Products/Portable\_Dust\_Extractors](https://www.datapowertools.co.uk/Products/Portable_Dust_Extractors)  
11. Dust Extractor | Dust Extraction For Your Workshop | Buying Guide ..., accessed February 28, 2026, [https://www.axminstertools.com/ideas-advice/dust-extractors/](https://www.axminstertools.com/ideas-advice/dust-extractors/)  
12. Dust Extraction. Any advice to clear my mind? : r/woodworking \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/woodworking/comments/2maa81/dust\_extraction\_any\_advice\_to\_clear\_my\_mind/](https://www.reddit.com/r/woodworking/comments/2maa81/dust_extraction_any_advice_to_clear_my_mind/)  
13. Woodworking tools \- Recordpower, accessed February 28, 2026, [https://www.recordpower.co.uk/?x=/magazine/page/buyers-guides/cat/dust-extraction/article/dust-extraction-buyers-guide/id/73](https://www.recordpower.co.uk/?x=/magazine/page/buyers-guides/cat/dust-extraction/article/dust-extraction-buyers-guide/id/73)  
14. Sizing and Designing Ductwork Layout \- Höcker North America, accessed February 28, 2026, [https://hockeramerica.com/sizing-and-designing-ductwork-layout/](https://hockeramerica.com/sizing-and-designing-ductwork-layout/)  
15. HVAC – How to Size and Design Ducts, accessed February 28, 2026, [https://www.cedengineering.com/userfiles/M06-032%20-%20HVAC%20-%20How%20to%20Size%20and%20Design%20Ducts%20-%20US.pdf](https://www.cedengineering.com/userfiles/M06-032%20-%20HVAC%20-%20How%20to%20Size%20and%20Design%20Ducts%20-%20US.pdf)  
16. The Ultimate MVHR Guide \- Paul Heat Recovery, accessed February 28, 2026, [https://www.paulheatrecovery.co.uk/information-on-domestic-ventilation-and-mvhr/mvhr-guide/](https://www.paulheatrecovery.co.uk/information-on-domestic-ventilation-and-mvhr/mvhr-guide/)  
17. Soundproofing a Dust Collection System \- Woodweb, accessed February 28, 2026, [https://woodweb.com/knowledge\_base/Soundproofing\_a\_Dust\_Collection\_System.html](https://woodweb.com/knowledge_base/Soundproofing_a_Dust_Collection_System.html)  
18. Workshop Dust Collection \- Miracle Truss, accessed February 28, 2026, [https://miracletruss.com/workshop-dust-collection/](https://miracletruss.com/workshop-dust-collection/)  
19. The 9 Best Dust Collector Machines for Woodworking, Tested and Reviewed, accessed February 28, 2026, [https://www.familyhandyman.com/list/best-dust-collector/](https://www.familyhandyman.com/list/best-dust-collector/)  
20. The Ultimate Guide to Decentralised Heat Recovery Ventilation, accessed February 28, 2026, [https://www.ventilation-alnor.co.uk/index/support/alnor-knowledge-base/heat-recovery/mvhr-guide.html](https://www.ventilation-alnor.co.uk/index/support/alnor-knowledge-base/heat-recovery/mvhr-guide.html)  
21. Decentralised Mechanical Ventilation Heat Recovery (dMVHR) \- Vent-Axia, accessed February 28, 2026, [https://www.vent-axia.com/decentralised-mechanical-ventilation-heat-recovery-dmvhr](https://www.vent-axia.com/decentralised-mechanical-ventilation-heat-recovery-dmvhr)  
22. Decentralised Mechanical Ventilation with Heat Recovery dMVHR \- Home Retrofit \- Carbon Co-op Community, accessed February 28, 2026, [https://community.carbon.coop/t/decentralised-mechanical-ventilation-with-heat-recovery-dmvhr/1021](https://community.carbon.coop/t/decentralised-mechanical-ventilation-with-heat-recovery-dmvhr/1021)  
23. Woodworking Extraction Systems \- Handling Dust from Wood, accessed February 28, 2026, [https://www.airplants.co.uk/news/woodworking-extraction-systems-handling-dust-from-wood/](https://www.airplants.co.uk/news/woodworking-extraction-systems-handling-dust-from-wood/)  
24. Mobile Dust Extractors \- Dustcontrol, accessed February 28, 2026, [https://dustcontrol.uk/product-category/industry/mobile-dust-extractors/](https://dustcontrol.uk/product-category/industry/mobile-dust-extractors/)  
25. Mobile Dust Extractors \- Rodstation, accessed February 28, 2026, [https://www.rodstation.co.uk/dust-control/mobile-dust-extractors/](https://www.rodstation.co.uk/dust-control/mobile-dust-extractors/)  
26. Ambient Air Cleaner | Industrial Air Cleaner \- Sentry Air Systems, accessed February 28, 2026, [https://www.sentryair.com/ambient-air-cleaner.htm](https://www.sentryair.com/ambient-air-cleaner.htm)  
27. Air Filters \- Dust Extractors \- Machinery \- Axminster Tools, accessed February 28, 2026, [https://www.axminstertools.com/machinery/dust-extractors/air-filters](https://www.axminstertools.com/machinery/dust-extractors/air-filters)  
28. Workshop Air Filters For Sale UK | Industrial Dust Filters | Scott+Sargeant, accessed February 28, 2026, [https://www.scosarg.com/new-machines/dust-extractors-waste/air-filters](https://www.scosarg.com/new-machines/dust-extractors-waste/air-filters)  
29. Dust Collection Vacuums & Extractors Archives \- Central Technology Systems, accessed February 28, 2026, [https://centraltechnologysystems.co.uk/product-category/dust-extraction/dust-collection-vacuums-extractors/](https://centraltechnologysystems.co.uk/product-category/dust-extraction/dust-collection-vacuums-extractors/)  
30. Anti DIY Audio: Managing workshop vacuum noise \- StereoNET, accessed February 28, 2026, [https://www.stereonet.com/forums/topic/282066-anti-diy-audio-managing-workshop-vacuum-noise/](https://www.stereonet.com/forums/topic/282066-anti-diy-audio-managing-workshop-vacuum-noise/)  
31. Automated Dust Collection Solutions for Small Shop? : r/woodworking \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/woodworking/comments/1f1reh1/automated\_dust\_collection\_solutions\_for\_small\_shop/](https://www.reddit.com/r/woodworking/comments/1f1reh1/automated_dust_collection_solutions_for_small_shop/)  
32. Recordpower \- Woodworking tools, accessed February 28, 2026, [https://www.recordpower.co.uk/magazine/page/buyers-guides/cat/dust-extraction/article/dust-extraction-buyers-guide/id/73](https://www.recordpower.co.uk/magazine/page/buyers-guides/cat/dust-extraction/article/dust-extraction-buyers-guide/id/73)  
33. Cyclone Pre-Separators: Save Filters, Keep Airflow \- Dust Arrest, accessed February 28, 2026, [https://dustarrest.com/blogs/dust-knowledge-hub/cyclone-pre-separators-save-filters-keep-airflow](https://dustarrest.com/blogs/dust-knowledge-hub/cyclone-pre-separators-save-filters-keep-airflow)  
34. Could you modify a dust extractor with a HEPA filter? : r/woodworking \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/woodworking/comments/124zvy4/could\_you\_modify\_a\_dust\_extractor\_with\_a\_hepa/](https://www.reddit.com/r/woodworking/comments/124zvy4/could_you_modify_a_dust_extractor_with_a_hepa/)  
35. How to build a 99% efficient Cyclone Dust Collector \- Carbide 3D Community Site, accessed February 28, 2026, [https://community.carbide3d.com/t/how-to-build-a-99-efficient-cyclone-dust-collector/1972](https://community.carbide3d.com/t/how-to-build-a-99-efficient-cyclone-dust-collector/1972)  
36. Dust Deputy vs. Dustopper \- scientific testing \- Shop Hacks, accessed February 28, 2026, [https://www.shophacks.com/dustdeputy\_vs\_dustopper.html](https://www.shophacks.com/dustdeputy_vs_dustopper.html)  
37. Cyclone Dust Collectors \- Nederman MikroPul, accessed February 28, 2026, [https://www.nedermanmikropul.com/Products/Cyclone-Separators/Cyclone-Dust-Collectors](https://www.nedermanmikropul.com/Products/Cyclone-Separators/Cyclone-Dust-Collectors)  
38. Cyclone efficiency \- General Woodworking Talk, accessed February 28, 2026, [https://www.woodtalkonline.com/topic/18285-cyclone-efficiency/](https://www.woodtalkonline.com/topic/18285-cyclone-efficiency/)  
39. Dust Collection Duct Layout Advice Needed \- NC Woodworker, accessed February 28, 2026, [https://ncwoodworker.net/forums/index.php?threads/dust-collection-duct-layout-advice-needed.72063/](https://ncwoodworker.net/forums/index.php?threads/dust-collection-duct-layout-advice-needed.72063/)  
40. Make Your Own Canister Filter for HF 2hp Dust Collector | NC Woodworker, accessed February 28, 2026, [https://ncwoodworker.net/forums/index.php?threads/make-your-own-canister-filter-for-hf-2hp-dust-collector.54556/](https://ncwoodworker.net/forums/index.php?threads/make-your-own-canister-filter-for-hf-2hp-dust-collector.54556/)  
41. Workshop Layout and Dust Collection Ducting Advice \- NC Woodworker, accessed February 28, 2026, [https://ncwoodworker.net/forums/index.php?threads/workshop-layout-and-dust-collection-ducting-advice.64862/](https://ncwoodworker.net/forums/index.php?threads/workshop-layout-and-dust-collection-ducting-advice.64862/)  
42. Quiet dust collection options : r/woodworking \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/woodworking/comments/yde2l6/quiet\_dust\_collection\_options/](https://www.reddit.com/r/woodworking/comments/yde2l6/quiet_dust_collection_options/)  
43. How to Make Blast Gates for Your Woodworking Shop Dust Collection System, accessed February 28, 2026, [https://benchblog.com/how-tos/how-to-make-blast-gates-for-your-woodworking-shop-dust-collection-system/](https://benchblog.com/how-tos/how-to-make-blast-gates-for-your-woodworking-shop-dust-collection-system/)  
44. How To Build A Soundproof Baffle Box, accessed February 28, 2026, [https://www.soundproofyourstudio.com/blog/how-to-build-a-soundproof-baffle-box](https://www.soundproofyourstudio.com/blog/how-to-build-a-soundproof-baffle-box)  
45. Sound proofing dust collector in garage wood shop : r/woodworking \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/woodworking/comments/wuvfhp/sound\_proofing\_dust\_collector\_in\_garage\_wood\_shop/](https://www.reddit.com/r/woodworking/comments/wuvfhp/sound_proofing_dust_collector_in_garage_wood_shop/)  
46. Sound Proof Enclosure for MPCNC \- Advice \- V1E.com Forum, accessed February 28, 2026, [https://forum.v1e.com/t/sound-proof-enclosure-for-mpcnc/8645](https://forum.v1e.com/t/sound-proof-enclosure-for-mpcnc/8645)  
47. How does mechanical ventilation keep the humidity lower than the outside air it brings in? \- Green Building Forum, accessed February 28, 2026, [https://www.greenbuildingforum.co.uk/newforum/comments.php?DiscussionID=15354](https://www.greenbuildingforum.co.uk/newforum/comments.php?DiscussionID=15354)  
48. MVHR vs Dehumidifier \- Smart Ventilation, accessed February 28, 2026, [https://smart-hrv.co.uk/mvhr-vs-dehumidifier/](https://smart-hrv.co.uk/mvhr-vs-dehumidifier/)  
49. Best (safe) way to heat and cool a woodworking workshop?, accessed February 28, 2026, [https://ncwoodworker.net/forums/index.php?threads/best-safe-way-to-heat-and-cool-a-woodworking-workshop.45871/](https://ncwoodworker.net/forums/index.php?threads/best-safe-way-to-heat-and-cool-a-woodworking-workshop.45871/)  
50. Solar Powered shop? \- NC Woodworker, accessed February 28, 2026, [https://ncwoodworker.net/forums/index.php?threads/solar-powered-shop.61215/](https://ncwoodworker.net/forums/index.php?threads/solar-powered-shop.61215/)  
51. Possible to power my shop totally off grid? | DIY Solar Power Forum, accessed February 28, 2026, [https://diysolarforum.com/threads/possible-to-power-my-shop-totally-off-grid.14105/](https://diysolarforum.com/threads/possible-to-power-my-shop-totally-off-grid.14105/)  
52. Please recommend a setup for power tool usage : r/SolarDIY \- Reddit, accessed February 28, 2026, [https://www.reddit.com/r/SolarDIY/comments/1np4t67/please\_recommend\_a\_setup\_for\_power\_tool\_usage/](https://www.reddit.com/r/SolarDIY/comments/1np4t67/please_recommend_a_setup_for_power_tool_usage/)  
53. iVAC Pro Blast Gates, accessed February 28, 2026, [https://www.ivacswitch.com/ivac-pro-blast-gate/](https://www.ivacswitch.com/ivac-pro-blast-gate/)  
54. iVac for Professionals, Schools and Institutions, accessed February 28, 2026, [https://www.ivacswitch.com/ivac-for-diyers-and-hobbyists/ivac-for-professionals/](https://www.ivacswitch.com/ivac-for-diyers-and-hobbyists/ivac-for-professionals/)  
55. Self‐Powered Autonomous Electrostatic Dust Removal for Solar Panels by an Electret Generator \- PMC, accessed February 28, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11234423/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11234423/)  
56. Dust worries | DIY Solar Power Forum, accessed February 28, 2026, [https://diysolarforum.com/threads/dust-worries.112228/](https://diysolarforum.com/threads/dust-worries.112228/)  
57. IVAC Pro Blast Gate \- Automated Dust Collection System Component (4 Units), accessed February 28, 2026, [https://loitx.com/IVAC-Pro-Blast-Gate-Automated-Dust-Collection-System-Component-f-797735](https://loitx.com/IVAC-Pro-Blast-Gate-Automated-Dust-Collection-System-Component-f-797735)  
58. IVAC PBG04 Pro Blast Gate \- Automated Dust Collection System For Workshop | Wireless Control For Dust Management, accessed February 28, 2026, [https://atcnts.com/780973/Gate-Automated-Dust-Collection-System-For-Workshop-Wireless](https://atcnts.com/780973/Gate-Automated-Dust-Collection-System-For-Workshop-Wireless)  
59. DIY Remote Blast Gates for the workshop | No Soldering, No Coding, Beginner Friendly, accessed February 28, 2026, [https://www.youtube.com/watch?v=aydZuas7LyM](https://www.youtube.com/watch?v=aydZuas7LyM)