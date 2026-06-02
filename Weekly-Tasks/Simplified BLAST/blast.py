from Indexing import DataBase
import Logic as logic
import math
import os
import argparse

BLOSUM62 = {
    "AA": 4, "AC": 0, "AD": -2, "AE": -1, "AF": -2, "AG": 0, "AH": -2, "AI": -1, "AK": -1, "AL": -1, "AM": -1, "AN": -2, "AP": -1, "AQ": -1, "AR": -1, "AS": 1, "AT": 0, "AV": 0, "AW": -3, "AY": -2,
    "CA": 0, "CC": 9, "CD": -3, "CE": -4, "CF": -2, "CG": -3, "CH": -3, "CI": -1, "CK": -3, "CL": -1, "CM": -1, "CN": -3, "CP": -3, "CQ": -3, "CR": -3, "CS": -1, "CT": -1, "CV": -1, "CW": -2, "CY": -2,
    "DA": -2, "DC": -3, "DD": 6, "DE": 2, "DF": -3, "DG": -1, "DH": -1, "DI": -3, "DK": -1, "DL": -4, "DM": -3, "DN": 1, "DP": -1, "DQ": 0, "DR": -2, "DS": 0, "DT": -1, "DV": -3, "DW": -4, "DY": -3,
    "EA": -1, "EC": -4, "ED": 2, "EE": 5, "EF": -3, "EG": -2, "EH": 0, "EI": -3, "EK": 1, "EL": -3, "EM": -2, "EN": 0, "EP": -1, "EQ": 2, "ER": 0, "ES": 0, "ET": -1, "EV": -2, "EW": -3, "EY": -2,
    "FA": -2, "FC": -2, "FD": -3, "FE": -3, "FF": 6, "FG": -3, "FH": -1, "FI": 0, "FK": -3, "FL": 0, "FM": 0, "FN": -3, "FP": -4, "FQ": -3, "FR": -3, "FS": -2, "FT": -2, "FV": -1, "FW": 1, "FY": 3,
    "GA": 0, "GC": -3, "GD": -1, "GE": -2, "GF": -3, "GG": 6, "GH": -2, "GI": -4, "GK": -2, "GL": -4, "GM": -3, "GN": 0, "GP": -2, "GQ": -2, "GR": -2, "GS": 0, "GT": -2, "GV": -3, "GW": -2, "GY": -3,
    "HA": -2, "HC": -3, "HD": -1, "HE": 0, "HF": -1, "HG": -2, "HH": 8, "HI": -3, "HK": -1, "HL": -3, "HM": -2, "HN": 1, "HP": -2, "HQ": 0, "HR": 0, "HS": -1, "HT": -2, "HV": -3, "HW": -2, "HY": 2,
    "IA": -1, "IC": -1, "ID": -3, "IE": -3, "IF": 0, "IG": -4, "IH": -3, "II": 4, "IK": -3, "IL": 2, "IM": 1, "IN": -3, "IP": -3, "IQ": -3, "IR": -3, "IS": -2, "IT": -1, "IV": 3, "IW": -3, "IY": -1,
    "KA": -1, "KC": -3, "KD": -1, "KE": 1, "KF": -3, "KG": -2, "KH": -1, "KI": -3, "KK": 5, "KL": -2, "KM": -1, "KN": 0, "KP": -1, "KQ": 1, "KR": 2, "KS": 0, "KT": -1, "KV": -2, "KW": -3, "KY": -2,
    "LA": -1, "LC": -1, "LD": -4, "LE": -3, "LF": 0, "LG": -4, "LH": -3, "LI": 2, "LK": -2, "LL": 4, "LM": 2, "LN": -3, "LP": -3, "LQ": -2, "LR": -2, "LS": -2, "LT": -1, "LV": 1, "LW": -2, "LY": -1,
    "MA": -1, "MC": -1, "MD": -3, "ME": -2, "MF": 0, "MG": -3, "MH": -2, "MI": 1, "MK": -1, "ML": 2, "MM": 5, "MN": -2, "MP": -2, "MQ": 0, "MR": -1, "MS": -1, "MT": -1, "MV": 1, "MW": -1, "MY": -1,
    "NA": -2, "NC": -3, "ND": 1, "NE": 0, "NF": -3, "NG": 0, "NH": 1, "NI": -3, "NK": 0, "NL": -3, "NM": -2, "NN": 6, "NP": -2, "NQ": 0, "NR": 0, "NS": 1, "NT": 0, "NV": -3, "NW": -4, "NY": -2,
    "PA": -1, "PC": -3, "PD": -1, "PE": -1, "PF": -4, "PG": -2, "PH": -2, "PI": -3, "PK": -1, "PL": -3, "PM": -2, "PN": -2, "PP": 7, "PQ": -1, "PR": -2, "PS": -1, "PT": -1, "PV": -2, "PW": -4, "PY": -3,
    "QA": -1, "QC": -3, "QD": 0, "QE": 2, "QF": -3, "QG": -2, "QH": 0, "QI": -3, "QK": 1, "QL": -2, "QM": 0, "QN": 0, "QP": -1, "QQ": 5, "QR": 1, "QS": 0, "QT": -1, "QV": -2, "QW": -2, "QY": -1,
    "RA": -1, "RC": -3, "RD": -2, "RE": 0, "RF": -3, "RG": -2, "RH": 0, "RI": -3, "RK": 2, "RL": -2, "RM": -1, "RN": 0, "RP": -2, "RQ": 1, "RR": 5, "RS": -1, "RT": -1, "RV": -3, "RW": -3, "RY": -2,
    "SA": 1, "SC": -1, "SD": 0, "SE": 0, "SF": -2, "SG": 0, "SH": -1, "SI": -2, "SK": 0, "SL": -2, "SM": -1, "SN": 1, "SP": -1, "SQ": 0, "SR": -1, "SS": 4, "ST": 1, "SV": -2, "SW": -3, "SY": -2,
    "TA": 0, "TC": -1, "TD": -1, "TE": -1, "TF": -2, "TG": -2, "TH": -2, "TI": -1, "TK": -1, "TL": -1, "TM": -1, "TN": 0, "TP": -1, "TQ": -1, "TR": -1, "TS": 1, "TT": 5, "TV": 0, "TW": -2, "TY": -2,
    "VA": 0, "VC": -1, "VD": -3, "VE": -2, "VF": -1, "VG": -3, "VH": -3, "VI": 3, "VK": -2, "VL": 1, "VM": 1, "VN": -3, "VP": -2, "VQ": -2, "VR": -3, "VS": -2, "VT": 0, "VV": 4, "VW": -3, "VY": -1,
    "WA": -3, "WC": -2, "WD": -4, "WE": -3, "WF": 1, "WG": -2, "WH": -2, "WI": -3, "WK": -3, "WL": -2, "WM": -1, "WN": -4, "WP": -4, "WQ": -2, "WR": -3, "WS": -3, "WT": -2, "WV": -3, "WW": 11, "WY": 2,
    "YA": -2, "YC": -2, "YD": -3, "YE": -2, "YF": 3, "YG": -3, "YH": 2, "YI": -1, "YK": -2, "YL": -1, "YM": -1, "YN": -2, "YP": -3, "YQ": -1, "YR": -2, "YS": -2, "YT": -2, "YV": -1, "YW": 2, "YY": 7
}

class BLAST:
    def __init__(self, path, is_nucleic, use_blosum, query, x, K, L, top, modifier, nucleic_k, protein_k, match_score, missmatch_score):
        self.path = path
        self.index_path = fr"{self.path}.idx"
        self.is_nucleic = is_nucleic
        self.use_blosum = use_blosum

        self.x = x
        self.K = K
        self.L = L
        self.modifier = modifier
        self.top = top
        self.match_score = match_score
        self.missmatch_score = missmatch_score

        if self.is_nucleic:
            self.k = nucleic_k
        else:
            self.k = protein_k

        if os.path.exists(self.index_path):
            self.db_object = logic.load_data(self.index_path)
        else:
            self.db_object = DataBase(self.path, self.is_nucleic, self.k)
            logic.save_data(self.db_object, self.index_path)

        self.query = query
        self.db = self.db_object.hash_table


        if self.query.endswith(".fasta") or self.query.endswith(".fa"):
            query_sequences = logic.get_sequences(self.query)
            for query_id in query_sequences:
                self.query_name = query_id
                self.query = query_sequences[query_id]
                self.use_colors = False
                self.match_query()
                logic.save_to_file_or_print(self, self.sorted_hsps, self.query_name, True)
        else:
            self.query_name = "Query_1"
            self.use_colors = True
            self.match_query()
            logic.save_to_file_or_print(self, self.sorted_hsps, self.query_name)

    def match_query(self):
        """ Finds matches of query k-mers in db """
        self.query_length = len(self.query)
        self.hashed_kmers = logic.get_kmers({self.query_name : self.query}, self.k)

        matches = {}  # Example: {3 #query match position : [(Sequence_1, 25), (Sequence_2, 12), ...]}

        for kmer in self.hashed_kmers:
            if kmer in self.db:
                for (id,q_pos) in self.hashed_kmers[kmer]:
                    if q_pos in matches:
                        for item in self.db[kmer]:
                            matches[q_pos].append(item)
                    else:
                        matches[q_pos] = self.db[kmer]

        self.hsps = self.ungapped_extension(matches)
        self.filtered_hsps = [hsp for hsp in self.hsps if hsp["Max Score"] >= self.k + self.modifier]
        self.sorted_hsps = sorted(self.filtered_hsps, key=lambda hsp: hsp["Max Score"], reverse=True)

    def extend_seed(self, max_score, target, direction, i, current_target_pos, max_i, max_target_i):
        """ Ungapped extension logic function """
        current_score = max_score
        while True:
            if i < 0 or i >= len(self.query) or current_target_pos < 0 or current_target_pos >= len(
                    target):
                break

            if not self.use_blosum:
                if target[current_target_pos] == self.query[i]:
                    current_score += self.match_score
                else:
                    current_score += self.missmatch_score
            else:
                pair = target[current_target_pos] + self.query[i]
                current_score += BLOSUM62.get(pair, self.missmatch_score)

            if current_score > max_score:
                max_score = current_score
                max_i = i
                max_target_i = current_target_pos

            if max_score - current_score > self.x:
                break

            i += direction
            current_target_pos += direction

        return [max_i, max_target_i, max_score]


    def ungapped_extension(self, matches):
        """ Ungapped extension logic function """
        extended_intervals = {}
        HSPS = []
        for match in matches:
            query_pos = match
            for target_id, target_pos in matches[match]:
                target = self.db_object.sequences[target_id]

                if target_id in extended_intervals:
                    if target_pos in extended_intervals[target_id]:
                        continue

                if not self.use_blosum:
                    max_score = self.match_score * self.k
                else:
                    max_score = sum([BLOSUM62.get(self.query[query_pos + _] * 2, self.missmatch_score) for _ in range(0, self.k)])

                kmer_cost = max_score

                right = self.extend_seed(max_score, target, 1, query_pos + self.k,
                                 target_pos + self.k, query_pos + self.k - 1, target_pos + self.k - 1)
                left = self.extend_seed(max_score, target, -1, query_pos - 1,
                                 target_pos - 1, query_pos, target_pos)

                total_score = right[2] + left[2] - kmer_cost

                eValue = self.K * self.db_object.length * self.query_length * math.e ** -(
                            self.L * total_score)

                HSP = {"Query_left": left[0], "Query_right": right[0],
                       "Target_left": left[1], "Target_right": right[1],
                       "Max Score": total_score, "Target_id": target_id,
                       "eValue": eValue}
                HSPS.append(HSP)

                if target_id in extended_intervals:
                    extended_intervals[target_id].update(range(left[1], right[1]+1))
                else:
                    extended_intervals[target_id] = set(range(left[1], right[1]+1))
        return HSPS


    def output(self, HSPS):
        """ Parse data to a *fancy* output """
        counter = 0
        for HSP in HSPS:
            counter += 1
            target_seq = self.db_object.sequences[HSP["Target_id"]]
            q_seq = self.query[HSP['Query_left']:HSP['Query_right']+1]
            t_seq = target_seq[HSP['Target_left']:HSP['Target_right']+1]

            q_start, q_end = HSP['Query_left'], HSP['Query_right']
            t_start, t_end = HSP['Target_left'], HSP['Target_right']

            m_seq = "".join(['|' if q == t else '.' for q, t in zip(q_seq, t_seq)])
            formatted_eValue = f"{HSP['eValue']:.2e}"

            header = f" Target: {HSP['Target_id']:<15} | Score: {HSP['Max Score']:<5} | E-value: {formatted_eValue:<5} | Length: {q_end - q_start + 1:<5} | Query: {self.query_name} "

            print("=" * len(header))
            print(header)
            print("-" * len(header))

            max_num_len = max(len(str(q_start)), len(str(q_end)), len(str(t_start)), len(str(t_end)))
            match_padding = " " * (8 + max_num_len + 1)

            GREEN = '\033[92m' if self.use_colors else ''
            RESET = '\033[0m' if self.use_colors else ''

            print(f"Query:  {q_start:>{max_num_len}} {q_seq} {q_end}")
            print(f"{match_padding}{GREEN}{m_seq}{RESET}")
            print(f"Target: {t_start:>{max_num_len}} {t_seq} {t_end}")

            print("=" * len(header) + "\n")
            if counter == self.top:
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simplified BLAST search")
    parser.add_argument("-db", "--database", type=str, required=True, help="Path to database FASTA file")
    parser.add_argument("-q", "--query", type=str, required=True, help="Query sequence or FASTA file")
    parser.add_argument("-b", "--use_blosum", action='store_true', help="Use BLOSUM62 matrix")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--nucleic", action='store_true', help="Search nucleic acids")
    group.add_argument("-p", "--protein", action='store_true', help="Search proteins")

    args = parser.parse_args()

    options = logic.load_options("options.json")

    blast = BLAST(
        path=args.database,
        is_nucleic=args.nucleic,
        use_blosum=args.use_blosum,
        query=args.query,
        x=options['x'],
        K=options['K'],
        L=options['L'],
        top=options['top'],
        modifier=options['modifier'],
        nucleic_k=options['nucleic_k-mer_size'],
        protein_k=options['protein_k-mer_size'],
        match_score=options['match_score'],
        missmatch_score=options['missmatch_score']
    )



