# Section 3 — Mortgage-Backed Securities

## How Mortgage Cash Flows Became Bonds

> "We rate every deal. It could be structured by cows and we would rate it."
> — S&P analyst, instant message exchange, April 5, 2007 (released by FCIC, 2010)

A mortgage-backed security is, in its essence, a claim on the cash flows of a pool of mortgage loans. The art of securitization is the construction of *multiple, differentiated claims* on a single cash flow stream — each claim with its own risk profile, yield, and credit rating, designed to satisfy a particular investor demand. This section explains the mechanics of that construction in sufficient detail that the reader can compute, at least at order-of-magnitude precision, why certain tranches survived the crisis and others did not.

The section moves from the simplest pass-through structure (agency MBS) through senior-subordinate tranching (private-label MBS) to the explicit credit enhancement methods (overcollateralization, excess spread, subordination, monoline wraps) that allowed pools of high-default subprime collateral to issue securities the rating agencies would mark AAA. Section 4 then takes the next step — repackaging the mezzanine tranches of these structures into CDOs — and Section 5 examines how a small set of investors decoded the structures' true risk characteristics ahead of the market.

---

## 3.1 The Foundational Idea: Pooling and Pass-Through

A single mortgage is a poor security. Its credit risk depends on one borrower; its prepayment risk depends on that borrower's idiosyncratic refinancing behavior; its size is small. It is illiquid, expensive to monitor, and exposed to single-name idiosyncratic risk.

A pool of mortgages is, statistically, a much better security:

- Credit risk diversifies across thousands of borrowers (under the assumption that defaults are imperfectly correlated — an assumption we will return to).
- Prepayment risk averages out, becoming a function of macro variables (rates, refi incentives) rather than individual borrower choice.
- The size is large enough to attract institutional capital.
- The pool can be administered by a professional servicer with economies of scale.

The simplest mortgage-backed security is a **pass-through**: a claim on a pro-rata share of all principal and interest cash flows from a pool, net of servicing fees. If you own 1% of a pass-through, you receive 1% of every payment the pool generates. There is no credit tranching, no payment timing rearrangement, no derivative overlay — just a pooled mortgage portfolio with shared ownership.

The Government National Mortgage Association (Ginnie Mae, established 1968) issued the first modern MBS pass-through in 1970. The structure was simple and brilliant: Ginnie did not originate or hold loans; it guaranteed the *timely payment* of principal and interest on pools of FHA/VA-insured loans assembled by approved private issuers. The full faith and credit of the U.S. government stood behind the guarantee. Investors thereby received a security with U.S. Treasury credit risk and mortgage-pool prepayment behavior — a combination that did not previously exist as a tradable instrument.

Fannie Mae and Freddie Mac developed analogous structures for conforming conventional loans (non-FHA/VA), with Fannie/Freddie guarantees instead of the U.S. government's. Their guarantees were not formally backed by the federal government, but were universally assumed to be implicitly so — a presumption confirmed when both GSEs were placed into conservatorship in September 2008 and the Treasury committed to support their senior debt.

---

## 3.2 Agency vs. Non-Agency (Private-Label) MBS

A critical distinction in the U.S. mortgage market is between **agency** MBS (issued or guaranteed by Ginnie Mae, Fannie Mae, or Freddie Mac) and **non-agency** or **private-label** MBS (issued by Wall Street investment banks or large private aggregators).

| Feature | Agency MBS | Private-Label MBS |
|---------|-----------|-------------------|
| Issuer | GSE or Ginnie | Investment bank / SPV |
| Collateral | Conforming, prime, full-doc loans | Subprime, Alt-A, jumbo, or non-conforming |
| Credit guarantee | GSE or federal | None at the pool level; achieved via tranching |
| Credit tranches | Single tranche (pass-through) typically | Multiple tranches (senior, mezz, equity) |
| Prepayment risk | Yes (TBA market priced this) | Yes, plus credit risk |
| Liquidity | Very high (TBA market) | Moderate to thin |
| 2007 universe size | ~$4 trillion | ~$2.1 trillion |
| Credit losses 2007–2012 | Minimal (GSEs took losses; investors paid in full) | Material; AAA-rated PLS suffered losses in some 2006–2007 vintages |

**Agency MBS** are essentially Treasury-credit-quality instruments with mortgage prepayment behavior. Their primary risk is prepayment timing (convexity), not credit. They trade in the highly liquid **TBA (to-be-announced)** market — a quirky pre-issuance forward market in which dealers commit to deliver a specified coupon and issuer of MBS on a specified settlement date, with the actual pool selected at the seller's option from any pool meeting the TBA specification ("good delivery" rules). TBA volume routinely runs $200+ billion daily, making agency MBS one of the deepest fixed-income markets in the world.

**Private-label MBS (PLS)** are structurally different. Because there is no GSE or federal guarantee, credit risk must be allocated within the deal itself. The entire purpose of tranching is to create that internal allocation: to redirect credit losses away from senior bondholders and toward subordinated investors in exchange for the subordinated investors' higher yield.

PLS is where the 2008 crisis primarily lived. Agency MBS suffered prepayment shock and price volatility but virtually no credit losses borne by investors. PLS — particularly subprime and Alt-A — generated the losses that propagated through the system.

---

## 3.3 The Cash Flow Waterfall

The defining structural feature of a private-label MBS (and by extension a CDO) is the **cash flow waterfall**: a deterministic, contractually-specified sequence of payments by which the pool's collected cash is distributed to claimants each period.

In its simplest form, a waterfall looks like this for each monthly period:

```
        ╔═══════════════════════════════════╗
        ║  Pool collections this period     ║
        ║  (P&I, prepayments, recoveries)   ║
        ╚═══════════════════════════════════╝
                      │
                      ▼
        ┌───────────────────────────────┐
        │ 1. Servicing fees             │
        │ 2. Trustee fees               │
        │ 3. Other admin                │
        └───────────────────────────────┘
                      │
                      ▼
        ┌───────────────────────────────┐
        │ Net available distribution    │
        └───────────────────────────────┘
                      │
                      ▼  INTEREST WATERFALL (Senior to Junior)
        ┌─────────────────────────────────────┐
        │  Pay interest:                      │
        │   A-1 (AAA, super-senior)           │
        │   A-2 (AAA, senior)                 │
        │   A-3 (AAA, senior mezz support)    │
        │   M-1 (AA)                          │
        │   M-2 (A)                           │
        │   M-3 (BBB+)                        │
        │   M-4 (BBB)                         │
        │   M-5 (BBB−)                        │
        │   B-1 (BB)                          │
        │   B-2 (B)                           │
        │   Equity / residual                 │
        └─────────────────────────────────────┘
                      │
                      ▼  PRINCIPAL WATERFALL
        ┌─────────────────────────────────────┐
        │  Pay principal in order:            │
        │   A-1 first, then A-2, …, until     │
        │   schedule met or pool exhausted    │
        └─────────────────────────────────────┘
                      │
                      ▼  RESIDUAL
        ┌─────────────────────────────────────┐
        │  Excess spread → equity tranche     │
        │  or to reserve account              │
        └─────────────────────────────────────┘
```

Each period, the pool generates cash. The cash is applied first to interest at every level senior to the equity, then to principal in the contractually specified order, then to the equity holder as the residual. **Credit losses, by contrast, flow up from the bottom**: defaults reduce the pool's total cash, and the shortfall is absorbed first by the equity tranche, then by the lowest-rated subordinated tranche, then by the next-lowest, and so on, with the most senior tranche taking losses only if every junior tranche has been wiped out.

This bottom-up loss absorption is the engine of credit tranching. The senior tranche is *protected* by the existence of the subordinated tranches below it: as long as cumulative losses do not exceed the total subordination supporting the senior, the senior receives all promised payments.

### A simplified numerical example

Consider a pool of $1 billion of subprime mortgages with:

- Weighted-average coupon (WAC): 8.5%
- Weighted-average servicing fee: 0.5%
- Net WAC available to bondholders: 8.0%
- Expected lifetime cumulative loss (pricing assumption): 6.0%

This pool is structured into tranches as follows:

| Tranche | % of Pool | Notional ($mm) | Rating | Coupon | Subordination Below |
|---------|----------:|---------------:|-------:|-------:|--------------------:|
| A-1 (super-senior) | 60% | $600 | AAA | 5.50% | 40% |
| A-2 (senior support) | 18% | $180 | AAA | 5.75% | 22% |
| M-1 | 6% | $60 | AA | 6.25% | 16% |
| M-2 | 4% | $40 | A | 6.75% | 12% |
| M-3 | 3% | $30 | BBB+ | 7.50% | 9% |
| M-4 | 2.5% | $25 | BBB | 8.00% | 6.5% |
| M-5 | 1.5% | $15 | BBB− | 9.00% | 5% |
| B-1 | 2% | $20 | BB | 11.00% | 3% |
| Equity | 3% | $30 | unrated | residual | 0% |
| **Total** | **100%** | **$1,000** | | | |

**Interpretation:** The AAA-rated A-1 tranche has 40% of the pool's notional sitting beneath it in loss-absorption capacity. For A-1 to take any principal loss, cumulative pool losses must exceed 40%. At the pricing assumption of 6% cumulative loss, A-1 is comfortably protected.

The pricing engine that produces this structure begins from the rating agency's required subordination level for each rating category, given the pool's collateral characteristics. If the agency's model says a AAA tranche on this collateral type requires 22% subordination, then the structurer can sell up to 78% of the pool as AAA-rated bonds. If the agency's model says 30%, then only 70% of the pool is salable as AAA — significantly less, with the rest having to be sold at lower ratings and lower prices.

**The economic value of the deal to the issuer is therefore directly proportional to how much of the pool can be designated AAA.** A 5-point shift in the AAA subordination requirement (from 22% to 27%) reduces AAA proceeds by 5% × $1 billion = $50 million, replacing them with a mix of mezz and equity that sells at far lower prices. The structurer's profit depends almost entirely on the rating agency's subordination model.

This is the single most important commercial pressure in the system.

---

## 3.4 Credit Enhancement: The Four Methods

The senior tranche's protection from credit losses is called **credit enhancement (CE)**. There are four principal methods, used in combination:

### 3.4.1 Subordination

The most important method. Lower-rated tranches absorb losses before higher-rated tranches. In the example above, the A-1 tranche enjoys 40% subordination from the structure below it.

Subordination is "real" credit support — there is actual cash in the form of subordinated bondholders' principal that absorbs losses. But it is *first-loss capital in the form of debt instruments*, which means the subordinated tranches retain the right to receive cash flows if the pool performs well. Subordination is therefore not equivalent to equity; it is more like a layered set of debt claims where the junior debt absorbs losses first and earns higher yield in compensation.

### 3.4.2 Overcollateralization (OC)

Overcollateralization is the difference between the pool's principal balance and the certificate notional outstanding. If a $1 billion pool issues $980 million of certificates, the deal is overcollateralized by $20 million. That $20 million serves as a cushion: it is principal in the trust that has no corresponding bondholder claim, so it absorbs the first $20 million of losses before any bondholder is impaired.

OC is created through one of two mechanisms:

- **Issue less than the pool balance** (as in the example above); the foregone proceeds go to the issuer or are subordinated.
- **Build OC over time using excess spread** (most common in subprime deals). Initial issuance might be at or near 100% of pool balance, but excess spread is captured into a reserve account each month until a target OC level is reached — typically 3–6% of the original pool balance.

The OC target is a structural lever. If the deal hits performance triggers (rising delinquencies, e.g., 90+ day delinquencies above a threshold), the OC build target may step up to a higher level — diverting cash that would otherwise have gone to the equity tranche back into the reserve.

### 3.4.3 Excess Spread

The pool's net WAC (8.0% in the example) is higher than the weighted-average coupon paid to the bondholders (which in this structure is approximately 5.75%, blended across tranches). The difference — roughly 2.25% — is **excess spread**.

Excess spread is paid each period after all tranche interest is satisfied. It can be paid to:

1. The OC build account (if OC is below target);
2. A cash reserve account (often separate);
3. The equity tranche, as the residual cash flow.

Excess spread is the *first* line of defense against credit losses. If the pool loses $100,000 in a given month due to defaults, but generated $200,000 of excess spread that month, the loss is fully absorbed by excess spread and no bondholder, not even the equity holder, takes a principal loss in cash terms. Excess spread is therefore a tremendously valuable form of CE — provided the pool is generating it.

The catch: excess spread depends on the pool's coupon staying high relative to the bond coupons. As prepayments accelerate (typically when rates fall), high-coupon loans pay off first and the pool's WAC drifts down. As defaults accelerate, defaulted loans cease paying interest, also reducing excess spread. Both forces can erode excess spread precisely when it is most needed.

### 3.4.4 Reserve Funds

A cash deposit at deal inception (typically funded by the issuer or by excess spread in early periods) sitting in a trust account. The reserve can be drawn to make interest payments if pool cash falls short. Reserves are usually small — 0.5–1% of pool balance — and serve primarily as a smoothing mechanism rather than a primary credit support.

### 3.4.5 External Credit Enhancement (Bond Insurance / "Monoline Wraps")

Some deals — particularly senior tranches of subprime, all of municipal bond securitizations, and many CDOs — were enhanced by monoline bond insurance from companies like MBIA, Ambac, FGIC, FSA, and CIFG. The monoline insurer would, for a one-time premium of 25–60 bps, guarantee the timely payment of principal and interest on the wrapped tranche. The tranche then carried the monoline's AAA rating regardless of its underlying credit profile.

Monoline wraps were structurally efficient (one transaction creates a AAA bond) but introduced concentrated counterparty risk: the wrapped bond was only as good as the monoline's solvency. When MBIA and Ambac were themselves downgraded in 2008, hundreds of billions of wrapped bonds were simultaneously downgraded, propagating losses across the financial system. Section 4 returns to the monolines and to their derivative-market exposures, which proved larger than their securitization wraps.

---

## 3.5 The Cash Flow Geography: Why Tranches Have Maturities

A pool of 30-year mortgages does not produce cash flows over 30 years — it produces them faster due to prepayments. The actual lifetime of a tranche is far shorter than the longest mortgage in the pool.

The **principal waterfall** in a typical sequential-pay structure pays all principal to the most senior outstanding tranche until that tranche is fully amortized, then to the next-most-senior, and so on. This produces dramatically different effective maturities:

- The **A-1 (super-senior)** tranche typically has a weighted-average life of 1–2 years.
- The **A-2 (senior support)** tranche, 3–4 years.
- The **mezzanine tranches**, 5–8 years.
- The **subordinate/equity tranche**, 8–15 years.

This is why mezzanine and equity tranches were rated lower even before considering credit risk: they are *exposed longer* to whatever risks exist. Time amplifies cumulative default probability, and the deeper in the pool's life one goes, the more its remaining loans tend to be those that didn't prepay early — often the worse credits.

For derivative pricing (Section 4), the time exposure of a tranche matters as much as its loss-absorption position. A mezzanine tranche with 7-year exposure and only 6% subordination behind it is qualitatively different from a senior tranche with 1-year exposure and 30% subordination, even though both might be labeled "BBB" or "AAA" at issuance.

---

## 3.6 Prepayment Risk and Convexity

The other major risk in MBS, separate from credit risk, is prepayment risk.

### Why prepayment matters

A borrower can repay a mortgage at any time without penalty (subject to occasional prepayment penalties on subprime loans). They typically do so when rates fall and they can refinance into a lower coupon, or when they sell the home. Both events return principal to the MBS investor sooner than scheduled.

If you bought a 6% MBS at par and rates fall to 4%, two things happen simultaneously:

1. The fair value of a non-callable 6% bond would rise (yields down → prices up).
2. But the borrower will refinance, repaying you at par exactly when the bond is worth most.

So the MBS investor experiences the rate decline as an *early return of principal at par*, rather than as a capital gain. The investor reinvests the returned principal at the new, lower rate. The MBS has "negative convexity" — its price rises less when rates fall than a non-callable bond would, and it falls more when rates rise (because borrowers stop refinancing and the loan's average life extends).

### Convexity in mathematical form

For a bond:
- **Duration** measures the price sensitivity to small interest rate changes (first derivative of price w.r.t. yield).
- **Convexity** measures how duration changes with yields (second derivative).

A Treasury bond has positive convexity: as yields fall, duration *rises*, amplifying capital gain.

A mortgage-backed security has *negative* convexity: as yields fall, prepayments rise, duration *falls*, capping the upside. This is the price the MBS investor pays for the higher coupon — they are short a prepayment option.

### Hedging negative convexity

Banks and dealers hedging MBS books must continuously rebalance their hedges as duration changes — a process called **convexity hedging**. When rates fall sharply, MBS portfolios' duration drops, requiring sellers to buy duration (Treasuries) to maintain their target exposure. When rates rise, MBS portfolios' duration extends, requiring buyers to sell duration. These flows amplify Treasury yield moves — a positive-feedback dynamic that has caused several large bond market sell-offs (1994 most notably; episodes in 2003, 2013, 2022, 2024 — see Section 9).

### Why prepayment models broke down

Pre-crisis prepayment models — the PSA standard, the OAS framework — were calibrated on prime, fully-amortizing loans, where prepayments responded to rate incentives in well-understood ways. They worked poorly on subprime hybrid ARMs. Subprime borrowers prepaid not for rate-refinancing reasons but for *credit*-refinancing reasons: they refinanced out of teaser-rate loans before the reset, drawing on the home equity that appreciation had provided. When appreciation stopped, the credit-refinance option vanished, prepayments collapsed, and the loans' effective lives extended into precisely the period of payment shock and default that the originator had implicitly assumed away.

This produced a counterintuitive cliff: in 2007, subprime prepayment speeds *fell* as defaults *rose*, a divergence from the historical pattern of correlated prepay-and-default behavior. Pricing models that had assumed historical correlation found themselves with widening errors. Risk officers using model-derived hedges discovered the hedges no longer protected them. The model risk is examined more carefully in Section 4.

---

## 3.7 The Rating Process

The credit rating is the *external endorsement* without which institutional buyers cannot purchase. Most large investors — pension funds, insurance general accounts, money market funds, bank treasury portfolios — are constrained by mandate or regulation to hold rated paper, and to hold predominantly investment-grade or higher.

The big three rating agencies (Moody's, S&P, Fitch) operated under an issuer-pays model: the issuer of the security pays the rating agency for the rating. In 2006, the structured finance business produced approximately 40% of Moody's revenue and a similar share of S&P's. The conflict of interest is obvious in the abstract; what made it acute in practice was the consolidation of the industry's issuance among a handful of investment banks. Losing a single client (Goldman, Lehman, Bear, Merrill, Citi, UBS, Deutsche, JPMorgan) was material. Losing two was existential.

### How the rating model worked

For a residential MBS, the agency's process involved:

1. **Collateral analysis**: borrower-level data (FICO, LTV, DTI, geographic distribution, loan type, documentation) fed into a credit model that estimated the loss distribution of the pool over its lifetime.
2. **Cash flow analysis**: the credit losses were applied to the proposed waterfall to determine, for each rating level (AAA, AA, A, etc.), the minimum subordination required to survive a stress scenario calibrated to that rating.
3. **Stress scenarios**: AAA was supposed to survive a Great Depression-equivalent stress; AA something less severe; and so on.
4. **The structurer iterated** with the rating agency, adjusting tranche sizes until the desired AAA proportion was achieved.

The rating model thus drove the structure, not the other way around. The structurer's job was to find the maximum AAA proportion consistent with the rating agency's model.

### How the rating model failed

The agencies' models suffered from several known and several less-known weaknesses:

1. **Geographic correlation**: agency models assumed cross-state housing correlations of 0.1–0.3, against actual stress correlations near 1. Pool-level "diversification" was largely illusory because the national housing market was driven by a common monetary impulse.

2. **No nationally-negative home price scenario**: the most stressed scenarios in the AAA models assumed regional declines but not national. The 2007–2012 outcome (peak-to-trough national decline of ~27% per Case-Shiller, with sand states down 50%+) was outside the agencies' stress envelope.

3. **Layered risks treated additively, not multiplicatively**: a loan with low FICO, high LTV, low documentation, and an ARM structure has loss probability much higher than the sum of those individual risk factor adjustments. Agency models did not adequately capture the interactions.

4. **The "vintage effect" (Section 2.6) not captured**: the agencies' models were calibrated on historical data and did not anticipate that observable loan characteristics increasingly understated actual underwriting quality.

5. **Pre-funding and revolving pools**: pools whose composition was finalized after the rating was issued were rated on representative collateral characteristics, not on the actual pool — a structural disconnect from the eventual loss reality.

6. **Insufficient analyst capacity**: by 2006, structured finance volumes had grown to the point where a single analyst at S&P or Moody's was producing dozens of ratings per quarter on multi-billion-dollar deals. The model output dominated; analyst judgment had little time to operate.

7. **Internal pressure**: post-crisis disclosure showed pervasive internal communications acknowledging the inadequacy of the models, the pressure from issuers to maintain favorable subordination levels, and the commercial cost of "losing deals" by being too conservative. The S&P "structured by cows" instant message is the most famous, but FCIC document releases revealed dozens of similar exchanges from Moody's and S&P analysts.

### Rating Inflation: A Structural Forecast Error

By post-crisis hindsight, the senior tranches of 2005–2007 subprime PLS that were rated AAA at issuance experienced cumulative impairment rates (downgrades to below investment grade, or principal losses) of approximately 30–40%. The AAA rating, which empirically suggested an annualized default rate below 0.01% over a 5-year horizon, proved compatible with a multi-thousand-fold higher realized impairment rate in this specific cohort. No previous rating cohort in any major asset class had ever exhibited error of that magnitude.

This is one of the most important facts of the crisis. The system that had been built on the premise of reliable, externally-validated AAA ratings discovered that the rating itself was an artifact of model assumptions that did not survive the stress they were ostensibly built to withstand.

---

## 3.8 The Gaussian Copula and Tranche Correlation

A separate but closely related modeling problem arose in the CDO market (Section 4) but originated in the MBS market: how to model the *correlation* among defaults in a pool.

If defaults are independent, a pool of 10,000 loans with a 5% individual default probability will, by the central limit theorem, experience close to exactly 500 defaults. The variance is small; the senior tranche is almost certainly safe.

If defaults are perfectly correlated, the pool will either experience 0 defaults or 10,000 defaults. Pool-level loss is binary; the senior tranche is no safer than the worst single loan.

Real default behavior lies between these extremes, and the *position* between them — the correlation — determines the loss distribution of the pool and therefore the required subordination for a given rating.

The industry standard model became David X. Li's **Gaussian copula** (Li 2000), which provided a tractable way to model joint default behavior across many obligors using a single correlation parameter. Its mathematical elegance and computational tractability were essential to the scaling of structured credit — without it, modeling a 100-name CDO was a multi-day computational exercise; with it, a desktop computer could price the tranches in seconds.

The Gaussian copula's three critical weaknesses:

1. **Single correlation parameter**: real correlation is state-dependent (low in normal times, high in stress), but the model uses a static, scalar correlation. Worse, the parameter was typically *calibrated to market prices* rather than to fundamental default data, meaning it reflected the consensus pricing of correlation, not its true value. Under stress, the pricing-implied correlation moved far from what underlying defaults actually exhibited.

2. **Gaussian (thin-tail) joint distribution**: actual joint default behavior exhibits fat tails — clusters of defaults occur more frequently than the Gaussian would predict. The copula's assumption of normality systematically understated tail risk.

3. **Calibration off CDS spreads**: when correlation parameters were inferred from credit default swap spreads, the model was calibrated against a market that was itself increasingly an artifact of structuring demand. As CDOs grew, CDS spreads on the names referenced in the CDOs were affected by the structuring activity itself, producing a circular calibration.

Felix Salmon's 2009 Wired article "Recipe for Disaster: The Formula That Killed Wall Street" popularized the criticism of the Gaussian copula. The reality was more nuanced — the model was a useful approximation that became dangerous when its limitations were forgotten, much like Black-Scholes for options. Practitioners knew (or should have known) that the copula's static correlation assumption broke down under stress. The systemic failure was not the model itself but the willingness to treat its outputs as gospel for purposes that exceeded its design specification.

The Gaussian copula matters principally in Section 4 (CDOs), where tranche correlation directly determined pricing. In MBS, the rating agency models used different (and even less transparent) correlation assumptions but produced the same kind of systematic understatement of joint default risk.

---

## 3.9 Why "Diversification" Failed

The single most important conceptual failure underlying the crisis was the belief that pooling regionally distributed mortgage loans produced meaningful diversification of credit risk. The argument was intuitive: California and Florida home prices have historically been weakly correlated; pool them, and you reduce idiosyncratic exposure.

The intuition was wrong for two reasons:

1. **The driver of housing prices was common, not idiosyncratic**: 2003–2006 housing appreciation was driven by national monetary conditions, national securitization demand, and a national lowering of underwriting standards — all of which affected California, Florida, Arizona, Nevada, and to a lesser extent every other state simultaneously. Calling this "diversified" because the loans were spread across states is like calling a portfolio of every NASDAQ stock "diversified" because the companies are in different industries. The variance you have eliminated is the variance you didn't need to worry about; the variance you have not eliminated is the variance that matters.

2. **Defaults respond non-linearly to a common driver**: once national home prices stopped rising, the loans most exposed to appreciation-dependent refinancing (subprime, Alt-A, high-LTV ARMs) began defaulting in synchronized cohorts across geography. The correlation of *defaults* under stress was approximately 1, not 0.2.

A simple way to see this: pool 1,000 loans, each with a 5% lifetime default probability. If defaults are independent, cumulative pool loss is normally distributed around a 5% mean with very small standard deviation, and a senior tranche with 15% subordination is bulletproof. If defaults are perfectly correlated, cumulative loss is 5% with 95% probability and 100% with 5% probability — the senior tranche has a 5% chance of total loss, regardless of subordination level.

The truth in 2006 was that subprime default correlation was much closer to the second case than the first. The system had built securities priced as though it was closer to the first case.

---

## 3.10 The Subprime PLS Pool Structure in Practice

A representative 2006 subprime PLS deal (drawn from the structural shape of deals like NHELI 2006-FM2, SAIL 2006-2, GSAMP Trust 2006-NC2):

**Pool characteristics:**
- Aggregate principal: $1.0 billion
- Approximately 5,500 loans
- WAC: 8.7%
- WALA (weighted-average loan age): 1.5 months
- Weighted-average FICO: 624
- Weighted-average original CLTV: 92%
- % owner-occupied: 88%
- % California: 28%; % Florida: 14%; % Arizona/Nevada: combined 8%
- % full documentation: 50% (i.e., half the pool was low- or no-doc)
- % 2/28 ARMs: 76%

**Capital structure** (with rating agency-required subordination):

| Tranche | Size ($mm) | % | Rating | Coupon (1m LIBOR +) |
|---------|-----------:|--:|-------:|---------------------:|
| A-1 (sr) | 760 | 76% | AAA | +12 bps |
| A-2 | 80 | 8% | AAA | +18 bps |
| M-1 | 30 | 3% | AA+ | +28 bps |
| M-2 | 25 | 2.5% | AA | +35 bps |
| M-3 | 20 | 2% | AA− | +50 bps |
| M-4 | 18 | 1.8% | A+ | +65 bps |
| M-5 | 15 | 1.5% | A | +80 bps |
| M-6 | 12 | 1.2% | A− | +100 bps |
| M-7 | 10 | 1% | BBB+ | +130 bps |
| M-8 | 10 | 1% | BBB | +200 bps |
| M-9 | 7 | 0.7% | BBB− | +280 bps |
| B-1 | 7 | 0.7% | BB+ | +450 bps |
| Equity / OC | 6 | 0.6% | unrated | residual |

**Credit support for A-1 (super-senior AAA):** 24% subordination + ~1% OC + excess spread (~3% per year, capitalizable to a multi-year cumulative cushion).

**At issuance, the structurer presented this as:** "AAA tranche supported by 28%+ of credit enhancement. Stress-tested to losses 4x historical experience."

**By late 2008, this pool was experiencing:**
- 60+ day delinquency rate: 35%
- Cumulative realized loss: 12% and rising
- Equity tranche: completely wiped out
- B-1 through M-7: completely wiped out
- M-1 through M-6: substantial principal impairment
- A-2: principal losses
- A-1: still receiving payments but downgraded to CCC or lower; market price 30 cents on the dollar

The realized credit losses on the 2006 subprime vintage approached 20% of original principal — within the range that subordination levels were *supposed* to absorb in extreme stress, but the structure of the waterfall meant that early credit losses concentrated in the mezzanine tranches and that the senior tranches' protection eroded faster than the cumulative loss numbers suggested.

The key insight: the mezzanine tranches of these PLS deals (the BBB and BBB− slices) became the **toxic inputs to the CDO machine described in Section 4**. They were small in dollar amount per deal but, when aggregated across thousands of deals and repackaged into CDOs, became the most consequential single category of structured credit instrument in the crisis.

---

## 3.11 The "AAA Bait-and-Switch": A Structural Diagnosis

To summarize Section 3's main mechanical claim: it was possible to take a pool of loans with an *average* expected cumulative loss of 6–8% and an expected loss volatility (under static correlation assumptions) of perhaps 1.5–2 percentage points, and to extract from that pool a senior tranche representing 75–80% of the pool's notional that the rating agencies would label AAA.

The implicit claim of that AAA label was: this tranche has approximately the same expected loss profile as a AAA corporate bond — that is, an annualized default rate on the order of 0.01% and a cumulative 5-year impairment rate well under 1%.

The actual mechanism by which the rating was conferred:

1. The agency model assumed regional housing correlations were 0.1–0.3.
2. The model assumed no nationally-negative home price scenario.
3. The model assumed that observable loan characteristics fully captured the credit profile (i.e., no vintage effect).
4. The model treated layered risk factors additively rather than multiplicatively.
5. The model was calibrated on a benign historical period (1990s–early 2000s) in which housing nationally never declined.
6. The model's output was used as the dispositive input to a process whose commercial structure incentivized the agency to find the most favorable subordination levels.

Each of these is an individually defensible modeling choice for an MBS portfolio of prime conforming loans in a normal macro environment. In aggregate, applied to subprime collateral in an environment where the macro fundamentals supporting the historical loss experience had reversed, the model produced ratings that were systematically and severely incorrect.

This is the foundational fact that the Big Short investors (Section 5) identified: not that the loans were bad — everyone knew that — but that the *AAA tranches* of the bonds built on the bad loans were dramatically mispriced because the rating itself was an artifact of an inapplicable model.

---

## 3.12 Closing Frame for Section 3

A residential mortgage-backed security is a contractual partition of a pool's cash flows into bonds with different priorities of payment and different positions in the loss-absorption stack. The structuring economics make the rating of the senior tranches the single most important commercial variable for the issuer. Rating agency models, under issuer-pays compensation and competitive pressure, produced subordination levels that allowed issuers to designate 75–80% of subprime pool principal as AAA.

This worked — generated returns matching the rating's implied risk — only under the conditions used to calibrate the models: rising home prices, regional correlation, no nationally negative scenarios, and observable loan characteristics fully capturing credit profile. When those conditions reversed in 2006–2008, realized losses on the cohort exceeded model stresses by an order of magnitude, and a generation of ostensibly-safe paper proved to be approximately the riskiness of the underlying mezzanine tranches of subprime pools.

The mezzanine tranches themselves — small in dollar amount but, by 2006, available in huge cumulative quantity — became the input to the next stage of financial engineering. Section 4 examines that stage: the construction of CDOs from MBS mezz tranches, the synthetic multiplication of mortgage exposure through credit default swaps, and the concentration of cumulative tail risk in the balance sheets of a small number of dealer banks and one large insurance company.
