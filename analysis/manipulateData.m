function [ftx, filter, filtered_data] = manipulateData(data)
    % Sampling frequency fe = 13.33 Hz
    % Number of samples N = 800 *minimum*

    % Calculate Fourier Transform to determine cutoff frequency
    ftx = calculateFT(data, false);
    % filter = ft;

    % Cutoff lowpass filter (in Hz)
    filter = createFilter();

    % Filter data with created filter
    filtered_data = filteringData(data, filter);
end

function filtered_data = filteringData(data, calcfilter)
    for i = 1 : length(data)
        for j = 1 : 22
            data{i}{:,6+3*(j-1)} = filtfilt(calcfilter(1, :), calcfilter(2, :), data{i}{:,6+3*(j-1)});
            data{i}{:,7+3*(j-1)} = filtfilt(calcfilter(1, :), calcfilter(2, :), data{i}{:,7+3*(j-1)});
            data{i}{:,8+3*(j-1)} = filtfilt(calcfilter(1, :), calcfilter(2, :), data{i}{:,8+3*(j-1)});
        end
    end
    filtered_data = data;
end

function filter = createFilter()
    % values were gotten from calculateFT graph analysis
    Fe = 13.3;
    fc = 0.41;
    filter = zeros(2,5);
    [filter(1,:), filter(2,:)] = butter(4, fc/(Fe/2), 'low');

end


% Calculates Fourier transform of each chanel to determine cutoff
function ftx = calculateFT(data, analysis_on)
    % Initialise array to store Fourier transform
    ftx = {[1,length(data)]};

    % Get data from each case measurements
    for i = 1:length(data)
        Te = data{i}{1, 2};
        Fe = 1/Te;
        Ps = height(data{i});

        allVars = 1:23;
        newNames = append("ch",string(allVars));
        newNames = replace(newNames, "ch23", "frequency");
        types = strings(1, 23);
        types = append("double", types);
        ftx{i} = table('Size', [length(data{i}{:,8}) 23], 'VariableTypes', types, 'VariableNames',newNames);
        % Get data from total oxy/deoxy blood chanels
        for j = 1 : 22
            ft = fftshift(abs(fft(data{i}{:,8 + (j - 1) * 3}))); % Fourier transform applied to data
            ftx{i}{:, j} = ft;
        end
        ftx{i}{:, 23} = linspace(-Fe/2, Fe/2, Ps)';
        ftx{i} = movevars(ftx{i},'frequency','Before','ch1');
    end
    
    %Display graph for analysis
    if analysis_on
        displayData(ftx,1,1,1,6,["ft"], 'Fourier Transform')
        displayData(ftx,1,1,7,12,["ft"], 'Fourier Transform')
        displayData(ftx,1,1,13,18,["ft"], 'Fourier Transform')
        displayData(ftx,1,1,19,22,["ft"], 'Fourier Transform')
    end
end