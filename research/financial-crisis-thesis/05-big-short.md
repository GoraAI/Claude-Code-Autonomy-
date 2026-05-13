# Section 5 — The Big Short Investors

## The Anatomy of a Correlation Trade Against the Housing Market

> "The market can remain irrational longer than you can remain solvent."
> — Attributed to John Maynard Keynes (likely apocryphal but widely cited; the operative principle remained binding)

A small number of investors — perhaps fifteen identifiable funds and individuals globally, with combined assets under management well under 0.5% of the structured credit market they shorted — identified the structural mispricing of subprime mortgage credit between 2005 and 2007 and constructed trades to profit from its collapse. The popular version of this story, told most famously in Michael Lewis's *The Big Short* (2010) and the 2015 film, emphasizes individual personalities and dramatic narrative. The technical version is more interesting.

This section addresses three questions:

1. **What did they actually see**, that the rest of the institutional system failed to see?
2. **How did the trade work mechanically** — what did they buy, from whom, at what price, with what cash flow profile?
3. **Why did most institutions fail to take the trade, even after some had seen the underlying data?**

The answer to the third question is the most institutionally interesting. The Big Short was not, primarily, an information advantage. The relevant data was largely public. It was a *behavioral*, *career-incentive*, and *liquidity* advantage. Understanding why is more useful than understanding the trade itself.

---

## 5.1 The Cast

The principal investors most commonly identified with the trade, in approximate order of conviction and notoriety:

**Michael Burry (Scion Capital).** Former neurology resident, self-taught investor, ran Scion from California. Identified the trade in 2004–2005 via loan-level analysis of mortgage prospectuses. Constructed his short by purchasing CDS on specific subprime MBS deals, primarily 2005–2006 vintage, from major dealer counterparties. Faced significant investor revolt in 2006–early 2007 as the trade carried negatively before paying out. Wound down Scion in 2008 after profiting heavily.

**Steve Eisman (FrontPoint Partners, a Morgan Stanley-owned hedge fund).** Career sell-side mortgage analyst turned hedge fund manager. Eisman had covered the subprime industry as a research analyst in the late 1990s and held a structurally bearish view from before the housing boom even began. Used CDS on MBS and ABX exposure, supplemented by short equity positions in subprime lenders, ratings agencies, and bond insurers.

**Greg Lippmann (Deutsche Bank).** Trader, not hedge fund manager. Lippmann was the head of Deutsche Bank's CDO trading desk and was the most aggressive seller of CDS protection on subprime to outside hedge funds during 2005–2006, while internally accumulating a large short subprime book at Deutsche. His January 2006 "Shorting Home Equity Mezzanine Tranches" presentation, which circulated widely on Wall Street, was the trade thesis pitched to dozens of hedge funds. Some bought; most declined.

**Cornwall Capital (Charlie Ledley, Jamie Mai, Ben Hockett).** Small fund (started with $110,000 of personal capital, ran at low tens of millions through the trade). Identified the trade via Lippmann's pitch and via independent reading of CDO prospectuses; focused specifically on the BBB tranches and on shorting the senior tranches of CDO-squareds, where they believed mispricing was most extreme.

**John Paulson (Paulson & Co.).** Macro hedge fund manager. Made what was probably the largest individual profit on the short trade — over $15 billion in 2007–2008 across his various funds. Paulson worked closely with Goldman Sachs to construct synthetic CDOs (including the Abacus 2007-AC1 deal that later produced the Goldman SEC settlement) in which Paulson selected the reference collateral with the explicit objective of shorting it. The legality of this is, in retrospect, a much-debated question. Paulson was a sophisticated counterparty and the disclosed structure was nominally adequate; the SEC's action was specifically against Goldman for inadequate disclosure of Paulson's role to other investors.

**Jeffrey Greene** (independent investor, sometimes operating in cooperation with Paulson). Lower profile but similar trade.

**Other identifiable shorts** included Hayman Capital (Kyle Bass, who used the trade as an entry into the family-office structured credit space), Andrew Redleaf at Whitebox Advisors, Stephen Schwarzman at Blackstone (smaller position, more cautious), and a handful of macro funds (Brevan Howard, BlueCrest in part) that took directional CDS positions.

What's worth noting: these were not the largest funds. They were generally credit-focused or independent-minded. Most large mainstream long/short equity funds, most of the major fixed-income shops, and essentially all of the major institutional asset managers were *not* on the trade. The shorts were concentrated in a handful of relatively small accounts.

---

## 5.2 What They Actually Saw

The mortgage market produced a remarkable amount of public information, much of it ignored. The key data sources accessible to anyone willing to do the work:

### 5.2.1 The Loan-Level Tape

Each MBS deal at issuance was accompanied by an *issuer-prepared prospectus supplement* (often 200–400 pages) and a *loan-level data tape* — a flat-file dataset listing every single loan in the pool with its characteristics: original balance, FICO, LTV, CLTV, documentation type, loan purpose, occupancy, geography (to the ZIP-code or sometimes property level), debt-to-income ratio, interest rate, ARM characteristics, prepayment penalty terms, and (for seasoned loans) updated delinquency status.

The tapes were distributed to bond investors via Bloomberg, INTEX (a third-party structured finance data and analytics platform), and the rating agencies. They were not "secret" — anyone with an INTEX subscription (a few thousand dollars per year) could pull them. Few participants outside structuring desks and a handful of dedicated buyside analysts actually read them.

The tapes told a clear story. A representative 2006 vintage subprime MBS pool would show:

- Median FICO around 620 (vs. national median ~720).
- 50%+ stated income (no income verification).
- 30%+ piggyback junior liens (so the borrower's effective LTV was 95%+).
- 75%+ 2/28 ARMs with first reset in 2008.
- Geographic concentration of 30%+ in California, Florida, Arizona, Nevada.
- Property type often investor (10–20%) rather than owner-occupied.
- DTI ratios at the upper edge of underwriting tolerance, computed on teaser rates.

A reader who simply read the tapes for a representative sample of pools could see that the borrowers were marginal, the loans were structurally dependent on home price appreciation, and the resets were concentrated in a narrow 2008 window. This was not hidden information.

What was hidden was the *vintage effect*: that even within the apparent characteristics, the actual underwriting was worse than the documentation suggested. The Big Short investors who looked carefully (especially Burry) became aware of this through anecdotal evidence — interviews with former originators, comparisons of loan-level vs. servicing-reported data showing early payment defaults — but they did not need to prove the vintage effect to take the trade. The observable characteristics alone, combined with the structural dependence on appreciation, were sufficient.

### 5.2.2 The Prospectus

The prospectus supplement disclosed the deal's tranche structure, subordination levels, OC and excess spread mechanics, loss triggers, and rating agency methodologies. Reading 100 prospectuses in a year (a few per week) was sufficient to develop a working understanding of how the agencies were constructing AAA out of subprime. Most institutional credit officers did not do this work, on the rationale that the rating was the relevant credit opinion and they were not in the business of second-guessing the agencies.

### 5.2.3 The Servicing Reports

Once a pool was issued, monthly servicing reports (filed with the SEC under Regulation AB after 2005, distributed to bondholders, available on Bloomberg) showed delinquency rates, loss rates, and prepayment speeds at the deal level. By late 2006, the servicing reports on 2005–2006 vintage subprime were already showing materially worse early performance than the rating agencies' base-case assumptions. By spring 2007, the data was emphatic: subprime was performing far worse than priced.

The Big Short investors tracked these reports in real time. Most institutional bond investors looked at them quarterly or less. Many retail and institutional investors holding subprime through mutual funds or fund-of-funds never saw the servicing data at all.

### 5.2.4 The Macro Backdrop

Housing prices had stalled by late 2005 in many bubble markets and were declining in some (San Diego, Phoenix, Las Vegas, parts of Florida) by mid-2006. The Case-Shiller national index peaked in mid-2006 and had visibly turned by year-end. National housing inventory was rising. Refinance activity was falling. Anyone who tracked the housing market itself, not just the bond market, could see that the subprime business model (refinance at the reset, on appreciated equity) was breaking.

### 5.2.5 The Synthesis

Putting it together — bad loans, bad ratings, falling housing prices, structural reset cliff, and the synthetic multiplier — the trade thesis was approximately:

> "BBB tranches of 2005–2007 vintage subprime MBS will experience cumulative losses substantially exceeding their subordination, leading to total writedowns within 18–36 months. CDS protection on these tranches is currently priced as though such an outcome has near-zero probability. Buying CDS protection at 100–300 bps per annum offers an asymmetric payoff: maximum loss is the premium paid; maximum gain is approximately the full notional (par minus recovery)."

The trade was not, by 2006 standards, particularly subtle. What was scarce was not the analysis but the willingness to put on a negatively-carrying trade and hold it for years against marks that moved against you for much of that period.

---

## 5.3 The Trade Mechanics

### 5.3.1 The Instrument

The primary short instrument was the **single-name CDS** on a specific subprime MBS tranche. The protection buyer:

- Identified a specific reference tranche (e.g., the BBB- tranche of "GSAMP Trust 2006-NC2 M-8").
- Negotiated bilaterally with a dealer counterparty (Deutsche Bank, Goldman, Bear, Lehman, Morgan Stanley) for a CDS contract.
- Agreed to pay quarterly premium of, say, 200 bps per annum on the notional amount.
- Received a payout if the reference tranche experienced a "credit event" — typically defined as principal writedown, interest shortfall, or failure to pay.

The contracts followed the ISDA standard credit derivatives confirmation for ABS reference entities ("Pay-As-You-Go" CDS, published in 2005). Key features:

- **Floating recovery**: actual loss settlement based on the realized cash flow shortfall, not a fixed recovery rate.
- **Pay-as-you-go**: payments flowed as the reference tranche experienced impairments, not in a single lump sum at default.
- **Step-up rates**: premium could increase if the protection buyer's position was at risk in certain ways.

The Big Short investors typically negotiated portfolios of these contracts, covering dozens or hundreds of specific reference tranches, in order to diversify deal-level idiosyncrasies and approximate a generic "short subprime" position.

### 5.3.2 The ABX

Once the ABX indices launched in January 2006, the alternative was to trade index CDS:

- **ABX.HE.06-1.BBB** — referencing the BBB tranches of 20 specific 2006 H1 subprime deals.
- **ABX.HE.06-2.BBB** — similar, second half of 2006.
- **ABX.HE.07-1.BBB** — first half 2007.

ABX positions were:

- More liquid (could be entered and exited at observable prices).
- More transparent (the underlying basket was public).
- Cheaper to establish (less negotiation overhead).
- Subject to standard ISDA documentation.

Most Big Short investors used a combination of single-name CDS (for the cleanest direct exposure to specific bad deals) and ABX positions (for liquidity and macro exposure).

### 5.3.3 The Carry

The premium paid by the protection buyer was the trade's negative carry. A typical trade in 2006:

- Notional: $10mm of CDS on a BBB- subprime MBS tranche.
- Premium: 200 bps per annum.
- Annual cost to maintain the position: $200,000 per $10mm of notional.
- Position size for a hedge fund running this trade: $500mm to $2bn of total notional.
- Annual carry cost: $10mm to $40mm per fund.

For a $1 billion AUM fund, this was 1–4% per year of negative carry. The fund manager had to convince investors that the trade payoff justified the multi-year drag on returns. This is the single most challenging aspect of the Big Short trade as an *investment management problem*: it required holding a money-losing position for an extended period before the thesis played out.

### 5.3.4 The Marks

Even worse than the carry was the *mark-to-market volatility* of the position during 2006 and early 2007. CDS positions are marked to model or to dealer quotes daily. As long as subprime credit spreads stayed tight, the CDS positions held by Big Short investors were marked at modestly negative variation margins — meaning the fund was required to post collateral to its counterparties as the position's mark deteriorated.

The mark-to-market volatility produced fund-level performance reports that looked terrible:

- Position size: $1bn notional CDS.
- Day-1 entry price: 200 bps premium.
- Mid-2006 mark: subprime spreads tighter at 150 bps premium → fund had a $5–10mm unrealized loss.
- End-2006 mark: subprime spreads tightened further to 120 bps → fund had $15–20mm unrealized loss.
- January 2007 mark: ABX launched and prices initially tracked low subprime spreads → continued mark-down.
- February 2007 mark: HSBC announced major subprime writedowns; ABX BBB collapsed → fund swung to large gain almost overnight.

The path was non-linear and excruciating. Funds running this trade lost 5–10% of NAV in 2006 before recovering massively in 2007–2008. Some investors redeemed at the worst point and missed the payout entirely.

### 5.3.5 Counterparty Risk

A subtle but important issue: the protection buyer's payoff depended on the protection seller's solvency at the time of payout. If your CDS was with Lehman Brothers and Lehman went bankrupt, your protection became an unsecured claim in the bankruptcy estate. Some Big Short investors held this counterparty exposure to dealers that would themselves fail — a tail risk on the tail risk.

The mitigations:

- **Collateral postings**: ISDA Credit Support Annex (CSA) terms required dealers to post variation margin against negative marks. This protected the protection buyer from gradual deterioration but not from sudden counterparty default.
- **Diversification across counterparties**: most funds spread CDS purchases across 5–10 dealers.
- **Conversion to listed exposure**: as the ABX market matured, some positions were transitioned to ABX index trades cleared through ISDA standardized terms.

Burry, Eisman, Paulson, and most other named Big Short investors successfully navigated the counterparty risk. The payouts were largely realized.

---

## 5.4 The Behavioral and Career Dynamics

If the trade was identifiable from public data, why did so few institutions take it? The answer is in the institutional structure of investing, not in any information asymmetry.

### 5.4.1 The Asymmetric Career Payoff

For a portfolio manager at a major institutional asset manager (Pimco, BlackRock, Fidelity, JPMorgan Asset Management), the career consequence structure of the long-subprime vs. short-subprime trade was sharply asymmetric:

- **Long subprime, makes money**: collect bonus, indistinguishable from peers (most of whom are also long subprime). Career: continues.
- **Long subprime, loses money**: everyone else also lost. "We were all wrong." Career: continues.
- **Short subprime, makes money**: hero, but only briefly. Most institutional bonuses are smoothed over multi-year periods; the upside is bounded by compensation structure. Career: better.
- **Short subprime, loses money**: you were wrong against the consensus. Career: damaged or terminated.

The expected career payoff to being a contrarian short was *negative* unless the trade paid out within the timeframe of the next performance review and bonus cycle. This is the structural reason most institutional managers cannot, in practice, take large contrarian positions even when they intellectually believe in them.

Hedge fund managers with multi-year lockups, low leverage, and concentrated personal stakes in their funds (Burry, Paulson, Lippmann's internal Deutsche book) had the freedom to absorb the negative carry and the mark volatility. Public mutual fund managers and large institutional accounts generally did not.

### 5.4.2 The Information Treatment Problem

Even when institutional analysts at large firms identified the trade, the information often did not propagate through their organizations to decision-making. Several documented examples:

- **Bear Stearns**: had multiple internal analysts producing bearish work on subprime in 2005–2006; the firm's High-Grade Structured Credit fund (collapsed July 2007) was a buyer of the very paper its analysts were warning about.
- **Merrill Lynch**: similar internal divergence between analysts and trading desks.
- **Citigroup**: research analyst raised concerns about super-senior retention positions in mid-2007; was overruled.
- **Goldman Sachs**: notably *did* shift its house position to short subprime in late 2006 and through 2007 (the "Big Short" within Goldman, distinct from the hedge fund trade). Goldman's risk committee identified the deteriorating mortgage market in December 2006 and instructed the structured products desks to reduce inventory aggressively. This is one reason Goldman emerged from the crisis less damaged than its peers — and one reason the firm faced subsequent litigation over whether it had adequately disclosed its short position to its clients on the other side of the trades.

The pattern: in most large institutions, the trading desks generating fee revenue from continued issuance had more organizational weight than the risk and research functions. The internal politics of dialing down a profitable business line on the basis of contrarian analysis were severe.

### 5.4.3 The Liquidity Constraint

A hedge fund running the Big Short trade needed to survive 18–24 months of negative carry and adverse marks. This required:

- **Patient capital**: investors who would not redeem during drawdowns. Burry famously locked horns with several of his largest LPs over redemption demands in 2006–2007.
- **Adequate balance sheet**: ability to post collateral against negative marks without forced liquidation.
- **Counterparty terms**: ISDA agreements with sufficient threshold and minimum-transfer-amount language to avoid being squeezed on small marks.

Funds that lacked any of these constraints were locked out of the trade even if they had the analytical conviction. The pre-conditions for the trade were as much capital structure as investment thesis.

### 5.4.4 The Information Cascade

Behaviorally, large institutional commitment to subprime credit created a self-reinforcing narrative. When Moody's, S&P, Fitch, Goldman, Citi, Lehman, Pimco, Fannie, Freddie, and dozens of other sophisticated institutions all held positions consistent with continued subprime performance, the analytical burden of being the lone dissenter was substantial. The default Bayesian update for any individual analyst was that "if I think these securities are mispriced, and the entire industry thinks they aren't, the more likely explanation is that I'm wrong than that the entire industry is wrong."

This is a textbook case of an *information cascade* (Banerjee 1992; Bikhchandani, Hirshleifer, Welch 1992). Once a sufficient number of sophisticated actors had committed to a position, additional actors rationally inferred that information must exist supporting that position, even if they couldn't see it. The cascade rolled in one direction until prices broke; then it rolled, equally violently, in the other.

---

## 5.4 A Specific Trade: The BBB Subprime CDS, Walked Through

To make the trade concrete, walk through a representative position.

**Position:**
- Date: March 2006.
- Instrument: CDS protection on the BBB- tranche of "GSAMP 2006-NC2 M-9" — a specific subprime MBS deal originated through New Century.
- Notional: $50 million.
- Counterparty: A major dealer.
- Premium: 250 bps per annum, paid quarterly.

**Cash flow profile:**

| Quarter | Premium Paid | Mark-to-Market Change | Cumulative P&L |
|--------:|-------------:|----------------------:|---------------:|
| Q2 2006 | −$312,500 | −$200,000 (spread tighter) | −$512,500 |
| Q3 2006 | −$312,500 | −$300,000 | −$1,125,000 |
| Q4 2006 | −$312,500 | −$400,000 | −$1,837,500 |
| Q1 2007 | −$312,500 | +$2,000,000 (ABX collapse) | −$150,000 |
| Q2 2007 | −$312,500 | +$8,000,000 (delinquencies spike) | +$7,537,500 |
| Q3 2007 | −$312,500 | +$15,000,000 (rating downgrades) | +$22,225,000 |
| Q4 2007 | −$312,500 | +$12,000,000 (price-to-recovery) | +$33,912,500 |
| 2008 ... | −$1,250,000 | +$6,000,000 (final settlement) | +$38,662,500 |

By late 2008, the reference tranche had experienced full writedown (BBB- of 2006 subprime was, in the realized outcome, essentially worthless). The protection buyer received approximately full notional minus recovery — close to $50 million on a $50 million notional position. Cumulative premium paid was approximately $2 million. **Net profit: ~$38 million on $50 million notional, or 76% gain over the trade duration of ~2.5 years.**

For a fund that had $1 billion of similar notional exposure, the trade returned approximately $760 million in profit — multiples of the fund's NAV at trade entry. This is the order of magnitude of the actual realized payoff to several of the named Big Short investors.

The asymmetry is the key feature: at entry, the maximum loss was the cumulative premium (capped at perhaps 5–10% of notional over the life of the trade); the maximum gain was approximately 80–100% of notional (loss of underlying minus recovery). A 10:1 payoff ratio on a trade with high conviction is a textbook asymmetric position. Burry's framing of the trade emphasized this asymmetry over the directional bet on housing.

---

## 5.5 Why the Banks Resisted Repricing

The Big Short trade only paid out when the protection sellers — primarily dealer banks and AIG — *recognized* the mark-to-market loss on their books. In 2006 and the first half of 2007, the banks systematically resisted repricing subprime exposure. The mechanisms:

### 5.5.1 Mark-to-Model

Illiquid positions (super-senior CDO tranches, retained mezzanine CDO exposure) were marked to internal models rather than observable market prices. The models continued to produce optimistic values even as broader credit indicators deteriorated. ASC 820 (formerly FAS 157), which required a hierarchy of fair-value inputs and disclosure of Level 3 marks (mark-to-model), only became fully effective in November 2007 — and even then, the banks retained significant discretion in choosing model assumptions.

### 5.5.2 Quote Manipulation

In bilateral OTC markets, the daily mark on a CDS or structured position was often set by dealer quotes. When the bank was both the protection seller (hedge fund counterparty) and the protection buyer (AIG counterparty), it had latitude to quote the position favorably. Several hedge funds running the Big Short reported that dealer marks on their positions diverged significantly from the marks the dealers were posting in their own internal risk systems — a "quote war" that played out throughout late 2006 and early 2007.

### 5.5.3 Selective Application of ABX

After ABX launched in January 2006, the index provided an observable market reference for subprime. But the marks on individual deals were not the same as the index — banks could (and did) argue that their specific positions were of higher quality than the index basket and warranted higher marks. The basis between specific-deal marks and ABX prices widened, then violently compressed in the realization of losses.

### 5.5.4 The HSBC Disclosure (February 2007)

HSBC's announcement of an additional $1.76 billion provision for subprime mortgage losses on February 7, 2007 was the first major break in the consensus. HSBC had acquired Household International in 2003, which gave HSBC a large subprime origination platform. The provision announcement signaled that the largest holders of subprime were now publicly recognizing material credit losses — and forced other banks to follow.

The subsequent timeline of subprime credit recognition:

- **February 7, 2007**: HSBC subprime provision.
- **February–April 2007**: subprime originator failures (New Century Financial filed Chapter 11 on April 2).
- **June 2007**: Bear Stearns High-Grade Structured Credit Fund and Enhanced Leverage Fund disclosed major losses, eventually wiped out.
- **July 2007**: Moody's and S&P announced large-scale downgrades of subprime MBS and CDO tranches (the first major rating action on the cohort).
- **August 9, 2007**: BNP Paribas froze redemptions on three structured-credit funds, citing inability to value the assets. This event is widely identified as the start of the funding crisis (Section 6).

Each event triggered another round of Big Short payoffs as marks moved adversely against the protection sellers.

### 5.5.5 The Rating Action as Trigger

The rating downgrades were the canonical trigger for cash settlement and collateral demands. ISDA documentation generally referenced rating actions as credit events or as triggers for collateral postings. When Moody's downgraded a tranche, the bank holding the CDS protection received payments (in pay-as-you-go form) and the protection seller had to post more collateral.

The cascading rating downgrades from July 2007 through 2008 are arguably the single most important "transmission mechanism" by which the underlying mortgage credit losses propagated through the financial system. Without the agencies' belated recognition of the deterioration, the structured products market might have remained nominally undamaged for longer. With the recognition, the propagation was rapid and severe.

---

## 5.6 The Deeper Lesson: Structure Beats Cleverness

The Big Short investors were intelligent, hardworking, and contrarian. But the trade they took was *not primarily an act of analytical genius*. The mispricing was visible to anyone willing to read loan-level data, prospectuses, and servicing reports. Greg Lippmann was actively pitching the trade to dozens of hedge funds in 2005–2006. The information was diffusing through the market.

What the Big Short investors had that most institutional capital did not was a *structure* that allowed them to take the trade:

- Concentrated personal stake (alignment with outcomes, not bonuses).
- Long-duration capital (no quarterly redemption pressure).
- Manageable size (could enter and exit positions without market impact).
- Bilateral relationship with dealer counterparties (could negotiate ISDA terms).
- Internal authority (no investment committee veto).

The lesson is structural rather than analytical: the institutional investing system in 2006 was *structurally incapable* of holding the trade that the data supported. Even when individuals within institutions saw the problem, the institutions could not act on it. This is a recurring pattern in financial crises and a critical input to thinking about modern fragility (Part II).

---

## 5.7 Adjacent Insights: What the Big Short Investors Didn't See

The story is incomplete without acknowledging what the shorts got wrong, or were lucky on:

1. **Timing**: most of them entered the trade earlier than the payoff arrived, and several would have been liquidated or forced to close had the carry phase lasted six months longer. The trade was not "right whenever it played out"; it was right within a window.
2. **Counterparty selection**: the bilateral CDS counterparty risk was real. Several funds had material exposure to dealers that, in late 2008, were themselves at risk of failure. Burry in particular voiced concern about Goldman and Deutsche as counterparties.
3. **Liquidity at the payoff**: the marks moved most violently in late 2007 and 2008, when many of the original dealer counterparties were themselves stressed. Realizing the gains on the positions required closing trades into dealers that did not want to recognize the losses, which produced friction in price discovery.
4. **The systemic outcome**: the Big Short investors profited from the subprime collapse, but the *broader* outcome — the global banking crisis, the recession, the policy interventions — was not a foregone conclusion at the time they entered the trade. Several of them have acknowledged in retrospect that the policy response (TARP, AIG support, QE) was a major source of uncertainty about realized outcomes.
5. **Post-trade career**: making the Big Short was not, for most of them, a career-extending success. Burry wound down Scion in 2008. Eisman left FrontPoint. The capital that flowed to "the next Burry" was largely allocated to people with no track record on the previous one. Markets are not particularly good at rewarding correctly-identified rare events; they are better at rewarding repeated, replicable strategies, which the Big Short was not.

The investors who walked away wealthiest were not necessarily the ones who saw the trade earliest or held it longest. Paulson, who entered the trade in 2006 (later than Burry or Eisman), profited more than any of them because he scaled it more aggressively, often via custom synthetic CDOs designed to maximize his short exposure. The trade rewards scale once timing is right; before that, scale destroys.

---

## 5.8 Closing Frame for Section 5

The Big Short trade is best understood as a correlation trade combined with a careful selection of structurally-impaired underlying instruments. The mispricing was identifiable from public data. The trade was constrained primarily by capital structure (the ability to hold negative carry and adverse marks) rather than by information access. Most institutions were structurally incapable of taking the trade even when individuals within them saw it.

The investors who succeeded were running small, founder-controlled vehicles with patient capital, often with personal stakes that aligned their incentives with the multi-year outcome rather than the quarterly carry. Their realized returns were large in proportional terms but small in aggregate terms — perhaps $30–50 billion of cumulative profit across all Big Short investors combined, versus a global banking system loss several orders of magnitude larger. The Big Short investors were the bookies for a wager that the rest of the system collectively lost.

The full unwind of the wager — the cascade of failures from Bear Stearns through Lehman to the AIG rescue and the bank recapitalizations — is the subject of Section 6.
