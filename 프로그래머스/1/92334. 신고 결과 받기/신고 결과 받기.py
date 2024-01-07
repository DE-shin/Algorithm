def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_name = [set() for _ in range(len(id_list))]
    report_num = [0] * len(id_list)
    
    for r in report:
        reporter, reportee = r.split()
        report_name[id_list.index(reporter)].add(reportee)
        
    for names in report_name:
        for name in names:
            report_num[id_list.index(name)] += 1
            
    for i, reported in enumerate(report_num):
        if reported >= k:
            for j, s in enumerate(report_name):
                if id_list[i] in s:
                    answer[j] += 1

    return answer