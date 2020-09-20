%Test script ettus ursp -> FM reciever
close all
% discover radios:
radioFound = false;
connectedRadios = findsdru;
if strncmp(connectedRadios(1).Status,'Success',7)
    address = connectedRadios(1).SerialNum;
    platform = connectedRadios(1).Platform;
    radioFound = true;
end

% initialization

% Reciever parameter structure
fmRxParams = getParamsSdruFMExamples(platform);

radio = comm.SDRuReciever('Platform',platform,...
    'IPAddress',address);

radio.CenterFrequency = 99.3e6;
radio.Gain = fmRxParams.RadioGain;
radio.DecimationFactor = fmRxParams.RadioDecimationFactor;
radio.SamplesPerFrame = fmRxParams.RadioFrameLength;
radio.OutputDataType = 'single';

hwinfo = info(radio)

% FM demod

fmBroadcastDemod = comm.FMBroadcastDemodulator(...
    'SampleRate',fmRxParams.RadioSampleRate,...
    'FrequencyDeviation', fmRxParams.FrequencyDeviation,...
    'FilterTimeConstant',fmRxParams.FilterTimeConstant,...
    'AudioSampleRate',fmRxParams.AudioSampleRate,...
    'PlaySound',true,...
    'BufferSize',fmRxParams.BufferSize,...
    'Stereo',true);

%stream proccessing loop
if radioFound
    %Loop until example reaches target stop time (10 s)
    timeCounter = 0;
    while timeCounter < fmRxParams.StopTime
        [x,len] = step(radio);
        if len > 0 
            %FM demod
            step(fmBroadcastDemod,x)
            %update counter
            timeCounter = timeCounter + fmRxParams.AudioFrameTime;
        end
    end
else
    warning(message('sdru:sysobjdemos:MainLoop'))
end
release(fmBroadcastDemod)
release(radio)