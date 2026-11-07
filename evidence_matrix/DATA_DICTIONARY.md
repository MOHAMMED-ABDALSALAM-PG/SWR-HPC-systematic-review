# Data dictionary: `evidence_matrix_17.csv`

One row per included study (17 rows: Tier A1 10, Tier A2 7). The study set, record identifiers, tiers, years and evidence classes are those of the 17 studies included in `screening/decisions_databases_v04.csv`. Each cell code is supported by the original paper; the location and quote for every cell are listed in `EVIDENCE_TRACE.md`.

## Identification fields

| Field | Content |
|---|---|
| `order` | Row order in the table: Tier A1 before Tier A2; within a tier by publication year, then by reference number. |
| `tier` | A1 = ship weather routing; A2 = closely related marine-vehicle route planning. |
| `year` | Publication year (Ferris et al.: OCEANS 2018, although the citation key says 2019). |
| `label` | Study label used in the table. One author: "Smith 2016"; two authors: "Smith and Jones 2021"; three or more: "Li et al. 2023". The two single-author 2016 papers of Dębski are distinguished as 2016a (`debski2016multispline`) and 2016b (`debski2016sailboat`) in the order of their reference numbers. |
| `citekey` | BibTeX key of the study in the manuscript's bibliography. |
| `rec_id` | Record identifier in the screening and extraction files. |
| `ref_no` | Reference number in the current compiled manuscript (changes if the citation order changes; the LaTeX mapping table uses `\cite`). |
| `evidence_class` | Evidence class of the study (E-S, E-C, E-T), unchanged from the extraction. |

## Evidence columns

Each column has a code field (`Cn_code`) and a short justification (`Cn_justification`).

| Column | Short name (table) | Question |
|---|---|---|
| C1 | Complete-solver comparison | Does the measured comparison with a same-method reference cover the complete route computation, or only a stage or component? |
| C2 | Same-method reference | Was a sequential or CPU-only run of the same method measured in the study? |
| C3 | Complete solver time | Is a measured time of the complete computation of the study's own method, from prepared inputs to the final route, Pareto set or policy, reported? |
| C4 | Processing elements varied | Were runs with different numbers of processing elements (cores, hardware or worker threads, MPI processes) reported? |
| C5 | Parallel efficiency | Is parallel efficiency E = S/p of the complete solver reported, or calculable from same-method measurements at a stated number p of processing elements? |
| C6 | Bottleneck or optimization | Was a bottleneck, overhead or optimization timed separately from the overall result? |
| C7 | Code or data available | Are source code or experiment data available for reproduction? |

## Codes

| Code | General meaning |
|---|---|
| M | Measured and documented in the study. |
| D | Partial evidence: implemented or described but not separately measured; the column-specific meaning is given below (for C1 and C3, D denotes evidence measured for one stage, component or scalarized subproblem only). |
| NR | Not reported or not established. NR does not mean that the element was absent from the implementation. |
| NA | Not applicable. |

## Column-specific coding rules

**C1 Complete-solver comparison.** M: the same-method comparison (times or speedup) covers the complete route computation, i.e. all computational stages from the prepared inputs to the route, Pareto set or policy. Exclusion of one-time initialization of data structures, stated by the authors, is noted in the justification but does not change the code. D: the comparison covers one stage or component only (for example MDP model building, or batch fitness evaluation), although the rest of the workflow is implemented. NA: no same-method reference was measured (C2 is D or NR), so there is no comparison whose scope could be coded.

**C2 Same-method reference.** M: a sequential or CPU-only run of the same method was timed in the study (also when the comparison covers one stage only; C1 records the scope). D: a reference is described but not measured in the study: modelled serial time, a value cited from earlier work, or an earlier implementation timed in another paper. NR: no same-method reference; comparisons, if any, are with other algorithms.

**C3 Complete solver time.** Three timing scopes are distinguished: (a) the complete computation of the study's own method, from prepared inputs (graph, grid or environmental fields already available to the solver) to the final route, Pareto set or policy; (b) individual computational stages, components or scalarized subproblems only; (c) the full operational routing workflow including forecast ingestion, pre-processing and post-processing. No included study reports (c). M: (a) is reported as a measured value or range (in a table, the text or a figure; approximate values such as "approximately two to four minutes" count). A value function that defines the optimal feedback control for every start position counts as a policy (Aguiar et al. 2019). One-time allocation or initialization of data structures, threads or device buffers excluded by the authors does not change the code but is recorded in the justification (Gold et al. 2025 and 2026); pre-processing not timed by the authors is also recorded. D: only (b) is reported, or the complete computation is described only by an order-of-magnitude statement without a value (Chowdhury and Subramani 2022: model building timed, total "of the order of a few minutes"), or the timed region ends before the final route is produced (Ferris et al. 2018: reachability fronts timed, tour selection and path backtracking not timed), or only the time of one scalarized subproblem is reported although the study's output is a set of solutions (Chowdhury et al. 2022: time per value of alpha, 21 values). NR: no time reported. A time available only in a figure is marked g (Eichhorn et al. 2012, Fig. 8).

**C4 Processing elements varied.** Processing elements are hardware or execution resources that run work concurrently: CPU cores, hardware threads, CPU worker threads or MPI processes mapped to cores, and on GPUs compute units, streaming multiprocessors (SMs) or the processing elements (CUDA cores) stated per compute unit. Launch or decomposition parameters are not processing elements: CUDA threads per candidate, threads per block, blocks, warps, OpenCL work-items and work-group sizes, segment or task counts. M: runs with at least two different numbers of processing elements of the same kind are reported. Comparing different devices (CPU vs GPU, or several GPU models) is not a variation of the number. D: a fixed hardware count is stated, or other counts are only modelled, without measured variation (Gold et al. 2026: 132 SMs, D; the 8448 warps are not counted). NR: no hardware count is reported and no variation is reported; a stated launch configuration alone gives NR (Chowdhury and Subramani 2022: 64/64/32 threads per block; Li et al. 2026: one GPU thread per candidate).

**C5 Parallel efficiency.** M: E = S/p is reported by the authors or calculable from same-method times or speedups given in a table or the text, at a stated number p of homogeneous processing elements (cores, threads, workers, MPI processes), for the complete solver as defined for C3. M with superscript g: as M, but the times or speedups are available only in a published figure; the value is read from the figure (vector coordinates or raster digitization) and is approximate. M with superscript s (field `stage_only`): calculable only for one stage of the solver; no study currently needs this mark. GPU-versus-CPU speedups and cross-algorithm runtime ratios do not qualify; CUDA-core counts are not accepted as p. NR: not reported and not calculable under this rule. Coded values: Gold et al. 2025, M, tabulated (Table 3: 64 worker threads, 256 label extractions per iteration, geometric mean 34x, E about 0.53; plain thread sweep 28x, E about 0.44); Zyczkowski et al. 2023, M^g, total time (Fig. 9, about 68 s at one thread vs about 42.5 s at four threads, E about 0.4; 0.40-0.44 depending on whether the 'thread1' curve or the Table 1 sequential total is the baseline); Eichhorn et al. 2012, M^g, whole program (Fig. 8, about 73 s serial vs about 22.4 s at 21 cores, E about 0.15-0.16), with the search-stage value (Fig. 10, E about 0.53 at 21 cores) given in the justification only. A term such as "spmd-parallelisation efficiency" used by a study for execution times and speedups is not E = S/p.

**C6 Bottleneck or optimization.** M: the study reports a time, or a gain relative to a run without it, that is attributable to one identified bottleneck, overhead, workflow stage or optimization, separately from the overall result. Qualifying evidence: per-component or per-stage times of the same run; a runtime breakdown; an overhead benchmark (for example an MPI start-up program or a one-time setup time); an ablation that removes one optimization; timed compiler optimization levels; or an algorithmic acceleration combined with the parallel version (pruning, surrogate model) timed with and without it on the sequential code. A parameter sweep that changes the decomposition or the algorithm itself (number of route segments, label extractions per iteration) does not qualify on its own, because the time difference cannot be attributed to one component; nor does a cross-algorithm comparison. D: a bottleneck or optimization is described, or a parameter is swept, but no component is timed separately. Applying this rule: Wang et al. 2019 remain M (each stage of the solution sequence is timed separately, Tables 11-12); the three Dębski studies with pruning or surrogate models remain M (base and accelerated sequential runs timed, Table 1 of each); Li et al. 2023 is D (runtime vs number of segments only).

**C7 Code or data available.** M: publicly accessible source code or experiment data (link or repository named in the paper). D: availability on request, or a project web page without a code or data release statement. NR: no availability statement; also used where the statement says that no data were used or that it is not applicable.

## Other fields

| Field | Content |
|---|---|
| `graphical_estimate` | Columns (semicolon-separated) whose M code rests on a value read from a published figure (currently C5 for Zyczkowski et al. 2023; C3 and C5 for Eichhorn et al. 2012). Shown as superscript g. |
| `stage_only` | Columns (semicolon-separated) whose M code rests on a value for one solver stage only (superscript s; currently empty). |
| `remarks` | Free-text remark for that marking. |

## Table file

`tab_evidence_matrix.tex` (Table 10 of the manuscript) is built from this CSV: rows in `order`, grouped by tier, with the citation key of each study; the summary row gives the number of M codes per column and, in parentheses, how many of them are graph-read. The table note describes D generically as partial evidence; the column-specific meanings are given above. Cell styles (`evidence_table_macros.tex`): M dark blue (#1F5A96, white bold text), D light blue (#8DBBE3), NR light grey with hatching, NA white; every cell also carries its code as text, so the coding does not depend on colour.
