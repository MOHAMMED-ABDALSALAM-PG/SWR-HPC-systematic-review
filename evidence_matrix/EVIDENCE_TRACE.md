# Evidence trace for the study-level evidence matrix (17 included studies)

Each cell gives the code, the location in the original paper (PDF page index of the published report counted from 1, followed by the section, table or figure cited by the study) and the supporting quote or number. Page indices were located automatically by searching the PDF text for the quoted fragment; 'p. ?' means the fragment could not be matched in the PDF text layer (for example, text inside an image) and the section/table reference must be used.

Codes marked ^g rest on values read from a published figure.

## 1. Dębski 2016a (`debski2016multispline`, X0377, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [115] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 10 (search: “opencl platforms comparison (example 1): speed”) | Sequential (-Os) and OpenCL execution times of the complete DP search compared; speedups up to 31.0 (Ex. 1, Fig. 11) and 15.2 (Ex. 2, sailboat routing, Fig. 15). |
| C2 Same-method reference measured | M | p. 9 (search: “runs of the sequen”) | Sequential version of the same algorithm timed (Tables 1 and 5). |
| C3 Complete solver time | M | pp. 10, 12 (Tables 3 and 7; p. 10 'host-GPU data transfer') | Average execution times of complete runs of the parallel algorithm reported (Tables 3 and 7; e.g. Ex. 2, n_c=128: 36,943 ms i7-OpenCL, 7,869 ms HD 4000); host-GPU transfer overhead lies inside the timed runs (p. 10); inclusion of OpenCL set-up and data input not stated. |
| C4 Processing elements varied | D | p. 8 (search: “192 processing elements”) | GT 650M stated as two compute units with 192 processing elements each (fn. 9); devices compared one at a time; count not varied. |
| C5 Parallel efficiency | NR | whole text searched | Speedups compare one device with the sequential CPU run; no processing-element count for the CPU-OpenCL or HD 4000 runs. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | M | p. 10 (search: “non-opencl code optimizations can improve”) | Compiler and OpenCL optimization levels timed separately (Tables 1-2 and 5-6; -Ofast alone 13.05x for the sequential code, Ex. 1). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 2. Dębski 2016b (`debski2016sailboat`, X0562, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [116] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 11 (search: “the execution time of the serial version”) | Serial algorithm (ts) and parallel OpenCL runs of the complete optimization compared (Table 2); S = 41.0 at C = 128. |
| C2 Same-method reference measured | M | p. 10 (search: “sequential algorithm run on the cpu”) | Serial version (-Os) timed (Tables 1-3). |
| C3 Complete solver time | M | pp. 11-12 (Table 2 legend; 'overhead related to data transfers') | Execution times of the complete serial (Algorithm 3) and parallel (Algorithm 4) optimization reported (Table 2, C = 128: 874.43 s serial, 128.63 s CPU, 21.33 s GPU); host-GPU transfer overhead lies inside the GPU times (p. 12); inclusion of OpenCL set-up not stated. |
| C4 Processing elements varied | D | p. 10 (search: “192 processing elements”) | GT 650M stated as two compute units with 192 processing elements each (fn. 10); work-items (C^2) vary with problem size but are not processing elements; processing elements not varied. |
| C5 Parallel efficiency | NR | p. 11 (search: “calculated in a classic way”) | Speedup compares the GPU with the serial CPU run; no efficiency reported. |
| C6 Bottleneck or optimization measured | M | p. 10 (search: “ofast option allows for the”) | Effect of compiler optimization levels on the serial time measured (Table 1: -Ofast 36%, -Os 32% lower than -O0). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 3. Dębski and Śnieżyński 2021 (`Dbski2021`, X0290, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [51] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 12 (search: “performance comparison of the two available processors”) | Sequential and OpenCL (CPU, iGPU) average execution times of the complete search compared (Table 2); maximum speedup 39.56 (Fig. 7). |
| C2 Same-method reference measured | M | p. 12 (search: “reference (sequential) variant”) | 'seq' columns of Table 2 (reference sequential variant). |
| C3 Complete solver time | M | p. 12 (Table 2) | Average execution times of the complete search reported (Table 2, n_c = 128: 654.8 s seq, 72.87 s CPU, 16.55 s iGPU); inclusion of set-up and data input not stated. |
| C4 Processing elements varied | NR | p. 10 (search: “two (operational) opencl-capable devices”) | Intel Core i7-3740QM and HD Graphics 4000 named; no core or execution-unit counts; devices compared, count not varied. |
| C5 Parallel efficiency | NR | whole text searched | No processing-element count; efficiency not reported. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | M | p. 10 (search: “reduced the sequential computation time from seventeen”) | Pruning gain measured separately by pruning type (Table 1, Fig. 6; 17-20x reduction of sequential time). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 4. Dębski and Dreżewski 2022 (`debski2022adaptive`, X0254, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [105] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 12 (search: “parallel-speedups are presented in table 2”) | Sequential (Table 1) and parallel (Table 2) execution times of the complete search compared; S = 5.6-54.2. |
| C2 Same-method reference measured | M | p. 11 (search: “duration of sequential computations”) | Sequential search timed (Table 1, 'duration of sequential computations'). |
| C3 Complete solver time | M | p. 12 (Table 2); Sec. 4.2 Remark 1 | Execution times of the complete surrogate-assisted search reported (Table 2: 0.980-5.439 s); the physics-based surrogate is evaluated inside the search (no separate training stage); inclusion of set-up not stated. |
| C4 Processing elements varied | NR | p. 10 (search: “intel core i5”) | Intel Core i5 (2.7 GHz) and Iris Graphics 6100 named; device used for Table 2 and core counts not stated. |
| C5 Parallel efficiency | NR | p. 12 (search: “spmd-parallelisation efficiency: execution times”) | No processing-element count; the paper's 'spmd-parallelisation efficiency' (Table 2 caption) denotes execution times and speedups, not E = S/p. |
| C6 Bottleneck or optimization measured | M | p. 12 (search: “efficacy of surrogate-assisted search”) | Surrogate-assisted gain measured separately from the parallel speedup (Table 1: 39.2-45.4x; force-evaluation counts). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 5. Zyczkowski et al. 2023 (`Zyczkowski2023`, X0230, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [68] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 7 (search: “comparison of execution times for sequential”) | Sequential and parallel times of all three application components and the total compared (Table 1); mean reduction 40.4%. |
| C2 Same-method reference measured | M | p. 7 (search: “traditional (sequential)”) | Sequential version timed (Table 1); execution on the same virtual machine is not stated (Sec. IV). |
| C3 Complete solver time | M | p. 7 (Table 1; 'measured the processing times') | Total time = sum of all three components (navigation area from the bitmap, edge weights from weather data, Dijkstra route search) reported (Table 1: 1.61-75.85 s sequential, 0.92-42.94 s parallel); weather-data collection and cloud deployment not timed; thread count of the parallel column not stated. |
| C4 Processing elements varied | M | p. 8 (search: “up to four engaged threads”) | Total time for 1-8 threads (Fig. 9); gains up to four threads (Sec. VI). |
| C5 Parallel efficiency | M^g | p. 8 (Fig. 9, raster 737x481 px, digitized); p. 7 (Table 1) | Graph-read, total time (whole application): Fig. 9 (raster, 737x481 px; legend 'thread1'-'thread8' legible at native resolution, curves identified by colour), largest graph (253,382,867 edges): about 68 s at one thread ('thread1', about 67.9 s) and about 42.5 s at four threads, S about 1.6, E about 0.40. The 'thread1' curve lies below 'thread2' (about 74.9 s), and the Table 1 sequential total (75.85 s) matches 'thread2'; with Table 1 (75.85 s / 42.94 s / 4) E is about 0.44, so the baseline is ambiguous (E 0.40-0.44; coded as about 0.4). No gain beyond four threads; not reported by the authors. |
| C6 Bottleneck or optimization measured | M | p. 8 (search: “much larger execution times for the parallel version”) | Per-component times (Table 1) quantify the sequential Dijkstra step (12.9-39.8% of the sequential total); parallel Dijkstra measured slower (Sec. VI). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 6. Qian et al. 2023 (`Qian2023`, X0206, Tier A1, E-C)

Source: full text of the published report (not redistributed); reference [69] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | NA | p. 15 (search: “comparison of our algorithm with three other algorithms”) | No measured same-method reference; Table 5 compares with Dijkstra, bidirectional A* and SSA. |
| C2 Same-method reference measured | NR | p. 15 (search: “comparison of our algorithm with three other algorithms”) | No sequential SPA* run; only other algorithms timed (Table 5). |
| C3 Complete solver time | M | p. 1 ('to plan a route'); Table 5 | Runtime of the complete VSM-SPA* model 'to plan a route' reported (Table 5: 0.84 s, Dataset 1; 13.11 s, Dataset 2; abstract); inclusion of data loading and risk-field preparation not stated. |
| C4 Processing elements varied | NR | p. 7 (search: “intel 12th generation i5”) | 'Intel 12th generation i5'; MATLAB parfor pool size not reported. |
| C5 Parallel efficiency | NR | whole text searched | No same-method reference; efficiency not calculable. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | D | p. 1 (search: “adaptive heuristic”) | Adaptive heuristic and segment-parallel structure described as runtime reductions; contributions not measured separately. |
| C7 Code or data available | NR | p. 16 (search: “no data was used for the research”) | Statement: 'No data was used for the research described in the article.' |

## 7. Li et al. 2023 (`li2023efficient`, X0589, Tier A1, E-C)

Source: full text of the published report (not redistributed); reference [70] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | NA | p. 13 (search: “static planning results of spa”) | No measured same-method reference; Tables 2-3 compare with six (static) and four (dynamic) other algorithms. |
| C2 Same-method reference measured | NR | p. 13 (search: “static planning results of spa”) | No sequential SPA* run. |
| C3 Complete solver time | M | p. 13 ('completing a planning within 1.5 s'); Tables 2-3 | Running time per complete SPA* planning reported (Table 2, 400x400: 1.2354 s; Table 3: 9.36 s daily, 2.4335 s six-hourly); inclusion of data loading not stated. |
| C4 Processing elements varied | NR | p. 10 (search: “run a* on the cpu cores separately”) | No hardware, core or worker count; m (6-200) is the number of route segments (tasks), not of processors. |
| C5 Parallel efficiency | NR | whole text searched | No same-method reference; efficiency not calculable. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | D | p. 14 (search: “parametric experiments for the number of segments”) | Runtime reported as a function of the number of segments m (Sec. 3.2, Fig. 6), a parameter that changes the decomposition granularity and the route; no bottleneck, overhead or optimization timed separately; adaptive heuristic described, not timed on its own. |
| C7 Code or data available | NR | p. 19 (search: “data availability statement: not applicable”) | Statement: 'Data Availability Statement: Not applicable.' |

## 8. Dębski and Dreżewski 2023 (`debski2023surrogate`, X0224, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [117] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 11 (search: “parallel-speedups are presented in table 2”) | Sequential surrogate-assisted (Table 1) and SPMD-parallel (Table 2) execution times of the complete search compared; S = 1.6-9.4. |
| C2 Same-method reference measured | M | p. 11 (search: “pruning-related speedup for”) | Sequential surrogate-assisted search timed on the same laptop (Table 1). |
| C3 Complete solver time | M | p. 11 (Table 2) | Execution times of the complete surrogate-assisted search reported (Table 2: 4.0-31.1 s); inclusion of set-up not stated. |
| C4 Processing elements varied | NR | p. 10 (search: “one operational opencl-capable device”) | Single Intel Iris Graphics 6100 device; no execution-unit or work-item count. |
| C5 Parallel efficiency | NR | whole text searched | No processing-element count; efficiency not reported. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | M | p. 2 (search: “pruning-related speedup”) | Pruning gain measured separately (Table 1: 43.5-60.0x) and shown as a factor of the total speedup (Fig. 4). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 9. Gold et al. 2025 (`gold2025opmos`, X0091, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [113] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 10 (search: “end-to-end execution time of opmos”) | Sequential NAMOA* and OPMOS end-to-end search times compared on the same CPU (Table 3); initialization excluded (Sec. 6). |
| C2 Same-method reference measured | M | p. 6 (search: “sequential mos”) | Sequential MOS with the same data structures on the same Grace CPU (Sec. 6, Table 3). |
| C3 Complete solver time | M | p. 10 ('does not include the initialization of the data structures and threads'); Table 3, p. 14 | 'End-to-end' time = main-thread while-loop of Alg. 2 from the start label to the exact Pareto set (Sec. 6, p. 10; Table 3, route 1: 2725 s sequential vs 48.22 s); initialization of data structures and threads excluded; graph generation (TMPLAR, Python) not timed. |
| C4 Processing elements varied | M | p. 11 (search: “increased from 1 to 128”) | 1-128 worker threads (Fig. 5). |
| C5 Parallel efficiency | M | p. 14 (Table 3); pp. 11-12 (Sec. 7, 'geometric mean 28x', 'all subsequent evaluations use 64'); p. 11 (Fig. 5) | Calculable from tabulated times, not reported by the authors: Table 3 (64 worker threads, 256 label extractions per iteration; complete search, initialization excluded) gives S = 17-57, geometric mean 34, E about 0.53 for p = 64 worker threads (0.52 if the main thread is counted, NUM_THDS = 65). Plain thread sweep (label extractions = worker threads): 28x geometric mean at 64 worker threads stated in the text (p. 12; Fig. 5), E about 0.44. |
| C6 Bottleneck or optimization measured | M | p. 6 (search: “runtime breakdown”) | Runtime breakdown into OPEN extractions, updates, label processing and communication overheads (Sec. 6, Fig. 2); labels extracted and extraction-count sweeps (Figs. 4-6). |
| C7 Code or data available | NR | p. 14 (search: “open-source mos bench”) | No code or data release statement. |

## 10. Gold et al. 2026 (`gold2026mpmos`, X0019, Tier A1, E-S)

Source: full text of the published report (not redistributed); reference [110] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 9 (search: “runtime does not include initialization”) | Sequential NAMOA* and MPMOS search times compared (Table 2; 13.4-3501x on ship graphs); initialization excluded (Sec. 5). |
| C2 Same-method reference measured | M | p. 9 (search: “the namoa* [18] algorithm serves as the baseline”) | Sequential NAMOA* on the Grace CPU of the same GH200 (Sec. 5, Table 2). |
| C3 Complete solver time | M | p. 9 ('does not include initialization'); p. 10 ('kernel completion time'); Table 2 | Search runtimes reported (Table 2: 0.006-2.92 s on ship graphs); MPMOS time = kernel completion time of the search loop (Sec. 5, p. 10); initialization of data structures (and threads) excluded (p. 9); host-device transfers not mentioned. |
| C4 Processing elements varied | D | p. 9 (search: “132 streaming multiprocessors”) | Fixed hardware count stated: one H100 with 132 SMs (Sec. 5); the 8448 warps (32 per block, 2 blocks per SM) are a launch configuration and are not counted as processing elements; the label-extraction parameter is varied (Fig. 10), the number of SMs is not. |
| C5 Parallel efficiency | NR | whole text searched | One GPU compared with a single-threaded CPU run; efficiency not reported. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | M | p. 10 (search: “optimization removed”) | Variants with each optimization removed (11.3x all-on vs all-off), sorting overhead of merge vs global sorting (Fig. 9) and runtime distributions measured. |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 11. Eichhorn et al. 2012 (`eichhorn2012parallelization`, X0424, Tier A2, E-S)

Source: full text of the published report (not redistributed); reference [114] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | M | p. 7 (search: “runtime of the path planning and mpi-noop”) | Serial and parallel runtimes of the whole path-planning program (Fig. 8) and of the search (Fig. 9) compared for 2-48 cores; values graphical only. |
| C2 Same-method reference measured | M | p. 7 (search: “it is only executed on a single core”) | Serial S-TVE executed on one SCC core (Sec. III-D). |
| C3 Complete solver time | M^g | p. 7 (Fig. 8, vector plot coordinates) | Runtime of the whole path-planning program (serial portions, graph construction and MPI start-up included) shown for the serial program and 2-48 cores (Fig. 8; graphical only, vector plot: about 73 s serial, about 22.4 s at 21 cores). |
| C4 Processing elements varied | M | p. 7 (search: “the number of slaves is always one less”) | 2-48 cores, one master and up to 47 slaves (Sec. III-D, Figs. 8-10). |
| C5 Parallel efficiency | M^g | p. 7 (Figs. 8-10, vector plot coordinates; Sec. III-D) | Graph-read, whole program: Fig. 8 (vector plot; one curve plus the serial point) gives about 73 s serial vs about 22.4 s at 21 cores (1 master, 20 slaves), S about 3.3, E about 0.15-0.16 (about 0.05 at 48 cores). Search stage only (Fig. 9 excludes 'the serial portions of the algorithm including the construction of graphs', p. 7): S about 11 at 21 cores (Fig. 10), E about 0.53; not reported by the authors. |
| C6 Bottleneck or optimization measured | M | p. 7 (search: “mpi-noop results measure the overhead”) | MPI start-up overhead measured with the MPI-NOOP program (Fig. 8); search-only vs whole-program runtime (Figs. 8-9); energy (Fig. 11). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 12. Ferris et al. 2018 (`ferris2019timeoptimal`, X0328, Tier A2, E-T)

Source: full text of the published report (not redistributed); reference [71] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | NA | p. 4 (search: “the average time taken to complete one reachability”) | No measured same-method reference; serial time modelled only (Table I). |
| C2 Same-method reference measured | D | p. 4 (search: “the average time taken to complete one reachability”) | Serial time modelled as Tave x Jn with Tave = 0.5 h (Table I); not measured. |
| C3 Complete solver time | D | p. 6 ('11 minutes to compute'); p. 7 ('1 hour and 7 minutes'); p. 2 ('the tour for which travel time is minimum is identified ... then obtained by solving the backtracking equation') | Only the reachability-front calculations are timed: 326 fronts in 11 min (five waypoints, p. 6); 1,957 fronts in 1 h 7 min (six waypoints, p. 7). Identification of the minimum-time tour and the backtracking equation for the optimal path are later steps (p. 2) and are not timed. |
| C4 Processing elements varied | D | p. 4 (search: “100-core”) | Infinite-core and 100-core times modelled (Table I); cluster size not stated; not varied in measured runs. |
| C5 Parallel efficiency | NR | whole text searched | No measured reference; efficiency not calculable. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | D | p. 3 (search: “practical limits of i/o”) | Dependency-ordered job flow, tour pruning and I/O and memory limits described (Sec. II); not measured. |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 13. Aguiar et al. 2019 (`aguiar2019optimizing`, X0325, Tier A2, E-T)

Source: full text of the published report (not redistributed); reference [118] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | NA | p. 1 (search: “approx. 5 hours”) | No measured same-method reference. |
| C2 Same-method reference measured | D | p. 3 (search: “near optimal speedup”) | Earlier MATLAB time (about 5 h) cited from the authors' previous paper; 'near optimal speedup' attributed to Detrixhe et al.; no in-study serial run. |
| C3 Complete solver time | M | p. 4 ('two to four minutes of wall clock time'); p. 3 ('interpolated in space') | Value-function (HJB) solve, which gives the optimal feedback control for any start position, 'takes approximately two to four minutes of wall clock time' (Sec. V, p. 4); interpolation of the current data and obstacle map (pre-processing, p. 3) and trajectory integration (post-processing) not timed. |
| C4 Processing elements varied | D | p. 4 (search: “eight hardware threads”) | Eight hardware threads stated (Sec. V); not varied. |
| C5 Parallel efficiency | NR | whole text searched | No measured reference; efficiency not calculable. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | D | p. 3 (search: “precalculated during program startup”) | Precomputed hyperplane sets and compile-time dimensions (loop unrolling, stack allocation) described (Sec. IV-C); not measured. |
| C7 Code or data available | M | p. 3 (search: “github.com/mcpca/marlin”) | 'The solver source code is available at https://github.com/mcpca/marlin' (Sec. IV-C). |

## 14. Wang et al. 2019 (`wang2019trajectory`, X0332, Tier A2, E-T)

Source: full text of the published report (not redistributed); reference [119] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | NA | p. 15 (search: “optimization runs in parallel”) | No measured same-method reference. |
| C2 Same-method reference measured | NR | p. 15 (search: “optimization runs in parallel”) | No sequential run of the parallel workflow. |
| C3 Complete solver time | D | p. 15 (Tables 11-12, 'optimization runs in parallel') | Wall-clock time per MINLP run and stage reported (Tables 11-12); no total time of the parallel solution approach. |
| C4 Processing elements varied | D | p. 9 (search: “processor with 12 cores”) | 'Intel Xeon (R) CPU E5-2680 processor with 12 cores' (Sec. 4); number of concurrent runs not stated. |
| C5 Parallel efficiency | NR | whole text searched | No measured reference; efficiency not calculable. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | M | p. 16 (search: “approximately 4.7 times larger”) | Each stage of the solution sequence timed separately (Tables 11-12, wall-clock time per stage and run); the paper notes that 'the computational time required by MINLP D is approximately 4.7 times larger than that of MINLP D' (Sec. 4.4, Table 12; the comparison is evidently with MINLP C). |
| C7 Code or data available | NR | whole text searched | No code or data availability statement. (Terms searched: available, github, code, data availability, repository, supplementary.) |

## 15. Chowdhury et al. 2022 (`Chowdhury2022`, X0252, Tier A2, E-T)

Source: full text of the published report (not redistributed); reference [106] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | NA | p. 2 (search: “600–1000”) | No measured same-method reference in the study. |
| C2 Same-method reference measured | D | p. 2 (search: “600–1000”) | 600-1000x model-building reduction cited from Chowdhury and Subramani (2022); no in-study reference run. |
| C3 Complete solver time | D | p. 13 ('average total computation time'); p. 14 ('within a few hours'); p. 10 ('intervals of 0.05'); p. 6 ('executed just once') | 'The average total computation time for each value of alpha is around 1 min'; '4 min per MDP' for 200x200x200 (Sec. 4.4, p. 13): per scalarized MDP only; the time for the full set of policies (alpha = 0-1 in steps of 0.05, p. 10) is not measured ('within a few hours', p. 14, is a projection), and whether the one-time model building (p. 6) is included is not stated. |
| C4 Processing elements varied | NR | p. 13 (search: “nvidia rtx 8000”) | Single RTX 8000; no core, thread or block counts. |
| C5 Parallel efficiency | NR | whole text searched | No measured reference; efficiency not calculable. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | D | p. 6 (search: “limited gpu memory poses a challenge”) | GPU memory limits addressed with the DO representation and sparse transition matrices (Sec. 3.2); effect not measured. |
| C7 Code or data available | D | p. 15 (search: “will be made”) | 'The raw data ... will be made available by the authors ... to any qualified researcher' (on request). |

## 16. Chowdhury and Subramani 2022 (`chowdhury2022optimal`, X0244, Tier A2, E-S)

Source: full text of the published report (IEEE J. Ocean. Eng. 47(4), pp. 864–879; page numbers below follow this version; not redistributed); reference [111] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | D | p. 877 (search: “model-building algorithm’s execution”) | GPU and sequential CPU versions compared for MDP model building only (Fig. 8); value iteration not timed against a reference. |
| C2 Same-method reference measured | M | p. 877 (search: “intel core i7-8700”) | Sequential version on an Intel Core i7-8700 for the model-building phase (Sec. IV-D). |
| C3 Complete solver time | D | p. 876 ('of the order of a few minutes'); p. 877 (Fig. 8a) | Model-building times measured (Fig. 8a); for model building plus value iteration only 'of the order of a few minutes' (p. 876), without a value. |
| C4 Processing elements varied | NR | p. 877 (search: “optimal threads per block”) | Three GPUs used one at a time; only the launch configuration (64, 64 and 32 threads per block) is stated, no SM or core counts. |
| C5 Parallel efficiency | NR | p. 877 (search: “speedup depends on the gpu”) | Speedup compares a GPU with the sequential CPU run; efficiency not reported. |
| C6 Bottleneck or optimization measured | D | p. 870 (search: “96 mb of memory”) | Memory reduction by the DO representation computed analytically (96 MB vs 8 GB); kernels 'individually optimized' for threads per block without reported timings. |
| C7 Code or data available | M | p. 865 (search: “software package for community use”) | Software package at https://github.com/rohit1607/e2e_GPU_DP ('for community use', ref. [51] of the study). |

## 17. Li et al. 2026 (`li2026glider`, X0008, Tier A2, E-S)

Source: full text of the published report (not redistributed); reference [112] in the manuscript.

| Col. | Code | Location | Evidence (quote or number) |
|---|---|---|---|
| C1 Complete-solver comparison | D | p. 21 (search: “isolated gpu-versus-cpu benchmark”) | GPU and CPU-only backends compared for batch fitness evaluation only (Sec. 5.7, Fig. 15a); differential-evolution operators and whole optimizer not compared. |
| C2 Same-method reference measured | M | p. 22 (search: “cpu-only backend”) | CPU-only backend of the same evaluation pipeline on the same workstation (Sec. 5.7); CPU threading not stated. |
| C3 Complete solver time | M | p. 20 ('total wall-clock time of each optimizer'); p. 22 ('one-time setup cost') | Total wall-clock runtime of each optimizer run reported (Table 5; Sec. 5.4 for Table 7), 31 runs per case; inclusion of the one-time backend set-up (Fig. 15b, p. 22) not stated. |
| C4 Processing elements varied | NR | p. 8 (search: “each gpu thread is assigned”) | Intel Core i9-12900K and RTX 4080; one GPU thread per candidate (population 100) is a launch configuration; no SM, core or CPU-thread counts; not varied. |
| C5 Parallel efficiency | NR | whole text searched | Speedup compares a GPU with a CPU backend; efficiency not reported. (Terms searched: efficiency, speedup, cores, threads, processing elements.) |
| C6 Bottleneck or optimization measured | M | p. 22 (search: “one-time setup overhead is reported”) | One-time setup overhead timed separately (Fig. 15b: 1.09-66.46 s CPU vs 3.91-69.08 s GPU); collision-checking strategies timed (Sec. 5.8, Fig. 16). |
| C7 Code or data available | D | p. 1 (search: “project website”) | Project website https://rapid-route.github.io/ given (p. 1); no code or data availability statement. |
