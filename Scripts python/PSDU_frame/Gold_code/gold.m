function [G]=gold(Rg,g)
%
% Project      : Space-time multiuser receiver for WCDMA.
% Module       : Data spreading.
% File         : gold2.m
% Description  : Generates a Gold code using one primitive polynom
%              : and calculating the second prefered sequence from
%              : a decimation of the given one.
%              : M=Register's size; Length of the sequence N=2^(M-1)
%              : h=h_m x^M + h_m-1 x^(M-1) + ... + h_1 x + h_0
%              : h='11101' = x^4 + x^3 + x^2 + 1
%              : g='1110' the term x^0 is not included in the routine !!!
%
% Reference    : Spreading codes for DS/CDMA WCDMA Cellular Networks.
%              : Esmel Dinan, IEEE Communication magazine, Sep. 1998.
% Implantation : MatLab v. 5.2
% Version      : 1.0
% Date/place   : March 99/NJIT
% Author       : Marco A. Hernandez
% 
% Arguments in :    Rg - Register initial condition in binary format.
%                    g - Primitive polynom in binary format (excluding the term x^0).
%
% Arguments out: G - Gold sequence of length N=2^(M)-1 .
%

size1=size(Rg);
size2=size(g);

if ( size1==size2 )
   Rsize=size1(1,2);
else
   error('Size of Register is different of size of polynom.');
end   

N=2.^Rsize-1;

if mod(Rsize,4)~=0
   if mod(Rsize,4)==2
      e=2; k=1;
      while gcd(Rsize,k)~=2,
         k=k+1;
      end
      f=2.^k+1;
   else         
      e=1; k=1;
      while gcd(Rsize,k)~=1,
         k=k+1;
      end
      f=2.^k+1;
   end
else
   error('No prefer sequences can be created.');
end

SR1=shiftReg(Rg,g);

for i=0:N-1
   k=mod(i*f,N)+1;
   SR2(1,i+1)=SR1(1,k);
end

G=-2*xor(SR1,SR2)+1;

cc=corr(G,G);
