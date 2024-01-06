def solution(data, ext, val_ext, sort_by):
    answer = []
    col_name = ["code", "date", "maximum", "remain"]
    selected = []
    for d in data:
        if d[col_name.index(ext)] < val_ext:
            selected.append(d)
            
    answer = sorted(selected, key=lambda x : x[col_name.index(sort_by)])
    return answer