function inter = interleaver(index,n)

if n>=1024 && n < 15120
    inter = 31*index + mod(64*index^2,n);
elseif n>=15120
    inter = 11*index + mod(21*index^2,n);
else
     error('Frame is to short')
end

end

