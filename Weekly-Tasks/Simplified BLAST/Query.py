from Indexing import DataBase
import Logic as logic

blosum62 = {
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
    def __init__(self):
        doIndexing = input('Index new DataBase? (Y/N): ') in ['Y', 'y']
        self.path = input('Path to file: ')
        self.isNucleic = input('Nucleic sequence? (Y/N): ') in ['Y', 'y']
        if self.isNucleic:
            self.k = 11
        else:
            self.k = 3
            self.useBlosum = input('Use blosum62? (Y/N): ') in ['Y', 'y']


        if doIndexing:
            self.fileName = input('New file name: ')
            self.db_object = DataBase(self.path, self.isNucleic)
            self.db = self.db_object.id_to_trees
            logic.save_data(self.db_object, self.fileName)
            print(fr"Saved database at {self.fileName}")
        else:
            self.db_object = logic.load_data(self.path)
            self.db = self.db_object.id_to_trees

        # self.path = r"test_dna.fasta" if self.isNucleic else r"test_protein.fasta"


        self.x = 5
        self.K = 0.1
        self.L = 0.3
        self.e = 2.71828

        while True:
            self.query = input('Enter a query to BLAST (q to exit): ')
            if self.query == 'q':
                print("Program exiting...")
                break
            elif self.query.endswith(".fasta") or self.query.endswith(".fa"):
                query_sequences = logic.get_sequences(self.query)
                for query_id in query_sequences:
                    self.query_name = query_id
                    self.query = query_sequences[query_id]
                    self.use_colors = False
                    self.match_query()
                    logic.save_to_file_or_print(self, self.sorted_hsps, self.query_name, True)
            else:
                self.query_name = "Nan"
                self.use_colors = True
                self.match_query()
                logic.save_to_file_or_print(self, self.sorted_hsps, self.query_name)

    def match_query(self):
        self.query_length = len(self.query)
        self.kmers = logic.get_kmers(self.query, self.k)
        self.hashed_kmers = logic.hash_sequence(self.kmers, self.k, self.isNucleic)
        # kmer_to_hash = dict(zip(kmers, hashed_kmers))

        matches = []  # Example: (Sequence_1, [1, 23], [3])
        for target in self.db:
            tree = self.db[target]

            for kmer in self.hashed_kmers:
                target_positions = tree.find(kmer)
                query_positions = self.hashed_kmers[kmer]

                if target_positions:
                    matches.append((target, target_positions.positions, query_positions))

        self.hsps = self.ungapped_extension(matches)
        self.filtered_hsps = [hsp for hsp in self.hsps if hsp["Max Score"] >= self.k + 3]
        self.sorted_hsps = sorted(self.filtered_hsps, key=lambda hsp: hsp["Max Score"], reverse=True)




    def ungapped_extension(self, matches):
        extended_intervals = {}
        HSPS = []
        for match in matches:
            target_id, target_positions, query_positions = match
            target = self.db_object.sequences[target_id]

            for target_pos in target_positions:
                if target_id in extended_intervals:
                    if any(target_pos in positions for positions in extended_intervals[target_id]):
                        continue

                for query_pos in query_positions:
                    left = None
                    right = None

                    for direction in [-1, 1]:
                        if self.isNucleic:
                            match_score = 1
                            missmatch_score = -3

                        if direction == 1:
                            i = query_pos + self.k
                            current_target_pos = target_pos + self.k

                            max_i = query_pos + self.k - 1
                            max_target_i = target_pos + self.k - 1
                        else:
                            i = query_pos - 1
                            current_target_pos = target_pos - 1

                            max_i = query_pos
                            max_target_i = target_pos

                        if not self.useBlosum:
                            max_score = match_score * self.k
                            current_score = match_score * self.k
                        else:
                            max_score = sum([blosum62[self.query[query_pos + _]*2] for _ in range(0, self.k)])
                            current_score = max_score

                        kmer_cost = max_score

                        while True:
                            if i < 0 or i >= len(self.query) or current_target_pos < 0 or current_target_pos >= len(
                                    target):
                                break

                            if not self.useBlosum:
                                if target[current_target_pos] == self.query[i]:
                                    current_score += match_score
                                else:
                                    current_score += missmatch_score
                            else:
                                current_score += blosum62[target[current_target_pos] + self.query[i]]

                            if current_score > max_score:
                                max_score = current_score
                                max_i = i
                                max_target_i = current_target_pos

                            if max_score - current_score > self.x:
                                break

                            i += direction
                            current_target_pos += direction

                        if direction == 1:
                            right = [max_i, max_target_i, max_score]
                        else:
                            left = [max_i, max_target_i, max_score]

                    eValue = self.K * self.db_object.length * self.query_length * self.e ** -(self.L * right[2]+left[2]-self.k)
                    HSP = {"Query_left": left[0], "Query_right": right[0],
                           "Target_left": left[1], "Target_right": right[1],
                           "Max Score": right[2]+left[2]-kmer_cost, "Target_id": target_id,
                           "eValue": eValue}
                    HSPS.append(HSP)

                    if target_id in extended_intervals:
                        extended_intervals[target_id].append([_ for _ in range(left[1], right[1]+1)])
                    else:
                        extended_intervals[target_id] = [[_ for _ in range(left[1], right[1]+1)]]
        return HSPS


    def output(self, HSPS):
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
            if counter == 3:
                break




# [('mock_sequence_2', [72], [15]), ('mock_sequence_6', [4], [10]), ('mock_sequence_8', [27], [12]), ('mock_sequence_13', [54], [14]), ('mock_sequence_15', [118], [14]), ('mock_sequence_18', [67, 118], [15]), ('mock_sequence_19', [169], [24]), ('mock_sequence_24', [34], [0]), ('mock_sequence_24', [35], [1]), ('mock_sequence_24', [36], [2]), ('mock_sequence_24', [37], [3]), ('mock_sequence_24', [2, 38], [4]), ('mock_sequence_24', [39], [5]), ('mock_sequence_24', [40], [6]), ('mock_sequence_24', [41], [7]), ('mock_sequence_24', [42], [8]), ('mock_sequence_24', [43], [9]), ('mock_sequence_24', [44], [10]), ('mock_sequence_24', [45], [11]), ('mock_sequence_24', [46], [12]), ('mock_sequence_24', [47], [13]), ('mock_sequence_24', [48], [14]), ('mock_sequence_24', [49], [15]), ('mock_sequence_24', [50], [16]), ('mock_sequence_24', [51], [17]), ('mock_sequence_24', [52], [18]), ('mock_sequence_24', [53], [19]), ('mock_sequence_24', [54], [20]), ('mock_sequence_24', [55], [21]), ('mock_sequence_24', [56], [22]), ('mock_sequence_24', [57], [23]), ('mock_sequence_24', [58], [24]), ('mock_sequence_26', [150], [15]), ('mock_sequence_38', [6], [2]), ('mock_sequence_44', [15], [10]), ('mock_sequence_44', [40], [18]), ('mock_sequence_45', [9], [19]), ('mock_sequence_47', [176], [0]), ('mock_sequence_49', [178], [19]), ('mock_sequence_52', [5], [24]), ('mock_sequence_57', [12], [14]), ('mock_sequence_58', [64], [6]), ('mock_sequence_59', [17], [5]), ('mock_sequence_63', [123], [6]), ('mock_sequence_63', [67], [22]), ('mock_sequence_65', [117], [11]), ('mock_sequence_73', [86], [14]), ('mock_sequence_74', [63], [16]), ('mock_sequence_74', [64], [17]), ('mock_sequence_75', [127], [6]), ('mock_sequence_77', [50], [9]), ('mock_sequence_78', [64], [5]), ('mock_sequence_78', [175], [24]), ('mock_sequence_81', [111, 131], [10]), ('mock_sequence_81', [127], [14]), ('mock_sequence_81', [172], [19]), ('mock_sequence_86', [167], [8]), ('mock_sequence_95', [7], [24]), ('mock_sequence_97', [83], [16]), ('mock_sequence_103', [238], [14]), ('mock_sequence_105', [172], [4]), ('mock_sequence_107', [24], [7]), ('mock_sequence_111', [61], [7]), ('mock_sequence_114', [50], [9]), ('mock_sequence_114', [132], [10]), ('mock_sequence_124', [70], [19]), ('mock_sequence_124', [38], [21]), ('mock_sequence_125', [190], [7]), ('mock_sequence_125', [48], [18]), ('mock_sequence_129', [132], [11]), ('mock_sequence_129', [84], [13]), ('mock_sequence_130', [87], [14]), ('mock_sequence_130', [26], [15]), ('mock_sequence_131', [90], [10]), ('mock_sequence_132', [130], [13]), ('mock_sequence_132', [70], [24]), ('mock_sequence_134', [157], [23]), ('mock_sequence_138', [73], [2]), ('mock_sequence_138', [126], [20]), ('mock_sequence_140', [123], [6]), ('mock_sequence_144', [231], [0]), ('mock_sequence_152', [26], [5]), ('mock_sequence_153', [65], [12]), ('mock_sequence_153', [205], [18]), ('mock_sequence_159', [153], [7]), ('mock_sequence_159', [171], [18]), ('mock_sequence_160', [143], [5]), ('mock_sequence_162', [62], [13]), ('mock_sequence_162', [4], [23]), ('mock_sequence_165', [98], [7]), ('mock_sequence_167', [90], [3]), ('mock_sequence_168', [179], [2]), ('mock_sequence_169', [21], [15]), ('mock_sequence_172', [11], [0]), ('mock_sequence_173', [52], [7]), ('mock_sequence_174', [57], [5]), ('mock_sequence_177', [39], [23]), ('mock_sequence_181', [82], [24]), ('mock_sequence_185', [70], [15]), ('mock_sequence_187', [129], [3]), ('mock_sequence_187', [155], [8]), ('mock_sequence_187', [23], [16]), ('mock_sequence_188', [15], [16]), ('mock_sequence_189', [111], [6]), ('mock_sequence_190', [66], [16]), ('mock_sequence_192', [1], [23]), ('mock_sequence_193', [30], [17]), ('mock_sequence_194', [57], [2]), ('mock_sequence_194', [121], [19]), ('mock_sequence_194', [94], [20]), ('mock_sequence_197', [177], [20]), ('mock_sequence_198', [54], [17]), ('mock_sequence_200', [60], [5]), ('mock_sequence_201', [27], [16]), ('mock_sequence_202', [22], [14]), ('mock_sequence_203', [87], [23]), ('mock_sequence_204', [169], [12]), ('mock_sequence_208', [7], [15]), ('mock_sequence_215', [21], [6]), ('mock_sequence_216', [172], [0]), ('mock_sequence_217', [24], [15]), ('mock_sequence_219', [64], [5]), ('mock_sequence_219', [109], [10]), ('mock_sequence_229', [82], [4]), ('mock_sequence_238', [87], [23]), ('mock_sequence_239', [168], [14]), ('mock_sequence_239', [193], [18]), ('mock_sequence_243', [49], [8]), ('mock_sequence_243', [50], [9]), ('mock_sequence_243', [40], [19]), ('mock_sequence_244', [65], [5]), ('mock_sequence_244', [172], [24]), ('mock_sequence_246', [52], [5]), ('mock_sequence_246', [53], [6]), ('mock_sequence_249', [89], [2]), ('mock_sequence_251', [92], [4]), ('mock_sequence_251', [21], [22]), ('mock_sequence_253', [40], [3]), ('mock_sequence_256', [5], [12]), ('mock_sequence_257', [207], [3]), ('mock_sequence_258', [58], [14]), ('mock_sequence_258', [59], [16]), ('mock_sequence_263', [46], [10]), ('mock_sequence_266', [60], [1]), ('mock_sequence_268', [30], [21]), ('mock_sequence_270', [80], [10]), ('mock_sequence_273', [32], [10]), ('mock_sequence_275', [36], [24]), ('mock_sequence_276', [152], [19]), ('mock_sequence_278', [2], [2]), ('mock_sequence_278', [200], [21]), ('mock_sequence_280', [61], [6]), ('mock_sequence_281', [164], [2]), ('mock_sequence_287', [108], [12]), ('mock_sequence_287', [126], [18]), ('mock_sequence_291', [171], [7]), ('mock_sequence_296', [160], [16]), ('mock_sequence_297', [0], [3]), ('mock_sequence_298', [175], [24]), ('mock_sequence_300', [224], [24]), ('mock_sequence_301', [47], [13]), ('mock_sequence_302', [111], [21]), ('mock_sequence_303', [158], [24]), ('mock_sequence_304', [71], [2]), ('mock_sequence_307', [2], [16]), ('mock_sequence_307', [36], [24]), ('mock_sequence_313', [16], [5]), ('mock_sequence_316', [24], [21]), ('mock_sequence_319', [89], [15]), ('mock_sequence_320', [164], [3]), ('mock_sequence_320', [162], [5]), ('mock_sequence_320', [51], [18]), ('mock_sequence_322', [4], [15]), ('mock_sequence_323', [101], [16]), ('mock_sequence_323', [108], [18]), ('mock_sequence_330', [78], [17]), ('mock_sequence_330', [79], [18]), ('mock_sequence_333', [87], [9]), ('mock_sequence_333', [157], [19]), ('mock_sequence_334', [124], [17]), ('mock_sequence_338', [39], [3]), ('mock_sequence_338', [40], [4]), ('mock_sequence_342', [140], [3]), ('mock_sequence_342', [37], [20]), ('mock_sequence_344', [9], [6]), ('mock_sequence_346', [24], [24]), ('mock_sequence_349', [50], [11]), ('mock_sequence_349', [70], [23]), ('mock_sequence_349', [71], [24]), ('mock_sequence_355', [84], [13]), ('mock_sequence_360', [83], [6]), ('mock_sequence_361', [62], [9]), ('mock_sequence_365', [5], [22]), ('mock_sequence_367', [89], [2]), ('mock_sequence_367', [36], [16]), ('mock_sequence_373', [43], [13]), ('mock_sequence_378', [36], [11]), ('mock_sequence_385', [82], [13]), ('mock_sequence_389', [65], [23]), ('mock_sequence_395', [60], [24]), ('mock_sequence_397', [33], [17]), ('mock_sequence_407', [220], [17]), ('mock_sequence_409', [68], [7]), ('mock_sequence_410', [34], [20]), ('mock_sequence_416', [8], [22]), ('mock_sequence_421', [23], [18]), ('mock_sequence_422', [21], [15]), ('mock_sequence_423', [56], [19]), ('mock_sequence_429', [95], [0]), ('mock_sequence_431', [143, 144, 145], [15]), ('mock_sequence_432', [109], [2]), ('mock_sequence_432', [58], [18]), ('mock_sequence_433', [136], [8]), ('mock_sequence_434', [127], [20]), ('mock_sequence_434', [128], [21]), ('mock_sequence_434', [129], [22]), ('mock_sequence_435', [107], [6]), ('mock_sequence_438', [189], [3]), ('mock_sequence_439', [127], [14]), ('mock_sequence_442', [92], [10]), ('mock_sequence_443', [43], [23]), ('mock_sequence_446', [171], [16]), ('mock_sequence_446', [159], [24]), ('mock_sequence_448', [16], [8]), ('mock_sequence_448', [42], [16]), ('mock_sequence_455', [43], [24]), ('mock_sequence_456', [5], [6]), ('mock_sequence_459', [84], [7]), ('mock_sequence_461', [122], [22]), ('mock_sequence_467', [17], [6]), ('mock_sequence_471', [38], [7]), ('mock_sequence_473', [38], [14]), ('mock_sequence_474', [19], [24]), ('mock_sequence_477', [65], [16]), ('mock_sequence_477', [66], [17]), ('mock_sequence_481', [158], [20]), ('mock_sequence_483', [48], [23]), ('mock_sequence_487', [13], [4]), ('mock_sequence_489', [47], [6]), ('mock_sequence_492', [77], [2]), ('mock_sequence_493', [56], [1]), ('mock_sequence_495', [93], [3]), ('mock_sequence_500', [25], [15])]

blast = BLAST()
