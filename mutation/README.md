# DNA Mutation Analysis Pipeline

A small bioinformatics pipeline written **from scratch in pure Python** to parse DNA sequences and analyze codon-level mutations between organisms. It parses FASTA input, computes basic sequence statistics, translates DNA across all six reading frames, and classifies mutations as **synonymous** (silent) or **non-synonymous** (amino-acid-changing).

I built this while learning bioinformatics, deliberately without relying on libraries like BioPython, so that I understood every step happening under the hood — FASTA parsing, reverse complements, codon splitting, translation, and mutation classification. The goal was understanding, not production speed.

---

## What it does

Given DNA sequences for two or more organisms, the pipeline:

1. **Parses FASTA input** into clean sequences.
2. **Calculates sequence length** for each organism.
3. **Calculates GC content** (percentage of G and C bases).
4. **Breaks each sequence into codons** across all **six reading frames** (three forward, three on the reverse complement strand).
5. **Translates** each reading frame into a protein sequence, stopping at stop codons.
6. **Classifies mutations** between two organisms as synonymous or non-synonymous by comparing codons position-by-position and checking whether the resulting amino acid changed.
7. **Writes a formatted report** (`results.txt`) with all results laid out in readable tables.

---

## Two versions

| File | How you run it | Input |
|------|----------------|-------|
| `mutation.py` | `python3 mutation.py` | Uses a built-in `dna.fasta` created by the script |
| `mutation_with_CLI.py` | `python3 mutation_with_CLI.py your_file.fasta` | Takes a FASTA file as a command-line argument |

- **`mutation.py`** is the simplest version. It writes a small example `dna.fasta` and runs on it. Good for just seeing the pipeline work end to end.
- **`mutation_with_CLI.py`** is the command-line version. You pass in **your own FASTA file** as an argument, so you can run it on any sequences you like.

---

## Requirements

- **Python 3** (developed on Python 3.13)
- The **`tabulate`** library, used to format the output tables.

Install `tabulate` before running:

```bash
pip install tabulate
```

> Developed on Windows using **WSL** with VS Code, but it should run on any system with Python 3 — Linux, macOS, or Windows. Use whatever terminal / environment you're comfortable with.

---

## How to run

**Simple version:**

```bash
python3 mutation.py
```

**Command-line version (with your own FASTA file):**

```bash
python3 mutation_with_CLI.py your_sequences.fasta
```

Both versions produce a `results.txt` file in the same folder, containing all the tables.

---

## Input format

The pipeline expects standard **FASTA** format — a header line starting with `>`, followed by the sequence:

```
>human
ATGCTGACATAG
>mouse
ATGTTGACAGAT
```

You can pass in your own FASTA file with as many sequences as you like (for length, GC content, codons, and translation). The **mutation comparison** compares two organisms at a time.

---

## Important note on the mutation analysis

The mutation-comparison step compares **two named organisms**. In the current code, those names are set to `"human"` and `"mouse"`:

```python
syn, nsyn = mutations(codons, "human", "mouse")
```

**If your FASTA file uses different organism names, you must change these two names to match the headers in your file**, or the comparison step will fail (it looks for those exact names in the data).

For example, if your FASTA headers are `>avian` and `>human`, change the line to:

```python
syn, nsyn = mutations(codons, "avian", "human")
```

---

## Output

Running the pipeline writes a `results.txt` file containing formatted tables for:

- **Sequence lengths** — length of each organism's sequence
- **GC content** — GC percentage for each organism
- **Codons by frame** — codons for each organism across all six reading frames
- **Amino acid translation** — protein sequence for each frame
- **Synonymous mutations** — mutations where the codon changed but the amino acid stayed the same
- **Non-synonymous mutations** — mutations where the amino acid changed

Each mutation entry shows the reading frame, the codon change (e.g. `GCA -> GCG`), and the amino acid change (e.g. `A -> A`).

---

## How it's built

The code is organized as separate functions, each doing one job:

- `clean_data()` — parses FASTA into a dictionary of sequences
- `length_of_seq()` — sequence lengths
- `gc_content()` — GC percentage
- `rev_comp()` — reverse complement of a strand
- `codon_breakage()` — splits sequences into codons across all six frames
- `translation()` — translates codons into protein
- `mutations()` — classifies synonymous vs non-synonymous mutations
- `make_report()` — a separate "display layer" that takes the computed data and writes the formatted report

The compute functions and the reporting function are kept separate on purpose, so that changing how results are displayed never risks breaking the analysis logic.

---

## Note

This is a learning project, built by hand to understand the fundamentals of sequence analysis. It's not optimized for large genomic datasets or edge cases like ambiguous bases (`N`) or partial codons. My next step is learning **BioPython** and applying these same concepts to real sequencing data.
