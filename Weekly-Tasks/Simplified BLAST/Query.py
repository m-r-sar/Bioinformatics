from Indexing import get_kmers, hash_sequence, DataBase

class BLAST:
    def __init__(self):
        self.isNucleic = bool(int(input('Nucleic sequence? (1/0): ')))
        self.k = 11 if self.isNucleic else 3
        self.path = r"test_dna.fasta" if self.isNucleic else r"test_protein.fasta"
        self.db_object = DataBase(self.path, self.isNucleic)
        self.db = self.db_object.id_to_trees
        self.x = 5
        self.K = 0.1
        self.L = 0.3
        self.e = 2.71828

        while True:
            self.query = input('Enter a query to BLAST: ')
            self.query_length = len(self.query)
            self.kmers = get_kmers(self.query, self.k)
            self.hashed_kmers = hash_sequence(self.kmers, self.k, self.isNucleic)
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
            self.filtered_hsps = [hsp for hsp in self.hsps if hsp["Max Score"] >= 7]
            self.sorted_hsps = sorted(self.filtered_hsps, key=lambda hsp: hsp["Max Score"], reverse=True)

            self.output(self.sorted_hsps)


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
                    for direction in [-1, 1]:
                        match_score = 1
                        missmatch_score = -3

                        if direction == 1:
                            i = query_pos + self.k
                            current_target_pos = target_pos + self.k
                        else:
                            i = query_pos
                            current_target_pos = target_pos

                        max_score = match_score * self.k
                        current_score = match_score * self.k
                        max_i = i
                        max_target_i = current_target_pos
                        matching = ""

                        while True:
                            i += direction
                            current_target_pos += direction

                            if i < 0 or i >= len(self.query) or current_target_pos < 0 or current_target_pos >= len(target):
                                max_i = i - direction
                                max_target_i = current_target_pos - direction
                                max_score = current_score

                                if direction == 1:
                                    right = [max_i, max_target_i, max_score, matching]
                                    break
                                else:
                                    left = [max_i, max_target_i, max_score, matching]
                                    break


                            if target[current_target_pos-1] == self.query[i-1]:
                                current_score += match_score
                                matching += "|"
                            else:
                                current_score += missmatch_score
                                matching += "."

                            if max_score < current_score:
                                max_i = i
                                max_target_i = current_target_pos
                                max_score = current_score

                            elif current_score < max_score - self.x:
                                if direction == 1:
                                    right = [max_i, max_target_i, max_score, matching]
                                    break
                                else:
                                    left = [max_i, max_target_i, max_score, matching]
                                    break


                    HSP = {"Query_left": left[0], "Query_right": right[0],
                           "Target_left": left[1], "Target_right": right[1],
                           "Max Score": right[2]+left[2]-self.k, "Target_id": target_id,
                           "Matching": left[3] + right[3]}
                    HSPS.append(HSP)

                    if target_id in extended_intervals:
                        extended_intervals[target_id].append([_ for _ in range(left[1], right[1]+1)])
                    else:
                        extended_intervals[target_id] = [[_ for _ in range(left[1], right[1]+1)]]
        return HSPS


    def output(self, HSPS):
        for HSP in HSPS:
            target_seq = self.db_object.sequences[HSP["Target_id"]]
            q_seq = self.query[HSP['Query_left']:HSP['Query_right']]
            t_seq = target_seq[HSP['Target_left']:HSP['Target_right']]

            q_start, q_end = HSP['Query_left'], HSP['Query_right']
            t_start, t_end = HSP['Target_left'], HSP['Target_right']

            m_seq = "".join(['|' if q == t else '.' for q, t in zip(q_seq, t_seq)])

            header = f" Target: {HSP['Target_id']:<15} | Score: {HSP['Max Score']:<5} | E-value: {self.K * self.db_object.length * self.query_length * self.e **-(self.L*HSP['Max Score']):<5} | Length: {q_end - q_start:<5} | Query: {self.query} "

            print("=" * len(header))
            print(header)
            print("-" * len(header))

            max_num_len = max(len(str(q_start)), len(str(q_end)), len(str(t_start)), len(str(t_end)))
            match_padding = " " * (8 + max_num_len + 1)

            GREEN = '\033[92m'
            RESET = '\033[0m'

            print(f"Query:  {q_start:>{max_num_len}} {q_seq} {q_end}")
            print(f"{match_padding}{GREEN}{m_seq}{RESET}")
            print(f"Target: {t_start:>{max_num_len}} {t_seq} {t_end}")

            print("=" * len(header) + "\n")




# [('mock_sequence_2', [72], [15]), ('mock_sequence_6', [4], [10]), ('mock_sequence_8', [27], [12]), ('mock_sequence_13', [54], [14]), ('mock_sequence_15', [118], [14]), ('mock_sequence_18', [67, 118], [15]), ('mock_sequence_19', [169], [24]), ('mock_sequence_24', [34], [0]), ('mock_sequence_24', [35], [1]), ('mock_sequence_24', [36], [2]), ('mock_sequence_24', [37], [3]), ('mock_sequence_24', [2, 38], [4]), ('mock_sequence_24', [39], [5]), ('mock_sequence_24', [40], [6]), ('mock_sequence_24', [41], [7]), ('mock_sequence_24', [42], [8]), ('mock_sequence_24', [43], [9]), ('mock_sequence_24', [44], [10]), ('mock_sequence_24', [45], [11]), ('mock_sequence_24', [46], [12]), ('mock_sequence_24', [47], [13]), ('mock_sequence_24', [48], [14]), ('mock_sequence_24', [49], [15]), ('mock_sequence_24', [50], [16]), ('mock_sequence_24', [51], [17]), ('mock_sequence_24', [52], [18]), ('mock_sequence_24', [53], [19]), ('mock_sequence_24', [54], [20]), ('mock_sequence_24', [55], [21]), ('mock_sequence_24', [56], [22]), ('mock_sequence_24', [57], [23]), ('mock_sequence_24', [58], [24]), ('mock_sequence_26', [150], [15]), ('mock_sequence_38', [6], [2]), ('mock_sequence_44', [15], [10]), ('mock_sequence_44', [40], [18]), ('mock_sequence_45', [9], [19]), ('mock_sequence_47', [176], [0]), ('mock_sequence_49', [178], [19]), ('mock_sequence_52', [5], [24]), ('mock_sequence_57', [12], [14]), ('mock_sequence_58', [64], [6]), ('mock_sequence_59', [17], [5]), ('mock_sequence_63', [123], [6]), ('mock_sequence_63', [67], [22]), ('mock_sequence_65', [117], [11]), ('mock_sequence_73', [86], [14]), ('mock_sequence_74', [63], [16]), ('mock_sequence_74', [64], [17]), ('mock_sequence_75', [127], [6]), ('mock_sequence_77', [50], [9]), ('mock_sequence_78', [64], [5]), ('mock_sequence_78', [175], [24]), ('mock_sequence_81', [111, 131], [10]), ('mock_sequence_81', [127], [14]), ('mock_sequence_81', [172], [19]), ('mock_sequence_86', [167], [8]), ('mock_sequence_95', [7], [24]), ('mock_sequence_97', [83], [16]), ('mock_sequence_103', [238], [14]), ('mock_sequence_105', [172], [4]), ('mock_sequence_107', [24], [7]), ('mock_sequence_111', [61], [7]), ('mock_sequence_114', [50], [9]), ('mock_sequence_114', [132], [10]), ('mock_sequence_124', [70], [19]), ('mock_sequence_124', [38], [21]), ('mock_sequence_125', [190], [7]), ('mock_sequence_125', [48], [18]), ('mock_sequence_129', [132], [11]), ('mock_sequence_129', [84], [13]), ('mock_sequence_130', [87], [14]), ('mock_sequence_130', [26], [15]), ('mock_sequence_131', [90], [10]), ('mock_sequence_132', [130], [13]), ('mock_sequence_132', [70], [24]), ('mock_sequence_134', [157], [23]), ('mock_sequence_138', [73], [2]), ('mock_sequence_138', [126], [20]), ('mock_sequence_140', [123], [6]), ('mock_sequence_144', [231], [0]), ('mock_sequence_152', [26], [5]), ('mock_sequence_153', [65], [12]), ('mock_sequence_153', [205], [18]), ('mock_sequence_159', [153], [7]), ('mock_sequence_159', [171], [18]), ('mock_sequence_160', [143], [5]), ('mock_sequence_162', [62], [13]), ('mock_sequence_162', [4], [23]), ('mock_sequence_165', [98], [7]), ('mock_sequence_167', [90], [3]), ('mock_sequence_168', [179], [2]), ('mock_sequence_169', [21], [15]), ('mock_sequence_172', [11], [0]), ('mock_sequence_173', [52], [7]), ('mock_sequence_174', [57], [5]), ('mock_sequence_177', [39], [23]), ('mock_sequence_181', [82], [24]), ('mock_sequence_185', [70], [15]), ('mock_sequence_187', [129], [3]), ('mock_sequence_187', [155], [8]), ('mock_sequence_187', [23], [16]), ('mock_sequence_188', [15], [16]), ('mock_sequence_189', [111], [6]), ('mock_sequence_190', [66], [16]), ('mock_sequence_192', [1], [23]), ('mock_sequence_193', [30], [17]), ('mock_sequence_194', [57], [2]), ('mock_sequence_194', [121], [19]), ('mock_sequence_194', [94], [20]), ('mock_sequence_197', [177], [20]), ('mock_sequence_198', [54], [17]), ('mock_sequence_200', [60], [5]), ('mock_sequence_201', [27], [16]), ('mock_sequence_202', [22], [14]), ('mock_sequence_203', [87], [23]), ('mock_sequence_204', [169], [12]), ('mock_sequence_208', [7], [15]), ('mock_sequence_215', [21], [6]), ('mock_sequence_216', [172], [0]), ('mock_sequence_217', [24], [15]), ('mock_sequence_219', [64], [5]), ('mock_sequence_219', [109], [10]), ('mock_sequence_229', [82], [4]), ('mock_sequence_238', [87], [23]), ('mock_sequence_239', [168], [14]), ('mock_sequence_239', [193], [18]), ('mock_sequence_243', [49], [8]), ('mock_sequence_243', [50], [9]), ('mock_sequence_243', [40], [19]), ('mock_sequence_244', [65], [5]), ('mock_sequence_244', [172], [24]), ('mock_sequence_246', [52], [5]), ('mock_sequence_246', [53], [6]), ('mock_sequence_249', [89], [2]), ('mock_sequence_251', [92], [4]), ('mock_sequence_251', [21], [22]), ('mock_sequence_253', [40], [3]), ('mock_sequence_256', [5], [12]), ('mock_sequence_257', [207], [3]), ('mock_sequence_258', [58], [14]), ('mock_sequence_258', [59], [16]), ('mock_sequence_263', [46], [10]), ('mock_sequence_266', [60], [1]), ('mock_sequence_268', [30], [21]), ('mock_sequence_270', [80], [10]), ('mock_sequence_273', [32], [10]), ('mock_sequence_275', [36], [24]), ('mock_sequence_276', [152], [19]), ('mock_sequence_278', [2], [2]), ('mock_sequence_278', [200], [21]), ('mock_sequence_280', [61], [6]), ('mock_sequence_281', [164], [2]), ('mock_sequence_287', [108], [12]), ('mock_sequence_287', [126], [18]), ('mock_sequence_291', [171], [7]), ('mock_sequence_296', [160], [16]), ('mock_sequence_297', [0], [3]), ('mock_sequence_298', [175], [24]), ('mock_sequence_300', [224], [24]), ('mock_sequence_301', [47], [13]), ('mock_sequence_302', [111], [21]), ('mock_sequence_303', [158], [24]), ('mock_sequence_304', [71], [2]), ('mock_sequence_307', [2], [16]), ('mock_sequence_307', [36], [24]), ('mock_sequence_313', [16], [5]), ('mock_sequence_316', [24], [21]), ('mock_sequence_319', [89], [15]), ('mock_sequence_320', [164], [3]), ('mock_sequence_320', [162], [5]), ('mock_sequence_320', [51], [18]), ('mock_sequence_322', [4], [15]), ('mock_sequence_323', [101], [16]), ('mock_sequence_323', [108], [18]), ('mock_sequence_330', [78], [17]), ('mock_sequence_330', [79], [18]), ('mock_sequence_333', [87], [9]), ('mock_sequence_333', [157], [19]), ('mock_sequence_334', [124], [17]), ('mock_sequence_338', [39], [3]), ('mock_sequence_338', [40], [4]), ('mock_sequence_342', [140], [3]), ('mock_sequence_342', [37], [20]), ('mock_sequence_344', [9], [6]), ('mock_sequence_346', [24], [24]), ('mock_sequence_349', [50], [11]), ('mock_sequence_349', [70], [23]), ('mock_sequence_349', [71], [24]), ('mock_sequence_355', [84], [13]), ('mock_sequence_360', [83], [6]), ('mock_sequence_361', [62], [9]), ('mock_sequence_365', [5], [22]), ('mock_sequence_367', [89], [2]), ('mock_sequence_367', [36], [16]), ('mock_sequence_373', [43], [13]), ('mock_sequence_378', [36], [11]), ('mock_sequence_385', [82], [13]), ('mock_sequence_389', [65], [23]), ('mock_sequence_395', [60], [24]), ('mock_sequence_397', [33], [17]), ('mock_sequence_407', [220], [17]), ('mock_sequence_409', [68], [7]), ('mock_sequence_410', [34], [20]), ('mock_sequence_416', [8], [22]), ('mock_sequence_421', [23], [18]), ('mock_sequence_422', [21], [15]), ('mock_sequence_423', [56], [19]), ('mock_sequence_429', [95], [0]), ('mock_sequence_431', [143, 144, 145], [15]), ('mock_sequence_432', [109], [2]), ('mock_sequence_432', [58], [18]), ('mock_sequence_433', [136], [8]), ('mock_sequence_434', [127], [20]), ('mock_sequence_434', [128], [21]), ('mock_sequence_434', [129], [22]), ('mock_sequence_435', [107], [6]), ('mock_sequence_438', [189], [3]), ('mock_sequence_439', [127], [14]), ('mock_sequence_442', [92], [10]), ('mock_sequence_443', [43], [23]), ('mock_sequence_446', [171], [16]), ('mock_sequence_446', [159], [24]), ('mock_sequence_448', [16], [8]), ('mock_sequence_448', [42], [16]), ('mock_sequence_455', [43], [24]), ('mock_sequence_456', [5], [6]), ('mock_sequence_459', [84], [7]), ('mock_sequence_461', [122], [22]), ('mock_sequence_467', [17], [6]), ('mock_sequence_471', [38], [7]), ('mock_sequence_473', [38], [14]), ('mock_sequence_474', [19], [24]), ('mock_sequence_477', [65], [16]), ('mock_sequence_477', [66], [17]), ('mock_sequence_481', [158], [20]), ('mock_sequence_483', [48], [23]), ('mock_sequence_487', [13], [4]), ('mock_sequence_489', [47], [6]), ('mock_sequence_492', [77], [2]), ('mock_sequence_493', [56], [1]), ('mock_sequence_495', [93], [3]), ('mock_sequence_500', [25], [15])]

blast = BLAST()
