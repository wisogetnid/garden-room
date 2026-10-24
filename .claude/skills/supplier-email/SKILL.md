---
name: supplier-email
description: Draft concise emails to building suppliers and merchants (quote requests, stock and lead-time questions, delivery quotes to the Isle of Wight, follow-ups on quotes). Use whenever the user asks to write, draft or reply to an email to a supplier, merchant, manufacturer or installer.
---

# Supplier Emails

Draft emails the user sends themselves. Never send anything.

## Principles

- **Concise.** Suppliers know their trade. Don't explain why you need something or how it will be used, and don't spell out what they'd obviously tell you anyway (delivery method, kerbside terms, whether they understood a term).
- **One term per thing.** Use one expression, not a term plus its synonym in brackets. They'll ask if they don't understand.
- **Keep materials generic** (type, size, quantity), so the supplier can offer what they stock. Name a specific brand or product only when:
  - it's a core element of the build (e.g. the dMVHR unit, windows, SIP system), or
  - the supplier lists that item on their own website or shop. Then give its exact name and **the product URL**: it removes all doubt.
- **No deadlines.** Ask for the lead time instead. If something is out of stock or not stocked, ask for a substitute.
- **Quantities come from the plan** (`plans/MASTER_PLAN.md`, the supplier lists in `research/suppliers/`, the order lists in `comms/`). Round to the supplier's pack sizes.
- **Project rules still apply:** Torx / T-STAR screws only, never Pozi or Phillips.

## Structure

1. **Subject:** what is being asked + delivered to Isle of Wight (PO31 7JY), when delivery applies.
2. **Greeting:** "Hello,".
3. **One opening line:** e.g. "I'd like a delivered quote for the following, for a garden room build on the Isle of Wight:".
4. **Numbered item list:** name (or generic spec), size, pack: quantity. Product URL on the next line when it is the supplier's own item.
5. **Numbered questions:** each starts with a short bold label (**Delivery:**, **Stock:**, **Substitute:**, ...), one or two sentences each. Typical questions:
   - total cost including carriage to the address, all items in one delivery;
   - for items shown out of stock: when they're expected back, the lead time and a possible substitute;
   - one factual product question the website doesn't answer.
6. **Sign-off:**
   ```
   Thank you,
   Tobias Vogel
   31 Coronation Road, Cowes, PO31 7JY
   [phone number]
   ```

## Output

Show the draft in the reply between horizontal rules, ready to paste. Then note anything to fill in (placeholders) and the supplier's contact address or phone number if it has been found. Mark an address as unconfirmed if it hasn't been checked.

## Example

---

**Subject:** Quote request: 60mm XPS boards + 60mm base track, delivered to Isle of Wight (PO31 7JY)

Hello,

I'd like a delivered quote for the following, for a garden room build on the Isle of Wight:

1. Kingspan GreenGuard GG300 R, 60mm, 1250 × 600mm, pack of 7: 1 pack
   https://www.insulationsuperstore.co.uk/product/kingspan-greenguard-gg300-r-rigid-extruded-polystyrene-60mm-5-25m2.html
2. Wemico 0.6mm Aluminium Base Track, 60mm, box of 10 × 2.5m: 1 box
   https://www.insulationsuperstore.co.uk/product/wemico-0-6mm-aluminium-base-track-60mm-box-of-10-2-5m-lengths.html

Could you please let me know:

1. **Delivery:** the total cost, including carriage, to Cowes, Isle of Wight, PO31 7JY, with both items in one delivery.
2. **Stock:** the base track shows as out of stock. When do you expect it back, and what's the lead time for both items together? If it's not available soon, is there a substitute?
3. **Drip edge:** does the 60mm base track have a drip edge? Do you have matching corner pieces or connectors?
4. **Rebate:** on the GG300 R boards, which edges are rebated (long edges only, or all four), and what size is the rebate?

Thank you,
Tobias Vogel
31 Coronation Road, Cowes, PO31 7JY
[phone number]

---
