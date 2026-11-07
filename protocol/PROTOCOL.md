# Review protocol

**Review question.** Which studies have implemented and evaluated parallel or high-performance computing (HPC) execution for ship weather routing (SWR)? What parallelization strategies, hardware and performance metrics do they report, and how strong is that evidence?

**Reporting standard.** PRISMA 2020, with the PRISMA-S extension for the search.

## 1. Review set

The review analyses one literature set, **SWR × HPC**: primary studies that implement and evaluate parallel or HPC execution for SWR. It is the evidence base of the HPC implementations section and its tables.

An earlier version of this protocol also defined a multi-objective optimization block (O) and a second literature set of multi-objective SWR studies. That set was removed from the review; the executed queries remain in `queries/` only as a record of the search.

## 2. Time window, language and document types

- **Time window:** from database inception to the search date. No lower year limit is set, because parallel SWR implementations are rare and early distributed work would otherwise be missed. The year distribution is reported instead.
- **Language:** English.
- **Document types:** peer-reviewed journal articles and peer-reviewed conference papers. Reviews, editorials, theses, patents and preprints without a peer-reviewed version are excluded.
- **Fields searched:** title, abstract and keywords (Scopus `TITLE-ABS-KEY`; WoS topic field `TS=`; IEEE Xplore: the Metadata Search API query covers all metadata, so the concept blocks are then evaluated on the title, abstract and keywords of the retrieved records).

## 3. Search blocks of the original protocol (v0.3, Scopus syntax)

- **R (routing):** `"weather routing" OR "ship routing" OR "vessel routing" OR "voyage optimi?ation" OR "voyage planning" OR ((route* OR routing OR path* OR trajector* OR voyage* OR navigation) W/3 (optimi* OR planning OR planner OR finding OR search* OR "decision support")) OR "optimal planning"`
- **M (maritime):** `ship* OR vessel* OR maritime OR sailboat* OR sailing OR yacht* OR ferry OR ferries OR "marine vehicle*"`
- **W (environment):** `weather OR meteorolog* OR metocean OR "meteo-ocean*" OR wave* OR wind* OR "ocean current*" OR current* OR "ocean flow*" OR "ocean environment*" OR "sea state*" OR forecast* OR sailboat* OR sailing`
- **H (HPC):** `"high performance computing" OR "high-performance computing" OR hpc OR parallel* OR gpu* OR "graphics processing unit*" OR cuda OR opencl OR openmp OR mpi OR "message passing" OR multicore OR "multi-core" OR multithread* OR "multi-thread*" OR supercomput* OR "distributed computing" OR "cloud computing" OR "computing cluster*" OR "hpc cluster*" OR "island model" OR "many-core" OR fpga*`
- **Search string** (v0.3) = R AND M AND W AND H. Amendment v0.4 replaced this string by RX AND MX AND H (section 10).

The exact strings executed in each database are in `queries/`. The WoS and IEEE Xplore versions use `NEAR/3` in place of `W/3`. OpenAlex supports neither wildcards nor proximity, so its strings enumerate the word forms instead.

Before the v0.3 search was frozen, the search string was checked against the parallel routing studies already known to the authors. A later completeness check showed two gaps in this string (the M block had no terms for underwater vehicles, gliders or unmanned surface vessels, and the W block missed studies that describe the weather model only in the full text); amendment v0.4 therefore extended the R and M blocks and removed the W block (section 10). Studies that are not indexed, or that describe their parallel execution only in the full text, are reached through citation snowballing.

## 4. Sources

| Source | Access |
|---|---|
| Scopus | Elsevier Search API (`TITLE-ABS-KEY`) |
| Web of Science Core Collection | WoS Starter API (topic field `TS=`) |
| IEEE Xplore | IEEE Xplore Metadata Search API (all-metadata query; concept blocks then evaluated on title, abstract and keywords, matching `TITLE-ABS-KEY`) |
| OpenAlex | title-and-abstract search (supplementary) |
| Citation snowballing | one round of backward and forward citations of the reports that had passed full-text assessment (OpenAlex, Crossref) ("other methods") |
| Studies known to the authors | studies from the submitted version of the paper whose reports were not among the database records ("other methods") |

## 5. Eligibility

A study is included if **all** of the following hold:

- **I1:** Primary study (peer-reviewed journal or conference paper), English.
- **I2:** Route, path or voyage planning of a marine vehicle in which meteo-oceanographic fields (wind, waves, currents, forecasts; static or time-varying) enter the cost or constraints. The field type is recorded.
  - **Tier A1 (direct SWR):** surface ship, ferry or sailboat weather routing.
  - **Tier A2 (closely related):** marine vehicles in stochastic or dynamic ocean flows; integrated routing and ship energy management.
- **I3:** The routing or optimization computation itself is executed with an implemented parallel or HPC scheme (multi-threaded CPU, GPU, cluster or distributed, parallel cloud workers, FPGA), and the scheme is described.
- **I4:** At least one computational performance result is reported (runtime, speedup, throughput, scaling).

A study is excluded if **any** of the following holds:

- **E1:** Parallel execution is only mentioned or proposed, e.g., as future work, or "parallel" is used in a non-computing sense.
- **E2:** HPC is used only for numerical weather prediction or ocean forecasting, or only to train a machine-learning model, not for the routing optimization.
- **E3:** The problem is not route, path or voyage planning of a marine vehicle (e.g., collision avoidance, vehicle control, fleet routing and scheduling, port scheduling, search-and-rescue search planning, non-marine problems); route planning without a meteo-oceanographic field is coded I2.
- **E4:** Review, editorial, thesis or patent.
- **E5:** Additional report of an included study (linked, counted once).

## 6. Selection

- **Deduplication:** by DOI, then by normalized title with publication years differing by at most one year.
- **Stages:** two (title and abstract screening, then full-text assessment).
- **Screening:** the first author conducted the initial screening and full-text eligibility assessment; the other two authors reviewed the provisionally eligible studies, borderline cases concerning HPC-related eligibility were additionally reassessed by a co-author with HPC expertise, and the final study selection was agreed upon following discussion among the authors (wording clarified 2026-10-25; see screening/author_decisions.md).
- **Recording:** at title and abstract screening, records are classified only as include or exclude; exclusion reasons are assigned only after full-text assessment. Each full-text exclusion is recorded with one criterion code: the E-code of an exclusion criterion when one applies; otherwise, the I-code of the inclusion criterion that is not met. Reports whose full text could not be obtained are counted as not retrieved.

## 7. Data items and evidence appraisal

**Data items:** publication year, tier, routing method, optimization type, environmental field type, decomposed workload, parallelism level (job, scenario, island, segment, label, population, kernel or data-parallel), programming model or API, hardware, problem size, baseline type, and the reported performance metrics with their units. Derived values are marked as derived. Data are extracted from the full texts of the included studies by the first author (wording clarified 2026-10-25).

**Evidence classes** (each study takes the strongest class present; the other result types are noted):

- **E-S:** a same-method parallel speedup against the study's own baseline implementation of the same method (a sequential or CPU-only version).
- **E-C:** a cross-algorithm or cross-method runtime comparison.
- **E-T:** throughput or absolute execution times only.
- **E-Q:** a qualitative claim without a measured result.

**Reporting-quality checklist** (Y = 1, P = 0.5, N = 0; used to describe reporting completeness, not to exclude or weight studies):

| Item | Criterion |
|---|---|
| QA1 | Hardware reported |
| QA2 | Parallel scheme described |
| QA3 | Same-method baseline reported |
| QA4 | Speedup or efficiency metric defined and reported |
| QA5 | Scaling tested (≥2 worker counts or problem sizes) |
| QA6 | Code or data released by the authors |

The full scoring rules are given in the paper's QA table.

## 8. Synthesis

The synthesis is descriptive. Performance results are not pooled, because hardware, problem sizes, baselines and metrics differ across studies. Negative findings are stated relative to the included set and the search dates. The included studies are also shown by publication year, parallelism level and tier; records assigned to an issue year after the search year are counted in the search year.

## 9. Data policy

Raw records from Scopus, Web of Science and IEEE Xplore are not redistributed. The package contains queries, dates, counts, identifiers and the screening decisions.

## 10. Deviations from the protocol

**Screening procedure (changed before screening began).** The protocol drafts specified independent screening by two authors at both stages. Before screening began, this was replaced by the procedure in section 6: the first author conducted the screening and eligibility assessment, and the other two authors reviewed the provisionally eligible studies, with an additional reassessment of borderline HPC-related cases by a co-author with HPC expertise (wording clarified 2026-10-25).

### Amendment v0.4 (2026-10-05)

**Timing and reason.** The v0.3 searches were run on 2026-09-30 (Scopus, Web of Science and OpenAlex) and 2026-10-01 (IEEE Xplore). The amendment was made after the screening of these records had been completed, prompted by an independent completeness check of the included set by the authors. A sensitivity check of the v0.3 search against the studies identified in this check showed two design gaps.
- The maritime block had no terms for underwater vehicles, gliders or unmanned surface vessels, although Tier A2 covers such vehicles in ocean flows.
- The environment block required a weather term in the title, abstract or keywords, which misses HPC studies that describe the weather model only in the full text.

**Changes.**
- **Search.** The search was re-run with an extended routing block (RX) and maritime block (MX), and without the environment block: **set X = RX AND MX AND H**. Set X contains every record retrieved by the v0.3 search string. The weather criterion (I2) is applied at screening, on the full text where needed. The OpenAlex search and the citation snowballing use the extended strings.
  - RX: `"weather routing" OR "ship routing" OR "vessel routing" OR "voyage optimi?ation" OR "voyage planning" OR ((route* OR routing OR path* OR trajector* OR voyage* OR navigation) W/3 (optimi* OR planning OR planner OR finding OR search* OR "decision support" OR build* OR construct* OR generat* OR select*)) OR "optimal planning" OR "collision avoidance" OR "collision-avoidance" OR "anti-collision" OR "obstacle avoidance" OR "motion planning" OR "shortest path*" OR "search and rescue"`
  - MX: `ship* OR vessel* OR maritime OR sailboat* OR sailing OR yacht* OR ferry OR ferries OR "marine vehicle*" OR auv OR auvs OR "autonomous underwater vehicle*" OR "underwater vehicle*" OR "underwater glider*" OR "ocean glider*" OR "sea glider*" OR seaglider* OR usv OR usvs OR "unmanned surface vehicle*" OR "unmanned surface vessel*" OR "autonomous surface vehicle*" OR "autonomous surface vessel*" OR "surface vehicle*" OR "autonomous ship*" OR "autonomous vessel*" OR "maritime autonomous surface ship*" OR boat* OR "marine robot*" OR "ocean vehicle*" OR "marine craft*"`
- **Scope.** The scope is unchanged: SWR × HPC (Tier A1 direct SWR, Tier A2 closely related marine vehicles in ocean flows).
  - Problems outside I2 remain excluded under E3: collision avoidance and manoeuvring, vehicle control or guidance architectures, fleet routing and scheduling, port scheduling, search-and-rescue search planning, and non-marine problems.
  - The problem type is decided from the title and abstract; the role of environmental fields in route or path planning studies is decided on the full text.
- **Unchanged.** The scope and the inclusion criteria I1–I4, the tiers, document types, language, the two-stage screening with author verification, and the evidence appraisal.
- **Clarifications (wording, not scope).** E1 and E3 are worded as applied: E1 also covers "parallel" used in a non-computing sense, and E3 names the problem types listed above (section 5) and is limited to the problem type, so that route planning without a meteo-oceanographic field is coded I2 (clarified 2026-10-07; no decision changed). E4 is worded as in the paper (review, editorial, thesis or patent); the only full-text E4 exclusion is the authors' earlier position paper. The E-S baseline is stated as "a sequential or CPU-only version" of the same method, and the parallelism levels include label and population (section 7). Each full-text exclusion is recorded with one criterion code (section 6).
- **Citation snowballing.** One round of backward and forward snowballing was run on 2026-10-06 with OpenAlex and Crossref. The seeds were the 19 reports that had passed full-text assessment at that date; newly included studies were not used as further seeds.
- **Author decision.** On 2026-10-06, after the snowballing, Ye et al. 2025 (10.3390/s25154699), one of the 19 seeds, was excluded under I2 by decision of the authors: its planning cost uses a risk map from historical marine meteorological data and satellite cloud images, but no wind, wave or current field enters the cost or constraints.
- **Author decision (2026-10-18).** Barbier et al. 1994 (10.1002/cpe.4330060805) met I1–I4 and none of E1–E5 but was not retained in the final evidence set after discussion among the authors: its 1994 transputer-based architecture is too distant from the contemporary multicore, GPU, cluster and cloud systems considered in the comparative analysis. It is recorded as `author decision`, without a criterion code; the search and the eligibility criteria are unchanged.

- **Recording rule and title/abstract reasons (2026-10-07; reporting only, no decision changed).** The rule for choosing between an E-code and an I-code (§6) was made explicit, and title/abstract exclusions are released as decisions only; indicative codes noted at that stage are not reported as exclusion reasons.
