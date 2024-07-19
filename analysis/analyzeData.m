clearvars, clc, close all;

% ask for data to filter
% フィルタリングするデータを要求する
dataset_type = input("Choose dataset to use : train for training dataset, real for real dataset\n>", "s");

% select folder on answer
% 回答に基づいてフォルダーを選択する
if dataset_type == "train"
    folder = "train_measurements/";
elseif dataset_type == "real"
    folder = "MEASUREMENTS/";
end
    
% call function to get experimental data
% 実験データを取得するために関数を呼び出す
expArrays = getExpData(folder + "cleaned");

% call function to filter data
% データをフィルタリングするために関数を呼び出す
[ftx, filter, filtered_data] = manipulateData(expArrays);

% before filtering
% フィルタリング前に
displayData(expArrays, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Collected Data')
displayData(expArrays, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Collected Data')

% after filtering
% フィルタリング後に
displayData(filtered_data, 1, 1, 13, 18, ["oxyHb", "deoxyHb"], 'Filtered Data')
displayData(filtered_data, 1, 1, 19, 22, ["oxyHb", "deoxyHb"], 'Filtered Data')

% Amplify only training data
% トレーニングデータのみを増幅する
if dataset_type == "train"
    % Amplify data
    % データを増幅する
    amp_data = amplifyData(filtered_data, ["warping", "scaling"], 2);

    % after amplifying
    % 増幅後に
    displayData(amp_data, 141, 141, 13, 18, ["oxyHb", "deoxyHb"], 'Amplified Data')
    displayData(amp_data, 141, 141, 19, 22, ["oxyHb", "deoxyHb"], 'Amplified Data')
end

% save filtered data
% フィルタリングされたデータを保存する
SaveCurrentData(amp_data, folder + "filtered\");

% This function save selected data to designated folder
% この関数は、選択されたデータを指定されたフォルダーに保存します
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