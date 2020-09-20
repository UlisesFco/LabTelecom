function scrambled_data = scrambler(int_data)
% data is already interleaved
L = 2^63;
for i =1:length(int_data)
    scrambled_data(i) = mod(or(int_data(i),gold_seq(mod(i,L))),2);
end
end