% manipulateData is used to calculate Fourier Transform and filter
% collected data
% manipulateData は、フーリエ変換を計算し、
% 収集したデータをフィルタリングするために使用されます
function [ftx, filter, filtered_data] = manipulateData(data)
    % Sampling frequency fe = 13.33 Hz
    % Number of samples N = 800 *minimum*
    % サンプリング周波数 fe = 13.33 Hz
    % サンプル数 N = 800 最小

    % Calculate Fourier Transform to determine cutoff frequency
    % カットオフ周波数を決定するためにフーリエ変換を計算する
    ftx = calculateFT(data, false);
    % filter = ft;

    % Cutoff lowpass filter (in Hz)
    % ローパスフィルターのカットオフ周波数（Hz）
    filter = createFilter();

    % Filter data with created filter
    % 作成したフィルターでデータをフィルタリングする
    filtered_data = filteringData(data, filter);
end

% This function filter data using pass-low filter
% この関数は、ローパスフィルターを使用してデータをフィルタリングします
function filtered_data = filteringData(data, calcfilter)
    for i = 1 : length(data)
        % filter all channels
        % すべてのチャネルをフィルタリングする
        for j = 1 : 22
            % filter deoxy, oxy and total blood
            % 脱酸素血液、酸素化血液、総血液をフィルタリングする
            data{i}{:,6+3*(j-1)} = filtfilt(calcfilter(1, :), calcfilter(2, :), data{i}{:,6+3*(j-1)});
            data{i}{:,7+3*(j-1)} = filtfilt(calcfilter(1, :), calcfilter(2, :), data{i}{:,7+3*(j-1)});
            data{i}{:,8+3*(j-1)} = filtfilt(calcfilter(1, :), calcfilter(2, :), data{i}{:,8+3*(j-1)});
        end
    end
    filtered_data = data;
end

function filter = createFilter()
    % values were gotten from calculateFT graph analysis
    % 値は calculateFT グラフ分析から取得されました
    Fe = 13.3;
    fc = 0.41;
    filter = zeros(2,5);
    [filter(1,:), filter(2,:)] = butter(4, fc/(Fe/2), 'low');

end


% Calculates Fourier transform of each chanel to determine cutoff
% 各チャネルのフーリエ変換を計算してカットオフを決定する
function ftx = calculateFT(data, analysis_on)
    % Initialise array to store Fourier transform
    % フーリエ変換を保存するための配列を初期化する
    ftx = {1,length(data)};

    % Get data from each case measurements
    % 各ケースの測定データを取得する
    for i = 1:length(data)
        Te = data{i}{1, 2};
        Fe = 1/Te;
        Ps = height(data{i});
        
        % Change variable names
        % 変数名を変更する
        allVars = 1:23;
        newNames = append("ch",string(allVars));
        newNames = replace(newNames, "ch23", "frequency");
        
        % Change variable types
        % 変数の型を変更する
        types = strings(1, 23);
        types = append("double", types);

        % Create the new table for Fourier Transform data
        % フーリエ変換データ用の新しいテーブルを作成する
        ftx{i} = table('Size', [length(data{i}{:,8}) 23], 'VariableTypes', types, 'VariableNames',newNames);
        
        % Get data from total oxy/deoxy blood channels
        % 総酸素化血液／脱酸素血液チャネルからデータを取得する
        for j = 1 : 22
            % Fourier transform applied to data
            % データにフーリエ変換を適用する
            ft = fftshift(abs(fft(data{i}{:,8 + (j - 1) * 3})));
            ftx{i}{:, j} = ft;
        end
        ftx{i}{:, 23} = linspace(-Fe/2, Fe/2, Ps)';
        ftx{i} = movevars(ftx{i},'frequency','Before','ch1');
    end
    
    % Display graph for analysis
    % 分析用のグラフを表示する
    if analysis_on
        displayData(ftx,1,1,1,6,["ft"], 'Fourier Transform')
        displayData(ftx,1,1,7,12,["ft"], 'Fourier Transform')
        displayData(ftx,1,1,13,18,["ft"], 'Fourier Transform')
        displayData(ftx,1,1,19,22,["ft"], 'Fourier Transform')
    end
end