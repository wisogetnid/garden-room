import re

with open('plans/MASTER_PLAN.md', 'r') as f:
    master_content = f.read()

# Pattern to find the section
pattern = re.compile(r"## Step-by-Step Construction Phases \(Overview\).*?---\n\n", re.DOTALL)
match = pattern.search(master_content)

if match:
    overview_text = match.group(0)
    # Remove from master plan
    master_content = master_content.replace(overview_text, "")
    with open('plans/MASTER_PLAN.md', 'w') as f:
        f.write(master_content)
    
    # Add to workplan
    with open('plans/WORKPLAN.md', 'r') as f:
        work_content = f.read()
    
    # Insert before Phase 1
    insert_point = "## 🗓️ Phase 1: Groundworks & The Floating Raft"
    work_content = work_content.replace(insert_point, overview_text + insert_point)
    
    with open('plans/WORKPLAN.md', 'w') as f:
        f.write(work_content)
    print("Successfully moved overview.")
else:
    print("Could not find overview in Master Plan.")
