# Screening decisions (search v0.4)

- `decisions_databases_v04.csv`: every deduplicated database record (`rec_id` as in `dedup/records_X.csv`) with the stage at which it was decided (title/abstract or full text), the decision (include, exclude, not_retrieved), the tier of included studies (A1, A2) and, for full-text exclusions, one criterion code (I1–I4, E1–E5; protocol §5–6) or, for one record, `author decision` (see `author_decisions.md`). Title/abstract exclusions carry no code: at that stage records were classified only as include or exclude.
- `decisions_other_methods_v04.csv`: records found by citation snowballing (`C` ids, with the route by which they were found) and the studies known to the authors from the submitted version, with the same fields; one known study was removed as a duplicate of a database record.
- `author_decisions.md`: decisions taken by the authors during the review.

The counts in `counts/prisma_counts.json` are computed from these files and the query logs by `scripts/07b_counts_v04.py`.
