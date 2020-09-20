%crc-4
function crc=crc4(msg)

%     % Reset the random generators to the original state
%     defaultStream=RandStream.getDefaultStream();
%     reset(defaultStream);

%msg1=rand(1,10)>0.5;

%msg=[0 0 0 msg1];


poly = [1 0 0 1 1];
%msg =[1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0];
          

M=length(msg);
N=length(poly);
mseg=[msg zeros(1,N-1)];

[~, r]=deconv(mseg,poly);
%r=abs(r);
%r=mod(r,2); % remainder
r=mod(abs(r),2);
crc=r(length(msg)+1:end);
%crc
%frame = bitor(mseg,r)
%msg(4)=0;
%frame=[msg crc];

% detection check
%msg2=frame;
%msg2=[msg1 crc];
%msg2(2)=1;

%[~, r]=deconv(msg2,poly);
%r=abs(r);
%r=mod(r,2);

%crc=r(length(msg2)+1:end);
      
% if sum(crc)==0
%     message=frame(1:M);
%     disp('no error');
% else
%     disp('error detection');
end

