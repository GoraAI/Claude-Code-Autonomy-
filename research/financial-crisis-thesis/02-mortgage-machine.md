# Section 2 — The Mortgage Machine

## How a Loan Application Became a Securitized Bond

> "The mortgage broker's incentive is to close the loan. The originator's incentive is to sell the loan. The aggregator's incentive is to securitize the loan. The rating agency's incentive is to rate the bond. The investor's incentive is to buy the bond. *No one's incentive is for the borrower to repay the loan.*"
> — Internal credit memo, large U.S. bank, 2006 (paraphrased from FCIC interview, 2010)

This section traces the end-to-end origination and pipeline that produced the loans underlying the 2004–2007 vintage of subprime MBS — the cohort responsible for the bulk of crisis losses. The objective is to make visible the mechanical structure of the pipeline, including each participant's incentive, each handoff's information loss, and each control failure.

The fundamental shift to internalize is the move from the **originate-to-hold** model (the lender keeps the loan on its balance sheet and earns the interest) to the **originate-to-distribute** model (the lender sells the loan and earns a fee). Originate-to-hold aligns the lender's interest with the borrower's ability to repay. Originate-to-distribute decouples them. Every pathology described below flows, more or less directly, from that decoupling.

---

## 2.1 The Old Mortgage and the New

### The traditional mortgage

For most of the twentieth century, an American mortgage was a relatively uniform contract:

- A 30-year fixed-rate, fully-amortizing, level-payment loan;
- Originated by a savings bank, thrift, or commercial bank;
- Held on the originator's balance sheet through maturity;
- Underwritten to the "28/36 rule" (housing expense ≤28% of gross income, total debt ≤36%);
- Secured by a property purchased with a 20% down payment;
- Documented with full income verification (W-2s, tax returns, pay stubs);
- Funded by deposits paying a regulated rate (Regulation Q's interest rate ceilings on deposits were not fully phased out until 1986).

This is the loan profile that produced the empirical default data on which mortgage credit models would later be trained. It was a low-default, high-recovery, geographically-diversified asset class. The bank, the borrower, and the community had aligned interests over the life of the loan.

This system died for many reasons — the savings-and-loan crisis of the late 1980s eliminated much of the thrift base; deregulation of deposit rates raised funding costs; Fannie and Freddie's expanded MBS operations created a deep secondary market; and the early-1990s explosion of asset-backed securitization created institutional appetite for private-label paper. What replaced it was a distributed, specialized, transaction-fee-driven pipeline with very different incentive properties.

### The new mortgage pipeline

By 2006, the typical subprime loan moved through the following chain:

```
  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
  │   Borrower   │───▶│   Mortgage   │───▶│   Lender /   │───▶│  Warehouse   │
  │              │    │    Broker    │    │  Originator  │    │   Line of    │
  └──────────────┘    └──────────────┘    └──────────────┘    │    Credit    │
                                                              └──────┬───────┘
                                                                     │
  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐
  │  Bond        │◀───│   Rating     │◀───│ Securitiz'n  │◀───│ Investment   │
  │  Investors   │    │   Agencies   │    │   Trust      │    │  Bank        │
  └──────────────┘    └──────────────┘    │  (SPV)       │    │  (Aggregator)│
                                          └──────────────┘    └──────────────┘
                                                  │
                                                  ▼
                                          ┌──────────────┐
                                          │  Mortgage    │
                                          │  Servicer    │
                                          │  (post-sale  │
                                          │  collection) │
                                          └──────────────┘
```

Each arrow is both a transfer of an asset and a transfer of risk — and, critically, an opportunity for fees to be skimmed off the asset's notional value. By the time a $200,000 loan reached the bond investor, between 4% and 8% of its principal had typically been consumed in compensation along the chain (broker yield-spread premium, origination fees, warehouse interest, gain-on-sale margin, securitization fees, rating fees, servicing strip, administrative reserves).

---

## 2.2 The Borrower

### The traditional U.S. mortgage borrower segments

Pre-securitization, lenders distinguished informally between "prime" and "non-prime" borrowers. The post-securitization industry formalized the segmentation:

| Segment | FICO Range (approx.) | Typical Loan Features | 2006 Origination Share |
|---------|---------------------:|------------------------|------------------------:|
| **Prime** | 720+ | Fixed-rate, ≤80% LTV, full documentation, GSE-conforming | ~36% |
| **Alt-A** | 660–720 | Often limited or stated documentation; higher LTV; investor properties; "near-prime" | ~16% |
| **Subprime** | <660 | Hybrid ARMs (2/28, 3/27); high LTV; impaired credit history; often refinances | ~21% |
| **Jumbo Prime** | 720+ | Loans above the conforming limit (then $417,000) | ~14% |
| **Other** (FHA, VA, HELOC) | varies | Government-insured or junior lien | ~13% |

*Source: Inside Mortgage Finance annual statistical report.*

The dramatic story of 2003–2007 was the explosion of the middle two categories. Subprime origination volume rose from approximately $190 billion in 2001 to a peak of $625 billion in 2005. Alt-A grew even faster as a percentage, from negligible levels in 2001 to over $400 billion in 2006. The two categories combined approached $1 trillion of annual originations at peak — more than the entire prime conforming market a decade earlier.

### The credit characteristics of the marginal borrower

By the 2006 vintage, the marginal new subprime borrower had:

- A FICO score in the 580–620 range (versus a U.S. median of approximately 720);
- A combined loan-to-value (CLTV) ratio of 95–100% (including any second lien), with cash-out refinances often pushing higher;
- A debt-to-income (DTI) ratio at the limit of underwriting tolerances (often 50%+), calculated against the *teaser-rate* monthly payment, not the post-reset payment;
- Frequently no documentation of income or assets;
- An adjustable-rate loan with a fixed initial period (typically 2 years for subprime "2/28" loans, 3 years for "3/27" loans) and a steep rate reset thereafter.

A representative 2006 vintage subprime 2/28 ARM might be structured as follows:

- Loan amount: $200,000
- Initial fixed rate: 7.75% for 24 months → monthly P&I: $1,432
- Margin over six-month LIBOR after reset: 6.00%
- LIBOR at origination: ~5.4% → fully indexed rate at first reset: 11.4%
- Monthly P&I post-reset: ~$1,964 (a 37% increase)
- Prepayment penalty active for 24–36 months (so the borrower could not refinance to escape the reset)
- Documentation: stated income, no asset verification
- Borrower's actual qualifying ratio at origination: ~42% on teaser; ~58% on fully indexed rate

The loan was, in effect, designed to require refinancing within two years. The implicit assumption was that home price appreciation would generate sufficient equity for the borrower to refinance into a new loan before the reset. If appreciation slowed or reversed, the loan would default by construction, not by accident.

This is one of the deep structural facts of the crisis: **a substantial fraction of 2005–2007 subprime loans were unrepayable on their own terms unless home prices kept rising**. The product was not "risky" — it was *contingent on house-price appreciation*. The credit risk was a hidden short position on the housing market itself.

---

## 2.3 The Mortgage Broker

### Function and growth

A mortgage broker is an independent intermediary who takes a borrower's loan application and shops it among wholesale lenders. The broker does not lend; the broker matches the borrower to a lender, in exchange for a fee.

In 1987, mortgage brokers originated approximately 20% of U.S. residential mortgages. By 2006, the broker share exceeded 60% in the subprime segment and 40% across all originations. The growth was driven by:

- Wholesale lenders' desire to scale origination without building branch networks;
- The technology of automated underwriting (Fair Isaac's FICO score plus desktop underwriting systems like Fannie's DU and Freddie's LP) that made loan decisions algorithmic rather than relational;
- Compensation structures that paid brokers more for higher-rate loans, channeling brokers toward subprime.

### The yield-spread premium (YSP)

The single most important pathological feature of broker compensation was the **yield-spread premium**. A YSP is a payment from the wholesale lender to the broker for delivering a loan with a *higher* interest rate than the borrower would have qualified for at par.

Example: A borrower qualifies for a 7.00% loan at the lender's rate sheet. The broker steers the borrower to a 7.75% loan. The lender pays the broker a YSP of, say, 1.5% of the loan amount — $3,000 on a $200,000 loan — because the higher-rate loan will sell into the secondary market at a premium.

The borrower received no benefit from the higher rate; the broker received the premium for placing them there; the lender's gain-on-sale was higher because the loan was worth more in the secondary market.

Compounding this: the broker was typically paid the YSP *plus* origination fees directly from the borrower (often financed into the loan, so the borrower didn't experience them as out-of-pocket). The total broker compensation on a subprime loan in 2006 commonly ran 3–5% of loan principal, or $6,000–$10,000 on a $200,000 loan.

The YSP was not illegal. It was disclosed (in HUD's Good Faith Estimate and HUD-1 Settlement Statement), though in dense regulatory language buried in pages of closing documents. The Federal Reserve had authority under HOEPA (the Home Ownership and Equity Protection Act of 1994) to restrict abusive lending practices but chose not to exercise it broadly until 2008.

### Broker incentive: close the loan

A broker is paid only if a loan closes. A broker is not paid if a borrower defaults. A broker's reputational capital is local and limited. A broker has no balance-sheet exposure to loan performance.

These four facts produce a single incentive: maximize loan volume, minimize friction, optimize fee per loan. Documentation that complicated underwriting was actively unhelpful to the broker. A borrower whose true financial picture wouldn't qualify for the loan was a problem to be solved through "stated income," not a reason to decline.

The phrase "liar loan" is often misunderstood as a description of fraud by borrowers. In practice, much of the dishonesty in stated-income documents originated with brokers, who knew which income figure would clear the lender's automated underwriting and instructed borrowers accordingly. Internal investigations after the crisis (notably from Wells Fargo, Bear Stearns, and Countrywide) found documented evidence of brokers altering income figures, falsifying employment verifications, and using fraudulent appraisers to support inflated loan values.

---

## 2.4 The Lender / Originator

### Originator types

By 2006, residential mortgage origination had segmented into:

1. **GSE-conforming originators** (large commercial banks, Wells Fargo, JPMorgan, Bank of America): originated to be sold to Fannie/Freddie.
2. **Private-label aggregators** (Countrywide, Washington Mutual, IndyMac, Wachovia, National City): originated for their own securitization shelves.
3. **Pure subprime monolines** (New Century, Ameriquest, Argent, BNC Mortgage, Long Beach Mortgage): originated subprime and Alt-A almost exclusively, sold to Wall Street aggregators or securitized themselves.
4. **Wall Street vertically integrated originators**: Lehman acquired BNC Mortgage and Aurora Loan Services; Bear Stearns acquired EMC Mortgage; Merrill Lynch acquired First Franklin; Morgan Stanley acquired Saxon Capital. By 2006, every major investment bank had an in-house mortgage origination platform.

Vertical integration is critical to understanding the crisis. When Lehman owned the originator and the securitization business and the trading desk, no arm's-length transaction occurred between them. Loans flowed from origination to securitization with minimal credit review. The price was set internally. The volume was set by the trading desk's demand for collateral. The entire pipeline was an internal manufacturing process — and like any manufacturing process under fee-based incentives, it optimized for throughput.

### The warehouse line

A warehouse line of credit is short-term bank financing extended to a mortgage originator to fund loans between closing and sale to the secondary market. A typical originator might fund 100% of the loan principal via the warehouse line at SOFR + 100 bps (in 2006 terms, LIBOR + 100), hold the loan on its balance sheet for 30–60 days while accumulating a salable pool, then sell the pool to an aggregator and pay down the warehouse line.

Warehouse lines are short-term, secured, and rolling. They were the lifeblood of independent originators (New Century, Ameriquest) that had no deposit funding. The total system of warehouse credit at peak supported approximately $200–300 billion of in-pipeline loans at any moment.

This funding structure had a critical fragility: it was *short-term financing of long-term assets*. If the loans could not be sold to the secondary market — if buyers disappeared or required price concessions exceeding the equity cushion — the originator could not pay down the warehouse line, the warehouse lender would demand collateral, and the originator's working capital would collapse within days. This is precisely what happened in February–March 2007: New Century Financial, the second-largest subprime originator, filed for bankruptcy on April 2, 2007, primarily because its warehouse lenders (Goldman, Bank of America, Morgan Stanley) refused to roll funding after the company disclosed early-payment-default repurchase demands. The same liquidity-mismatch problem would, eighteen months later, take down the major dealer banks themselves.

### The originate-to-distribute mindset

In an originate-to-distribute model, the originator's only sustained exposure to a loan's performance is the **early payment default (EPD) clause** in its sale contract with the aggregator. EPD clauses require the originator to repurchase any loan that becomes 60+ days delinquent within the first 90 days (sometimes 6 months) of origination. Beyond the EPD window, performance is the buyer's problem.

The EPD provision did create a tail risk for originators — and was the immediate accelerant of the early-2007 subprime originator failures, as repurchase demands accumulated faster than the firms' equity could absorb. But operationally, it produced a short-horizon credit standard: a loan needed to perform for ~90 days, not 30 years. A 2/28 ARM whose borrower might default after 24 months when the rate reset was, from the originator's perspective, a perfectly good loan.

---

## 2.5 The Loan Products

The 2004–2007 vintages exhibited an explosion of non-traditional product features, often combined in a single loan. The four most consequential are described below.

### The 2/28 (and 3/27) hybrid ARM

A hybrid ARM has a fixed initial rate for an initial period (2 or 3 years), then floats based on a margin over a short-rate index (six-month LIBOR was standard). The initial rate is set *below* the fully-indexed rate — meaning that if the index does not fall, the loan's rate will automatically rise at first reset *regardless of any change in the macro environment*.

A typical 2006 2/28 ARM:

- 2-year fixed at 7.5%
- Index: 6-month LIBOR
- Margin: 6.0%
- LIBOR at origination: 5.4%
- Implied fully-indexed rate: 11.4%
- First reset: month 25, then every 6 months thereafter
- Periodic cap: 1.5% per reset (sometimes 1% or 2%); lifetime cap: usually ~6% over initial rate
- Prepayment penalty: typically 80% of 6 months' interest, in effect 24–36 months

The loan was sold to the borrower on the affordability of the 7.5% payment, often with the assurance that "you can refinance before the reset." This was a promise that the originator could not make and was not contractually required to honor.

### Pay-option ARMs (negative amortization)

A pay-option ARM offered the borrower four payment choices each month:

1. A 30-year amortizing payment at the fully-indexed rate;
2. A 15-year amortizing payment (rare in practice);
3. An interest-only payment at the fully-indexed rate;
4. A "minimum payment" calculated at a teaser rate (e.g., 1.5%).

Option 4 was nearly always selected. The minimum payment was insufficient even to cover the actual interest accrual, so the unpaid interest was added to the principal balance — **negative amortization**. The loan balance grew month over month.

Pay-option ARMs typically recast (became fully amortizing on the new, higher balance) at the earlier of:

- The 5-year anniversary, or
- A balance-cap trigger (typically 110%, 115%, or 125% of original principal).

At recast, the monthly payment could double or triple as the loan amortized the now-larger balance over the remaining term at the fully-indexed rate. This was called "payment shock."

Pay-option ARMs were a Countrywide, Washington Mutual, IndyMac, and Wachovia specialty. By 2007, an estimated $750 billion of these loans were outstanding. Their cure rate after default was minimal because by the time payment shock hit, the borrower owed more than the original purchase price on a property whose value had fallen.

### Stated-income and "NINJA" loans

"Stated income" loans (sometimes called SISA — Stated Income, Stated Assets) accepted the borrower's representation of income without verification documents. They had been originally designed for the self-employed, where W-2 documentation was unavailable. By 2006, stated-income products were used across employment categories.

"NINJA" — No Income, No Job, No Assets — was an industry shorthand for loans approved with no documentation of any underwriting variable. Whether NINJA was a formal product category is debated; what is clear is that automated underwriting systems were configured, at major lenders, to approve loans on FICO and stated values alone for certain high-LTV ARM products.

A 2007 audit of approximately 100 stated-income loans by the Mortgage Asset Research Institute (MARI) found that 60% had stated incomes overstated by more than 50%, and almost a third overstated by 100% or more. The borrowers' actual incomes, where they could be reconstructed from tax returns or credit pulls, would not have qualified them for the loans they received.

### Piggyback / silent seconds and 100%+ LTV financing

To eliminate the down payment, borrowers were often originated with two simultaneous loans:

- A first mortgage at 80% LTV (the "80"); and
- A second-lien mortgage at 20% LTV (the "20"), often a HELOC.

The combined LTV was 100%, meaning the borrower had zero equity. Sometimes the structure was "80/10/10" (80% first, 10% second, 10% cash down). In cash-out refinances during peak appreciation, CLTVs of 105%, 110%, even 125% were not uncommon when appraisal inflation was added to the formal LTV.

The piggyback structure was tax-advantaged (mortgage interest deductibility for the second lien up to limits), avoided private mortgage insurance (which is required on first mortgages above 80% LTV), and allowed the first-lien MBS pool to report an "80% LTV" headline while the borrower had no equity at all. The bond investor saw an 80% LTV pool. The actual collateral was a 100% LTV exposure.

---

## 2.6 Underwriting Standards: Deterioration in Layers

The dominant academic study of this is Demyanyk and Van Hemert (2008), "Understanding the Subprime Mortgage Crisis," published as a NY Fed working paper. Using LoanPerformance loan-level data, they decomposed performance deterioration into:

1. **Observable loan characteristics** (FICO, LTV, documentation, product type). These deteriorated steadily from 2001 to 2007, but accounted for only part of the rising default rate.
2. **The vintage effect**: even controlling for observables, each successive vintage from 2001 to 2007 performed materially worse than the prior vintage at every horizon. Demyanyk and Van Hemert show that 2006-vintage loans had default rates 6–8x those of 2001-vintage loans with apparently identical observable characteristics.

The vintage effect captures unobservable underwriting deterioration: appraiser collusion, broker fraud, falsified employment, manipulated assets, and *adverse selection* — borrowers who could find no other source of credit migrating into the subprime channel and bringing risk characteristics not captured by the credit score.

A complementary study by Mian and Sufi (Mian and Sufi 2009, QJE, "The Consequences of Mortgage Credit Expansion") demonstrated using ZIP-code-level data that mortgage credit grew most rapidly in ZIP codes with declining incomes and previously high denial rates — the opposite of what would be expected if credit was being extended on improved economic fundamentals. The credit expansion was supply-driven, not demand-driven, and the supply was directed precisely at the most credit-risky pockets of the population.

A simplified table of representative subprime underwriting metrics by vintage:

| Vintage | Median FICO | Median CLTV | % Low-Doc | % ARM | % 2nd lien piggyback | Cumulative 24-mo serious delinquency |
|--------:|------------:|------------:|----------:|------:|----------------------:|--------------------------------------:|
| 2001    | 612         | 80%         | 28%       | 51%   | 4%                    | 5.6%                                 |
| 2003    | 619         | 84%         | 36%       | 65%   | 11%                   | 6.1%                                 |
| 2005    | 624         | 89%         | 46%       | 75%   | 24%                   | 12.4%                                |
| 2006    | 622         | 92%         | 50%       | 78%   | 29%                   | 22.8%                                |
| 2007    | 618         | 93%         | 52%       | 73%   | 28%                   | 31.4%                                |

*Indicative figures, drawn from LoanPerformance/CoreLogic data and Federal Reserve studies. Cumulative serious delinquency is 60+ days within 24 months of origination.*

The combination of falling FICO, rising CLTV, rising low-doc share, rising piggyback share, and rising ARM share would, by itself, predict deteriorating performance. The actual deterioration was worse than the observable variables alone would predict — the vintage effect.

---

## 2.7 The Appraisal Problem

Mortgage underwriting relies on the appraisal as the independent determination of property value. An appraisal's quality determines the loan's actual LTV.

In a vertically-integrated, fee-driven pipeline, the appraiser had a strong incentive to provide a value that hit the number needed for the loan to close. Loans that didn't close generated no fees for the appraiser, the broker, or the originator. Appraisers who consistently came in low got fewer assignments.

Investigations by the New York Attorney General (which produced the 2008 Home Valuation Code of Conduct settlement with Fannie Mae and Freddie Mac) and Congressional testimony documented widespread cases of:

- Appraisers being shown the "target" value before performing the inspection;
- Appraisers blacklisted by brokers/lenders for delivering low values;
- "Comp shopping" — using selected comparable sales to support inflated values;
- Direct collusion between appraisers and brokers, sometimes with kickback arrangements.

The HVCC reforms (effective May 2009, later codified into the Dodd-Frank appraisal independence rules) created formal separation between loan production staff and appraisers, generally via the use of appraisal management companies (AMCs). Whether this fixed the structural problem or merely added an opaque intermediary remains debated.

---

## 2.8 The Aggregator and the Securitization Trust

Once a sufficient pool of loans had accumulated at the originator — typically $300 million to $2 billion — it was sold to an aggregator (a large bank or investment bank) or to a securitization trust directly.

### The trust structure

A residential mortgage-backed securitization is legally structured as follows:

1. **Originator** sells the loans to a **depositor** (typically a wholly-owned bankruptcy-remote subsidiary of the aggregator).
2. **Depositor** sells the loans to an **issuing trust**, typically a Delaware or New York statutory trust, in exchange for the certificates representing claims on the trust.
3. **Trust** issues the certificates (the MBS) to investors.
4. **Servicer** is contracted to collect mortgage payments and remit cash to the trust according to the **Pooling and Servicing Agreement (PSA)**.
5. **Trustee** (typically a bank trust department — Bank of New York, U.S. Bank, Deutsche Bank Trust, Wells Fargo) administers the trust.

The "true sale" from originator to trust is a critical legal feature. If the sale is not a true sale, the loans remain assets of the originator in a bankruptcy proceeding, and the trust certificates would be claims on those assets rather than claims on the loans directly. Mortgage securitizations are structured (through "true sale" legal opinions, two-step transfers, and specific contractual provisions) to ensure bankruptcy remoteness — the loans are isolated from the credit risk of the originator.

This structure has profound implications:

- It produces a **special purpose entity** holding the loans with no operating activity except passing through cash flows.
- It allows the originator to remove the loans from its balance sheet for accounting purposes (depending on the rules in effect at the time), freeing capital for new originations.
- It separates the legal owner of the loan from the operational handler (the servicer), creating the chain-of-custody problems that would emerge in foreclosure litigation in 2010–2012 (robo-signing).

### Structuring economics

The aggregator's economic incentive is the gain-on-sale spread between the price paid for the whole loans and the proceeds of selling the certificates. A simplified example:

- Aggregator buys a $1 billion pool of subprime loans from originators at par.
- Aggregator pays origination overhead, due diligence costs, legal fees, rating fees, etc., totaling ~$10 million.
- Aggregator structures the pool into certificates totaling $1 billion notional, divided across tranches with different yields.
- Aggregator sells the certificates for total proceeds of $1.025 billion.
- Gain-on-sale: $1.025bn − $1bn − $10mm = $15 million.

This is a thin margin, but it scales linearly with volume. A bank doing $50 billion of subprime securitization at a 1.5% gain-on-sale margin generates $750 million of pre-tax earnings — a material contribution to a major investment bank's annual P&L.

The aggregator's incentive is therefore *volume*. Underwriting quality matters only to the extent that it affects (a) the price the rating agencies will give the structure, and (b) the price investors will pay. Both inputs were, as we will see, gameable.

### Pre-funding, revolving features, and ramp periods

To accelerate the securitization timeline, aggregators developed structures that allowed pools to be "pre-funded" — investors bought certificates against a pool whose final composition was not yet determined, with the residual collateral to be added in the first 60–90 days. This compressed origination-to-securitization timelines and reduced warehouse interest expense.

Similar features existed in CDOs (Section 4), where a ramp period of 6–12 months allowed the manager to gradually accumulate collateral. The result was that investors increasingly purchased securities whose actual underlying collateral was determined after their commitment — a profound information asymmetry that the rating process did not adequately reflect.

---

## 2.9 The Servicer

The mortgage servicer is the operational layer that interacts with the borrower after origination. Servicers collect monthly payments, manage escrows for taxes and insurance, handle delinquencies, manage modifications and workouts, and pursue foreclosure where required.

A servicer is compensated through the **servicing strip** — a fee, typically 25–50 basis points per annum on the unpaid principal balance, deducted from each month's interest payment before it reaches the trust. On a $200,000 loan at a 35 bps servicing strip, the servicer earns $700 per year — about $58 per month. The servicing strip is capitalized into the **mortgage servicing right (MSR)**, a balance-sheet asset reflecting the discounted value of future servicing fees.

MSRs are economically odd assets:

- They appreciate when prepayments slow (loans last longer → more fees collected).
- They depreciate when prepayments accelerate.
- They are therefore *short prepayment*, which is roughly *long interest rates* (higher rates → slower prepayments).
- Their valuation depends on prepayment models, default models, and discount rates — all of which are model-dependent.

The 2008 crisis introduced a perverse servicer incentive: in a stressed environment, the servicer's economic interest may diverge from the investor's. A delinquent loan generates more fee revenue (late fees, modification fees, foreclosure fees) than a performing loan. A foreclosure recovery is often a worse outcome for the trust than a loan modification — but a worse outcome for the servicer than continued delinquency. This misalignment was a major issue in modification rates from 2009 onward and was a driver of the robo-signing crisis as servicers cut corners to process foreclosure volume.

### The robo-signing problem

When loans were transferred from originator to depositor to trust, the physical mortgage notes (the IOUs evidencing the borrower's debt) and the assignments of the mortgages (the security interests in the property) had to be properly endorsed and transferred in accordance with the PSA's strict timing requirements (typically within 90 days of trust closing). In practice, this paperwork was often incomplete, missing, or improperly executed.

When foreclosures began in volume in 2008–2009, servicers' foreclosure mill operations (law firms and document preparation companies) discovered they could not produce the original notes or properly executed assignments. Employees of these mills signed thousands of foreclosure affidavits per day, often without reviewing the underlying documents — the "robo-signing" practice that, when disclosed in 2010, led to the National Mortgage Settlement in 2012 and to permanent reputational damage for major servicers.

The deeper issue raised by robo-signing was whether the trusts actually owned the loans they purported to own. If the chain of assignment was broken, the legal status of the trust certificates was uncertain. Litigation on this question is still ongoing in pockets a decade and a half later.

---

## 2.10 Incentive Map of the Pipeline

The full pipeline incentives can be summarized:

| Participant | Compensation Source | Incentive | Exposure to Loan Performance |
|-------------|---------------------|-----------|------------------------------|
| Borrower | Use of property; equity appreciation | Close loan, hope for appreciation | Down payment (often $0) + credit score |
| Mortgage broker | Origination fee + yield-spread premium | Close any loan | None |
| Appraiser | Per-appraisal fee | Hit the value the broker wants | Reputational only (and weak) |
| Originator / lender | Origination fees + gain-on-sale | Maximize volume sold | EPD repurchase clause (~90 days) |
| Warehouse lender | Interest on warehouse line | Keep originator solvent enough to roll | Collateral value of in-pipeline loans |
| Aggregator / investment bank | Securitization fees + trading P&L on retained tranches | Maximize securitization volume | Retained tranches (often equity, sometimes AAA) |
| Rating agency | Per-deal fees from issuer | Rate the deal to the issuer's satisfaction | Reputational (eventually); fees if downgraded |
| Servicer | Servicing strip + ancillary fees | Process volume; collect late fees | None (paid before trust) |
| Trustee | Per-trust administrative fee | Process administration efficiently | None |
| Bond insurer (monoline) | Premium income | Write guarantees; collect premiums | Full notional via guarantee |
| AAA bond investor | Coupon | Yield pickup over Treasuries | Full principal, but assumed near-zero default |
| Equity tranche investor (often the structurer) | First-loss return | Carry trade with embedded vol | First-loss exposure |
| Insurance/pension investor | Coupon | Achieve assumed return | Full notional |

Note how few participants in the chain have *durable* loan-performance exposure. The originator's EPD window is short. The aggregator's retained tranches are often small (and increasingly placed via synthetic transfer mechanisms — Section 4). The rating agency has no direct exposure. The servicer has no direct exposure. The trustee has no direct exposure.

The bondholder bears the credit risk, but the bondholder is rationally relying on the rating, on the documentation, and on the disclosure — none of which provided sufficient information to assess the actual quality of the underwriting. *The party with the exposure is the party with the least information.* This is the textbook condition for adverse selection at scale.

---

## 2.11 Fraud, Negligence, and the Spectrum Between

It is worth being precise about how much of the deterioration was outright fraud, how much was negligence, and how much was rational responses to bad incentives.

A useful taxonomy (drawn from FCIC findings, FBI mortgage fraud reports, and academic literature):

1. **Borrower fraud**: misrepresentation of income, employment, occupancy intent (claiming owner-occupied for an investment property to get better terms), or assets. Often coached by brokers; not always volunteered.
2. **Broker fraud**: alteration of borrower documents; submission of false employment verifications; coordination with appraisers; "double-app" schemes presenting the same borrower with different facts to multiple lenders.
3. **Appraiser inflation**: not always fraud in a legal sense; often "professional judgment" exercised toward the desired value.
4. **Originator negligence / willful blindness**: automated underwriting systems calibrated to approve loans the human underwriter would have declined; documented internal warnings ignored.
5. **Aggregator due diligence failures**: third-party due-diligence firms (Clayton Holdings, Bohan Group) were hired by aggregators to sample-check pools before purchase. Clayton's data, later released in litigation, showed that 28% of sampled loans in 2006–2007 had material exceptions to stated underwriting guidelines. Of those exceptions, the aggregators waived ~39% — bought the loans anyway with no remediation. The waived exception data was rarely disclosed to bond investors or to rating agencies.
6. **Rating agency negligence**: insufficient skepticism of issuer-provided data; models known internally to be inadequate; the explicit business decision that updating criteria might cost market share.

Most of the loss came not from fraud in a criminal sense but from the second, third, and fourth categories — negligence at scale, performed by people responding to compensation systems that rewarded the negligent behavior. Criminal prosecutions following the crisis were notably sparse. The system's design made it possible to produce a catastrophic outcome without any single participant doing anything they could be straightforwardly indicted for.

---

## 2.12 Foreclosure and Loss Severity

A defaulted mortgage produces a recovery to the trust, but the recovery is far less than the unpaid principal. The gap is the **loss severity**.

For 2005–2007 vintage subprime loans, ultimate loss severities reached 60–75% — meaning the trust recovered only 25–40% of the unpaid principal balance. The components of the loss:

- **Decline in property value** (the largest component): peak-to-trough, sand-state housing fell 30–50%; loans originated at 100% LTV with that decline meant the property alone was insufficient collateral.
- **Foreclosure costs**: attorneys' fees, court costs, property maintenance during the foreclosure period (often 12–24 months), property taxes, insurance.
- **Advances**: the servicer advances interest, taxes, and insurance to the trust during delinquency; these are recovered from sale proceeds, reducing recovery to bondholders.
- **REO (real-estate owned) carrying costs**: the property must be marketed, maintained, and ultimately sold, often at a 10–25% discount to the appraised value.

The combination of high default rate (>30% on the worst vintages) and high loss severity (~70%) produced cumulative losses on subprime collateral pools of 20–25% of original principal. This is the figure to hold in mind for Section 3's discussion of why senior tranches that "should" have been bulletproof in fact suffered losses.

---

## 2.13 Closing Frame for Section 2

By 2006, the U.S. mortgage origination pipeline had transformed from a relationship-based, balance-sheet-funded credit business into a transactional, fee-driven manufacturing process whose participants were systematically separated from the credit risk they were producing. The product mix had shifted toward loans that were viable only under continuing house-price appreciation. Underwriting documentation had degraded to the point where the loan's stated facts often bore little relation to the borrower's actual situation. Approximately 28% of loans sampled by professional due-diligence firms had material exceptions to stated guidelines, and roughly 11% were knowingly purchased with those exceptions intact.

The system was generating, at peak, over $1 trillion per year of new mortgage paper, the majority of which would be packaged into the securities described in Section 3. Those securities — and the derivative overlays on them described in Section 4 — were the substrate through which mortgage credit risk propagated into the global financial system. The pipeline did not cause the crisis on its own; it produced the *fuel*. The structuring machinery added the *oxygen*, and the derivative market added the *spark*.
