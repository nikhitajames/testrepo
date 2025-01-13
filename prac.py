def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * numRows
    cur_row = 0
    going_down = False

    # Traverse the string character by character
    for char in s:
        rows[cur_row] += char  # Add the current character to the current row

        # If we're at the top or bottom row, reverse direction
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down

        # Move to the next row (either down or up)
        cur_row += 1 if going_down else -1

    # Join all rows to form the final string
    return ''.join(rows)





"""def convert(s, numRows):
    l = [""] * numRows
    c=0
    j=1
    while c<len(s):
        if j==numRows:
            while(j!=1):
                l[j-1]=l[j-1]+s[c]
                j-=1
                c+=1
        else:
            l[j-1]=l[j-1]+s[c]
            j+=1
            c+=1
    return (''.join(l))"""
print(convert("PAYPALISHIRING",3))
