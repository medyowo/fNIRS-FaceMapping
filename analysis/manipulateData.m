function filter = manipulateData()
    % Load data
    data = getExpData();
    % Sampling frequency fe = 13.33 Hz
    % Number of samples N = 800 *minimum*
    % Cutoff lowpass filter (in Hz)
    cutoff = calculateCutOff();
    % Fréquence de coupure du filtre passe-bas

end

% Calculates Fourier transform of each chanel to determine cutoff
function cutoff = calculateCutOff()
    data = getExpData();

    % Adds first element of the total oxy/deoxy blood from chanel 1
    x = [data{1}{:,8}];
    ftx = [abs(fft(x(1)))];

    % Get data from each case measurements
    for i = 2:14
        % Get data from total oxy/deoxy blood chanels
        for j = 11:3:71
            x = [x; data{i}{:,j}];
            ftx = [ftx; abs(fft(x(i)))];
        end
    end
    % Calculate Fourier transform on each chanel to determine noise
    cutoff = 1;
    % Visualise each Fourier transform
end