import math  # 引入 math 函數庫

ue_rnti = 17020  # 這是一個變數，表示用戶的 RNTI（無線臨時識別碼）
csId = 1  # 這是一個變數，表示某個類別的 ID
cnt_slot = 7  # 這是一個變數，表示時隙的計數
candidate_num = 4  # 這是一個變數，表示候選人的數目
AL = 2  # 這是一個變數，表示一個參數
freqDomainRes = 45  # 這是一個變數，表示頻域解析度
pdcchDuration = 1  # 這是一個變數，表示 PDCCH 的持續時間

def create_Y_tbl():
    y = []  # 這是一個向量，用於存儲 Y 值
    tmp_Y = ue_rnti  # 這是一個變數，表示臨時 Y 值
    
    # 根據類別 ID 選擇一個常數
    if csId % 3 == 0:
        Ap = 39827  # 這是一個變數，表示常數
    elif csId % 3 == 1:
        Ap = 39829  # 這是一個變數，表示常數
    else:
        Ap = 39839  # 這是一個變數，表示常數
    print("Ap", Ap)
    
    # 生成一個序列
    for i in range(20):
        tmp_Y = (Ap * tmp_Y) % 65537  # 這是一個數學運算，計算 Y 值
        y.append(tmp_Y)  # 將 Y 值添加到向量中
        print("Calculating y[{}]:".format(i))
        if i == 0:
            print("tmp_Y[{}] = (Ap * tmp_Y[{}]) % 65537".format(i, i-1))
            print("tmp_Y[{}] = ({} * {}) % 65537".format(i, Ap, ue_rnti))
        else:
            print("tmp_Y[{}] = (Ap * tmp_Y[{}]) % 65537".format(i, i-1))
            print("tmp_Y[{}] = ({} * {}) % 65537".format(i, Ap, y[i-1]))
        print("tmp_Y[{}] = {}".format(i, tmp_Y))  # 輸出 tmp_Y 值
    
    return y  # 返回 Y 值向量

def main():
    y = create_Y_tbl()  # 呼叫函數生成 Y 值向量
    
    for candidate_idx in range(candidate_num):  # 循環遍歷候選人索引
        # 計算 CCE 索引
        cce_idx = ((y[cnt_slot] + math.floor(candidate_idx * (pdcchDuration * freqDomainRes) / (AL * candidate_num))) % (math.floor(pdcchDuration * freqDomainRes / AL))) * AL
        print("Calculating cce_index for candidate_idx", candidate_idx, ":")
        print("cce_idx = ((y[cnt_slot] + math.floor({} * ({} * {}) / ({} * {}))) % (math.floor({} * {} / {}))) * {}".format(candidate_idx, pdcchDuration, freqDomainRes, AL, candidate_num, pdcchDuration, freqDomainRes, AL, AL))
        print("cce_idx = (({} + math.floor({} * {} / {}) % (math.floor({} / {}))) * {}".format(y[cnt_slot], candidate_idx, (pdcchDuration * freqDomainRes), (AL * candidate_num), (pdcchDuration * freqDomainRes), AL, AL))
        print("cce_idx = (({} + math.floor({} / {}) % {}) * {}".format(y[cnt_slot], (candidate_idx * (pdcchDuration * freqDomainRes)), (AL * candidate_num), (math.floor(pdcchDuration * freqDomainRes / AL)), AL))
        print("cce_idx = (({} + {}) % {}) * {}".format(y[cnt_slot], math.floor(candidate_idx * (pdcchDuration * freqDomainRes) / (AL * candidate_num)), (math.floor(pdcchDuration * freqDomainRes / AL)), AL))
        print("cce_idx = ({} % {}) * {}".format((y[cnt_slot] + math.floor(candidate_idx * (pdcchDuration * freqDomainRes) / (AL * candidate_num))), (math.floor(pdcchDuration * freqDomainRes / AL)), AL))
        print("cce_idx = {} * {}".format(((y[cnt_slot] + math.floor(candidate_idx * (pdcchDuration * freqDomainRes) / (AL * candidate_num))) % (math.floor(pdcchDuration * freqDomainRes / AL))), AL))
        print("cce_idx =", cce_idx)  # 輸出 CCE 索引

if __name__ == "__main__":
    main()  # 執行主函數
