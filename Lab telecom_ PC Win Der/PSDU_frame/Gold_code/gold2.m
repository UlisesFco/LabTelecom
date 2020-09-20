%Gold sequence
function GS = gold2(m)


y = dec2bin(1,m);
for l=1:size(y,2)
    Rg(1,l) = str2num(y(1,l));
end


pp = primpoly(m);
g_char = dec2bin(pp);
g_char(:,size(g_char,2)) = [];
for i=1:size(g_char,2)
    g(1,i) = str2num(g_char(1,i));
end

size1 = size(Rg);
size2 = size(g);

if (size1==size2)
    Rsize=size1(1,2);
else
    error('size of Register is different of size of polynomial.');
end

N = 2.^Rsize-1;

if mod(Rsize,4)~=0
    if mod(Rsize,4)==2
        e=2;
        k=1;
        while gcd(Rsize,k)~=2,
            k=k+1;
        end
        f = 2.^k+1;
    else
        e=1;
        k=1;
        while gcd(Rsize,k)~=1,
            k=k+1;
        end
        f = 2.^k+1;
    end
else
    error('No prefer sequences can be created.');
end

%M-sequence generator (LFSR)
for i=1:m
    shiftreg(1,i) = Rg(1,i);
end
for i=1:2.^m-1
    SR1(1,i) = shiftreg(1,1);
    for l=1:m-1
        shiftreg(1,l) = shiftreg(1,l+1);
    end
    shiftreg2 = SR1(1,i);
    for l=1:m-1
        if g(1,m-l+1)==1
            shiftreg2 = xor(shiftreg2,shiftreg(1,l+1));
        end
    end
    shiftreg(1,m) = shiftreg2;
end

for i=0:N-1
    k = mod(i*f,N)+1;
    SR2(1,i+1) = SR1(1,k);
end

GS(1,:) = SR1;
GS(2,:) = SR2;
GS(3,:) = xor(SR1,SR2);
SR3 = SR1;
for l=1:N-1
    a = SR3(1,1);
    for i=1:N-1
        SR3(1,i) = SR3(1,i+1);
    end
    SR3(1,N) = a;
    GS(l+3,:) = xor(SR3,SR2);
end
GS = 2.*GS-1;