import numpy as np

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

def function(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1
    nf = -np.inf
    M = np.zeros((rows, cols))
    I = M.copy()
    J = M.copy()

    gap_opening = -11
    gap_extension = -1

    M[0, 1:] = [nf for _ in range(len(M[0])-1)]
    M[1:, 0] = [nf for _ in range(len(M[1:, 0]))]

    I[0][0] = gap_opening
    I[0, 1:] = [nf for _ in range(len(I[0])-1)]
    I[1:, 0] = [gap_opening-1+i*gap_extension for i in range(len(I[1:, 0]))]

    J[0][0] = gap_opening
    J[0, 1:] = [gap_opening-1+i*gap_extension for i in range(len(J[0])-1)]
    J[1:, 0] = [nf for _ in range(len(J[1:, 0]))]

    for row in range(1, rows):
        for col in range(1, cols):
            s_ij = blosum62.get(s1[row-1] + s2[col-1], 0)

            M[row][col] = s_ij + max(M[row-1][col-1],
                                    I[row-1][col-1],
                                    J[row-1][col-1])
            I[row][col] = max(I[row-1][col] + gap_extension,
                              J[row-1][col] + gap_opening,
                              M[row-1][col] + gap_opening)
            J[row][col] = max(J[row][col - 1] + gap_extension,
                              I[row][col - 1] + gap_opening,
                              M[row][col - 1] + gap_opening)

    M_score = M[-1][-1]
    I_score = I[-1][-1]
    J_score = J[-1][-1]
    print(M)
    print(I)
    print(J)
    # final_score = max(M_score, I_score, J_score)
    # if final_score == M_score:
    #     matrix = M
    # elif final_score == I_score:
    #     matrix = I
    # else:
    #     matrix = J
    #
    # align1 = ""
    # align2 = ""
    # i = rows - 1
    # j = cols - 1
    #
    # matching = ""
    # while i > 0 or j > 0:
    #     print("--------------------------------------------------")
    #     current_score = matrix[i][j]
    #     print(current_score)
    #
    #     if i > 0 and j > 0:
    #         s_ij = blosum62.get(s1[i-1] + s2[j-1], 0)
    #         print([M[i - 1][j - 1] + s_ij, I[i - 1][j - 1] + s_ij, J[i - 1][j - 1] + s_ij])
    #         if current_score in [M[i - 1][j - 1] + s_ij, I[i - 1][j - 1] + s_ij, J[i - 1][j - 1] + s_ij]:
    #             align1 += s1[i - 1]
    #             align2 += s2[j - 1]
    #
    #             if s1[i - 1] == s2[j - 1]:
    #                 matching += "|"
    #             else:
    #                 matching += "."
    #
    #             i -= 1
    #             j -= 1
    #
    #             continue
    #     print([I[i-1][j] + gap_extension, J[i-1][j] + gap_opening, M[i-1][j] + gap_opening])
    #     if i > 0 and current_score in [I[i-1][j] + gap_extension, J[i-1][j] + gap_opening, M[i-1][j] + gap_opening]:
    #         align1 += s1[i - 1]
    #         align2 += "-"
    #         i -= 1
    #         matching += "-"
    #         continue
    #     print([J[i][j - 1] + gap_extension, I[i][j - 1] + gap_opening, M[i][j - 1] + gap_opening])
    #     if j > 0 and current_score in [J[i][j - 1] + gap_extension, I[i][j - 1] + gap_opening, M[i][j - 1] + gap_opening]:
    #         align1 += "-"
    #         align2 += s2[j - 1]
    #         j -= 1
    #         matching += "-"
    #     print(align1)
    #     print(align2)
    #
    # return align1[::-1], align2[::-1], final_score, matching[::-1]


from Parse_FASTA import Parse_FASTA
s = Parse_FASTA(r"C:\Users\rodio\PycharmProjects\Bioinformatics\Rosalind.txt")
s1, s2 = s.values()
result = function(s1, s2)
print(result)