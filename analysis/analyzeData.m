clearvars, clc, close all;

expArrays = getExpData();    
[ftx, filter, filtered_data] = manipulateData(expArrays);

% before filtering
displayData(expArrays, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Collected Data')
displayData(expArrays, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Collected Data')

% after filtering
displayData(filtered_data, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Filtered Data')
displayData(filtered_data, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Filtered Data')
