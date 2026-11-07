# Evidence coverage matrix (Table 10 of the manuscript)

- `evidence_matrix_17.csv`: one row per included study (17), with a code for each of seven evidence columns and its justification (page, table or figure of the study): C1 complete-solver comparison, C2 same-method reference, C3 complete solver time, C4 processing elements varied, C5 parallel efficiency, C6 bottleneck or optimization timed separately, C7 code or data available. Codes: M measured and documented, D partial, NR not reported or not established, NA no same-method comparison measured; `graphical_estimate` marks values read from a published figure.
- `DATA_DICTIONARY.md`: definitions and coding rules of every column.
- `EVIDENCE_TRACE.md`: source location of every coded cell.
- `tab_evidence_matrix.tex`: the table as included in the manuscript; `evidence_table_macros.tex`: its cell styles (pdfLaTeX).
