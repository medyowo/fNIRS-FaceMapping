function filter = manipulateData()
    % Sampling frequency fe = 13.33 Hz
    % Number of samples N = 800 *minimum*
    
    % Load data
    data = getExpData();

    % Calculate Fourier Transform to determine cutoff frequency
    ft = calculateFT();

    % Cutoff lowpass filter (in Hz)
    filter = 1;
end

% Calculates Fourier transform of each chanel to determine cutoff
function ftx = calculateFT()
    data = getExpData();

    % Initialise array to store Fourier transform
    ftx = [];

    % Get data from each case measurements
    for i = 1:length(data)
        % Get data from total oxy/deoxy blood chanels
        for j = 8:3:71
            x = data{i}{:,j};
            ft = abs(fft(x)); % Fourier transform applied to data
            ftx = [ftx; ft];
        end
    end
end