clearvars, clc, close all;

% ask for data to filter
dataset_type = input("Choose dataset to use : train for training dataset, real for real dataset\n>", "s");

% select folder on answer
if dataset_type == "train"
    folder = "train_measurements/";
elseif dataset_type == "real"
    folder = "MEASUREMENTS/";
end
    
% call function to get experimental data
expArrays = getExpData(folder + "cleaned");

% call function to filter data
[ftx, filter, filtered_data] = manipulateData(expArrays);

% before filtering
displayData(expArrays, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Collected Data')
displayData(expArrays, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Collected Data')

% after filtering
displayData(filtered_data, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Filtered Data')
displayData(filtered_data, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Filtered Data')

% Amplify only training data
if dataset_type == "train"
    % Amplify data
    amp_data = amplifyData(filtered_data, ["warping", "scaling"], 2);

    % after amplifying
    displayData(amp_data, 141, 141, 13, 18, ["oxyHb", "deoxyHb"], 'Amplified Data')
    displayData(amp_data, 141, 141, 19, 22, ["oxyHb", "deoxyHb"], 'Amplified Data')
end

% save filtered data
SaveCurrentData(amp_data, folder + "filtered\");

% This function save selected data to designated folder
function hasSuccessed = SaveCurrentData(toSaveData, folderName)
    disp("[Saving] filtered data in " + folderName)
    if saveData(toSaveData, folderName)
        disp("[Saving complete]")
        hasSuccessed = true;
    else
        disp("[Error] Could not save filtered Data")
        hasSuccessed = false;
    end
end