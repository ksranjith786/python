'''
Input : ababc         
Output : a, ab, aba, abab, ababc, a, ab
          
Input : abdabc          
Output : a, ab, abd, abda, abdab, abdabc, a, ab  
'''

str1 = "abdabc"

prefix_sub_str = [str1[i:j] for i in range(len(str1)) for j in range(i+1, len(str1)+1) if str1[i:j] == str1[0:j]]
print(prefix_sub_str)

# ['a', 'ab', 'abd', 'abda', 'abdab', 'abdabc']


