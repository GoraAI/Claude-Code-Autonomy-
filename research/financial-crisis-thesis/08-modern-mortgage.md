# Section 8 — The Modern Mortgage Market

## A Structural Map of U.S. Residential Mortgage Credit as of 2026

> "The cure for the 2008 mortgage crisis was the elimination of the kinds of mortgages that caused it. The unintended consequence is a mortgage market that is overwhelmingly agency-guaranteed, federally regulated, and structurally dependent on the post-2008 monetary regime to function at all."
> — Composite paraphrase of arguments in FHFA, Urban Institute, and AEI Housing Center research, 2023–2025

This section maps the U.S. residential mortgage market as it stands roughly fifteen years after the 2008 crisis. The objective is to identify how the market has been restructured, where the post-crisis reforms have been effective, where new structural features have emerged, and what residual or new fragilities exist. The treatment is descriptive and analytical, not predictive.

The dominant structural fact: the U.S. residential mortgage market is, in 2026, predominantly an *agency* market. Over 60% of outstanding mortgage debt is held in securities guaranteed by Fannie Mae, Freddie Mac, or Ginnie Mae. The private-label securitization market that produced the 2008 crisis is, in volume terms, a small fraction of its pre-crisis size. The mortgage market has, in a meaningful sense, been *nationalized in everything but name* — the federal government, through the GSEs in conservatorship, directly guarantees the credit risk on the majority of U.S. home loans.

This section first describes the structural shape of today's market, then examines underwriting and credit quality, then surveys the major affordability and household-balance-sheet dynamics, then identifies institutional structures (servicer concentration, non-bank originator dominance, MBS investor composition) that have changed materially since 2008.

---

## 8.1 The Size and Shape of the Market

### 8.1.1 Aggregate metrics

The U.S. residential mortgage market in 2026 is approximately:

| Metric | Approximate Value (2026) |
|--------|-------------------------:|
| Outstanding U.S. residential mortgage debt | ~$13.5 trillion |
| Of which: held in agency MBS | ~$9.0 trillion |
| Of which: held in private-label / non-agency | ~$0.7 trillion |
| Of which: held on bank balance sheets (whole loans) | ~$2.5 trillion |
| Of which: HELOCs and home equity | ~$0.5 trillion |
| Of which: government-direct loans (FHA, VA portfolios) | ~$0.8 trillion |
| Total U.S. household debt (all forms) | ~$18.5 trillion |
| Mortgage share of household debt | ~73% |

*Approximate ranges, drawn from Federal Reserve Z.1 Flow of Funds, FHFA conforming loan data, and SIFMA fact book. Numerical values are illustrative of the magnitudes and structural ratios; exact figures fluctuate quarter to quarter.*

The agency MBS market is among the deepest fixed-income markets in the world. Daily TBA volume routinely exceeds $200 billion. The Fed's MBS holdings, accumulated through QE programs from 2009 forward, peaked above $2.7 trillion and remain a material share of the outstanding agency MBS universe — meaning that the largest single holder of U.S. mortgage credit is the central bank.

### 8.1.2 The agency dominance

The pre-2008 distinction between conforming (GSE-eligible) and non-conforming (private-label) loans persists, but the relative scale has inverted relative to peak-bubble years. Approximately 70% of new mortgage originations in 2026 are conforming and securitized through Fannie, Freddie, or Ginnie. The remaining 30% is split between:

- **Jumbo prime**: loans above the conforming limit ($766,550 in most areas in 2024; higher in high-cost markets). Typically held on portfolio by large banks or sold to insurance companies/REITs. High-quality, fully documented loans to high-income borrowers.
- **Non-QM (Non-Qualified Mortgage)**: a successor category for loans that don't meet the CFPB's Qualified Mortgage standard. Often originated for self-employed borrowers with non-traditional income documentation; smaller market than pre-crisis subprime but the closest functional analog.
- **CRA-driven portfolio lending**: lending to borrowers in low-income census tracts or with low FICO scores held on bank balance sheet to satisfy Community Reinvestment Act obligations.
- **Bank portfolio**: large banks (JPMorgan, Wells Fargo, Bank of America) holding selected jumbo and high-net-worth lending on balance sheet rather than securitizing.

### 8.1.3 The non-bank originator phenomenon

A structural shift that occurred *after* the 2008 crisis: non-bank mortgage originators (independent mortgage companies — IMCs) have come to dominate originations. Rocket Mortgage (formerly Quicken Loans), United Wholesale Mortgage, Fairway Independent, loanDepot, and others are now larger originators than most traditional banks. Approximately 65% of U.S. mortgage originations in 2026 are from non-bank originators.

This is paradoxical given that the 2008 crisis was, in part, about non-bank originators (Countrywide, IndyMac, New Century) producing low-quality loans. The post-crisis evolution:

- **Bank originators retreated** from mortgage originations after taking large losses. Wells Fargo dramatically scaled back; Bank of America similarly. The capital and regulatory cost of mortgage origination at a G-SIB became unattractive relative to other business lines.
- **The CFPB's Qualified Mortgage rule** standardized underwriting; non-bank originators could now compete on operations and customer experience without taking the same kinds of credit-quality risks pre-crisis subprime originators had taken.
- **GSE securitization** absorbs the credit risk; non-bank originators originate-to-sell and recycle warehouse credit. The originate-to-distribute model survived the crisis essentially intact in the agency channel.

The non-bank dominance has structural implications:

1. **Warehouse funding fragility**: non-bank originators rely on bank-provided warehouse lines to fund originations between closing and sale to the GSEs. In a stress event (such as the COVID-19 spread widening in March 2020), warehouse lenders can withdraw lines, threatening the operational solvency of non-bank originators.

2. **Servicing concentration**: non-bank servicers (Mr. Cooper, Pennymac, Lakeview Loan Servicing) now service a large share of GSE and Ginnie Mae loans. Their financial structures differ from bank servicers; they hold mortgage servicing rights (MSRs) as a major balance-sheet asset and finance them with corporate debt. MSR valuation is sensitive to prepayment speeds and interest rates, and a sharp rate move can produce significant fair-value swings.

3. **Operational continuity risk**: in a stress event in which a large non-bank originator/servicer fails, the GSEs and Ginnie Mae have limited tools to maintain continuity of servicing on the loans. Ginnie Mae faces particularly acute risk on its FHA/VA portfolios, where servicer advances of taxes and insurance must be funded by the servicer pending recovery from sale of the property.

The 2022–2023 period saw notable stress at non-bank servicers as MSR values fell sharply with rates. Several smaller servicers exited the business. Larger servicers like Mr. Cooper continued to operate but with elevated funding costs.

---

## 8.2 Underwriting Standards Today

### 8.2.1 The Qualified Mortgage (QM) framework

The Dodd-Frank Ability-to-Repay rule (12 CFR §1026.43) and the related Qualified Mortgage standard fundamentally reshaped mortgage underwriting. The QM framework defines a category of mortgage loans that automatically satisfies the lender's ability-to-repay obligation. To qualify, a loan must:

- Have a maximum debt-to-income ratio of 43% (or be eligible for purchase by a GSE in conservatorship under a temporary "QM Patch" — now substantially replaced by the "Price-Based QM" rule which uses the loan's APR relative to a benchmark instead of a DTI cap).
- Not include features the regulation defines as high-risk: interest-only periods, negative amortization, balloon payments, loan terms exceeding 30 years, or "no-doc" / limited documentation.
- Use a fully amortizing payment to calculate qualification (not a teaser rate).
- Have origination fees and points not exceeding 3% of the loan amount.

Loans satisfying QM provide the lender with a safe harbor (or rebuttable presumption, depending on the loan's pricing) against ability-to-repay litigation. Most mortgage originations in the agency channel are originated as QM loans; non-QM is a small, specialty segment.

The effect: the worst products of the pre-crisis era — no-doc loans, pay-option ARMs, interest-only ARMs with negative amortization features, 2/28 hybrid ARMs with payment-shock resets — are essentially gone from the mainstream U.S. mortgage market. They have been replaced by 30-year fixed-rate, fully amortizing, full-documentation loans originated to borrowers with documented ability to repay at the fully indexed rate.

This is the single largest underwriting improvement since the crisis. The current cohort of mortgage borrowers, on average, looks dramatically different from the 2006 cohort.

### 8.2.2 Borrower credit quality

Representative metrics on 2024–2025 vintage GSE conforming originations:

| Metric | 2006 Subprime | 2025 GSE Conforming |
|--------|--------------:|--------------------:|
| Median FICO | 622 | 760+ |
| Median CLTV | 92% | 78% (purchase); 65% (refi) |
| Median DTI | 42% (teaser) / 58% (fully indexed) | 36% |
| % low/no documentation | 50%+ | <2% |
| % adjustable-rate | 73% | ~10% |
| % piggyback/HELOC at origination | 28%+ | <5% |
| % owner-occupied | 88% (often misreported) | 87% (verified) |

*Illustrative figures drawn from FHFA Conforming Loan Limits Quarterly Reports, Fannie Mae Single-Family Acquisition Profiles, and Urban Institute Housing Finance at a Glance chartbook.*

The contrast is dramatic. The current mortgage borrower is, on average, significantly higher credit quality than the average 2006 borrower across every observable underwriting variable. Realized delinquency and default rates on post-2010 GSE vintages have been a small fraction of pre-crisis equivalents, even during the COVID-19 dislocation.

### 8.2.3 The FHA channel

A more nuanced picture exists in the FHA channel. The Federal Housing Administration insures loans to borrowers with lower credit scores and lower down payments (as little as 3.5%). FHA loans are securitized through Ginnie Mae. FHA's median FICO in 2025 is approximately 680 — still well above subprime, but below GSE conforming. FHA's serious delinquency rate (90+ days) is materially higher than GSE conforming — typically 4–6% during normal periods, vs. 1% or less for GSE conforming.

The FHA loan profile most closely resembles a "near-prime" segment. FHA serves first-time homebuyers, lower-income borrowers, and borrowers without large down payments. The credit losses on the FHA portfolio are absorbed by FHA's insurance fund (the Mutual Mortgage Insurance Fund, MMIF) and ultimately by the federal government if the MMIF is depleted. The MMIF was significantly stressed during 2008–2012; it has since rebuilt capital to its statutory 2% minimum capital ratio and beyond.

### 8.2.4 The non-QM segment

A small but growing non-QM market has developed to serve:

- Self-employed borrowers with non-W-2 income (use of bank statements as income documentation, for example);
- High-income borrowers with cash-out refinances exceeding QM points-and-fees limits;
- Investor-property borrowers (debt-service-coverage-ratio underwriting based on rental income);
- Foreign nationals;
- Other niches.

Non-QM origination volume in 2025 was approximately $90–110 billion — far smaller than pre-crisis subprime in real terms and concentrated in segments with higher down payments and stronger borrower profiles than 2006 subprime. The credit performance of non-QM has been good. The market participants are aware of the historical pattern and have been deliberately conservative.

Whether non-QM will deteriorate over time toward pre-crisis subprime is one of the empirical questions worth monitoring. The structural protections — the QM regulation's safe harbor for compliant loans, the absence of demand from major institutional buyers for high-risk loans, and the 5% retention requirement under Dodd-Frank Section 941 — make a 1:1 repeat of the pre-crisis dynamics unlikely. But the historical pattern is that boom-bust cycles in credit standards recur, and the absence of subprime in any meaningful form is itself an indicator that the cycle may not yet be ready to repeat.

---

## 8.3 The Interest Rate Regime and Its Effects

### 8.3.1 The rate path 2020–2026

The U.S. mortgage market in 2026 carries the imprint of one of the most extraordinary interest rate cycles in modern history:

- **2020–2021**: Federal Reserve emergency response to COVID; policy rates at 0%; the Fed purchased an additional ~$1.3 trillion of agency MBS through QE4. The 30-year fixed mortgage rate fell to approximately 2.65% in early 2021 — historically unprecedented low levels.
- **2022–2023**: Aggressive Fed tightening to address inflation; policy rate raised to 5.25–5.50% by mid-2023. 30-year fixed mortgage rate peaked above 7.5% in late 2023.
- **2024–2025**: Modest easing; policy rate gradually reduced; mortgage rates settled in a 6.0–7.0% range.
- **2026**: Mortgage rates approximately 6.0% — high by post-2008 standards, normal by pre-2008 standards.

The implication: an enormous share of outstanding mortgage debt — perhaps 65–70% of all U.S. mortgages — was originated or refinanced into rates below 4%, often below 3.5%. Those borrowers have a strong economic incentive *not* to sell their homes and *not* to refinance, because doing so would require taking on debt at the current rate.

### 8.3.2 The "lock-in effect"

The mortgage rate lock-in effect is one of the defining structural features of the modern U.S. housing market. With existing borrowers holding sub-4% mortgages and current rates at 6%, moving from one home to another requires either:

- Bringing extra cash to substantially reduce the new mortgage balance;
- Accepting a much higher monthly payment on the same loan amount;
- Buying down the rate via points (expensive).

The result is unprecedented inventory tightness:

- **Existing home sales** have fallen to multi-decade lows.
- **Housing inventory** remained near multi-decade lows for an extended period.
- **Price appreciation** has continued at modest rates despite weak transaction volume, because supply is even more constrained than demand.

The lock-in effect is good for incumbent homeowners (preserving their below-market financing) and bad for housing market function (impairing mobility, suppressing supply, raising prices). It is a direct artifact of the post-2008 monetary policy regime — extraordinary easing produced extraordinarily low mortgage rates, and the subsequent normalization left those low rates as durable assets to their holders.

### 8.3.3 Affordability

Despite the lock-in effect on incumbents, the *marginal* buyer faces severe affordability pressure. The "house payment as percent of median income" — the canonical affordability metric — reached the highest levels since the early 1980s in 2023–2024:

| Year | Median Home Price | Median Mortgage Rate | Monthly P&I @ 20% Down | Median Household Income | P&I as % of Income |
|------|------------------:|---------------------:|-----------------------:|------------------------:|-------------------:|
| 2000 | $145,000 | 8.05% | $853 | $42,000 | 24.4% |
| 2006 | $230,000 | 6.41% | $1,151 | $48,000 | 28.8% |
| 2012 | $190,000 | 3.65% | $695 | $51,000 | 16.4% |
| 2021 | $355,000 | 2.96% | $1,194 | $70,000 | 20.5% |
| 2024 | $410,000 | 6.85% | $2,145 | $76,000 | 33.9% |

*Illustrative figures; actual values vary by data source. The directional trend is consistent across sources: affordability has deteriorated sharply since 2021.*

The decline in affordability is producing identifiable second-order effects:

- **First-time homebuyer share** has fallen to multi-decade lows (under 30% of purchases vs. historical 40%+).
- **Single-family rental demand** has risen, supporting the institutional rental investor sector (Section 8.5).
- **Household formation** has slowed as young adults delay homeownership.
- **Geographic relocation** has shifted toward lower-cost states (Texas, North Carolina, Tennessee, Idaho) and away from high-cost coastal markets.
- **Multi-generational housing** has increased as adult children remain in or return to parental homes.

None of these is a financial-stability concern in itself. The aggregate affordability problem is, however, a relevant context for whether the housing market remains stable: it is the marginal buyer who clears the market, and the marginal buyer in 2026 is under significant payment pressure.

---

## 8.4 Household Debt and the Balance Sheet

### 8.4.1 Aggregate household debt

U.S. household debt, total across all categories:

| Category | 2007 ($trn) | 2026 ($trn approx.) |
|----------|------------:|---------------------:|
| Mortgages | 10.5 | 13.5 |
| HELOCs and home equity | 1.1 | 0.5 |
| Auto loans | 0.8 | 1.7 |
| Credit cards | 0.9 | 1.2 |
| Student loans | 0.6 | 1.8 |
| Other (BNPL, other consumer) | 0.3 | 0.5 |
| **Total** | **14.2** | **19.2** |

The composition has shifted materially. Mortgage debt has grown relatively modestly. Student loans, auto loans, and credit cards have all grown faster. The U.S. household balance sheet is more exposed to consumer credit and less concentrated in mortgage credit than it was in 2007.

### 8.4.2 Household debt as a share of income

Household debt as percent of disposable personal income:

- **2007 peak**: 132%.
- **2012 (post-deleveraging)**: 105%.
- **2020**: 92%.
- **2026**: ~96%.

The deleveraging of 2008–2013 was substantial. Households reduced mortgage debt absolutely (through defaults, modifications, and conservative new origination) even as nominal income grew. The current debt-to-income ratio is materially lower than pre-crisis, reflecting both the underwriting discipline of the post-QM era and the equity buildup of the post-2012 housing recovery.

### 8.4.3 Home equity position

Aggregate U.S. home equity reached approximately $30 trillion by mid-2024 (Federal Reserve Z.1). With aggregate mortgage debt of ~$13.5 trillion, the loan-to-value ratio of the U.S. housing market is approximately 31% — *the lowest level in modern data*. Borrowers in 2006 were, on average, deeply leveraged into their homes (with LTVs near 90%+ at the bubble peak). Borrowers in 2026 are, on average, substantially equity-rich.

This is one of the most significant differences between the 2008 and 2026 setups. A 2008-style 20–30% national home price decline, *should it occur*, would generate far fewer underwater borrowers in 2026 because the starting equity position is much higher. Underwater borrowers are the primary source of strategic default; a market with substantial equity is structurally more resilient.

The caveat: this aggregate figure obscures considerable heterogeneity. Borrowers who purchased in 2021–2022 at peak prices with low down payments have much less equity. Borrowers in certain markets (Austin, Boise, Phoenix) experienced significant price corrections in 2022–2024 and may have negative or marginal equity. The aggregate equity number is dominated by long-tenure owners and is not representative of marginal borrowers.

### 8.4.4 Delinquency trends

Mortgage delinquency rates (90+ days past due) in 2026 are approximately 0.8% of all conventional mortgages and 4–5% of FHA loans. Both figures are well below pre-crisis peaks and approximately consistent with the early 2020s baseline.

By contrast:
- Credit card delinquencies are at multi-year highs and rising in 2024–2025.
- Auto loan delinquencies are at the highest level since the 2009–2011 period.
- Student loan delinquencies are confused by the payment pause and resumption dynamics.

The pattern suggests stress is appearing at the consumer credit margin (Section 9) rather than in mortgages. This is a meaningful structural distinction — mortgages are the largest single household exposure and remain stable, while smaller categories show clear deterioration.

---

## 8.5 The Institutional / Investor Housing Market

A new feature of the post-2010 U.S. housing market is the substantial institutional investor presence in single-family rentals (SFR). Beginning around 2012, large funds (Blackstone, Invitation Homes, American Homes 4 Rent, Tricon, Progress Residential, Pretium Partners, and others) began acquiring single-family homes at scale for use as rentals.

The current scale:

- **Institutional SFR holdings** (defined as 1,000+ home portfolios): approximately 700,000+ homes across the largest 30 institutional owners. Total stake in the U.S. single-family rental market: roughly 3–5% of all single-family rentals nationwide, concentrated in specific Sunbelt markets where it may approach 15–20% locally.
- **Build-to-rent**: institutional development of new single-family rental communities — a market segment that essentially did not exist before 2014 and has grown to tens of thousands of units per year.
- **SFR securitization**: institutional SFR operators have created a parallel ABS market, with bonds backed by rental cash flows from large portfolios of single-family homes. The first such issue (Invitation Homes 2013-SFR1) launched in November 2013; the market has grown to $40–50 billion of outstanding paper.

The economic role of institutional SFR is contested:

- **Critics argue** it has pushed prices higher in specific markets, displaced first-time homebuyers, and concentrated rental ownership in ways that may impair tenant outcomes and local housing markets.
- **Defenders argue** it has professionalized a previously mom-and-pop rental segment, provided durable rental supply, and offered an alternative path to housing for households not yet ready to purchase.

The financial-stability question is whether institutional SFR represents a new concentration of housing risk. The major operators are heavily leveraged through a combination of corporate debt, SFR ABS, and warehouse facilities. A material decline in single-family home prices would erode the equity in these portfolios, potentially forcing sales that further depress prices. The aggregate leverage in the institutional SFR sector is in the tens of billions of dollars — small relative to the $30 trillion housing market, but concentrated and visible.

A separate consideration: large institutional SFR owners now have an incentive to *suppress* additional homeownership (which would compete with their rental business) and to support the *politics* of housing supply restriction. The political economy of housing has, in the post-2010 era, shifted in ways that may produce supply-side rigidity beyond the contributions of zoning and NIMBY-ism.

---

## 8.6 The GSEs in Conservatorship

A major unresolved item from the 2008 crisis: Fannie Mae and Freddie Mac remain in federal conservatorship as of 2026. The conservatorships, established September 7, 2008, were intended to be temporary; they have continued for over 17 years.

The current structural setup:

- The Treasury holds senior preferred stock in both entities with a quarterly dividend of all profits (the "net worth sweep," modified in 2019 to allow the GSEs to retain capital).
- The Treasury holds warrants exercisable for 79.9% of common stock.
- The FHFA exercises conservatorship authority, directing operational decisions.
- Private shareholders (common and junior preferred) hold residual claims that are largely worthless under current arrangements but which retain optional value if reform unwinds the conservatorship.

The GSEs have collectively earned hundreds of billions of dollars in net income since conservatorship and have rebuilt capital ratios significantly. The 2020 capital framework (the FHFA Enterprise Regulatory Capital Framework) sets minimum capital ratios — a 4% leverage ratio, plus various capital buffers — for the GSEs to operate at if released.

The political economy of GSE reform has remained unresolved through three U.S. administrations. The fundamental policy choices:

1. **Recapitalize and release**: rebuild GSE capital to the point that they can operate without federal support, then end conservatorship. This is technically achievable but would require either accepting lower returns on the Treasury's senior preferred or significant private capital raise.

2. **Maintain conservatorship indefinitely**: continue current arrangements as a de facto nationalization of the agency mortgage market.

3. **Replace with new entities**: legislation to create successor entities with explicit federal guarantees and private capital — most thoroughly developed in the Corker-Warner and Johnson-Crapo Senate bills (2013–2014, never enacted).

4. **Eliminate**: wind down the GSEs and replace their function with banks and private securitization. This was the position in early Trump administration proposals; not currently active.

The continued conservatorship has the practical effect that the U.S. mortgage market depends on an *implicit but operationally complete* federal guarantee. Investors in agency MBS face zero realized credit losses — the GSEs absorb defaults under the conservatorship arrangements, and the Treasury stands behind the GSEs. This has supported continuous market function but has institutionalized the very moral hazard that pre-crisis critics warned about.

A genuine release of the GSEs from conservatorship would require, at minimum, several years of further capital accumulation, a credible replacement for the implicit guarantee (either explicit federal guarantee or substantial private capital), and political consensus on the structure of the resulting entities. None of these conditions appears imminent in 2026.

---

## 8.7 Securitization in the Post-Crisis Era

### 8.7.1 Volume and structure

Private-label residential mortgage securitization is a small fraction of its pre-crisis size. The current state:

- **Agency RMBS issuance**: ~$1.5 trillion per year (cyclical with origination volume; lower in 2023–2024 after rate increases reduced refinance volume).
- **Non-agency RMBS issuance**: ~$50–80 billion per year, segmented into:
  - Prime jumbo (Sequoia, JPMorgan's Chase Mortgage Trust shelves) — high-quality jumbo loans.
  - Non-QM — the post-crisis successor segment.
  - Re-performing loans (RPL) — modified loans from the 2008 crisis re-securitized.
  - GSE Credit Risk Transfer (CRT) securities — see below.
  - Single-family rental securitization.

Non-agency RMBS has not recovered to its pre-crisis $1+ trillion annual issuance levels and likely will not. The credit-quality of non-agency issuance in 2026 is dramatically higher than 2006: weighted average FICO 730+, weighted average LTV under 75%, predominantly full documentation. The institutions structuring these deals have absorbed the lessons of the 2008 crisis through both regulation and bitter experience.

### 8.7.2 The 5% retention rule

Dodd-Frank Section 941 imposed a 5% credit risk retention requirement on issuers of asset-backed securities, intended to ensure that originators retain "skin in the game" in their securitizations. Implementing regulations took effect in December 2016 for most asset classes (CMBS retention rules took effect in December 2016 also; RMBS in December 2015).

The retention rule has exceptions for "qualified residential mortgages" (the QRM definition was eventually harmonized with the QM definition, exempting most agency-eligible loans), making the rule operationally binding mainly on non-QM, jumbo, and other private-label issuance. Its effect:

- It has eliminated the most aggressive originate-to-distribute dynamics in private-label RMBS.
- It has imposed real economic skin-in-the-game costs on private-label issuers, raising the bar for non-prime origination.
- It has likely contributed to the persistent small size of the private-label RMBS market by raising the issuer's cost of doing the business.

The retention rule has been criticized for both being too weak (5% may not be enough to drive behavior) and too strong (deterring private-label issuance and entrenching GSE dominance). Both criticisms have merit. The honest answer is that it has produced one specific behavioral change — eliminating the worst pre-crisis practices — without resolving the broader structural distortion that the GSEs' implicit guarantee creates.

### 8.7.3 Credit Risk Transfer (CRT)

A post-crisis innovation: the GSEs themselves transfer a portion of their credit risk to private capital through Credit Risk Transfer (CRT) securities. The mechanics:

- The GSE retains the senior credit position on a pool of mortgages.
- The GSE issues debt-like CRT securities that bear the first-loss credit position on the pool.
- Private investors buy the CRT securities, receiving spread compensation for the credit risk.
- The CRT securities can be either Fannie's Connecticut Avenue Securities (CAS) or Freddie's Structured Agency Credit Risk (STACR) deals.

CRT issuance has totaled approximately $100–150 billion per year in recent vintages, transferring credit risk on perhaps $4 trillion of underlying mortgage exposure (CRT typically references multi-year pools). The mechanism creates a private price discovery for GSE credit risk and shifts a portion of the loss exposure from the government to private capital.

In market stress (March 2020 COVID), CRT securities widened sharply (Class B-1 STACR spreads went from approximately 250 bps over SOFR to over 1,500 bps in two weeks). The CRT market has since recovered and continues to function, but the experience demonstrated that even high-quality conforming credit can experience violent repricing during stress events.

---

## 8.8 The Refinancing Wave Dynamics

A specific dynamic worth examining: the refinancing patterns of 2020–2021 created the largest aggregation of low-rate mortgage debt in U.S. history. Over 14 million households refinanced during the COVID-era rate decline, often into 30-year fixed rates between 2.65% and 3.5%.

The implications:

1. **Massive household interest expense savings**: aggregate annual interest savings for refinancing households approached $100 billion per year.
2. **Massive prepayment shock to MBS holders**: investors who had purchased pre-2020 MBS at par received their principal back early at par, experiencing significant convexity losses.
3. **The Federal Reserve's MBS holdings absorbed much of this prepayment**: the Fed received over $300 billion of unscheduled principal repayments during 2020–2021, reducing its MBS position somewhat.
4. **Mortgage servicing rights (MSRs) crashed in value**: with refinances accelerating, the duration of MSRs collapsed, producing large fair-value losses at non-bank servicers.
5. **The lock-in effect** (Section 8.3.2) was established as a structural feature.

The aftermath, as rates rose in 2022–2023:

- Refinance volume essentially evaporated.
- MSR values recovered as prepayment speeds slowed.
- Existing mortgage portfolios extended in duration.
- Sellers of homes withdrew from the market.

The mortgage rate cycle and the associated MBS prepayment/extension dynamics matter beyond the mortgage market: they affect bank duration risk (the regional bank crisis of 2023, Section 9), pension fund and insurance company asset allocation, and Federal Reserve balance sheet management.

---

## 8.9 The Fed's Role in the Modern Mortgage Market

The Federal Reserve, through its post-2008 QE programs and its subsequent COVID-era expansion, became the largest single holder of agency MBS in the world. At peak (early 2022), the Fed held over $2.7 trillion of agency MBS — approximately 25% of all outstanding agency MBS.

The implications:

1. **Mortgage rate suppression**: the Fed's MBS purchases lowered mortgage rates by an estimated 50–100 bps relative to a counterfactual without QE. This supported housing demand and price appreciation during 2010–2021.

2. **Balance sheet runoff**: from mid-2022 forward, the Fed began allowing its MBS holdings to roll off through prepayments and maturity, without reinvesting the proceeds. The "balance sheet normalization" or "QT" process is gradual; at current pace, the Fed's MBS holdings will not return to pre-COVID levels until well into the 2030s.

3. **Implicit subsidy to mortgage credit**: by holding agency MBS at par, the Fed effectively provides ongoing demand for the asset. Whether this continues during future stress events (and on what terms) is a critical policy question.

4. **The 2022 unrealized loss problem**: as rates rose, the Fed's MBS portfolio went into massive unrealized loss positions. Because the Fed marks its portfolio at amortized cost (held-to-maturity for its operating purposes), these losses are not realized in income but appear as "unrealized losses" on supplementary disclosures. The mark-to-market value of the Fed's MBS portfolio is hundreds of billions below its book value. This does not constrain the Fed's operations (the Fed cannot become insolvent in any operational sense), but it has been a politically sensitive feature of QT.

The Fed's massive presence in the agency MBS market is, by any measure, a structural feature of the modern market. The market would function differently — perhaps quite differently — without it.

---

## 8.10 The Commercial Mortgage Market

A brief note on commercial real estate (CRE) mortgages, given their importance to the overall picture. While Sections 8.1–8.9 focused on residential, CRE is a major separate market with its own dynamics:

- **Total CRE debt outstanding**: ~$5.7 trillion (2026).
- **Bank-held CRE loans**: ~$3.0 trillion, concentrated at smaller regional banks (CRE accounts for over 30% of total loans at banks under $250bn in assets, vs. ~10% at G-SIBs).
- **CMBS outstanding**: ~$0.9 trillion.
- **Insurance company CRE holdings**: ~$0.7 trillion.
- **GSE multifamily**: ~$1.1 trillion (Fannie and Freddie multifamily; Ginnie Mae HUD).

The CRE market's stress dynamics are dramatically different from residential. Office buildings in particular have faced a structural revaluation following the COVID-era shift to remote and hybrid work, with major-market office prices down 30–50% peak-to-trough. CRE delinquencies have risen sharply through 2023–2025. The regional bank exposure to CRE is the proximate concern.

This is addressed in detail in Section 9.

---

## 8.11 Summary Comparison: Mortgage Market 2006 vs 2026

| Feature | 2006 | 2026 |
|---------|------|------|
| Outstanding residential mortgage debt | $10.1 trillion | $13.5 trillion |
| Share in agency MBS | ~45% | ~67% |
| Share in private-label MBS | ~22% | ~5% |
| Median origination FICO | 705 | 760 |
| Median origination CLTV | 84% | 78% |
| Subprime share of originations | 21% | <1% |
| Stated-income share | ~33% | <2% |
| ARM share of originations | ~35% | ~10% |
| Average household mortgage debt service / income | 11.1% | 8.4% |
| Aggregate home equity | $13.0 trillion | $30.1 trillion |
| Mortgage delinquency rate (90+ days) | 1.3% rising | ~0.8% stable |
| QM/QRM regulatory regime | None | Comprehensive |
| GSE status | Public companies with implicit guarantee | Federal conservatorship |
| Largest MBS holder | Disparate institutions | Federal Reserve |
| Originator structure | Bank-dominated | Non-bank dominated |
| Servicer concentration | Diverse | Increasingly non-bank-concentrated |
| Capital required for retained mortgage exposure | 4% (Basel I) | 12%+ (Basel III + buffers) |

The mortgage market is structurally safer than in 2006 by nearly every measure that contributed to the 2008 crisis. The risks that exist today are different in form and are concentrated in different parts of the system. Section 9 examines those risks across the broader financial landscape — not as a 2008 redux but as the emergent structural fragilities of the current era.

---

## 8.12 Closing Frame for Section 8

The U.S. residential mortgage market in 2026 is, by every comparable historical measure, more conservatively underwritten and better capitalized than at any prior moment in modern history. The combination of QM regulation, the de facto nationalization of credit risk through the GSE conservatorship, the 5% retention rule, and elevated capital requirements at large banks has effectively prevented a repetition of the pre-crisis dynamics in the residential mortgage market.

The trade-off: the system that has replaced the pre-crisis structure is heavily dependent on the federal government's implicit guarantee. The GSEs operate in conservatorship; the Federal Reserve holds the largest single position; the FHA insures the high-risk segment. Whether this constitutes "stability" or "displaced fragility" is a judgment call — the dependence is real, and a future political or institutional disruption to any of these structures would produce significant market stress.

What is clearly true: the next major financial crisis is unlikely to originate in the U.S. residential mortgage market in the way 2008 did. The next crisis, if and when it comes, will arrive from somewhere else. Section 9 maps the most plausible candidates.
