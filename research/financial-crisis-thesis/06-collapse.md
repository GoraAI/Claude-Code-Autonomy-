# Section 6 — The Collapse

## Funding, Repo, Confidence, and the Mechanics of a Bank Run on the Wholesale System

> "A liquidity crisis is what a solvency crisis looks like when you are still telling yourself it is a liquidity crisis."
> — Anonymous central banker, quoted in private communication, 2009

The fundamental insight required to understand the events of 2007–2008 is that **the bank run did not occur at the deposit window**. It occurred in the wholesale funding markets — the repo market, the asset-backed commercial paper market, the prime brokerage relationships, the interbank lending market — where the major financial institutions financed their long-dated, illiquid assets with overnight or short-term liabilities. When the providers of that short-term funding lost confidence in their counterparties, they refused to roll, and institutions worth tens or hundreds of billions of dollars in apparent assets ran out of cash in a matter of days.

This section traces the collapse in roughly chronological order, with emphasis on the *funding-market mechanics* that turned each individual institution's problem into a system-wide event.

---

## 6.1 The Architecture of Wholesale Funding

Before tracing the timeline, it is essential to understand the structure of the funding markets that failed.

### 6.1.1 Repo

The **repurchase agreement** ("repo") is the workhorse of dealer bank funding. A repo is, legally, the sale of a security with an agreement to repurchase it at a later date at a slightly higher price. Economically, it is a collateralized loan.

- The borrower (typically a dealer bank, hedge fund, or other levered investor) "sells" Treasury bonds or other high-quality securities to the lender (typically a money market fund, pension fund, securities lender, or corporate treasury).
- The lender pays cash for the securities; the borrower pays slightly more cash to repurchase them at a future date — often the next business day.
- The difference between the sale price and the repurchase price is the implicit interest on the loan.

A repo trade has the following economic features:

- **Collateralized lending**: the lender has the collateral if the borrower defaults; the loan is therefore "secured."
- **Short-term**: typically overnight or, at most, a few weeks. Repo is rolled — the borrower repays the loan with proceeds of a new repo, ad infinitum.
- **Haircut**: the lender lends less than the full market value of the collateral. A 2% haircut on $100 million of Treasury collateral means the lender provides $98 million of cash. The haircut absorbs collateral price volatility during the repo term.
- **Bankruptcy-remote**: under the U.S. Bankruptcy Code (§559) and corresponding provisions elsewhere, repo collateral is exempt from the automatic stay in bankruptcy. The lender can immediately seize and sell the collateral upon counterparty default, without waiting for court proceedings.

The repo market in 2007 was approximately $4–4.5 trillion in size in the U.S. (gross, daily). The dealers were the largest borrowers. Money market funds, pension funds, corporate treasurers, and securities lenders were the largest lenders.

### 6.1.2 Tri-Party Repo

A specific structure within repo deserves attention: **tri-party repo**, in which a clearing bank (in the U.S., almost entirely Bank of New York Mellon and JPMorgan Chase) sits between the borrower and the lender, managing collateral and cash flows for both sides.

In tri-party:

- The clearing bank holds the collateral in a custodial account.
- Each morning, the clearing bank "unwinds" the trades — returning collateral to the borrower's account in exchange for the cash from the lender. The borrower has the collateral free during the day for use in other trades (settlements, hedging operations).
- Each afternoon, the trades are "rewound" — collateral is moved back to the lender's account, and the cash loan is recommitted.

During the intraday window between unwind and rewind, the clearing bank is effectively extending credit to the borrower against the collateral. In normal times, this is operational plumbing. In a crisis, it is a critical pressure point: if the clearing bank becomes uncertain about the borrower's overnight survival, it can refuse to rewind, effectively triggering a default.

This dynamic mattered in March 2008 (Bear) and again in September 2008 (Lehman). The clearing banks — particularly JPMorgan Chase, which served Lehman — had real-time visibility into their counterparties' funding stress and discretionary authority over whether to extend the daylight credit. JPMorgan's collateral demands on Lehman in the days before Lehman's failure are now widely understood to have been a critical accelerant.

### 6.1.3 Asset-Backed Commercial Paper (ABCP)

ABCP is short-term debt (typically 1–270 days, often 30–90 days) issued by special-purpose entities, secured by pools of receivables — credit card balances, auto loans, mortgages, or, in the relevant cases, asset-backed securities.

The ABCP market grew to approximately $1.2 trillion outstanding by mid-2007. The structures behind it included:

- **Single-seller conduits**: SPEs financing the receivables of a single sponsoring bank. Common for credit card and auto loan securitization.
- **Multi-seller conduits**: SPEs financing receivables from multiple corporate originators, with the sponsoring bank typically providing a liquidity backstop.
- **Structured Investment Vehicles (SIVs)**: SPEs holding long-dated MBS, CDO, and corporate bond assets, financed with a mixture of medium-term notes and ABCP. SIVs were leveraged 10–15x and earned the spread between long asset yields and short funding costs.
- **ABCP-funded CDOs**: short-duration ABCP financing long-duration CDO collateral.

The critical structural feature: ABCP issuance depended on continuous market access. If the conduit could not roll its commercial paper, it had to either liquidate assets (often at fire-sale prices) or draw on its bank liquidity backstop. The backstop banks — which had treated these as off-balance-sheet during normal times — would be forced to consolidate the assets onto their own balance sheets, taking the credit risk back.

ABCP was particularly important to European banks. Citigroup, HSBC, IKB Deutsche Industriebank, Sachsen LB, Landesbank Baden-Württemberg, Société Générale, and others sponsored conduits and SIVs that held subprime-related collateral. When ABCP funding broke down in August 2007, these banks were forced to absorb tens of billions of dollars of assets — a major channel through which the U.S. subprime crisis was transmitted to European balance sheets.

### 6.1.4 Money Market Funds

U.S. money market funds (MMFs) held approximately $3.5 trillion of assets at peak. They were structured to maintain a constant $1.00 net asset value per share, achieved by holding only short-duration, high-quality paper and amortizing prices rather than marking to market.

MMFs were major lenders in:

- The repo market.
- The commercial paper and ABCP market.
- The Treasury bill market.
- The interbank deposit market (through certificates of deposit).

When MMFs become uncertain about a counterparty, they refuse to roll lending. The same dynamic applies in reverse: when MMF investors become uncertain about the MMF, they redeem. In September 2008, both ends of this dynamic ruptured simultaneously, with consequences described later in the section.

### 6.1.5 Inter-Bank Term Funding (LIBOR)

Banks lent unsecured to each other in the London Interbank Offered Rate market — the rate banks were willing to lend to each other on unsecured terms for a defined term (overnight, one month, three months). The LIBOR rate is the price of unsecured interbank credit and was, prior to the crisis, only modestly above the risk-free rate (Fed funds or repo).

The spread between 3-month LIBOR and the overnight indexed swap (OIS) rate — the "**LIBOR-OIS spread**" — became the most-watched stress indicator of the crisis. In normal times, LIBOR-OIS sits at 5–15 bps. During the crisis it widened to 364 bps at peak (October 2008), reflecting banks' refusal to lend unsecured to each other even at very short maturities.

---

## 6.2 The Asset-Liability Mismatch of the Major Dealers

The major investment banks and large universal banks ran a profound asset-liability maturity mismatch:

- **Assets**: long-dated, often illiquid — corporate loans (3–7 year), commercial real estate loans (5–10 year), MBS (5–10 year average life), CDO tranches (5–10 year), private equity commitments, mortgage origination pipeline, prime brokerage receivables.
- **Liabilities**: short-dated, often overnight — repo, commercial paper, intra-day clearing credit, customer prime-brokerage cash balances.

A representative dealer in 2007:

| Asset Side | Approximate % | Average Maturity |
|-----------|--------------:|------------------|
| Trading inventory (liquid: Treasuries, agencies) | 25% | <1 month |
| Trading inventory (less liquid: corporate, MBS, CDO) | 35% | 5–10 years (modeled) |
| Loans and receivables | 25% | 1–10 years |
| Other (PE, real assets) | 15% | 7+ years |

| Liability Side | Approximate % | Average Maturity |
|----------------|--------------:|------------------|
| Repo financing | 35% | overnight to 1 week |
| Commercial paper | 8% | 1–3 months |
| Unsecured short-term notes | 10% | 1–9 months |
| Customer balances (prime brokerage) | 12% | overnight to call |
| Medium-term notes | 10% | 1–3 years |
| Long-term debt | 15% | 3–10 years |
| Equity | 5% | n/a |

At 30:1 leverage, equity was a 3.3% cushion against asset price moves. A 5% mark-to-market decline in the inventory book — readily achievable in stressed credit conditions — could wipe out 1.5× the firm's equity. The system was solvent only if asset values remained close to model and funding remained continuously available. Both conditions failed in 2007–2008.

---

## 6.3 The Timeline: Phase 1 — The Slow Crack (February 2007 – August 2007)

The first phase of the collapse is best characterized as the *recognition phase* — the system gradually accepting that subprime credit losses would be larger than priced.

**February 7, 2007 — HSBC Provision.** HSBC announces an additional $1.76 billion provision for U.S. subprime mortgage losses, related to its 2003 acquisition of Household International. First major recognition by a global bank.

**February 27, 2007 — Chinese stock market correction.** Apparently unrelated but coincides with renewed risk-off positioning globally. The S&P 500 falls 3.5% on the day. Subprime-related credit spreads widen.

**March 2007 — Subprime originator failures begin.** Fremont General, Accredited Home Lenders, Indymac, and others announce major reserves, layoffs, or operational shutdowns. New Century Financial's stock falls 90%.

**April 2, 2007 — New Century Financial Chapter 11.** The second-largest subprime lender in the U.S. files for bankruptcy. Triggered by warehouse lender refusals to fund and accumulating early-payment-default repurchase demands.

**May–June 2007 — Bear Stearns hedge funds.** Bear Stearns' High-Grade Structured Credit Strategies Fund and High-Grade Structured Credit Strategies Enhanced Leverage Fund — two internal hedge funds at the firm running long subprime CDO positions with up to 25x leverage — begin showing severe losses. By late June, Bear suspends redemptions; by mid-July the funds are effectively wiped out. Bear advances $3.2 billion to the high-grade fund (the senior fund) to prevent forced asset sales; the enhanced leverage fund is liquidated.

**July 10, 2007 — Major Rating Downgrades.** Moody's and S&P announce reviews of approximately $17 billion of 2006-vintage subprime RMBS and follow with downgrades. The first systemic recognition by the rating agencies of the depth of the loss problem. ABX indices and CDO marks fall sharply.

**July 31, 2007 — IKB Deutsche Industriebank emergency rescue.** German regional bank IKB requires a $4–5 billion bailout from KfW and a banking syndicate after its Rhineland Funding conduit cannot roll ABCP backed by subprime collateral.

**August 9, 2007 — BNP Paribas freezes funds.** BNP Paribas suspends redemptions on three of its asset-backed securities funds, citing "complete evaporation of liquidity" in certain market segments. This event is widely identified as the *start* of the global liquidity crisis. ECB injects €95 billion of overnight liquidity the same day. LIBOR-OIS spread widens from 10 bps to 60 bps essentially overnight.

The August 9 event matters because it was the moment the funding markets — not just credit markets — began to fail. Up to that point, sophisticated holders of subprime had been taking writedowns. After that point, the providers of *funding* (the MMFs, the ABCP investors, the interbank lenders) began withdrawing credit from any counterparty perceived as exposed to subprime, regardless of the counterparty's actual solvency.

---

## 6.4 The Timeline: Phase 2 — The Funding Crisis Spreads (August 2007 – February 2008)

**August–September 2007.** ABCP outstanding falls from $1.18 trillion to $0.95 trillion over 8 weeks — a $230 billion funding shortfall that has to be absorbed by sponsoring banks (via liquidity backstops) or by asset sales. SIVs unwind rapidly through 2007–2008; most are absorbed onto sponsoring bank balance sheets by Q4 2007.

**September 14, 2007 — Northern Rock bank run.** UK mortgage lender Northern Rock — heavily dependent on wholesale funding (over 75% of its liabilities) — fails to roll its short-term funding. The Bank of England announces emergency support; depositors form lines outside branches (the first UK bank run since 1866). Northern Rock is nationalized in February 2008.

**September 18, 2007 — Fed cuts 50bp.** Federal funds target cut from 5.25% to 4.75%. Beginning of the Fed's easing cycle.

**October–November 2007 — Major bank writedowns.** Citigroup, Merrill Lynch, UBS announce multi-billion-dollar writedowns on subprime, super-senior CDO retentions, and SIV consolidations. Citigroup CEO Charles Prince and Merrill Lynch CEO Stan O'Neal resign.

**December 12, 2007 — Term Auction Facility.** The Fed launches the TAF, allowing banks to borrow term funds against a broad range of collateral. First major expansion of the Fed's liquidity facilities beyond the traditional discount window.

**January–February 2008.** Monoline insurers come under pressure. Ambac and MBIA face downgrade reviews. ACA Capital, a smaller monoline, is effectively insolvent and unable to meet collateral demands. Credit spreads on insured municipal bonds widen as the wraps lose value.

**February 13, 2008 — Auction-rate securities (ARS) market fails.** Dealers stop supporting auctions for variable-rate municipal and student loan securities; investors holding ARS find themselves locked into illiquid positions. A $330 billion market becomes unmarketable in a week. Several state and municipal issuers face refinancing problems.

---

## 6.5 The Timeline: Phase 3 — Bear Stearns (March 2008)

Bear Stearns was the smallest of the five major U.S. investment banks but had the largest relative exposure to mortgage origination, securitization, and trading. It also had the most extreme reliance on overnight repo funding — over $50 billion of overnight repo by early 2008.

**Monday, March 10, 2008.** Rumors circulate that Bear Stearns is facing severe liquidity stress. Hedge funds with prime brokerage relationships at Bear begin moving balances to other dealers. CDS spreads on Bear senior debt widen from 200 to over 500 bps.

**Tuesday, March 11, 2008.** Bear Stearns CEO Alan Schwartz publicly denies liquidity problems. The Federal Reserve announces the Term Securities Lending Facility (TSLF), allowing primary dealers to swap less-liquid collateral for Treasury securities. Markets initially rally but Bear's funding access continues to deteriorate.

**Wednesday, March 12, 2008.** Bear's prime brokerage balances continue to flee. Repo counterparties — particularly Renaissance Technologies, Citadel, and several large mutual funds — pull funding. Bear's cash position falls from $18 billion to under $5 billion over the day.

**Thursday, March 13, 2008.** Bear Stearns informs the SEC and the Federal Reserve that it cannot meet its obligations on Friday morning. The firm is, in funding terms, insolvent — it does not have the cash to settle the next day's repo obligations and clearing settlements.

**Friday, March 14, 2008.** The Federal Reserve, through JPMorgan Chase, extends an emergency loan to Bear Stearns. The Bear Board, the Fed, and Treasury negotiate over the weekend.

**Sunday, March 16, 2008 (evening).** JPMorgan Chase announces an agreement to acquire Bear Stearns at $2 per share (vs. Bear's $30 closing price on Friday and $170 peak the prior year), with the Federal Reserve providing $30 billion of non-recourse financing against a defined pool of Bear's mortgage-related assets (the "Maiden Lane I" facility). The acquisition price is later raised to $10 per share to facilitate shareholder approval.

**March 16, 2008 — Primary Dealer Credit Facility (PDCF).** The Fed launches the PDCF, allowing primary dealers (the major investment banks) to borrow directly from the Fed's discount window against a broad collateral set, on overnight terms. This is the first time the Fed has extended its lender-of-last-resort function beyond commercial banks since the Great Depression. The PDCF allowed the surviving investment banks (Goldman, Morgan Stanley, Lehman, Merrill) to access central bank funding directly — the regulatory framework around which they had operated for decades was effectively abandoned in a weekend.

### Why Bear Failed When It Did

Bear Stearns was, by most contemporaneous solvency measures, not obviously insolvent. Its mortgage book had losses but the firm's reported equity was approximately $12 billion at end of 2007. What killed Bear was a **classic run on a wholesale-funded balance sheet**:

1. Counterparties (prime brokerage, repo) lost confidence in Bear's continued operation.
2. They withdrew funding overnight.
3. Bear lacked the cash to replace the funding with alternative sources.
4. Without funding, Bear could not settle its obligations.
5. Without settlement, Bear was operationally insolvent.

The distinction between *liquidity insolvency* and *solvency insolvency* matters. Bear's assets, marked at fundamental long-term values, would arguably have covered its liabilities. But Bear's liabilities were due overnight, and the market price for Bear's assets in a forced-sale scenario was substantially below model value. A solvent-on-paper firm with a wholesale-funded balance sheet is, in a run, indistinguishable from an insolvent firm. The Fed's intervention prevented the question from being tested.

---

## 6.6 The Timeline: Phase 4 — Spring 2008 to Lehman (April–September 2008)

The post-Bear summer of 2008 was a period of *false calm*. Credit spreads stabilized; LIBOR-OIS narrowed (though still elevated); equity markets recovered some lost ground. The narrative that the worst had passed was widespread. In reality, the system was sliding into a more severe phase.

**April–May 2008.** Major investment banks announce additional writedowns. UBS announces a $19 billion writedown and a Swiss government-supported capital injection. Citigroup raises capital from sovereign wealth funds (Abu Dhabi, Singapore, Korea).

**June 2008.** Oil prices peak at $147/barrel. Inflation concerns rise. The Fed pauses its easing cycle.

**July 11, 2008 — IndyMac fails.** IndyMac Bancorp, a major mortgage lender, is placed in FDIC receivership after deposit runs. The 7th largest U.S. bank failure in history and the largest since 1984.

**July 13, 2008 — Fannie and Freddie crisis intensifies.** Treasury Secretary Paulson announces a "bazooka" — proposed legislative authority to provide unlimited capital to Fannie Mae and Freddie Mac. The GSEs' market access to debt funding had deteriorated to crisis levels as their loss exposure became apparent.

**July 30, 2008 — Housing and Economic Recovery Act.** The legislation Paulson sought is signed into law, authorizing Treasury support to the GSEs and creating the Federal Housing Finance Agency.

**August 2008.** Continued slow deterioration. AIG announces $5 billion of Q2 losses. Lehman Brothers reports a $2.8 billion Q2 loss and announces a $6 billion capital raise.

**September 7, 2008 — Fannie and Freddie conservatorship.** Treasury places Fannie Mae and Freddie Mac into conservatorship under the FHFA. The Treasury commits to invest up to $200 billion (later raised to $400 billion) in preferred stock of each GSE. Senior debt is, in effect, made fully government-guaranteed. Common and preferred equity holders are essentially wiped out.

The Fannie/Freddie action stabilized the agency MBS market but had a critical side effect: holders of GSE *preferred* stock — many of them U.S. regional banks and Japanese institutions that had viewed GSE preferreds as quasi-government securities — took severe losses. Several U.S. community banks failed in subsequent months substantially because of GSE preferred losses.

---

## 6.7 Lehman Brothers (September 2008)

The Lehman Brothers bankruptcy on September 15, 2008 is the canonical event of the crisis. It is also the most misunderstood.

### The Lehman balance sheet

At end of Q2 2008 (reported in July 2008), Lehman reported:

- Total assets: $639 billion.
- Total liabilities: $613 billion.
- Total equity: $26 billion.
- Leverage ratio: ~25x.
- Of which mortgage-related: approximately $80 billion of residential mortgage exposure plus $40 billion of commercial mortgage exposure, plus undisclosed CDO/structured exposures.

The mortgage exposure alone exceeded Lehman's reported equity by a factor of 5. If those positions were mismarked by even 30%, Lehman was insolvent.

### The week of September 8–14, 2008

**Monday, September 8.** Lehman's stock falls 14% after reports that Korea Development Bank had walked away from a potential capital investment. CDS spreads on Lehman widen sharply.

**Tuesday, September 9.** Lehman's stock falls another 45%. Counterparties begin moving prime brokerage balances away from Lehman.

**Wednesday, September 10.** Lehman announces $3.9 billion Q3 loss and a planned spin-off of its commercial real estate and asset management businesses. Markets respond negatively.

**Thursday, September 11.** Discussions begin between Lehman, Bank of America (a potential acquirer), Barclays (another potential acquirer), the Federal Reserve, and the Treasury.

**Friday, September 12.** Treasury Secretary Paulson, NY Fed President Geithner, and SEC Chairman Cox convene a meeting of major bank CEOs at the NY Fed. The Treasury makes clear it will not provide federal money for a Lehman bailout. Bank of America turns its attention to Merrill Lynch instead. Barclays continues exploring a Lehman acquisition.

**Saturday–Sunday, September 13–14.** Barclays' acquisition of Lehman runs aground on a regulatory obstacle: UK authorities require a Barclays shareholder vote before Barclays can guarantee Lehman's trading obligations — a process that cannot be completed in time. Without a buyer and without federal support, Lehman has no Monday morning funding.

**Sunday, September 14, late evening.** Lehman's board votes to file for bankruptcy.

**Monday, September 15, 1:45 AM.** Lehman Brothers Holdings Inc. files Chapter 11. With $639 billion in assets, it is the largest bankruptcy in U.S. history.

### Why no rescue?

The decision not to rescue Lehman remains controversial. Several considerations:

1. **Legal authority**: Paulson and Bernanke have stated, both at the time and subsequently, that the Fed could not lend to Lehman because Lehman did not have adequate collateral. Under Section 13(3) of the Federal Reserve Act, the Fed required "satisfactory collateral" for emergency lending. The Fed has subsequently disputed how binding this constraint actually was.
2. **Political constraint**: the Bush administration faced strong public and Congressional opposition to financial bailouts. The Bear Stearns rescue had been heavily criticized. There was political appetite for letting at least one major firm fail to demonstrate market discipline.
3. **Moral hazard concern**: a uniform rescue policy was seen as creating perverse incentives for future risk-taking.
4. **The buyer problem**: even with federal support, no private buyer was prepared to take Lehman. Bank of America preferred Merrill; JPMorgan was already burdened with Bear; Barclays could not complete the deal in time.

The post-mortem consensus is that the lack of preparation for the Lehman scenario was the deeper failure. The Treasury and Fed had not constructed a clear resolution framework that could be deployed in a weekend. Once the decision sequence ran out of time, the only remaining option was bankruptcy.

### What Lehman's bankruptcy revealed

The Lehman bankruptcy demonstrated several previously-theoretical risks:

1. **Cross-border insolvency**: Lehman's U.S. broker-dealer subsidiary, UK subsidiary, Japanese subsidiary, and others were separately incorporated and entered separate insolvency proceedings. Customer assets in the UK subsidiary (LBIE) were frozen for years; recovery rates were modest and litigation continues a decade and a half later. Cross-border resolution was demonstrably broken.

2. **Tri-party repo unwind**: Lehman's tri-party book was approximately $200 billion at end. JPMorgan, as Lehman's clearing bank, demanded substantial additional collateral in the days before failure, contributing to Lehman's liquidity collapse. The clearing bank's discretionary actions in the days before a counterparty failure were not regulated and produced systemically destabilizing outcomes.

3. **Derivatives unwind**: Lehman had approximately $35 trillion of notional derivatives. Counterparties had to close out positions individually under ISDA. The settlement process took years and produced enormous one-time losses for hedge funds that had been long protection on Lehman or had pending trades with Lehman.

4. **Money market fund break-the-buck**: The Reserve Primary Fund, a major money market fund holding $785 million of Lehman commercial paper, was forced to "break the buck" on September 16 — reporting a NAV of $0.97 per share. This triggered an immediate run on prime MMFs broadly. Within a week, MMFs experienced approximately $300 billion of redemptions, threatening to collapse the commercial paper market entirely. The Treasury responded by guaranteeing MMF balances on September 19 — an emergency action that prevented full collapse of the commercial paper market.

---

## 6.8 The AIG Rescue (September 16, 2008)

Twenty-four hours after Lehman's bankruptcy, AIG informed the Federal Reserve that it could not meet its collateral obligations under its CDS book. The dynamics of AIG's collapse are described in Section 4.6.

The Federal Reserve, under Section 13(3) authority, extended an $85 billion credit facility to AIG against its insurance subsidiaries as collateral. The terms were punitive — initial interest rate of LIBOR + 850 bps, plus a 79.9% equity stake to the Treasury. The total support facility eventually exceeded $180 billion through multiple modifications and additional programs.

The AIG rescue had two distinct objectives:

1. **Preserve AIG's insurance operations**: separate subsidiaries had policyholders whose claims would be impaired in a parent-level bankruptcy.
2. **Honor AIG's CDS obligations to counterparty banks**: AIG owed approximately $80 billion of collateral and settlements to dealer banks on its super-senior CDO CDS book. A failure to pay would have produced corresponding losses at the banks, accelerating their own solvency stress.

The Maiden Lane III facility, established in November 2008, specifically purchased the super-senior CDO bonds underlying AIG's CDS exposure from the counterparty banks at par. This effectively converted the counterparty banks' CDS receivables from AIG into U.S. Treasury exposure — a backdoor bank recapitalization through the AIG vehicle. The Maiden Lane III payments to counterparty banks (including approximately $14 billion to Goldman Sachs, $12 billion to Société Générale, $11 billion to Deutsche Bank, $7 billion to Merrill Lynch, $5 billion to UBS) were the subject of significant subsequent congressional inquiry.

---

## 6.9 The Bank Run Within the Bank Run (September 17–October 14, 2008)

After Lehman and AIG, the wholesale funding markets experienced a near-total freeze:

- **Inter-bank lending**: 3-month LIBOR-OIS spread peaks at 364 bps on October 10. Banks refuse to lend unsecured even at overnight maturity.
- **Commercial paper**: total outstanding falls from $1.97 trillion to $1.40 trillion over five weeks. Major issuers (General Electric Capital, Caterpillar, Ford Motor Credit) face funding-market closure.
- **Money market funds**: redemptions of $300+ billion in the week after Lehman.
- **Repo haircuts**: rise from 1–3% to 25–40% on private-label MBS and other less-liquid collateral. Effectively a 30+ percentage point increase in the haircut equals a 30+ point reduction in lending capacity against the same collateral.
- **Equity markets**: S&P 500 falls 27% between September 12 and November 20.

**Sunday, September 21, 2008.** Goldman Sachs and Morgan Stanley convert from investment banks to bank holding companies, allowing direct access to the Fed's discount window and other commercial-bank funding facilities. The U.S. investment bank model that had existed since Glass-Steagall is effectively ended — by Christmas 2008, none of the five major pre-crisis U.S. investment banks remained in their pre-crisis form (Bear absorbed by JPMorgan; Lehman bankrupt; Merrill absorbed by Bank of America; Goldman and Morgan Stanley converted to bank holding companies).

**September 25, 2008.** Washington Mutual is seized by the FDIC and sold to JPMorgan Chase. The largest U.S. bank failure ever, with $307 billion of assets.

**September 29, 2008.** The House of Representatives initially rejects the Emergency Economic Stabilization Act (TARP). S&P 500 falls 8.8% in a single session — the largest one-day point decline in its history at that time.

**October 3, 2008.** EESA passes after revision; signed into law. TARP authorizes the Treasury to purchase up to $700 billion of "troubled assets" — a mandate that was rapidly modified in implementation to focus on capital injections rather than asset purchases.

**October 7, 2008.** Federal Reserve announces the Commercial Paper Funding Facility (CPFF), purchasing 3-month commercial paper directly from issuers. The CPFF eventually purchases over $350 billion of CP, effectively replacing the private commercial paper market for several months.

**October 13, 2008.** Treasury Secretary Paulson convenes a meeting of the CEOs of the nine largest U.S. banks. The Treasury offers — and effectively requires — capital injections through the TARP Capital Purchase Program (CPP). The banks accept $125 billion of preferred equity investments (Citigroup, JPMorgan, Bank of America, Wells Fargo, Goldman Sachs, Morgan Stanley, State Street, Bank of New York Mellon, Merrill Lynch). The action provides a uniform recapitalization of the banking system, removing the stigma of individual capital raises.

**October 14, 2008.** The full suite of emergency interventions has been deployed: TARP, FDIC bank debt guarantees (the Temporary Liquidity Guarantee Program), Federal Reserve liquidity facilities, MMF guarantees, AIG support. From this point, the funding markets begin to stabilize, though credit conditions remain severe through 2009.

---

## 6.10 The Repo Run Mechanism

A useful unifying frame for the 2007–2008 collapse is Gary Gorton's "repo run" thesis (Gorton 2008, Gorton and Metrick 2010). The framework:

1. The financial system had increasingly funded long-dated, illiquid assets (MBS, CDOs, corporate loans) with short-dated repo financing against the same assets as collateral.
2. The system relied on the perceived safety of the collateral to keep haircuts low and funding continuous.
3. When the perceived safety of the collateral broke down — first for subprime, then for mortgage paper generally, then for any private-label structured product — haircuts on repo rose.
4. Rising haircuts forced borrowers (dealers, SIVs, hedge funds) to either post additional collateral or reduce position size by selling assets.
5. Asset sales depressed prices, further raising haircuts, in a self-reinforcing spiral.
6. The system experienced a "run on the repo market" — the wholesale equivalent of a depositor run on traditional banks.

The Gorton frame highlights why deposit insurance, which had largely prevented commercial bank runs since 1933, was insufficient for the 2008 crisis. The institutions that failed (Bear, Lehman, Merrill in part) were not funded by insured deposits; they were funded by uninsured wholesale markets. The protection that deposit insurance provided to retail depositors did not extend to repo lenders, ABCP holders, or money market funds — and those markets, in aggregate larger than the insured deposit base, ran.

This insight directly motivated the post-crisis regulatory response, particularly the Liquidity Coverage Ratio (LCR), the Net Stable Funding Ratio (NSFR), and the changes to money market fund regulation. The objective of these reforms is to reduce wholesale funding fragility by requiring institutions to hold more high-quality liquid assets and to lengthen the average maturity of their funding. Section 8 examines whether these reforms have achieved their objective.

---

## 6.11 Rehypothecation and Collateral Chains

A subtle but important feature of the wholesale funding market is **rehypothecation** — the practice by which a lender of collateral (e.g., a prime broker holding a hedge fund's securities) reuses that collateral to fund its own positions. Collateral can be rehypothecated multiple times, producing **collateral chains**.

A typical chain in 2007:

1. A pension fund owns a Treasury bond.
2. The pension fund lends the bond to a securities lender (e.g., State Street).
3. The securities lender lends the bond to a hedge fund via the prime broker.
4. The hedge fund pledges the bond to its prime broker as collateral against margin loans.
5. The prime broker rehypothecates the bond to a money market fund via tri-party repo to fund its own position.
6. The money market fund treats the bond as its asset, supporting MMF NAV.

The same Treasury bond is, simultaneously:
- An asset of the pension fund.
- An asset of the securities lender.
- An asset of the hedge fund (as collateral against margin).
- An asset of the prime broker (in custody and rehypothecated).
- An asset of the money market fund (via tri-party repo).

When one link in the chain fails — say, the hedge fund defaults, or the prime broker goes bankrupt — the chain unwinds in ways that produce contested ownership claims and operational chaos. Lehman's bankruptcy revealed the scale of these chains: hedge fund clients of Lehman's UK prime brokerage discovered their securities had been rehypothecated and were now part of the LBIE estate, with recovery uncertain.

UK regulations (notably permissive pre-crisis rehypothecation rules) allowed essentially unlimited rehypothecation; U.S. rules (Rule 15c3-3, the "customer protection rule" for broker-dealers) imposed a 140% cap on customer credit balances available for rehypothecation. The differential treatment meant that hedge funds increasingly preferred to clear in London for capital efficiency reasons, concentrating risk in jurisdictions with weaker investor protections — a textbook case of regulatory arbitrage producing systemic vulnerability.

---

## 6.12 The Policy Response: TARP, QE, and Emergency Facilities

The policy response to the crisis was unprecedented in scale and scope. A summary of the major programs:

### Treasury / TARP ($700bn authorized; ~$420bn deployed)

- **Capital Purchase Program (CPP)**: $250bn for bank preferred stock investments. Returned with profit ($15bn+ of total dividends, interest, and warrant exercises by 2014).
- **Targeted Investment Program**: $40bn for Citigroup and Bank of America (additional capital).
- **AIG support**: ~$70bn via TARP, with additional $112bn via Fed facilities.
- **Auto industry support**: $80bn for GM, Chrysler, and auto finance.
- **PPIP (Public-Private Investment Program)**: planned but minimally deployed.
- **Home Affordable Modification Program (HAMP)**: ~$30bn for mortgage modifications.

### Federal Reserve facilities

- **Term Auction Facility (TAF)**: $400bn peak; standard auction of term funds to commercial banks.
- **Term Securities Lending Facility (TSLF)**: $200bn peak; collateral swaps for primary dealers.
- **Primary Dealer Credit Facility (PDCF)**: $130bn peak; overnight loans to primary dealers.
- **Asset-Backed Commercial Paper Money Market Fund Liquidity Facility (AMLF)**: $150bn peak.
- **Commercial Paper Funding Facility (CPFF)**: $350bn peak.
- **Term Asset-Backed Securities Loan Facility (TALF)**: $50bn peak (against ABS and CMBS).
- **Maiden Lane I, II, III**: special-purpose vehicles holding Bear Stearns and AIG assets.
- **Central Bank Liquidity Swap Lines**: peak $586bn outstanding, supporting foreign central bank dollar liquidity provision.

### Quantitative Easing (QE)

- **QE1** (November 2008–March 2010): $1.75 trillion of agency MBS, agency debt, and Treasury purchases.
- **QE2** (November 2010–June 2011): $600bn of Treasury purchases.
- **Operation Twist** (September 2011): $400bn of duration extension.
- **QE3** (September 2012–October 2014): open-ended, $85bn/month at peak.

By 2014, the Fed's balance sheet had grown from approximately $900 billion (mid-2008) to $4.5 trillion. The policy stance was unprecedented in U.S. history and remained a central feature of monetary policy through the 2020s.

### FDIC Programs

- **Temporary Liquidity Guarantee Program (TLGP)**: federal guarantee of new senior unsecured bank debt and non-interest-bearing transaction accounts. Approximately $618bn of debt issued under the guarantee through 2009.

### Combined Scale

The combined federal commitment (including loan guarantees and not just outlays) peaked at approximately $13–16 trillion (Bloomberg estimate; precise figures vary by methodology). Actual cash outlays were far smaller — the realized cost to the Treasury of TARP was approximately negative (a small net profit when all programs were unwound). The Fed's balance sheet expansion has been gradually unwound (and re-expanded for COVID). The TLGP closed without losses.

The pattern of crisis response — extensive guarantees, modest realized costs, eventual program wind-down — became the template for subsequent crisis interventions (the European sovereign crisis, COVID-19, the 2023 regional bank stress).

---

## 6.13 The Confidence Mechanism

A unifying observation about the policy response: it functioned primarily by *restoring confidence*, not by absorbing losses. The cumulative realized credit losses on bank holdings and AIG were perhaps $1–2 trillion across all major institutions. The face value of guarantees issued was an order of magnitude larger. The difference between the guarantees and the realized losses is the *confidence dividend* of credible intervention.

When the Treasury guaranteed money market funds, deposit redemptions slowed and the cost to taxpayers was minimal. When the Fed committed to unlimited dollar swap lines with foreign central banks, the cross-border funding crisis abated and the swap lines were largely unwound at par. When the FDIC guaranteed new senior bank debt, banks could issue at near-Treasury rates and no claims were paid.

This is a deep insight about the structure of financial crises. The losses are real, but they are bounded; the *confidence collapse* is unbounded and reflexive. A credible commitment by the sovereign to absorb tail losses — even if the commitment never has to pay out in cash — is enormously valuable because it changes the equilibrium of the funding market from "bank run" to "normal operation."

Conversely, a *non*-credible commitment, or a commitment that arrives too late, may be worth less than its dollar value because the underlying confidence has eroded so far that recovery requires more drastic action. The case for *early, decisive* intervention in financial crises is grounded in this insight; the contrast between the U.S. response (early and overwhelming) and the European sovereign debt response (delayed and incrementalist) is the canonical comparison.

---

## 6.14 The Post-Crisis Reforms

The Dodd-Frank Wall Street Reform and Consumer Protection Act (July 2010) and parallel international reforms (Basel III, EU directives) constituted the largest financial regulatory overhaul since the New Deal. A summary of the major elements:

### Dodd-Frank highlights

- **Title I — Financial Stability Oversight Council (FSOC)**: macroprudential coordination across federal regulators.
- **Title II — Orderly Liquidation Authority (OLA)**: bankruptcy-alternative resolution regime for systemically important financial institutions.
- **Title III — FDIC and OTS reforms**: elimination of the Office of Thrift Supervision; FDIC powers expanded.
- **Title IV — Private fund registration**: hedge fund advisers required to register with the SEC.
- **Title V — Insurance reforms**: Federal Insurance Office (FIO) created.
- **Title VI — Volcker Rule**: prohibition on proprietary trading by banks and limits on bank investment in hedge funds and private equity funds.
- **Title VII — Derivatives reform**: central clearing for standardized OTC derivatives; trade reporting to swap data repositories; margin requirements for uncleared swaps; CFTC and SEC jurisdiction over swap markets.
- **Title VIII — Payment, clearing, and settlement supervision**: Federal Reserve oversight of systemically important market utilities.
- **Title IX — Investor protections**: SEC rulemaking authority expanded.
- **Title X — Consumer Financial Protection Bureau**: new agency for consumer financial product regulation.
- **Title XI — Federal Reserve transparency**: GAO audit of Fed emergency facilities; conditions on future use of Section 13(3).
- **Title XII–XV — Various provisions**: including mortgage reform and skin-in-the-game requirements for securitization sponsors (5% retention rule).

### Basel III (international, phased 2013–2019)

- **Higher minimum common equity Tier 1 ratio**: 4.5% of risk-weighted assets, plus a 2.5% capital conservation buffer, plus a 0–2.5% countercyclical buffer, plus a 1–3.5% G-SIB surcharge for systemically important banks.
- **Leverage ratio**: 3% minimum (5% for U.S. G-SIBs) — a non-risk-weighted constraint.
- **Liquidity Coverage Ratio (LCR)**: ratio of HQLA to net cash outflows over 30 days; required ratio 100%.
- **Net Stable Funding Ratio (NSFR)**: stable funding required for assets and off-balance-sheet exposures over a 1-year horizon.
- **Stress testing**: annual scenarios assessing capital adequacy under stress (CCAR in the U.S.; ECB stress tests in Europe).

The combined effect of Dodd-Frank and Basel III was a significant tightening of capital, liquidity, and operational constraints on the largest banks. Pre-crisis leverage of 30:1 at investment banks fell to 10:1 or lower by 2014. The largest U.S. banks accumulated common equity Tier 1 ratios of 11–13% by 2018, up from 6–8% pre-crisis.

Whether this reduced systemic risk or merely shifted it elsewhere is one of the central questions of Part II.

---

## 6.15 What the Collapse Reveals About Financial Systems

Several structural lessons emerge from the 2008 collapse that generalize beyond mortgage credit:

1. **Liquidity is a function of confidence, not of asset quality.** The same asset is highly liquid in normal times and effectively unsellable in stress. Wholesale-funded balance sheets are stable only as long as funding providers retain confidence; that confidence can evaporate in 48 hours.

2. **Systemic risk lives in the connections, not the nodes.** Lehman was not the largest U.S. financial firm; it was the most connected. The connections — through repo, derivatives, prime brokerage, and counterparty exposures — turned a single firm's failure into a global event.

3. **Mark-to-market accounting in stressed markets is reflexive.** When prices fall, mark-to-market losses force position closures, which depress prices further. The accounting regime that produced transparency in normal times became a fire-sale accelerator in stress.

4. **The lender of last resort is the only viable counterparty in a panic.** When private balance sheets are simultaneously distressed, only the sovereign — with the power to create money — can take the other side of the panic-driven trade. The scope of this role has expanded with every crisis.

5. **Resolution authority is at least as important as capital ratios.** A bank can be well capitalized and still fail through funding loss. The legal and operational framework for resolving a failing institution without contagion is the most important structural defense against systemic crisis. Title II of Dodd-Frank addresses this; it has not been tested in practice for a major dealer.

6. **The boundary of the regulated banking system is the boundary of stability.** Shadow banking (MMFs, SIVs, repo, dealer balance sheets, hedge funds) was outside the prudential perimeter and produced the most severe failures. The post-crisis reforms expanded the perimeter but did not eliminate the boundary; new shadow systems have grown since (Section 9).

7. **Behavior is endogenous to the rules.** Each successive regulatory change produced new behaviors and new vulnerabilities. The post-crisis reforms have shifted leverage, opacity, and liquidity mismatch from the traditional banks to the non-bank financial system. The question is not whether risk has been eliminated but where it now lives.

These lessons are taken up systematically in Section 7 (lessons from 2008) and Part II (today's landscape).
