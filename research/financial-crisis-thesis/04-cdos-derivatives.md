# Section 4 — CDOs, Synthetic CDOs, and the Derivative Layer

## How Mortgage Risk Was Multiplied Far Beyond the Mortgage Market

> "The greatest danger lies not in the products themselves, but in the connections between them."
> — Andrew Haldane, Bank of England, "Rethinking the Financial Network," 2009

If the MBS structures of Section 3 were the architecture of mortgage credit, the derivatives layer described in this section was the architecture by which mortgage credit risk metastasized into a global solvency crisis. The CDO and CDS markets did not create the bad loans. They did three things that turned a contained subprime loss into a systemic event:

1. They **repackaged the riskiest tranches of subprime MBS into instruments that were re-rated AAA**, vastly expanding the pool of senior-rated mortgage paper.
2. They **created synthetic exposures** to mortgage risk that did not require any underlying mortgage to exist — effectively allowing multiple investors to be long, and multiple others to be short, the same notional pool.
3. They **concentrated the resulting risk** in a small number of dealer balance sheets and counterparties — most notably AIG Financial Products — whose collapse would have systemic spillover effects.

This is the most technically dense section of Part I. The mechanics matter. Without understanding them, it is impossible to explain why a fundamentally bounded credit problem (perhaps $500 billion of actual subprime mortgage losses) produced a multi-trillion-dollar financial system writedown and required state intervention on a scale unprecedented in peacetime.

---

## 4.1 The CDO: What It Is

A **collateralized debt obligation** is a securitization whose collateral is itself a portfolio of debt securities — corporate bonds, leveraged loans, MBS tranches, ABS tranches, or even other CDOs. The CDO issues its own tranches against this collateral, following the same waterfall logic as an MBS (Section 3) but on a different underlying.

The taxonomy of CDOs (relevant to the crisis):

1. **CLO** — Collateralized *Loan* Obligation. Collateral is leveraged loans (corporate bank loans). This market existed before the crisis and survived it largely intact; CLOs are the subject of Section 9, where they appear in the modern landscape.
2. **CBO** — Collateralized *Bond* Obligation. Collateral is corporate bonds. A modest market in the late 1990s, less relevant post-2001.
3. **ABS CDO** — Collateral is asset-backed securities tranches, typically the mezzanine tranches of MBS, ABS-of-mortgages, or even other CDOs. **This is the structure responsible for the 2008 crisis losses.**
4. **CDO-squared** — Collateral is tranches of other CDOs. A genuine financial nightmare.
5. **Synthetic CDO** — Collateral is a portfolio of CDS contracts referencing other securities, rather than the securities themselves.

The reader should keep these distinctions firmly in mind. CLOs and ABS CDOs are not the same instrument and behaved very differently in the crisis. Popular treatments often conflate them.

---

## 4.2 The Cash ABS CDO

The cash ABS CDO is the workhorse villain of 2007–2008. The structure works as follows:

**Step 1 — Collateral acquisition.** A CDO manager (often an arm of an investment bank, sometimes an independent fund manager like Harding Advisory or GSC Group) accumulates a portfolio of mezzanine tranches of subprime and Alt-A MBS — typically the BBB and BBB− slices. A typical $1 billion ABS CDO might hold:

- 80–100 different mezzanine MBS tranches;
- Drawn from perhaps 70 underlying MBS deals;
- Spanning vintages from 2005, 2006, and 2007;
- Originated through perhaps 20–30 different originators.

**Step 2 — Trust formation.** The collateral is held in a bankruptcy-remote SPV (the CDO trust).

**Step 3 — Liabilities issuance.** The trust issues its own tranches, which are sold to investors:

| Tranche | % of Notional | Approx. Rating | Approx. Coupon (1m LIBOR +) |
|---------|--------------:|---------------:|----------------------------:|
| Super-senior | 60% | AAA | +12–25 bps |
| Senior AAA | 20% | AAA | +30–50 bps |
| Junior AAA | 7% | AAA | +60–90 bps |
| AA | 5% | AA | +100–150 bps |
| A | 3% | A | +250–350 bps |
| BBB | 3% | BBB | +500+ bps |
| Equity | 2% | Unrated | residual |

**Note carefully the rating transformation.** The CDO took collateral whose *highest rating was BBB* (these are mezzanine tranches of MBS) and reissued it as ~87% AAA-rated bonds. This is the "magic" of CDOs: a pool of BBB-rated paper, repackaged with subordination, generated mostly AAA paper.

How does this work mathematically? It works *if and only if* the defaults in the underlying BBB collateral are imperfectly correlated. If the BBBs default independently, with say 20% individual default probability, then a portfolio of 100 of them will lose close to 20% of notional with very small variance, and a senior tranche with 40% subordination will be safe. If the BBBs default with correlation near 1, the portfolio will either lose 0% or near-100%, and no level of subordination protects the senior tranche.

The Gaussian copula models (Section 3.8) typically assumed BBB-MBS default correlations in the 0.2–0.3 range. The actual correlation under stress was approximately 1.0. This is why the structure broke.

**Step 4 — Risk transfer.** The investment bank arranging the CDO sells the senior tranches to investors hunting yield over Treasuries (institutional money market funds, foreign banks, GSEs, asset managers, structured investment vehicles). The bank often retains the super-senior tranche on its own balance sheet — frequently hedged with an AIG-FP credit default swap (Section 4.6). The mezzanine and equity tranches are sold to hedge funds and CDO-squared structures.

### Why the Bank Retained the Super-Senior

This is the structural quirk that brought down Citigroup, UBS, Merrill Lynch, and several others. A super-senior tranche — the top 60% of an ABS CDO — was generally regarded as so far away from any conceivable loss that it carried minimal default risk. Its yield over LIBOR was only 12–25 bps, too low to attract third-party investors at scale, but the bank could hold it on its own book and earn a small positive carry over its funding cost. The bank's capital charge for holding super-senior AAA was minimal under Basel I (20% risk weight at most) and zero on the trading book if marked to model.

What looked like an arbitrage — a positive-spread asset with near-zero capital cost — was in fact an enormous concentrated tail-risk position. When the underlying mezz collateral collapsed in 2007–2008, the super-senior tranches that banks had retained went from "money-good" to severely impaired in months. Citigroup wrote down approximately $40 billion on retained super-senior CDO positions; Merrill Lynch wrote down more than $30 billion; UBS more than $50 billion. The aggregate retained super-senior losses across the global banking system were on the order of $200–400 billion.

The retained super-senior position was an unhedged tail-risk bet that ate the banks' capital. It is the proximate cause of the banking sector's recapitalization needs in 2008–2009.

---

## 4.3 CDO-Squared

A CDO-squared is a CDO whose collateral is tranches of *other* CDOs. The construction is identical in form to an ABS CDO, but the underlying is even further removed from the original mortgage loans.

A representative CDO-squared collateral portfolio might consist of 50 mezzanine tranches of ABS CDOs, each of which in turn has 70 mezzanine tranches of subprime MBS as its collateral. The CDO-squared therefore has *indirect* exposure to perhaps 3,500 different MBS tranches, and through them to perhaps 500,000 underlying mortgage loans. The investor in a CDO-squared tranche cannot, in any practical sense, perform diligence on the actual underlying credit exposure.

CDO-squared structures were predominantly a 2005–2007 phenomenon. They emerged because:

- The mezzanine tranches of cash ABS CDOs were hard to place — there were too many of them being issued and not enough natural mezzanine buyers.
- A CDO-squared could repackage the unsold mezz CDO paper into new AAA, AA, and A tranches that *could* be sold.
- The model assumed (again) low correlation among ABS CDO defaults — even less defensible than the assumption of low correlation among subprime MBS defaults.

When the crisis came, CDO-squared performance was even worse than ABS CDO performance, because the layering of correlation errors compounded. Many CDO-squared issues experienced 100% loss of original principal across every tranche, including the original AAA.

---

## 4.4 The Synthetic CDO

A synthetic CDO is a CDO whose "collateral" is not bonds but a *portfolio of credit default swap contracts*. Understanding this requires first understanding the CDS instrument.

### 4.4.1 The Credit Default Swap (CDS)

A credit default swap is a bilateral contract between a **protection buyer** and a **protection seller**, referenced to a specific underlying credit (a corporate bond, a sovereign bond, or — in our case — an MBS or ABS tranche). The contract works as follows:

- The protection buyer pays a periodic premium (the "spread") to the protection seller, typically quarterly, expressed in basis points per annum on the notional amount.
- If the reference credit experiences a defined "credit event" (default, bankruptcy, failure to pay, restructuring — defined precisely in the ISDA standard documentation), the protection seller pays the protection buyer the loss on the reference credit, typically through a physical delivery of the bond at par or, more commonly, cash settlement after an auction-determined recovery price.

The protection buyer is *long credit protection* — they benefit from a default. The protection seller is *short credit protection* — they pay if a default occurs.

Two parallels make CDS easier to understand intuitively:

- **Insurance**: protection buyer pays premiums to protection seller, who pays out on a loss event. But CDS has no insurable-interest requirement (you can buy protection on a bond you don't own) and no regulatory framework for reserves.
- **A short position**: protection buyer profits if the reference credit deteriorates. CDS allows short-selling of credit without locating and borrowing the underlying bond. This is the "naked CDS" use case — and it is what the Big Short investors used to short subprime.

The CDS market in 2007–2008 was enormous. The Bank for International Settlements reported total notional CDS outstanding peaking at approximately $58 trillion in mid-2007 — larger than global GDP, larger than the global stock market, larger than the entire bond market. The vast majority of this exposure was inter-dealer (banks hedging with each other), with the *net* positions much smaller than gross notional. But the gross figures matter for collateral and counterparty risk, especially in stress.

### 4.4.2 ABX and CDX: The Indices

By 2006, the CDS market on subprime ABS had grown sufficiently that standardized indices were created:

- **ABX.HE** — A series of indices launched in January 2006 by Markit, referencing baskets of 20 subprime MBS deals. Each ABX series referenced a specific vintage (06-1, 06-2, 07-1, 07-2) and was sliced into separate indices for each rating bucket (AAA, AA, A, BBB, BBB−).
- **CMBX** — Analogous index for commercial MBS, less central to the crisis.
- **TABX** — A tranche of ABX, allowing exposure to a slice of the index (e.g., the 7–12% tranche of ABX.HE 06-2 BBB).

The ABX created a *liquid, observable* market price for subprime credit. Before ABX, subprime MBS traded over-the-counter in low volumes, with prices reported quarterly at best. After ABX, the price of subprime credit was visible in real time on dealer screens.

The launch of ABX is one of the most important technical events of the crisis. It gave bearish investors a tradable short-vehicle (the BBB tranche of ABX was the canonical short). It also gave the broader market a daily mark-to-market reference for subprime exposure — when ABX.HE.06-2.BBB collapsed in price in February 2007, every holder of BBB subprime exposure took a mark-to-market loss, regardless of whether the underlying collateral had yet defaulted. The accounting consequences of ABX's existence are explored in Section 6.

### 4.4.3 Synthetic CDO Construction

A synthetic CDO replaces the cash collateral of a traditional CDO with a portfolio of CDS contracts. The CDO trust sells protection on, say, 100 reference subprime MBS tranches. The premium income from those CDS contracts funds the coupons on the synthetic CDO's tranches. If the reference subprime tranches default, the trust pays out on the CDS, and those losses flow up the synthetic CDO's waterfall — first eroding the equity tranche, then the mezz, then potentially the senior.

The synthetic structure has critical properties that distinguish it from cash CDOs:

1. **No physical collateral required**: the CDO trust does not need to actually own the reference securities. It only needs to sell CDS on them.
2. **Effectively unlimited supply**: any number of synthetic CDOs can reference the same underlying MBS tranches. There is no constraint from the size of the cash market.
3. **A short counterparty is required**: every synthetic CDO has a "short" party (the protection buyer on the reference portfolio) on the other side. Without a short, the CDO does not exist.

This last point is what made synthetic CDOs structurally explosive. The short side was, by 2006, largely *the same investment banks structuring the deals* — they were taking the short positions in their own synthetic CDOs by serving as the protection buyer counterparty. Goldman Sachs in particular pursued this dynamic aggressively in 2006–2007, sourcing CDS protection on subprime through synthetic deals it was structuring and selling to (often unwitting) investors. The Abacus 2007-AC1 SEC enforcement action (settled by Goldman in 2010 for $550 million) was one of multiple cases involving this dynamic.

### 4.4.4 Why Synthetic CDOs Multiplied Systemic Risk

The cash subprime MBS market was bounded — roughly $1.3 trillion of subprime origination in the peak year 2006, and a slightly smaller amount of MBS issuance. The synthetic market faced no such bound. By 2007, estimates (from FCIC and BIS work) suggest that synthetic exposure to subprime mortgages exceeded the cash market by a factor of 4–10x.

Mechanically: a single $100 million subprime MBS tranche might be the reference asset for $1 billion of CDS contracts on it. Each CDS creates a long-protection (short-credit) and a short-protection (long-credit) position. So the system effectively has $1 billion of synthetic long exposure and $1 billion of synthetic short exposure on the same $100 million of physical bond. The net effect: 10x the actual cash market in dollar-volume terms of credit risk.

When the underlying tranche took a 100% loss, the synthetic chain produced $1 billion of payment obligations from protection sellers to protection buyers — quite apart from the $100 million of cash bond losses. The system had multiplied the credit loss by an order of magnitude — *not because the underlying losses were larger, but because the synthetic structure had created derivative claims on those losses worth multiples of the underlying notional.*

This is the engine that turned a contained mortgage problem into a global solvency crisis. The math is straightforward; the consequences were not.

---

## 4.5 The Collateralized Debt Obligation as Tranche Correlation Trade

Step back from the mechanics and consider what a CDO investor is actually buying.

A senior tranche of a CDO is, in derivatives-pricing terms, a *short option on correlation*. The investor receives a small spread over LIBOR; in exchange, they bear the risk of unexpected joint default behavior in the underlying portfolio. As long as defaults are moderately correlated, the senior tranche's expected loss is near zero — most defaults are absorbed by the mezz and equity below. If correlation spikes (because the underlying defaults turn out to share common drivers), the senior tranche's expected loss balloons — multiple sub-tranches fail simultaneously, and the loss reaches the senior.

The mezzanine tranche of a CDO is, by contrast, a *long option on correlation* in the middle of the distribution. The equity tranche is a *short option on correlation* at the bottom.

This taxonomy was developed in the credit-derivatives quant literature (e.g., Andersen, Sidenius, and Basu 2003; "All your Hedges in One Basket"). It was well understood by sophisticated practitioners. What was less well understood — or was understood but commercially convenient to ignore — was that the correlation parameter being used to price these structures was systematically too low for a portfolio of mortgage-backed mezz securities whose defaults were driven by a common housing market.

A 2007 trade that several Big Short investors made:

- **Short** the AAA tranche of an ABS CDO (or buy CDS protection on it).
- **Long** the equity tranche of the same or similar ABS CDOs (or sell CDS protection on the equity).
- The trade is approximately net-zero on small defaults (equity absorbs them; AAA is untouched).
- The trade is hugely profitable on systemic stress (equity is already gone; AAA collapses too).
- The trade benefits from correlation rising from "what the model assumed" to "what is actually true."

This is, in derivatives-theoretic terms, a **correlation trade**. The Big Short investors did not need housing prices to fall by any specific amount; they needed defaults to be *more correlated* than the structures had been priced to. Given that defaults across a national housing market driven by national underwriting standards are obviously highly correlated, the trade was, ex ante, a near-certainty for whoever could hold the negative carry long enough.

---

## 4.6 AIG Financial Products

AIG Financial Products (AIG-FP) was a subsidiary of American International Group, the world's largest insurer. AIG-FP was nominally a small London-based unit; by 2007 it had become the most important single counterparty in the credit derivatives market.

### What AIG-FP Did

AIG-FP wrote credit default swap protection on the super-senior tranches of cash ABS CDOs — the same 60% slice that the dealer banks retained on their own books. The bank could buy protection from AIG, hedge out the credit risk, free up risk capital, and continue to earn the small positive carry on the super-senior position.

From AIG's perspective:

- The premium income was small (10–30 bps per annum on the super-senior notional).
- The expected loss, by AIG's model, was effectively zero — super-senior AAA-rated paper had a vanishingly small historical default rate.
- The credit was good (the reference was super-senior of AAA — "AAA-of-AAA"), and the counterparty was a dealer bank with strong credit.
- The position was off-balance-sheet for AIG and required no statutory reserves.

The premium income from this business — totaling several hundred million dollars per year by 2006 — was, from AIG-FP's perspective, free money. AIG-FP wrote progressively more of it.

### The Scale

By mid-2007, AIG-FP had written CDS protection on approximately $440 billion of notional reference credit, of which roughly $80 billion was on subprime-CDO-related references. By end of 2008, the subprime-CDO-related notional had grown to approximately $79 billion (after some run-off), and the cumulative collateral demands against this book exceeded $40 billion.

### The Catastrophic Misunderstanding

AIG-FP wrote CDS protection on a one-way basis: it received premium income but, unlike inter-dealer CDS, *did not initially post variation margin against changes in the mark-to-market value of the contracts*. The ISDA Master Agreements that AIG-FP signed with its counterparties had collateral schedules tied to AIG's own credit rating: as long as AIG was AAA-rated, no collateral was required up to certain large thresholds. Below AAA, increasing amounts of collateral were required. Below AA, very large amounts. Below A, essentially the full mark-to-market loss had to be posted as collateral.

AIG-FP's modeling treated the collateral requirement as an unlikely-to-trigger contingency. Internally, the firm believed the probability of AIG losing its AAA rating was negligible, and the probability of the underlying super-senior tranches taking actual cash losses was also negligible. The combined probability of both was assumed to be effectively zero.

Three things went wrong simultaneously:

1. **The reference tranches' market value collapsed**: even before any actual cash default on the super-seniors, the mark-to-market price of these securities (now visible via ABX) plunged in 2007. This triggered "soft" collateral demands on AIG.
2. **AIG's credit rating was downgraded**: from AAA to AA in 2005 (separately related to accounting issues), then further downgraded as the crisis progressed. Each downgrade triggered an additional layer of collateral requirements on the CDS book.
3. **The combined effect was a liquidity death spiral**: the more AIG had to post collateral, the more pressure on its liquidity, the more its credit deteriorated, the more collateral it had to post.

By September 15, 2008 (the day of Lehman's bankruptcy), AIG had received cumulative collateral demands of approximately $32 billion on its CDS portfolio and was projecting demand for tens of billions more. The firm had insufficient liquid assets to meet the demand. Without an immediate intervention, AIG would have defaulted on the CDS contracts.

### Why AIG's Default Would Have Been Systemic

AIG was the protection seller to nearly every major global bank: Goldman Sachs, Société Générale, Deutsche Bank, Merrill Lynch, UBS, Calyon, Barclays, Banco Santander, Royal Bank of Scotland — the list runs to dozens of counterparties. A failure of AIG to pay out on its CDS book would have:

1. Voided the hedges that allowed banks to carry the super-senior CDO retentions at zero (or low) capital charge — forcing them to recognize the underlying credit losses immediately.
2. Imposed counterparty losses on the banks for the unpaid CDS receivables — at notional values that, summed across counterparties, ran to many tens of billions of dollars.
3. Triggered cross-default provisions in AIG's other obligations, including its securities lending business (separately, AIG's securities lending operation had been investing collateral in subprime — another concentrated tail-risk position).
4. Cascaded into the broader insurance industry: AIG's various insurance subsidiaries owed obligations to policyholders and held reserves that would have been at risk in a parent-level bankruptcy.

The Federal Reserve's September 16, 2008 emergency lending facility to AIG ($85 billion initial, ultimately exceeding $180 billion through various Treasury and Fed programs) was undertaken because the alternative — AIG's failure 24 hours after Lehman — was assessed to be catastrophic. The Fed's Maiden Lane III vehicle was specifically designed to absorb the worst of AIG's super-senior CDO CDS exposure at par value to dealers, effectively bailing out the dealer banks through AIG.

The AIG intervention has been criticized on multiple grounds (excessive payments to dealer counterparties; lack of haircuts on the CDS settlements; ad hoc legal authority). The deeper question raised by the AIG case is not whether the intervention was handled optimally but how a single insurance-company subsidiary in London was permitted to accumulate counterparty exposure that, when stressed, threatened the solvency of every major global bank.

The answer involves the Commodity Futures Modernization Act of 2000 (Section 1.9), the lack of any central clearing for CDS, the absence of margining requirements, and the lack of supervisory authority over OTC derivatives. These are not modeling failures or trader errors — they are policy choices that allowed a counterparty risk concentration of historic proportions to develop in plain sight.

---

## 4.7 Counterparty Risk and the Collateral Spiral

The AIG story generalizes. The credit derivatives market in 2007–2008 was characterized by:

- Bilateral OTC contracts with no central clearing.
- Variable collateral terms — some counterparties posted variation margin daily; others didn't.
- Rating-dependent collateral thresholds — downgrades triggered collateral calls.
- Concentrated exposures — a handful of dealers and AIG accounted for most of the net positions.

When credit deteriorated:

1. **Marks moved against protection sellers** as ABX, CMBX, and CDX prices fell.
2. **Collateral demands rose** from protection buyers to protection sellers.
3. **Protection sellers had to fund collateral postings**, often by selling other assets into stressed markets, depressing those prices further.
4. **Counterparty creditworthiness deteriorated**, raising collateral demands further.
5. **A "liquidity spiral"** developed: protection sellers' liquidity drained even as their solvency may not have been impaired.

This dynamic was central to the 2008 collapse. The dealers were both protection buyers (from AIG and others) and protection sellers (to hedge funds and clients). When their counterparties needed cash, they pulled cash from the dealers. When the dealers were stressed, they pulled cash from their own counterparties. The system became a mutual margin call.

The systemic implication: even if no underlying credit ultimately defaulted, the *funding requirements* of the derivative market could force institutions into insolvency. A solvent but illiquid bank in a fully-collateralized derivatives market is, in a stress event, indistinguishable from an insolvent one. This is the canonical "liquidity-solvency confusion" of financial crises — and Section 6 will return to it in the context of Bear Stearns and Lehman.

---

## 4.8 The Monoline Bond Insurers

A separate counterparty story involves the monoline bond insurers — MBIA, Ambac Financial, Financial Guaranty Insurance Company (FGIC), Financial Security Assurance (FSA), and a few smaller firms. Originally chartered to wrap municipal bonds, the monolines expanded into structured finance in the 2000s, writing wraps on senior tranches of MBS and ABS CDOs.

The monolines were small relative to AIG — their combined statutory capital was in the tens of billions of dollars, against insured notional exposure of roughly $2.5 trillion at peak. Their credit ratings were AAA (essential to the wrap business: a wrapped bond inherited the monoline's rating). When MBIA and Ambac were downgraded in 2008 (Moody's downgraded MBIA to Aa3 in June 2008; S&P followed), wrapped bonds were simultaneously downgraded, with cascade effects on banks holding those bonds.

The monolines did not, individually, threaten the system as AIG did. Their collective downgrade did contribute to the spread-widening and mark-to-market loss avalanche of 2008.

---

## 4.9 The Dealer Bank Balance Sheet in 2007

To make the leverage picture concrete, consider the simplified pre-crisis balance sheet of a representative dealer bank:

```
                  ASSETS                          LIABILITIES + EQUITY
        ┌────────────────────────────┐    ┌────────────────────────────┐
        │ Cash and equivalents       │    │ Customer deposits          │
        │ Trading book inventory:    │    │ Short-term unsecured debt   │
        │   - Cash MBS                │    │ Repo financing             │
        │   - CDO super-senior        │    │ Commercial paper            │
        │     (retained)              │    │ Medium-term notes           │
        │ Loans (corporate, real estate)│    │ Long-term debt              │
        │ Other receivables          │    │ Equity                     │
        │ Goodwill                   │    │  (4–5% of total assets)    │
        └────────────────────────────┘    └────────────────────────────┘
                  Leverage: ~25:1 (commercial bank), 30–40:1 (investment bank)
```

Key features:

- **Long-dated, illiquid assets** (CDO tranches, retained super-seniors, loans to leveraged buyouts) financed by **short-term, market-based funding** (repo, commercial paper).
- **Mark-to-market accounting** on the trading book — daily price moves directly impacted reported earnings and capital.
- **Off-balance-sheet exposures** — conduits, structured investment vehicles (SIVs), and synthetic positions not consolidated under pre-crisis accounting rules.
- **Concentrated counterparty exposures** to AIG, monolines, and other dealers via derivatives.

When the asset side took mark-to-market losses, equity was eroded. When the liabilities side (repo, commercial paper) refused to roll, the bank had to either sell assets (at fire-sale prices) or obtain emergency funding. The leverage made the equity cushion thin; the asset-liability maturity mismatch made the funding fragile; the concentrated counterparty exposures made the failure modes correlated.

This is the structural setup that detonated in 2007–2008, and the mechanics of the detonation are the subject of Section 6.

---

## 4.10 Value-at-Risk and Model Risk

A separate but adjacent failure was in the *risk management methodology* of major financial institutions. Most large banks managed market risk through some variant of **Value-at-Risk (VaR)**, typically expressed as the loss that the trading book would not exceed with 95% or 99% confidence over a 1-day or 10-day horizon.

VaR has well-known weaknesses, including:

1. **It tells you nothing about the tail beyond the confidence threshold.** A 99% 1-day VaR of $100mm tells you that on 1 day in 100 you would lose more than $100mm. It does not tell you whether the loss on that day would be $101mm or $10 billion.
2. **It is typically estimated from a short historical window** (250 or 500 days), and thus produces low VaR readings during calm periods and high readings during volatile periods. This means it *contracts pro-cyclically* — banks report low risk and increase position size during calm, and report high risk and de-risk into a panic, amplifying the cycle.
3. **It does not handle correlation regime changes well.** Pre-crisis VaR models calibrated on 2003–2006 data systematically understated the joint risk of mortgage and credit positions in stress.

Beyond these familiar issues, the crisis revealed a more specific problem with how VaR was applied at major banks: positions in illiquid structured credit (CDOs, super-senior retentions) were marked-to-model rather than to market, and the models used the same correlation assumptions that had produced the bad ratings in the first place. The risk reports produced by these systems essentially could not see the tail.

Several quantitative analysts at major firms (Til Schuermann at the NY Fed, Andrew Haldane at the Bank of England, several Goldman Sachs and Deutsche Bank model-validation teams) raised concerns about this prior to the crisis. The concerns were generally accepted as accurate in principle but did not translate into commercial action — partly because the alternative (de-risking) was costly in the short term, and partly because the entire industry was using comparable methodologies, so any individual firm that broke ranks would lose return-on-equity relative to peers.

This is a recurring pattern in financial crises and worth naming explicitly: when the dominant industry methodology for risk measurement contains a systematic error, and the error reduces measured risk and increases reported returns, no individual firm has an incentive to correct the error unilaterally. Correction must come from regulation, market collapse, or both.

---

## 4.11 Why "Tail Risk Blindness" Is the Right Frame

Different observers have offered different unifying frames for the crisis: "greed," "fraud," "regulatory failure," "subprime lending," "rating agencies," "leverage." Each has truth. But the most precise technical frame is **tail risk blindness**:

- The pricing of structured credit assumed loss distributions whose tails were too thin.
- The capital regimes assumed risk weights whose dispersion was too narrow.
- The risk management systems assumed return distributions whose tails were too thin.
- The compensation systems rewarded carry trades that resembled selling deep out-of-the-money options.
- The macro environment had suppressed realized tail events for long enough that the priors of the entire system had shifted.

The financial system in 2006–2007 was, in a deep sense, a massive aggregate sale of tail risk. The buyers (the Big Short investors) were a small minority of capital. The sellers were essentially the entire institutional financial system — banks, money market funds, insurance companies, pension funds, sovereign wealth funds, GSEs, individual investors via 401(k) mutual funds. When the tail event arrived, the sellers had no aggregate capacity to absorb the loss they had collectively underwritten. The state stepped in not because the loss was unconscionable but because no remaining private balance sheet was large enough to hold it.

Section 5 examines how the few buyers of that tail risk identified the trade. Section 6 examines what happened when the system tried to absorb the realized loss.

---

## 4.12 Numerical Worked Example: The Path of a Single Mortgage

To make Sections 2–4 concrete, follow the path of a single representative subprime mortgage through the structured finance machinery.

**The loan:**
- Borrower: Florida homeowner, FICO 605, stated income, 95% LTV.
- Originator: New Century Financial.
- Loan amount: $250,000.
- Product: 2/28 ARM, 7.5% initial, +6.0% margin over 6m LIBOR, no prepayment penalty after 24 months.
- Date: April 2006.

**Step 1: Origination.** Broker collects $7,500 in origination fees + YSP. New Century closes the loan and funds it via warehouse line.

**Step 2: Sale to aggregator.** Loan sold within 60 days to investment bank "X" (the aggregator) at 101 (1% premium to par). New Century earns $2,500 gain on sale plus interest carry. EPD clause covers 90 days.

**Step 3: Pool aggregation.** Loan added to a $1.2bn pool of similar loans being assembled for securitization. Pool composition finalized over 3 months.

**Step 4: Securitization.** Pool placed into "X 2006-7" Trust. Tranches issued:
- A-1 super-senior $900mm AAA (75% of pool)
- A-2 senior $108mm AAA (9%)
- M-1 thru M-6 mezz approximately $120mm spread across AA to BBB- (10%)
- B and equity approximately $72mm (6%)

Our specific $250,000 loan represents 0.02% of the pool.

**Step 5: Mezz tranche sold to CDO.** The BBB tranche of X 2006-7 ($30mm) is sold to "ABS CDO Y 2007-3" — an ABS CDO managed by an external advisor and structured by bank X.

**Step 6: CDO tranches issued.** Y 2007-3 has $1bn total notional, collateralized by 80 BBB tranches drawn from 80 subprime MBS deals. It issues:
- Super-senior $600mm AAA (60%)
- Senior AAA $200mm AAA (20%)
- Junior AAA $70mm AAA (7%)
- AA $50mm (5%)
- A $30mm (3%)
- BBB $30mm (3%)
- Equity $20mm (2%)

The $30mm BBB tranche of X 2006-7 (which has $250k of our loan) is now part of the $1bn collateral of Y 2007-3.

**Step 7: Super-senior wrapped by AIG-FP.** Bank X retains the $600mm super-senior of Y 2007-3 on its balance sheet, hedged by purchasing CDS protection from AIG-FP at 25 bps per annum.

**Step 8: Synthetic CDO references Y 2007-3.** Separately, "Synthetic CDO Z 2007-1," a $500mm synthetic structured by a different bank, has Y 2007-3's mezz tranche in its reference portfolio. Z also references many other tranches from many other CDOs and MBS deals.

**Step 9: CDO-squared references Y and other CDOs.** "CDO-Squared W 2007-1" holds Y 2007-3's mezz tranche, along with mezz tranches from 30 other CDOs. W issues its own $700mm of tranches, mostly rated AAA.

**Step 10: CDS on W.** Various market participants buy and sell CDS on tranches of W, including some hedge funds going short. The total CDS notional on W's tranches exceeds W's cash notional.

**By the end of 2007 our single $250,000 mortgage is part of:**

- The $1.2 billion cash MBS pool (X 2006-7).
- The $1 billion ABS CDO (Y 2007-3) via the mezz tranche.
- The $500 million synthetic CDO (Z 2007-1) via the reference portfolio.
- The $700 million CDO-squared (W 2007-1) via Y's mezz.
- Multiple CDS contracts referencing tranches of all of the above.
- The ABX.HE 06-2.BBB index, which includes X 2006-7.

The total derivative and structured notional exposure that depends, in part, on whether *that one Florida borrower* keeps paying her mortgage is conservatively over $10 million — 40x the original loan size — and could plausibly run higher if rehypothecation and inter-dealer CDS positions are counted.

**The default:** The borrower defaults in May 2008 at the ARM reset. Her property sells in foreclosure for $145,000 net of costs in March 2009 (Florida prices have fallen 35% peak-to-trough). The loss on the original mortgage: $105,000 (42% of unpaid principal).

This single loss propagates through:

- The X 2006-7 pool: $105k is added to cumulative losses.
- The BBB tranche of X 2006-7: takes incremental loss (the mezz absorbs first).
- The Y 2007-3 CDO: takes incremental loss in its equity, then mezz.
- The W 2007-1 CDO-squared: similar.
- The CDS contracts on all of the above: protection sellers owe variation margin and ultimately payouts.
- The AIG-FP book: needs to post collateral as marks deteriorate.

By the time this single mortgage's default has played out across the system, the dollar value of writedowns and collateral postings is far larger than the underlying $105,000 loss — perhaps several million dollars in propagated impact. Multiply by millions of similar defaults, and the system-wide impact runs into hundreds of billions to low trillions of dollars.

This is the meaning of "multiplied systemic risk." The base loss is bounded by the mortgage market. The propagated loss is bounded only by the gross notional of the derivative overlay, which was multiples of the cash market and existed in a regulatory vacuum.

---

## 4.13 Closing Frame for Section 4

The derivatives layer is the reason the 2008 crisis was global rather than a contained U.S. mortgage problem. The mechanics of CDOs and synthetic CDOs created multiple distinct vehicles by which losses on a single underlying mortgage could propagate into derivative exposure 10x or more the size of the loan. The concentration of synthetic exposure at AIG-FP and the dealer banks meant that those losses, once realized, were absorbed by a small number of institutions whose failure would have systemic spillover effects.

The next section examines how a small number of investors — operating without inside information, often using publicly available data — identified the structural mispricing of these instruments and constructed trades to profit from the unwind. They are commonly remembered as visionaries; in the technical sense, they were correlation traders who recognized that the system's pricing of joint mortgage default was systematically too low and that the appropriate vehicle for expressing that view was credit default swaps on the BBB tranches of subprime MBS and CDO indices.
