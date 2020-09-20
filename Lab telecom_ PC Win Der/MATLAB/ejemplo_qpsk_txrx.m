%Ejemplo qpsk tx
clc
clear all
close all

%Detect radios
connectedRadios = findsdru;
if strncmp(connectedRadios(1).Status, 'Success', 7)
  switch connectedRadios(1).Platform
    case {'B200','B210'}
      address1 = connectedRadios(1).SerialNum;
      platform1 = connectedRadios(1).Platform;
    case {'N200/N210/USRP2'}
      address1 = connectedRadios(1).IPAddress;
      platform1 = 'N200/N210/USRP2';
    case {'X300','X310'}
      address1 = connectedRadios(1).IPAddress;
      platform1 = connectedRadios(1).Platform;
  end
else
  address1 = '192.168.10.2';
  platform1 = 'N200/N210/USRP2';
end

if strncmp(connectedRadios(2).Status, 'Success', 7)
  switch connectedRadios(2).Platform
    case {'B200','B210'}
      address2 = connectedRadios(2).SerialNum;
      platform2 = connectedRadios(2).Platform;
    case {'N200/N210/USRP2'}
      address2 = connectedRadios(2).IPAddress;
      platform1 = 'N200/N210/USRP2';
    case {'X300','X310'}
      address2 = connectedRadios(2).IPAddress;
      platform2 = connectedRadios(2).Platform;
  end
else
  address2 = '192.168.10.3';
  platform2 = 'N200/N210/USRP2';
end
%============================= Tx =========================================
% Transmitter parameter structure
prmQPSKTransmitter = sdruqpsktransmitter_init(platform1,false)
prmQPSKTransmitter.Platform = platform1;
prmQPSKTransmitter.Address = address2;
compileIt  = false; % true if code is to be compiled for accelerated execution
useCodegen = false; % true to run the latest generated mex file

if compileIt
    codegen('runSDRuQPSKTransmitter', '-args', {coder.Constant(prmQPSKTransmitter)}); %#ok<UNRCH>
end
if useCodegen
   clear runSDRuQPSKTransmitter_mex %#ok<UNRCH>
   runSDRuQPSKTransmitter_mex(prmQPSKTransmitter);
else
   runSDRuQPSKTransmitter(prmQPSKTransmitter);
end

%============================= Rx =========================================
% Receiver parameter structure
prmQPSKReceiver = sdruqpskreceiver_init(platform1,false)
prmQPSKReceiver.Platform = platform1;
prmQPSKReceiver.Address = address1;
compileIt  = false; % true if code is to be compiled for accelerated execution
useCodegen = false; % true to run the latest generated code (mex file) instead of MATLAB code

if compileIt
    codegen('runSDRuQPSKReceiver', '-args', {coder.Constant(prmQPSKReceiver)});
end
if useCodegen
   clear runSDRuQPSKReceiver_mex %#ok<UNRCH>
   BER = runSDRuQPSKReceiver_mex(prmQPSKReceiver,false);
else
   BER = runSDRuQPSKReceiver(prmQPSKReceiver,false);
end

fprintf('Error rate is = %f.\n',BER(1));
fprintf('Number of detected errors = %d.\n',BER(2));
fprintf('Total number of compared samples = %d.\n',BER(3));

