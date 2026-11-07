# Search-record keyword maps (Appendix C, Figs. 10 and 11)

Author-keyword co-occurrence maps of the 906 deduplicated database records (717 with author keywords; 62 keywords occurring in at least five records, 282 links, eight clusters; VOSviewer 1.6.21, association-strength normalization).

- `thesaurus/`: the thesaurus that merges spelling variants and abbreviations (`thesaurus_keywords.json`) and the plural-to-singular merges (`plural_merges_DE.json`); `THESAURUS_NOTE.txt` explains the correction that keeps "AIS" (automatic identification system) separate from "artificial intelligence".
- `data/`: the mapped keywords with cluster, map coordinates, occurrences, included-study counts and shares and publication-year statistics (`keyword_table_t5_corrected.csv`), the 282 links (`link_table_t5_corrected.csv`), yearly counts per keyword (`keyword_years_t5_corrected.csv`), the merged variants (`keyword_variants_t5.csv`), and the threshold sensitivity check at 3, 5 and 10 occurrences (`sensitivity_*.csv`).
- `figures/`: the two maps as printed.

The maps describe the vocabulary retrieved by the search string, not the included studies, and a later mean publication year of a keyword does not indicate the growth of a topic.
