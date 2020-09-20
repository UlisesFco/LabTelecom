%PHY layer frame
function head = PHY_header(rate,length,burst,seed1,seed2,ft)
%returns the header of frame
%rate: (0-7)
%length: paylodad length(0-127) in bits
%burst: burst mode on/off -> (0/1)
%seed1 & seed2: scrambler seeds (0-31) each one
%ft -> frame type (0/1)
if ((rate > 7 || rate <=0) || (length>127 || length<0) || ...
    (burst ~= 0 && burst~=1) || (ft~=0 && ft~=1) || (seed1 >= 2^5 ...
    || seed1 < 0) || (seed2 >= 2^5 || seed2<0))
    error('Invalid parameters')
end
bin_rate = de2bi(rate,3);
data_res = 0;
bin_len = de2bi(length,8);
bin_s1 = de2bi(seed1,6);
bin_s2 = de2bi(seed2,6);

head = [bin_rate,data_res,bin_len,data_res,data_res,burst ...
    bin_s1,bin_s2,ft];
crc = crc4(head);
head = [head,crc];
end

