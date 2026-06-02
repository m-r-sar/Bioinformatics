
# Simplified BLAST (Basic Local Alignment Search Tool)

A lightweight, object-oriented Python implementation of the BLAST algorithm for local sequence alignment. This tool supports both nucleotide and protein sequences, utilizing a hash-table index for exact k-mer seeding and an ungapped extension strategy with a drop-off threshold.

## Features

* **Database Indexing & Caching**: Parses FASTA files and generates an internal k-mer hash-table index. The index is automatically serialized to a `.idx` file using `pickle` to skip re-indexing on subsequent runs.
* **Exact Match Seeding**: Extracts overlapping k-mers from the query sequence and matches them against the database index in $O(1)$ time per lookup.
* **Configuration Management**: Runtime parameters are isolated in a JSON configuration file for easy tuning.

## Project Structure

* `blast.py`: The main entry point. Contains the execution flow, CLI argument parsing, and the core alignment extension logic.
* `Indexing.py`: Defines the `DataBase` class which manages sequence storage, total database length, and index orchestration.
* `Logic.py`: Internal utility module handling FASTA parsing via Biopython (`SeqIO`), file I/O, serialization, and console/file output formatting.
* `options.json`: External configuration file for algorithm hyperparameters.

## Configuration (options.json)

```json
{
  "x": 5,
  "K": 0.1,
  "L": 0.3,
  "top": 3,
  "modifier": 3,
  "nucleic_k-mer_size": 11,
  "protein_k-mer_size": 3,
  "match_score": 1,
  "missmatch_score": -3
} 
```

* `x`: Extension drop-off threshold ($X$). Stops bidirectional extension when the current score drops more than $X$ below the maximum achieved score.
* `K` / `L`: Karlin-Altschul statistical parameters used for raw score to E-value estimation.
* `top`: Maximum number of High-scoring Segment Pairs (HSPs) to display or report.
* `modifier`: Applied to the k-mer length (`k + modifier`) to define the minimum raw score cutoff for filtering out short, non-significant matches.
* `nucleic_k-mer_size` / `protein_k-mer_size`: Seeding word size ($k$) for DNA and protein search respectively.
* `match_score` / `missmatch_score`: Raw score values applied during nucleotide alignment.

## Dependencies

* Python 3.x
* Biopython

Install dependencies via pip:

```bash
pip install biopython

```

## Usage

The program accepts arguments via the command-line interface. You must specify the database path, the query (sequence string or FASTA file), and the sequence type flag.

### 1. Nucleotide Search (DNA/RNA)

To search using simple match/mismatch logic with a default k-mer size of 11:

```bash
python blast.py -db path/to/database.fasta -q "ATCGTAGCTAGCTAG" -n

```

### 2. Protein Search (BLOSUM62)

To search protein sequences using the BLOSUM62 substitution matrix and a default k-mer size of 3:

```bash
python blast.py -db path/to/proteins.fasta -q test_query_protein.fasta -p -b

```

### 3. File-Based Batch Query

If the `-q` parameter receives a path to a `.fasta` or `.fa` file, the script processes all sequences within that file sequentially and automatically writes the formatted outputs into the `./results/` directory.

## Output Format

Alignments are sorted by raw score in descending order. The terminal display includes alignment metrics, sequence coordinates, and identity tracking lines:

```text
=============================================================================
 Target: Seq_ID_123     | Score: 24    | E-value: 1.42e-04 | Length: 24    | Query: Query_1 
-----------------------------------------------------------------------------
Query:   12 MREIVHIQAGQCGNQGIGFAFWGL 35
            ||||||||.|||||||||||||||
Target:  84 MREIVHIQGGQCGNQGIGFAFWGL 107
=============================================================================

```