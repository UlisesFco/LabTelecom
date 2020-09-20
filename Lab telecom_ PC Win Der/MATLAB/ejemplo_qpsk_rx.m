%ejemplo qpsk rx
connectedRadios = findsdru;
if strncmp(connectedRadios(2).Status, 'Success', 7)
  switch connectedRadios(2).Platform
    case {'B200','B210'}
      address = connectedRadios(2).SerialNum;
      platform = connectedRadios(2).Platform;
    case {'N200/N210/USRP2'}
      address = connectedRadios(2).IPAddress;
      platform = 'N200/N210/USRP2';
    case {'X300','X310'}
      address = connectedRadios(2).IPAddress;
      platform = connectedRadios(2).Platform;
  end
else
  address = '192.168.10.2';
  platform = 'N200/N210/USRP2';
end

% Receiver parameter structure
prmQPSKReceiver = sdruqpskreceiver_init(platform,0)
prmQPSKReceiver.Platform = platform;
prmQPSKReceiver.Address = address;
compileIt  = false; % true if code is to be compiled for accelerated execution
useCodegen = false; % true to run the latest generated code (mex file) instead of MATLAB code

if compileIt
    codegen('runSDRuQPSKReceiver', '-args', {coder.Constant(prmQPSKReceiver)});
end
if useCodegen
   clear runSDRuQPSKReceiver_mex %#ok<UNRCH>
   BER = runSDRuQPSKReceiver_mex(prmQPSKReceiver);
else
   BER = runSDRuQPSKReceiver(prmQPSKReceiver);
end

fprintf('Error rate is = %f.\n',BER(1));
fprintf('Number of detected errors = %d.\n',BER(2));
fprintf('Total number of compared samples = %d.\n',BER(3));