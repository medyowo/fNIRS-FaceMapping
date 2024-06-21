clearvars, clc, close all;

% call function to get experimental data
expArrays = getExpData('measurements/cleaned');

% call function to filter data
[ftx, filter, filtered_data] = manipulateData(expArrays);

% before filtering
displayData(expArrays, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Collected Data')
displayData(expArrays, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Collected Data')

% after filtering
displayData(filtered_data, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Filtered Data')
displayData(filtered_data, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Filtered Data')

% save filtered data
SaveCurrentData(filtered_data, "measurements\filtered\");

% This function save selected data to designated folder
function hasSuccessed = SaveCurrentData(toSaveData, folderName)
    disp("[Saving] filtered data in" + folderName)
    if saveData(toSaveData, folderName)
        disp("[Saving complete]")
        hasSuccessed = true;
    else
        disp("[Error] Could not save filtered Data")
        hasSuccessed = false;
    end
end