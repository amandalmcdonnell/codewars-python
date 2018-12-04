def snail(array):
    st=[]
    if array==[[]]:
        return []
    if len(array)==1:
        return array[0]
    while array!=[]:
        #step1 top l to r
        for i in range(len(array[0])):
            st.append(array[0][i])
        del array[0]
        #step2 right t to b
        if array==[]:
            return st
        else:
            for i in range(len(array)):
                st.append(array[i][-1])
                del array[i][-1]

        #step3 bottom r to l
        if array==[]:
            return st
        else:
            for i in range(len(array[0])-1,-1,-1):
                st.append(array[-1][i])
            del array[-1]
        #step4 left b to t
        if array==[]:
            return st
        else:
            for i in range(len(array)-1,-1,-1):
                st.append(array[i][0])
                del array[i][0]
    return st
