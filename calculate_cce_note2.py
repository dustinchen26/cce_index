import math
ue_rnti = 17020
csId = 1
cnt_slot = 7
candidate_num = 4
AL = 2
freqDomainRes = 45
pdcchDuration = 1
def create_Y_tbl():
    y = []
    tmp_Y = ue_rnti
    
    if csId % 3 == 0:
        Ap = 39827
    elif csId % 3 == 1:
        Ap = 39829
    else:
        Ap = 39839
    print("Ap", Ap)
    
    for _ in range(20):
        tmp_Y = (Ap * tmp_Y) % 65537
        y.append(tmp_Y)
        print("y[{}] {}".format(_, tmp_Y))
    
    return y
def main():
    y = create_Y_tbl()
    
    for candidate_idx in range(candidate_num):
        part1 = y[cnt_slot]
        part2 = candidate_idx * (pdcchDuration * freqDomainRes) / (AL * candidate_num)
        part3 = math.floor(part2)
        part4 = (part1 + part3) % (math.floor(pdcchDuration * freqDomainRes / AL))
        cce_idx = part4 * AL
        print("CCE idx = (({} + math.floor({} * ({} * {}) / ({} * {}))) % (math.floor({} * {} / {}))) * {}".format(
            part1, candidate_idx, pdcchDuration, freqDomainRes, AL, candidate_num, pdcchDuration, freqDomainRes, AL, AL))
        print("        = (({} + math.floor({})) % ({})) * {}".format(
            part1, part2, math.floor(pdcchDuration * freqDomainRes / AL), AL))
        print("        = (({} + {})) % ({})) * {}".format(
            part1, part3, math.floor(pdcchDuration * freqDomainRes / AL), AL))
        print("        = ({} % {}) * {}".format(part4, math.floor(pdcchDuration * freqDomainRes / AL), AL))
        print("        = {} * {}".format(part4, AL))
        print("        = {}".format(cce_idx))
if __name__ == "__main__":
    main()