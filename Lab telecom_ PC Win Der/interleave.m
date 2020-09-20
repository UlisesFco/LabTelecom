%Interleave data
function interleaved_data = interleave(data)
for i=1:length(data)
    interleaved_data(i) = data(interleaver(mod(i,length(data)),length(data)));
end
end