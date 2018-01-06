def emod (a,b,c):
    if (b == 0 )
        return 0;
    else if (b%2 == 0)
        int d = emod(a,b/2,c)
        return (d*d)%c
    else
        return ((a%c)*emod(a,b-1,c))%c)
